# DPG Standard screening answers — CRLN-TRG-001

Prepared 2026-09-21 for nomination to the Digital Public Goods Alliance registry.

**What is being nominated:** CRLN-TRG-001, the competency framework, as a
**standard**. Type `standard` under the DPG schema.

**What is not being nominated:** the CRLN platform. The four applications, the
Readiness Index engine, the item bank and the scenario content are proprietary
and remain so. Nominating them would fail indicator 2 on the first check, and
claiming otherwise would be dishonest. The standard is separable by design, and
`NOTICE.md` draws the line in public.

---

## 1. Relevance to Sustainable Development Goals

Claimed: SDG 3 (target 3.c health workforce), SDG 4 (target 4.4 relevant
skills), SDG 8 (target 8.5), SDG 10 (target 10.3). Evidence text and URLs are in
`dpg-nominee.json`.

## 2. Use of an approved open licence

**CC BY 4.0**, SPDX `CC-BY-4.0`, which is on the DPGA approved list for content
and standards.

`LICENSE` is now the verbatim Creative Commons legal code so that automated
licence detection resolves it. `NOTICE.md` states the scope: the framework,
specification, machine-readable form, crosswalks, documentation and translations
are covered; the measurement engine, item parameters, calibrations, scenario
content and learner data are not, and are not required to implement the standard.

## 3. Clear ownership

Yes. Owned by Clinical Research Learning Network LLC, a Florida limited liability
company, EIN 99-2279850, UEI YZL8XNJLRAZ3.

Documented in `LICENSE`, `NOTICE.md`, and the custodian section of
`GOVERNANCE.md`. Author identified by ORCID 0009-0005-2538-8333.

Ownership URL: https://github.com/jwebber-cmyk/crln-trg-001/blob/main/NOTICE.md

## 4. Platform independence

**No mandatory proprietary dependency.** This is the indicator most likely to be
probed, because the publisher sells a product in the same space, so the answer is
given in full.

Implementing CRLN-TRG-001 requires no CRLN software, no licence, no contract and
no conversation. Everything needed to apply it is in the open files:

- the role spine and the ten canonical competency domains (`STANDARD.md` §2)
- the weighted competency statements, 84 of them across 14 role tracks
  (`crln-trg-001.json`)
- the four-level rating scale (`crln-trg-001.json`, `scale`)
- the scoring rules, pass threshold, conditional-pass threshold and safety rule
  (`crln-trg-001.json`, `scoring`)
- the ICH E6(R3) Annex 1 and JTF crosswalks (`STANDARD.md`)

The CRLN Readiness Index engine is one implementation of that scoring, not a
precondition for it. An implementer can score on paper.

## 5. Documentation

Yes, in the repository:

- `STANDARD.md` — the framework, human-readable
- `SPEC.md` — the specification
- `crln-trg-001.json` — the machine-readable form
- `ADOPT.md` — how to use it in training, assessment or hiring
- `GOVERNANCE.md` — how changes are decided, the review board, the
  conflict-of-interest register
- `CHANGELOG.md` — every version and why it changed
- `translations/` — Spanish, Brazilian Portuguese and Simplified Chinese, marked
  unofficial with English authoritative

Immutable versioned releases with per-version DOIs on Zenodo. Concept DOI
10.5281/zenodo.22049549 always resolves to the latest.

## 6. Mechanism for extracting non-PII data

Yes, and it is the whole artifact. The standard is non-PII content by
construction. It is obtainable by `git clone`, by direct file download from the
repository, or from Zenodo under the DOI, in both human-readable Markdown and
machine-readable JSON. No account, no API key, no rate limit.

## 7. Adherence to privacy and applicable laws

The standard itself collects, stores and transmits nothing. It has no users, no
runtime and no telemetry. There is no privacy surface to comply with.

The publisher separately operates a training platform which does process personal
data, under a published privacy policy at https://crln-learn.com/privacy and
terms at https://crln-learn.com/terms, with a documented GDPR legitimate-interests
assessment and an opt-out route. That platform is not part of this nomination,
and no learner data of any kind is present in, derived from, or required by the
standard.

## 8. Adherence to standards and best practices

Standards the framework aligns to, with the crosswalk published rather than
asserted:

- **ICH E6(R3) Annex 1** — section anchors verified against the adopted guideline.
  Crosswalk SME-VALIDATED 2026-09-21 by three independent reviewers who agreed on all
  ten canonical domains, named with consent in `GOVERNANCE.md`
- **Joint Task Force for Clinical Trial Competency Framework**
- **TDR Global Competency Framework for Clinical Research** (UNICEF/UNDP/World Bank/WHO,
  2016) — crosswalk published 2026-09-22 in `crosswalks/`. PROVISIONAL and unreviewed
- **ICH E6(R3) Annex 2** (adopted 2026-06-03, in force 2027-01-15; decentralised and
  pragmatic elements, real-world data) — crosswalk published 2026-09-22. PROVISIONAL
- **Regulation (EU) No 536/2014** — crosswalk published 2026-09-22 covering the 32 of 99
  articles that impose duties on individuals in trial roles. PROVISIONAL
- ACRP and SOCRA relevance noted per domain

**Each crosswalk is machine-readable as well as human-readable, and each is referenced
from `crln-trg-001.json` so a consumer of the spec can find them without reading prose.**

**Each one is published with what it found MISSING from this framework**, which is the
point of doing them: TDR surfaced the absence of community engagement, Annex 2 the absence
of real-world data, and EU CTR the absence of vulnerable-population and non-standard
consent. `proposals/PROPOSAL-001` sets out the resulting change and explicitly does not
adopt it, because the Board cannot yet approve it.

