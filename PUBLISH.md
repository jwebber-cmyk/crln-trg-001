# How to publish this as the public CRLN-TRG-001 repository

Everything in this directory is ready to be a public repository. It has been
scanned for personal names, credentials and learner emails; all four checks
returned nothing. `GOVERNANCE.md` here is the **redacted** copy: the seated Board
member is not named, because consent is not on file.

I could not create the public repository myself. That action was blocked by a
permission guardrail, which is the correct outcome for "create a public record of
a company" and not something to work around.

## One command

```
cd ops/public-standard && gh repo create crln-trg-001 --public --source=. --push \
  --description "CRLN-TRG-001: an open competency framework for clinical research roles. CC BY 4.0. Crosswalked to ICH E6(R3) and the JTF Clinical Trial Competency Framework."
```

(`git init && git add -A && git commit` first if `gh` asks for a commit.)

## Check before you run it

1. **`GOVERNANCE.md` names nobody.** Verified. If you get the Board member's
   written consent, swap in the unredacted copy from `ops/grants/` and note the
   consent source the way `v_nameable_validators` records RMP's.
2. **The `translations/` files say unofficial, English authoritative.** They are
   machine-assisted and unreviewed. That is stated at the top of each file and in
   `translations/README.md`. Do not quietly drop the caveat later.
3. **`ADOPTERS.md` is empty on purpose** and says so.

## The DPG submission

**Done as far as it can go without you.** The repository is public and current,
and `dpg-nominee.json` validates against the DPGA schema.

**The route in the old version of this file no longer works.**
`DPGAlliance/publicgoods-candidates` was archived on 2026-08-31 and rejects pull
requests. Submission has moved to https://app.digitalpublicgoods.net.

Both paths there need a person: either create a DPGA account, or use the
"Create new application" control, which needs no account but does require
accepting their terms of use. Once an application is open, every answer it asks
for is already written in `DPG-SCREENING.md`.
