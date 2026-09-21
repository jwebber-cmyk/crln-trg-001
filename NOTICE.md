# Scope of the CC BY 4.0 licence

`LICENSE` is the verbatim Creative Commons Attribution 4.0 International legal
code, so that automated tooling can detect it. This file states what it covers,
which is the part a human needs.

## Covered by CC BY 4.0

- `STANDARD.md` — the framework
- `SPEC.md` — the specification
- `crln-trg-001.json` — the machine-readable form
- the ICH E6(R3) and JTF crosswalks
- `ADOPT.md`, `GOVERNANCE.md`, `CHANGELOG.md`
- `translations/`

You may use, adapt, translate and redistribute all of it, commercially or
otherwise, with attribution and without asking. That includes building a product
that competes with CRLN.

## Not covered

The following are proprietary to Clinical Research Learning Network LLC and are
**not** licensed here:

- the CRLN Readiness Index measurement engine
- item parameters and calibrations
- scenario content
- all learner data

None of these are required in order to implement the standard. The four-level
scale, the scoring rules and the pass thresholds are published in `STANDARD.md`
and `crln-trg-001.json`, so an implementer can score against the framework
entirely with their own tooling. That separation is deliberate: the measurement
layer is open, the product built on top of it is not.

Copyright (c) 2024-2026 Clinical Research Learning Network LLC, a Florida
limited liability company.
