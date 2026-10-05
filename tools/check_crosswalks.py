#!/usr/bin/env python3
"""
Check every crosswalk in crosswalks/ against itself and against the framework.

Three checks, because a crosswalk's summary is what a reader quotes and a reviewer
checks first, and nothing else verifies that it still describes its own table:

  1. Markdown crosswalks: the counts in the summary table ("12 full, 11 partial, 9 none")
     equal the verdicts in the mapping table below it.
  2. JSON crosswalks: summary.full / summary.partial / summary.none equal the count of
     mappings with that status.
  3. JSON crosswalks: every crln_ids entry is a competency id that exists in
     crln-trg-001.json. A mapping to an id the framework does not define is a claim about
     nothing.

    python3 tools/check_crosswalks.py
    python3 tools/check_crosswalks.py --json

Exit 0 when everything agrees, 1 on any mismatch, 2 if a file or a summary is missing.
A crosswalk that cannot be verified must not report clean.

Ported from CRLN's internal check (check-crosswalk-claims.py), with checks 2 and 3 added.
Standard library only.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
XW = ROOT / "crosswalks"
FRAMEWORK = ROOT / "crln-trg-001.json"

# A verdict is spelled differently in a domain-to-domain crosswalk than in an
# item-to-item one. The JTF document says "mapped" where TDR says "full", and
# "one secondary mapping only" where TDR says "partial". Same three verdicts.
VERDICTS = {
    "full": ("full", "mapped"),
    "partial": ("partial", "one secondary mapping only", "secondary mapping only"),
    "none": ("none", "no crln counterpart", "no counterpart"),
}
MAPPING_HEADINGS = ("## Full mapping", "## The mapping")


def summary_counts(text: str) -> dict:
    out = {}
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip().strip("*").strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2:
            continue
        label = cells[0].lower()
        nums = [c for c in cells[1:] if re.fullmatch(r"\d+", c)]
        if not nums:
            continue
        n = int(nums[0])
        if "full" in label or "with a crln canonical domain" in label:
            out["full"] = n
        elif "partial" in label:
            out["partial"] = n
        elif "no crln" in label or "no counterpart" in label:
            out["none"] = n
    return out


def mapping_counts(text: str) -> dict:
    out = {k: 0 for k in VERDICTS}
    body = None
    for h in MAPPING_HEADINGS:
        if h in text:
            body = text.split(h, 1)
            break
    if not body or len(body) < 2:
        return {}
    for line in body[1].splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip().strip("*").strip().lower() for c in line.strip().strip("|").split("|")]
        # Two columns is a legitimate mapping table: a domain-to-domain crosswalk needs
        # only "domain | verdict".
        if len(cells) < 2 or cells[0] in ("", "#", "---") or set(cells[0]) <= set("-: "):
            continue
        # Substring, most specific first, so a cell naming two verdicts is not counted as
        # the weaker one.
        joined = " ".join(cells)
        for k in ("none", "partial", "full"):
            if any(sp in joined for sp in VERDICTS[k]):
                out[k] += 1
                break
    return out


def framework_ids() -> set:
    text = FRAMEWORK.read_text(encoding="utf-8")
    return set(re.findall(r'"id":\s*"(CRLN-[A-Z]+-D\d+)"', text))


def check_markdown(results, bad, unverifiable):
    files = sorted(XW.glob("*.md"))
    for f in files:
        t = f.read_text(encoding="utf-8")
        s, m = summary_counts(t), mapping_counts(t)
        if not s:
            unverifiable.append((f.name, "no summary table"))
            continue
        if not m:
            unverifiable.append((f.name, "no '## Full mapping' section"))
            continue
        agree = all(s.get(k) == m.get(k) for k in s)
        results.append({"file": f.name, "check": "summary-vs-table", "summary": s, "mapping": m, "agree": agree})
        if not agree:
            bad.append(f.name)
    return len(files)


def check_json(results, bad, unverifiable, ids):
    files = sorted(XW.glob("*.json"))
    for f in files:
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            unverifiable.append((f.name, f"invalid JSON: {e}"))
            continue
        summ, maps = d.get("summary"), d.get("mappings")
        if not isinstance(summ, dict) or not isinstance(maps, list):
            unverifiable.append((f.name, "no summary object or mappings array"))
            continue
        counted = {k: sum(1 for m in maps if m.get("status") == k) for k in VERDICTS}
        s = {k: summ[k] for k in VERDICTS if k in summ}
        agree = all(s[k] == counted[k] for k in s)
        results.append({"file": f.name, "check": "summary-vs-mappings", "summary": s, "mapping": counted, "agree": agree})
        if not agree:
            bad.append(f.name)
        unknown = sorted({i for m in maps for i in (m.get("crln_ids") or []) if i not in ids})
        results.append({"file": f.name, "check": "ids-resolve", "unknown_ids": unknown, "agree": not unknown})
        if unknown:
            bad.append(f.name)
    return len(files)


def main() -> int:
    if not XW.is_dir() or not FRAMEWORK.is_file():
        print(f"FAIL  missing {XW} or {FRAMEWORK}", file=sys.stderr)
        return 2
    ids = framework_ids()
    if not ids:
        print("FAIL  no competency ids found in crln-trg-001.json", file=sys.stderr)
        return 2
    results, bad, unverifiable = [], [], []
    n = check_markdown(results, bad, unverifiable) + check_json(results, bad, unverifiable, ids)
    if n == 0:
        print(f"FAIL  no crosswalks found under {XW}", file=sys.stderr)
        return 2
    code = 1 if bad else (2 if unverifiable else 0)

    if "--json" in sys.argv:
        print(json.dumps({"results": results, "mismatched": sorted(set(bad)),
                          "unverifiable": unverifiable}, indent=2))
        return code

    for r in results:
        mark = "OK   " if r["agree"] else "DRIFT"
        if r["check"] == "ids-resolve":
            print(f"{mark} {r['file']}  ids resolve in crln-trg-001.json"
                  + ("" if r["agree"] else f": unknown {', '.join(r['unknown_ids'])}"))
            continue
        print(f"{mark} {r['file']}  {r['check']}")
        for k in ("full", "partial", "none"):
            if k in r["summary"]:
                sm, mp = r["summary"][k], r["mapping"].get(k, 0)
                flag = "" if sm == mp else f"   <-- summary says {sm}, rows have {mp}"
                print(f"        {k:<8} summary {sm:>3}   rows {mp:>3}{flag}")
    for name, why in unverifiable:
        print(f"SKIP  {name}: {why}")
    if bad:
        print(f"\n{len(set(bad))} crosswalk(s) failed. Fix the count or the rows, not the check.")
    elif unverifiable:
        print(f"\n{len(unverifiable)} crosswalk(s) could not be verified. That is not a pass.")
    else:
        print("\nEvery crosswalk summary matches its own rows, and every mapped id exists.")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
