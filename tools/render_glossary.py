#!/usr/bin/env python3
"""
Render a per-language term list as a readable Markdown glossary.

    python3 tools/render_glossary.py terminology/crln-terms-fi.json > glossary-fi.md

The JSON is the source of truth. The Markdown is derived and should never be edited by
hand. Rows are grouped by area; each shows the English concept, the required rendering,
its status (reviewer ruling or proposal), and any forbidden renderings with the reason.
Reviewer names are printed only as they appear in the list, and only lists whose
reviewer has agreed to be named should carry a name at all.

Standard library only.
"""
import json
import sys
from collections import defaultdict
from pathlib import Path

STATUS = {
    "confirmed": "reviewer ruling",
    "keep_en": "reviewer ruling: keep in English",
    "proposed": "proposed, not yet reviewed",
}


def esc(s) -> str:
    return str(s or "").replace("|", "\\|").replace("\n", " ")


def render(d: dict) -> str:
    out = [f"# {d.get('language_name', d.get('language'))} glossary ({d.get('language')})", ""]
    out.append(f"*Generated from `crln-terms-{d.get('language')}.json` by `tools/render_glossary.py`. Do not edit by hand.*")
    out.append("")
    out.append(f"- **Status of this list:** {esc(d.get('list_status'))}")
    out.append(f"- **Reviewer:** {esc(d.get('reviewer')) or 'none yet'}")
    if d.get("review_basis"):
        out.append(f"- **What was reviewed:** {esc(d.get('review_basis'))}")
    out.append(f"- **Revised:** {esc(d.get('revised') or d.get('created'))}")
    out.append("")
    out.append("Only rows marked *reviewer ruling* are binding. Proposed rows are suggestions.")
    out.append("")
    by_area = defaultdict(list)
    for e in d.get("entries", []):
        by_area[e.get("area") or "Other"].append(e)
    for area in sorted(by_area):
        out += [f"## {area}", "", "| id | English | Rendering | Status | Context | Do not use |", "|---|---|---|---|---|---|"]
        for e in sorted(by_area[area], key=lambda x: x.get("id", "")):
            bad = "; ".join(f"{esc(f.get('display'))} ({esc(f.get('why'))})" for f in e.get("forbidden") or [])
            out.append(f"| {esc(e.get('id'))} | {esc(e.get('en'))} | {esc(e.get('target'))} | "
                       f"{STATUS.get(e.get('status'), esc(e.get('status')))} | {esc(e.get('context'))} | {bad} |")
        out.append("")
    return "\n".join(out)


def main(argv) -> int:
    if len(argv) != 1:
        print(__doc__.strip().splitlines()[2], file=sys.stderr)
        return 2
    d = json.loads(Path(argv[0]).read_text(encoding="utf-8"))
    sys.stdout.write(render(d) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
