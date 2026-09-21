# CRLN-TRG-001 — Change log

The governance section of the standard states that "changes are tracked in the CRLN
methodology registry with change notes." This is that record, published openly so
the claim is checkable rather than asserted.

Published versions are immutable. Each receives its own DOI. This file is appended
to, never rewritten.

Concept DOI (all versions, always resolves to the latest):
[10.5281/zenodo.22049549](https://doi.org/10.5281/zenodo.22049549)

> **Correction, 2026-09-09.** This line previously named 10.5281/zenodo.22049550 as the
> concept DOI. That is the **version 1.1** DOI. Anyone who followed it has pinned a
> citation to v1.1 while believing they had cited the framework in general. The READMEs
> in `publications/` were correct throughout; this file was not.
>
> **Correction, 2026-09-21.** The 2026-09-09 fix was applied to this file only. `ADOPT.md`
> and `STANDARD.md` carried the same error for a further twelve days: `ADOPT.md` labelled
> `10.5281/zenodo.22049550` as the concept DOI in its header and in the attribution block it
> asks adopters to copy, and `STANDARD.md` cited it in section 7. Both are corrected to
> `10.5281/zenodo.22049549`. `ADOPT.md` also pointed readers at `CRLN-TRG-001-Standard-v1.1.md`,
> a filename that has not shipped since 1.1.1; it now names the current file. Copies of
> `ADOPT.md` inside published Zenodo records up to and including 1.7.1 are immutable and still
> carry the wrong DOI; the correction reaches a published record at the next release.

Governance — who decides, how to propose a change, how to appeal, and what is not yet in
place: [CRLN-TRG-001-GOVERNANCE.md](CRLN-TRG-001-GOVERNANCE.md)

---

## 1.7.1 — 2026-09-21 (the competency crosswalk stops being provisional)

Published: [10.5281/zenodo.22884111](https://doi.org/10.5281/zenodo.22884111)

**Nothing in the framework changed. What changed is that we stopped understating it.**

Every published version since 1.0 has said the standards crosswalk was "undergoing SME review" and
"provisional until signed off." That review finished. Three independent reviewers rated all ten
canonical domains against ICH E6(R3) Annex 1 and the Joint Task Force framework, and agreed on all
ten, unanimously:

| reviewer | organisation |
|---|---|
| Jeffrey Smyth, MS, CCRP | TrueBlue Clinical Research, Tampa |
| Rotceh Rios | RMP SMO |
| *(third reviewer, name withheld)* | *(withheld)* |

> **Correction, 2026-09-21, same day.** This table was first published naming all three
> reviewers. Only two of the three have publication consent on file. The third was named
> without ever being asked, and the name and organisation were removed within the hour. A
> reviewer's identity is theirs to release, not ours to use because it strengthens a claim,
> and the fact that the claim is true does not make the naming consented. The name will be
> restored if and only if that reviewer says yes to wording shown to them first, which is the
> same process the other two went through.

The records were in the review table and the published documents had simply not caught up, which is
an error in the safe direction and still an error. A standard that describes itself as less validated
than it is misleads a reader exactly as much as one that describes itself as more.

**What this release does NOT claim.**

- **The jurisdiction and regulatory-regime crosswalk remains provisional.** It has had no SME review at
  all. Zero reviewers, zero ratings. Nothing about the competency validation extends to it, and this is
  stated in every place the competency status is stated.
- **Not board-ratified.** The Methodology Review Board has one seated member and has not reached
  quorum, so approval here is by the custodian on SME review, exactly as §6 of the governance document
  requires every release to say.
- **Not accredited.** CRLN-TRG-001 is not an accredited standard and must not be represented as one.

Patch rather than minor under §6 of the governance document: no competency was added, removed or
reworded, no weight or threshold moved. Only the validation statement changed.

Changed: `STANDARD.md` maturity notice and §Validation status · `SPEC.md` §7 and the status header ·
`crln-trg-001.json` (`status` is now `published-sme-validated`, `alignment.validation_status` rewritten).

---

## 1.7.0 — 2026-09-18 (the published standard catches up with what is applied)

**This release publishes five versions that had been applied and never written down.**

Between 2026-09-01 and 2026-09-18 the framework moved from eight role tracks to
fourteen. The engine, the safety table and the version stamp all moved with it;
the published standard and this changelog did not. Every competency signal CRLN
emitted in that period was stamped `CRLN-TRG-001 v1.7`, and a reader who looked
up v1.7 found a document describing v1.1 — eight roles, 48 competency statements.

A version stamp that cannot be looked up is worse than no stamp, because it is
trusted. The same reasoning corrected the stamp itself on 2026-08-31; this is
that correction applied to the document rather than to the constant.

**What actually changed, per version, all of it additive.** The 1–4 scale, the
safety rule and the composite are untouched throughout, so scores remain
comparable across every version. Assessments keep the stamp they were scored
under and are never restamped.

| version | date | adds | role tracks | competency statements |
|---|---|---|---|---|
| 1.2 | 2026-09-01 | RN, Research Nurse | 9 | 54 |
| 1.3 | 2026-09-01 | PHARM, Clinical Trial Pharmacist | 10 | 60 |
| 1.4 | 2026-09-01 | DCT, Decentralized Trial Coordinator | 11 | 66 |
| 1.5 | 2026-09-01 | ASSIST, Research Assistant / Study Coordinator I | 12 | 72 |
| 1.6 | 2026-09-01 | LAB, Specimen Processing / Laboratory Technician | 13 | 78 |
| 1.7 | 2026-09-01 | SUBI, Sub-Investigator | 14 | **84** |

Each was released as its own point version rather than folded together, even
where several landed the same day, because the stamp records what was applied
**at the time of scoring**. An assessment scored under 1.2 was scored by an
engine with nine roles; restamping it to claim ten would make the provenance
record a convenience rather than a fact.

**Why each role was added.**

- **RN (1.2).** Modelled at ~128,000 FTE across 120 countries, the largest role
  the framework did not cover. Its domains are not a re-cut of the coordinator's:
  the coordinator owns eligibility, consent logistics and the source record; the
  nurse owns assessment, administration and specimens, and is usually the first
  person to see an adverse event.
- **PHARM (1.3).** ~80,000 FTE modelled. Holds custody of the investigational
  product from arrival to destruction, which is a different competency from
  administering it: the nurse gives what the pharmacist releases.
- **DCT (1.4).** Defined by distance rather than by a subject: the same
  competencies as a site role, each made harder by the participant not being in
  the room. Its crosswalk spreads across the canonical spine rather than
  clustering.
- **ASSIST (1.5).** The first track that goes *down* rather than sideways. Every
  other role assumes the learner is already in clinical research; this one does
  not. Its weights are deliberately unlike the others, with escalation at 0.25,
  because an assistant's defining competency is knowing the edge of their own
  authority.
- **LAB (1.6).** The bench, and the first role whose harm route does not run
  through touching a participant. It runs through the *result*. A trial's primary
  endpoint is very often a number produced at a bench, and the ways that number
  goes wrong were invisible to the other twelve roles. Four of six domains map
  onto records entry (D-06), which is the honest crosswalk.
- **SUBI (1.7).** Delegated medical oversight, distinct from the Principal
  Investigator who delegates it.

**How this was reconstructed.** The role set, domain labels, weights,
safety-critical flags and regulatory references in this release were extracted
directly from the scoring implementation rather than re-authored, and the
resulting counts were checked independently: 14 roles, 84 statements, every
role's weights summing to 1.00. The published form is now generated from the
thing that scores assessments, which is what should have prevented this drift and
will now.

**Known gap, stated rather than left to be found.** The standards crosswalk
remains marked provisional. One independent reviewer has completed all ten
canonical domain mappings; the Methodology Review Board that would ratify them
holds one seat of five. "Provisional" is the accurate word until that changes.

---

## 1.2.1 — 2026-09-09 (governance stated honestly)

Published: [10.5281/zenodo.22681637](https://doi.org/10.5281/zenodo.22681637)
Verified live by resolving the public record, not by reading the draft page.

> **1.2.0 remains publicly readable** at
> [10.5281/zenodo.22554748](https://doi.org/10.5281/zenodo.22554748) with the uncorrected §6.
> A Zenodo record is immutable, so this release supersedes it rather than replacing it. That
> record had 51 views and 8 downloads before the correction went out.

> **A first publish attempt failed** with "The draft was not published. Please try again." The
> cause was an empty **Dates** row — a date entry with no value but with required Date and
> Type subfields, which InvenioRDM accepts client-side and rejects server-side. Removing the
> empty row cleared it. Worth knowing for future releases: the error message does not name
> the field.

### §6 asserted governance that did not exist

Versions 1.1 through 1.1.3 stated that "a Methodology Review Board, conflict-of-interest
policy, and appeals process govern updates." **Two of those three did not exist.** There was
no board and no appeals process — only the sentence, in an openly licensed, DOI'd document
that adopters were invited to build on.

§6 now states what is true: the custodian approves changes on external SME review requiring
2-of-3 consensus; the Board is specified but **not constituted**; the appeals process is
defined and **has never been invoked**; and the custodian's commercial interest in adoption is
disclosed. The section points to the new `CRLN-TRG-001-GOVERNANCE.md`, which also lists what
is still missing.

### §7 cited the wrong version and the wrong DOI

The citation block in the v1.2 document still read "Version 1.1" and gave
`10.5281/zenodo.22049550`. That is the **v1.1 version DOI**, not the concept DOI. Corrected to
`10.5281/zenodo.22049549` with an explicit note on the difference, because the same confusion
appeared in this change log and has been propagating.

### Also

- `CRLN-TRG-001-GOVERNANCE.md` added to the release folder.
- `crln-trg-001.json` gains a `governance` block naming the approval route and stating
  `review_board_constituted: false`.
- PDF rebuilt from the corrected Markdown with `scripts/build-standard-pdf.py`.

### Also corrected in this release

The published 1.2.0 document's own header block reads **"Version: 1.1 · Release: 1.1.3"** — the
version banner was never updated when 1.2 was cut. Corrected to 1.2.1.

### Released

Published as a new version under concept DOI 22049549, so the concept DOI now resolves here.
Seven files, including `CRLN-TRG-001-GOVERNANCE.md` for the first time.

---

## 1.1.3 — 2026-09-01 (regulatory citations corrected)

Published: [10.5281/zenodo.22217886](https://doi.org/10.5281/zenodo.22217886)

**No change to the competencies, the scale, the weights or the scoring.** This
release corrects where the framework points in the regulation, and names the
publishing entity.

### The citations pointed at the wrong sections

ICH E6(R3) Annex 1 renumbered the guideline. R2 placed the Investigator at §4, the
Sponsor at §5 and Essential Documents at §8; R3 places them at §2, §3 and Appendix
C. **Thirty-eight of the forty-eight** competency domains cited R2 section numbers
while labelling them "ICH E6(R3)":

| | cited | should point to |
|---|---|---|
| PI-D2 — Informed Consent | ICH E6(R3) §4.8 | ICH E6(R3) Annex 1 §2.8 |
| CDM-D1 — Data Management Plan | ICH E6(R3) §5.5 | ICH E6(R3) Annex 1 §2.12 |
| RA-D6 — Regulatory Documentation | ICH E6(R3) §8 | ICH E6(R3) Annex 1 Appendix C |
| CTA-D2 — IRB / IEC | ICH E6(R3) 3.0 | ICH E6(R3) Annex 1 §1 |

The mapping was right — those domains do correspond to those obligations. The
address was wrong. For a framework whose value is that a competency claim can be
traced to the regulation behind it, a citation pointing at the wrong section of the
named document is close to the worst kind of error available: it reads as
authoritative and cannot be followed.

`CTA-D2` and `RA-D2` are worth singling out. They cited §3 for IRB/IEC review,
which was correct under R2 — and under R3, §3 is the **Sponsor** chapter. Read
literally against the guideline they now name, they pointed at the wrong party.

### How the new numbers were obtained

Not by translating R2 sections into R3 by hand. The subsection numbering does not
map one-to-one, and inventing plausible numbers is how the original error would be
repeated in a new form.

Each competency domain maps to one of the ten canonical domains, and each canonical
domain carries an anchor set from the **adopted R3 guideline text**. This release
substitutes those verified anchors.

The trade is deliberate and worth stating: citations are now correct at
**canonical-domain granularity** rather than precise-but-wrong at role granularity.
A reader following `ICH E6(R3) Annex 1 §2.8` from the informed-consent domain lands
on informed consent. Every non-ICH citation is preserved unchanged — 21 CFR parts,
GCDMP, CDISC, ALCOA+, ICH E2A, TransCelerate, the Declaration of Helsinki.

### Publisher

`publisher` now reads **Clinical Research Learning Network LLC**, the registered
entity, rather than the trading name.

---

## 1.1.2 — 2026-08-31 (specification completeness)

Published: [10.5281/zenodo.22216241](https://doi.org/10.5281/zenodo.22216241)

**No normative change to the framework.** Two omissions in the machine-readable
specification are filled. Both were found the same day 1.1.1 was published, by a
type checker rather than by reading — which is the point of shipping the spec as
data.

### The safety rule was only half-specified

The five role tracks added at 1.1 — CDM, PM, RA, PV, PI — carried no
`safety_critical` flags and no regulatory `refs` in the spec, while the original
three did.

The safety rule is **normative**: a failure in a safety-critical domain cannot be
averaged away by strength elsewhere. A specification in which five of eight tracks
do not say *which* domains are safety-critical does not let an implementer apply
that rule. The framework was never ambiguous — the assessment engine and the
competency registry both carried the flags all along — but the published artifact
was incomplete.

All 48 domains now carry `safety_critical` and their regulatory `refs`, taken from
the competency registry. **Eleven domains are safety-critical, and every role track
has at least one:**

| track | safety-critical domains |
|---|---|
| CRC | D2, D5 |
| CRA | D3 |
| CTA | D5 |
| CDM | D5 |
| PM | D4 |
| RA | D5 |
| PV | D3, D4 |
| PI | D2, D4 |

The registry's domain weights were checked against the engine's in the same pass
and agree exactly, which is independent confirmation of both.

### `alignment` had drifted into two disjoint halves

The specification carried `validation_status` — what is *not* yet SME-validated —
while the copy rendered on the public framework page carried `standards_alignment`,
which names the published standards this framework maps to and states explicitly
that the mapping is authored by CRLN and is **not** a third-party audit or
validation.

Both are honest and both are load-bearing, and each file had only one of them.
The specification now carries both.

---

## 1.1.1 — 2026-08-31 (editorial + companion artifacts)

Published: [10.5281/zenodo.22215185](https://doi.org/10.5281/zenodo.22215185)

**No normative change.** The competency content of 1.1 is exactly as published on
2026-08-21. This release corrects two incorrect figures in the 1.1 document, brings
the machine-readable spec and the assessment engine into agreement with it, and adds
the companion artifacts the standard's own governance section promised.

### Two published figures corrected

The 1.1 document stated that the framework "comprises 56 competency statements
across these domains and 3 tracked framework versions." Both numbers came from
counting the methodology registry without filtering, so both included the eight
**JTF v3.1** reference statements — the framework CRLN-TRG-001 is crosswalked *to*,
not composed *of*.

The correct figures are **48 statements** (18 at 1.0, plus 30 added at 1.1) across
**2 published versions**. The document now carries the corrected paragraph and a
visible note of what it previously said, because a standard that silently restates
its own size is not one anybody should cite.

### The three artifacts now agree

At publication of 1.1 the document said 1.1, but the machine-readable spec still
said 1.0 and the assessment engine still stamped `v1.0` — in both its client and
edge-function implementations — while the hub's framework registry already carried
all eight role tracks. Every assessment against one of the five tracks added at 1.1
was therefore being labelled with a version that did not contain that track.

The 398 assessments emitted between 2026-08-11 and 2026-08-30 keep their `v1.0`
stamp. **The stamp is not retroactive and must never be:** it records which version
was applied, and a corrected stamp would destroy the only evidence of what actually
scored those rows. Assessments from 2026-08-31 stamp `v1.1`.

A regression test now asserts that the engine constant, the scale, the normalisation
formula and the eight-track role set agree, so they cannot drift apart silently
again. The same bug had reached the signed credential narrative, which stated `v1.0`
inside an Ed25519-signed Open Badges 3.0 document that anyone can verify without
contacting CRLN; it now reads the constant.

### Registry correction

The framework registry listed **14** active roles while defining **8**. The six
extra tracks (QA, BIOS, MW, DCT, RN, PHARM, registered 2026-08-24) had zero
competency domains, zero weight and no scenarios. No learner ever saw them, because
every learner-facing query joins through the domain table and dropped them — which
is precisely why it went unnoticed. They are now marked inactive rather than
deleted, and `is_active` means what it says: **assessable**. A role becomes active
by acquiring competency definitions, not by being named. An integrity check now runs
with the platform's monitors and raises if any active role has no domains, or if any
role's weights stop summing to 1.0.

**These six roles are not part of 1.1 and are not claimed to be covered.**

### Domain codes are positional within a role

Added to the machine-readable spec in this release as a normative note, because it is the single
easiest way to misuse this framework, and we misused it ourselves:

> `D1`–`D6` are positional **within a role**. `D1` for a CRA and `D1` for a CDM are
> different competencies. Compare using the fully-qualified id
> (`CRLN-<ROLE>-<Dn>`), never the bare code.

Aggregating on the bare code silently averages unrelated competencies together.
The result is well-formed, in range, and wrong.

### Added to the record

- This change log.
- `crln-trg-001.json` — the machine-readable spec at 1.1, with all eight role
  tracks, weights validated to sum to 1.0, and the positional-domain-code note.
- `CRLN-TRG-001-ADOPT.md` — how to adopt and cite the framework under CC BY 4.0,
  and what is explicitly *not* licensed.

### Current status, unchanged

- Standards crosswalk (CRLN-TRG-001 ↔ JTF ↔ ICH E6(R3)) remains **provisional**
  pending SME sign-off. **0 of 31 items independently attested.**
- Of 200 jurisdictions, **39 are verified against primary sources**; the remaining
  161 record an inference and remain provisional.
- Status: `published-provisional`.
- Licence: CC BY 4.0 for the framework and crosswalk. The measurement engine, item
  parameters, calibrations and underlying data are proprietary and not licensed.

---

## 1.1 — 2026-08-21

Published: [10.5281/zenodo.22049550](https://doi.org/10.5281/zenodo.22049550)

**Additive. Non-breaking.** The domain taxonomy, the four-level performance scale,
the safety rule and the composite/readiness scoring rules are unchanged from 1.0.
A 1.0 score and a 1.1 score of the same role are directly comparable.

### What 1.1 adds

Five further role tracks, each with a complete six-domain competency definition,
weights summing to 1.0, safety-critical flags, a regulatory basis, and assessable
scenarios in the measurement engine:

| track | role | regulatory basis |
|---|---|---|
| CDM | Clinical Data Manager | ICH E6(R3) §5.5; GCDMP; CDISC; 21 CFR Part 11 |
| PM | Clinical Trial / Project Manager | ICH E6(R3) §5.0/§5.18; ICH E8(R1); FDA RBM |
| RA | Regulatory Affairs Specialist | 21 CFR 312/56; EU CTR 536/2014; ICH E6(R3) §3 |
| PV | Pharmacovigilance / Drug Safety Associate | ICH E2A/E2C/E2D/E2E; 21 CFR 312.32; GVP |
| PI | Principal Investigator / Sub-Investigator | ICH E6(R3) §4; 21 CFR 50/312; Declaration of Helsinki |

This takes the operational role×domain matrix from 18 competency ids across three
tracks (CRC, CRA, CTA) to **48 across eight**, `CRLN-CRC-D1` … `CRLN-PI-D6`.

## 1.0 — 2026-08 (initial open publication)

- Ten canonical competency domains, D-01…D-10, aligned to the ICH E6(R3) structure.
- Standards crosswalk: CRLN-TRG-001 ↔ JTF Clinical Trial Competency Framework ↔
  ICH E6(R3). **Marked provisional pending SME review.**
- Four-level performance scale (1 Critical Gap … 4 Exceeds), with a safety rule and
  composite/readiness-index scoring rules.
- Regulatory jurisdiction coverage across 200 jurisdictions, of which **39 are
  verified against primary sources** as of 2026-08-31 (the EU-27 under Regulation
  536/2014; ICH member jurisdictions; and the US, Canada, UK, Australia and Japan
  instruments individually). The remaining 161 record an inference that the
  jurisdiction relies on ICH E6(R3) as its GCP baseline and **remain provisional**.
- Licence: CC BY 4.0 for the framework and crosswalk. The measurement engine, item
  parameters, calibrations and underlying data are proprietary and not licensed.
- Status: `published-provisional`. Independent SME validation is in progress;
  **0 of 31 items have been independently attested** as of 2026-08-31.

## Related CRLN publications

- **CRLN-HB-001 — The Human Baseline** v0.2, published 2026-09-10.
  Version DOI [10.5281/zenodo.22690693](https://doi.org/10.5281/zenodo.22690693) ·
  concept DOI [10.5281/zenodo.22690692](https://doi.org/10.5281/zenodo.22690692).
  Declares CRLN-TRG-001 as `isDerivedFrom`. First CRLN release to carry a
  published human performance distribution.
- **The Competency Coverage Atlas** v0.1, published 2026-09-10.
  Version DOI [10.5281/zenodo.22691086](https://doi.org/10.5281/zenodo.22691086) ·
  concept DOI [10.5281/zenodo.22691085](https://doi.org/10.5281/zenodo.22691085).
  Declares CRLN-TRG-001 as `isDerivedFrom`. Reports that CRLN's own instrument
  covers five of the eight JTF domains and none of the other three.
- **Site Readiness Index** v0.1, published 2026-09-10.
  Version DOI [10.5281/zenodo.22690959](https://doi.org/10.5281/zenodo.22690959) ·
  concept DOI [10.5281/zenodo.22690958](https://doi.org/10.5281/zenodo.22690958).
  Declares CRLN-TRG-001 as `isDerivedFrom`. 20 countries at k>=5, published as a
  floor rather than an estimate.
- **Assessment Integrity Tests** v0.1.0, published 2026-09-10 via the
  GitHub-Zenodo integration. Version DOI
  [10.5281/zenodo.22691684](https://doi.org/10.5281/zenodo.22691684) · concept DOI
  [10.5281/zenodo.22691683](https://doi.org/10.5281/zenodo.22691683).
  Repo: https://github.com/jwebber-cmyk/assessment-integrity-tests
