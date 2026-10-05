# Terminology

Per-language clinical research term lists, one file per language: `crln-terms-<lang>.json`.

| file | what it is |
|---|---|
| `crln-terminology.schema.json` | the format (`crln-terminology/2`), JSON Schema draft 2020-12 |
| `crln-terms-TEMPLATE.json` | a starting point with one example row; copy it, do not edit it |

**Status: no language list is published here yet.** CRLN maintains a Finnish list under
review with a named practitioner; it will be added once the review is complete and the
reviewer has agreed how to be named.

How the fields work, in short:

- `status` is `confirmed` or `keep_en` only when a named reviewer ruled on the row. Those rows
  are binding on translators. `proposed` rows are suggestions and are never enforced.
- `forbidden` lists renderings that change the meaning. `enforce: true` makes a translation
  containing one fail a post-check, and only on reviewer-ruled rows.
- `triggers` are the English forms that mean the concept is present. Lowercase matches at the
  start of a word, ALL CAPS matches a whole-word acronym, `re:` is a regular expression.
- `stem` in a forbidden rendering matches anywhere in a word, which catches inflections and
  compounds (important in languages such as Finnish). `pattern` is a JavaScript regular
  expression, anchored at a word start.

Tools:

```
python3 tools/check_terminology.py                                 # validate every list
python3 tools/render_glossary.py terminology/crln-terms-<lang>.json  # readable glossary
```

The schema is copied unchanged from CRLN's internal terminology layer, so a list that
validates here is accepted by the translators that use it. See `CONTRIBUTING.md`.