Practices followed:

- SPDX licence identifier
- semantic versioning, with an append-only public change log
- immutable releases with DOIs, so a citation cannot silently drift
- ORCID author identification
- a public correction record: where an earlier release cited ICH E6(R2) section
  numbers under an E6(R3) label, and where this repository named the wrong
  concept DOI, both are recorded as corrections in `CHANGELOG.md` rather than
  quietly edited

## 9. Do no harm by design

**Overall.** Yes. The specific harm this artifact could do is being believed more
than it has earned, because a competency standard that looks authoritative can be
used to gate someone out of a job. The mitigations are disclosure rather than
restriction:

- Release status is `published-provisional` and every release says so. The
  crosswalk has had subject matter expert review; the Methodology Review Board
  has one seated member and has not reached quorum. `GOVERNANCE.md` states this
  plainly, including that §6 of an earlier version claimed a standing board that
  did not exist, and that the sentence was withdrawn.
- The positional-domain trap is documented in the machine-readable form:
  codes D1 to D6 mean different competencies in different roles, and comparing
  bare codes across roles produces wrong scores. This is called out in
  `domain_code_semantics` because it has caused real mis-scoring.
- Translations are marked unofficial with English authoritative, so a
  mistranslation cannot become the operative text.
- Adoption is not counted or claimed. `ADOPTERS.md` explains that under CC BY the
  publisher cannot know who uses the framework, so any number it publishes is a
  floor and not a count.

**9.a Data privacy and security.** The project collects and stores no personally
identifiable information. Not applicable.

**9.b Inappropriate and illegal content.** The project distributes one
specification document and its translations. It hosts no user-submitted content
and has no upload path, so there is nothing to moderate.

**9.c Protection from harassment.** The project facilitates no interaction
between users. There are no accounts, no comments and no messaging. Contribution
is by pull request or email to `standard@crln-learn.com`, governed by
`GOVERNANCE.md`.

## Locations

- **Developed in:** United States
- **Deployed in:** United States, declared conservatively. The standard is
  applied inside the publisher's own platform, which has registered learners in
  67 countries, but third-party adoption is unverifiable by design: CC BY permits
  use with no notification. `ADOPTERS.md` is a voluntary register and is
  currently empty. Listing countries we cannot evidence would be the wrong answer
  to give a registry.

---

## Known weaknesses a reviewer will find, stated here first

1. **Provisional status, and it is now more mixed than it was.** The competency crosswalk
   to ICH E6(R3) Annex 1 and the JTF framework is SME-validated but not board-ratified.
   The three crosswalks added 2026-09-22 (TDR, ICH E6(R3) Annex 2, EU CTR 536/2014) are
   PROVISIONAL and have had NO review of any kind: they are the custodian's judgement
   alone. They are labelled as such in their first line, in the change log, and in the
   machine-readable spec. A reader must not treat them as carrying the validation the
   competency crosswalk carries.
2. **The framework has known, published gaps.** Three crosswalks each found something
   missing, and none is fixed: community engagement, real-world data, and consent for
   vulnerable populations. These are disclosed rather than repaired because repairing them
   is a MINOR version change requiring review the Board cannot currently give.
3. **A jurisdictional imbalance, measured and recorded.** An audit of all 84 competency
   statements found roughly 37 references to US federal sources against one to EU CTR
   536/2014 before the crosswalk existed. A framework describing itself as global while
   citing one jurisdiction forty times and another once was not yet global.
4. **Board below quorum.** One seated member. A chair and three further members
   are still required, including psychometric expertise and low- or
   middle-income country representation.
5. **No independent adopters on the public register.** Real, and structural
   rather than hidden.
6. **The publisher sells a product built on the standard.** Addressed under
   indicator 4: the open files are sufficient to implement without it.

None of these are disqualifying under the DPG Standard. All of them are worse if
a reviewer finds them before we say them.

## Submission status

**Already submitted.** Application **GID0094193** was filed on 2026-09-08 through
`app.digitalpublicgoods.net` and is in the DPGA review queue. A DPGA portal
account exists.

**Checked 2026-09-21, and the worry was unfounded.** The submitted application
describes "10 competency domains, 84 weighted competency statements" and does not
state a role-track count at all. It was written from the engine, which has carried
fourteen roles and 84 statements throughout. It was the *published* standard that
was stale at eight and 48 until release 1.7.0, not the application. The submission
was right and the public documents were wrong, which is the reverse of what was
assumed here.

**The application is read-only while under review.** Every section renders without
input fields or a save control, so nothing in it can be corrected from the portal.

**What the application genuinely lacks** is this repository. It cites the Zenodo
record only, because the public repository did not exist when it was submitted, and
the "other repositories" field is empty. So the machine-detectable licence, NOTICE.md
and this screening document are all invisible to a reviewer working from the form.
That was sent to `support@digitalpublicgoods.net` as supplementary evidence rather
than as a request to change an answer.

The repository the application points at was corrected on 2026-09-21: the CC BY
4.0 licence is now machine-detectable, the PDF is rebuilt at the current release,
and this file was added.

**The pull request route no longer exists.** `DPGAlliance/publicgoods-candidates`
was archived on 2026-08-31 and is read-only. The DPGA's own `CONTRIBUTING.md`
still describes it. A 404 on `nominees/<name>.json` there is not evidence that a
project has not been nominated, because nominations no longer land in that
repository at all. That inference was made here once and was wrong.

The nominee JSON in this repository stays as the canonical record of the
submitted facts and still validates against the DPGA's published schema.
