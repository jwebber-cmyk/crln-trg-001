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

## Then, and only then, the DPG submission

`dpg-nominee.json` in this directory is the Digital Public Goods Alliance entry,
built against their live schema. It references the repository URL, so it cannot be
submitted before the repository exists.

Submit by either route:
- the nomination form at https://www.digitalpublicgoods.net/submission-guide
- or a pull request adding `nominees/crln-trg-001.json` to
  `DPGAlliance/publicgoods-candidates`

Both are public acts under your identity, which is why neither is automated here.
