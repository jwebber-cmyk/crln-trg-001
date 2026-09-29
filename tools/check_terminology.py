#!/usr/bin/env python3
"""
Validate per-language term lists in terminology/ against crln-terminology.schema.json.

    python3 tools/check_terminology.py            # every terminology/crln-terms-*.json
    python3 tools/check_terminology.py FILE ...   # specific files

Uses the `jsonschema` package when it is installed (full Draft 2020-12 validation).
Without it, runs the structural checks below, which cover every rule the schema states
for entries. Either way it adds three rules the schema cannot express:

  * ids are unique within a list, and share the list's language prefix;
  * a row with status "confirmed" or "keep_en" names a reviewer and a review date,
    because those statuses are reviewer rulings and are binding;
  * a row with status "proposed" that sets enforce: true is reported as a WARNING. The
    translators ignore enforce on proposed rows (an unreviewed row must not fail anyone's
    translation), so the flag does nothing, and a reader may believe it does.

Exit 0 clean, 1 on any error, 2 if nothing could be checked. Standard library only
(jsonschema optional).
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TERMS = ROOT / "terminology"
SCHEMA = TERMS / "crln-terminology.schema.json"

TOP_REQUIRED = ["schema", "language", "language_name", "governs", "list_status", "entries"]
ENTRY_REQUIRED = ["id", "en", "triggers", "target", "rendering", "status", "source",
                  "reviewer", "review_date", "context", "area", "forbidden", "note"]
ENUMS = {
    "rendering": {"translate", "keep_english"},
    "status": {"confirmed", "keep_en", "proposed"},
    "source": {"reviewer", "reviewer-raised", "crln-proposed"},
}
ID_RE = re.compile(r"^[a-z]{2,3}(-[A-Za-z0-9]+)*-[0-9]{3}$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def structural(d: dict) -> list:
    errs = []
    for k in TOP_REQUIRED:
        if k not in d:
            errs.append(f"missing top-level field '{k}'")
    if d.get("schema") != "crln-terminology/2":
        errs.append("schema must be 'crln-terminology/2'")
    entries = d.get("entries")
    if not isinstance(entries, list) or not entries:
        errs.append("entries must be a non-empty array")
        return errs
    for i, e in enumerate(entries):
        where = f"entries[{i}] ({e.get('id', '?')})"
        for k in ENTRY_REQUIRED:
            if k not in e:
                errs.append(f"{where}: missing '{k}'")
        if "id" in e and not ID_RE.match(str(e["id"])):
            errs.append(f"{where}: id does not match {ID_RE.pattern}")
        for k, allowed in ENUMS.items():
            if k in e and e[k] not in allowed:
                errs.append(f"{where}: {k} '{e[k]}' not in {sorted(allowed)}")
        if not isinstance(e.get("triggers"), list) or not e.get("triggers"):
            errs.append(f"{where}: triggers must be a non-empty array")
        if e.get("review_date") is not None and not DATE_RE.match(str(e["review_date"])):
            errs.append(f"{where}: review_date must be YYYY-MM-DD or null")
        for j, f in enumerate(e.get("forbidden") or []):
            fw = f"{where}.forbidden[{j}]"
            for k in ("display", "why", "enforce"):
                if k not in f:
                    errs.append(f"{fw}: missing '{k}'")
            if ("stem" in f) == ("pattern" in f):
                errs.append(f"{fw}: exactly one of 'stem' or 'pattern' is required")
            # Patterns are JavaScript (Unicode) regular expressions, e.g. \p{L}, and are not
            # compiled here: Python's re module would reject valid ones.
    return errs


def extra_rules(d: dict, warns: list) -> list:
    errs, seen = [], set()
    lang = str(d.get("language", ""))
    for e in d.get("entries") or []:
        i = e.get("id", "?")
        if i in seen:
            errs.append(f"{i}: duplicate id")
        seen.add(i)
        if lang and not str(i).startswith(lang.lower() + "-"):
            errs.append(f"{i}: id should start with the list language '{lang.lower()}-'")
        if e.get("status") in ("confirmed", "keep_en") and (not e.get("reviewer") or not e.get("review_date")):
            errs.append(f"{i}: status '{e.get('status')}' is a reviewer ruling and needs reviewer and review_date")
        if e.get("status") == "proposed" and any(f.get("enforce") for f in e.get("forbidden") or []):
            warns.append(f"{i}: proposed row sets enforce: true, which has no effect until a reviewer rules")
    return errs


def main(argv) -> int:
    paths = [Path(a) for a in argv if not a.startswith("-")] or sorted(TERMS.glob("crln-terms-*.json"))
    if not paths:
        print(f"FAIL  no term lists found under {TERMS}", file=sys.stderr)
        return 2
    try:
        import jsonschema  # type: ignore
        validator = jsonschema.Draft202012Validator(json.loads(SCHEMA.read_text(encoding="utf-8")))
    except ImportError:
        validator = None
    failed = 0
    for p in paths:
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as x:
            print(f"FAIL  {p.name}: {x}")
            failed += 1
            continue
        if validator is not None:
            errs = [f"{'/'.join(map(str, e.path)) or '(root)'}: {e.message}" for e in validator.iter_errors(d)]
        else:
            errs = structural(d)
        warns: list = []
        errs += extra_rules(d, warns)
        for w in warns:
            print(f"WARN  {p.name}: {w}")
        if errs:
            failed += 1
            print(f"FAIL  {p.name}")
            for e in errs:
                print(f"        {e}")
        else:
            mode = "jsonschema" if validator is not None else "structural"
            print(f"OK    {p.name}  ({len(d['entries'])} entries, {mode} validation)")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
