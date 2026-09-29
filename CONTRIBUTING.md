# Contributing to CRLN-TRG-001

Anyone may propose a change. No account, affiliation or fee is required. You can open an
issue in this repository or email `standard@crln-learn.com`; both are treated the same.

This file explains **what** you can propose and **what happens next**. The rules for
deciding are in [`GOVERNANCE.md`](GOVERNANCE.md), and where the two differ, GOVERNANCE.md
wins.

## Before you start: who decides today

CRLN-TRG-001 is custodied by the Clinical Research Learning Network, a sole-founder
organization. The Methodology Review Board described in GOVERNANCE.md section 2 is **not
yet constituted** (one of five seats is filled), so changes are approved by the custodian
on subject-matter expert (SME) review, and every release says so in `CHANGELOG.md`. We say
this first so that nobody contributes believing a board will rule on their proposal.

## What you can propose

| You want to | Use | Reviewed by |
|---|---|---|
| Correct a mapping: a competency domain mapped to the wrong ICH E6(R3) section, JTF domain, TDR competency or EU CTR article, or a wrong verdict (full, partial, none) | Issue template **Mapping correction** | Citation and structural errors: the custodian, treated as urgent. A changed verdict: SME review |
| Propose a new crosswalk to another framework or regulation | Issue template **Crosswalk proposal** | SME review. A new crosswalk is published as *provisional* until reviewed |
| Contribute a term list for a language | Issue template **New language term list** | A named reviewer for that language (see below) |
| Declare that your organization uses the framework | Issue template **Declare that you use CRLN-TRG-001** | Listed as declared; we do not audit |
| Change a competency, a domain, the rating scale or the weights | Email `standard@crln-learn.com` or a blank issue, citing the evidence | SME review, then a minor or major version |
| Report a defect in wording, a broken link or a typo | A blank issue or a pull request | The custodian |

## What happens next (GOVERNANCE.md section 4)

1. **Acknowledgement within 10 working days**, with a decision on whether it proceeds to
   review.
2. **Review.** SME review where the change affects competency content or a mapping verdict;
   custodian review for editorial, citation or structural changes.
3. **Decision:** accepted, accepted with modification, deferred, or declined, **with reasons
   published in `CHANGELOG.md`**.
4. **Release.** Accepted changes appear in the next version, with you credited unless you ask
   otherwise. Published versions are immutable; a correction is a new version with its own
   DOI.
5. **Appeal.** If you think a decision was wrong, ask for review within 60 days
   (GOVERNANCE.md section 5).

Corrections of fact, such as a mis-cited regulation, do not wait for a scheduled release.

## Crosswalks and mappings

A crosswalk row **is** the claim: there is no answer key behind it, so the reviewers are the
only check. That shapes how we handle them.

- **Every crosswalk is provisional until reviewed.** The JSON crosswalks in `crosswalks/`
  carry `"status": "provisional-unreviewed"`. Nothing about the review of the competency
  domains extends to them.
- **Say why.** A proposed correction must give the regulatory or evidential basis: the
  section, article or competency text, and what it actually says. "This mapping is wrong"
  without a reason cannot be acted on.
- **Quote the primary source.** Cite the adopted text (for ICH, the Step 4 guideline on
  database.ich.org), not a summary or training slide. ICH E6(R3) Annex 1 numbering differs
  from E6(R2); a section number carried over from R2 is the most common defect we have fixed.
- **Keep summary and rows in step.** Each crosswalk opens with a summary count. If your
  change moves a row between full, partial and none, change the summary too, then run:

  ```
  python3 tools/check_crosswalks.py
  ```

  It checks that every summary matches its own rows, and that every CRLN id a JSON crosswalk
  maps to exists in `crln-trg-001.json`. It exits 1 on drift and 2 if a crosswalk cannot be
  verified, which is not a pass. It runs on every pull request.

## Language term lists

Machine translation of clinical research text fails fluently: a rendering can read well and
say something different. A per-language term list tells translators which rendering to use
for each concept and which renderings change the meaning. The format is
[`terminology/crln-terminology.schema.json`](terminology/crln-terminology.schema.json).

- Start from [`terminology/crln-terms-TEMPLATE.json`](terminology/crln-terms-TEMPLATE.json).
  Copy it to `crln-terms-<language code>.json` and replace every value.
- **Rows you write are `proposed`.** Only a named reviewer who works in clinical research in
  that language can make a row `confirmed` or `keep_en`. Those two statuses are binding on
  translators, so they require a reviewer and a review date.
- **A reviewer is named only with their consent**, in the words they choose. Until then,
  `reviewer` stays `null`.
- **Do not paste assessment item text.** `source_en` is optional. If you give an example
  sentence, take it from `STANDARD.md` or write your own; never paste a question, scenario or
  answer option from any CRLN assessment or practice tool.
- Validate before opening a pull request, and render a readable glossary if you want one:

  ```
  python3 tools/check_terminology.py
  python3 tools/render_glossary.py terminology/crln-terms-<lang>.json
  ```

English is authoritative for the standard itself (see `translations/README.md`).

## What this repository does not contain, and will not accept

The framework, its crosswalks and its tooling are published here under CC BY 4.0. Some
things are deliberately **not** published, because publishing them would destroy the
measurement the framework supports:

- assessment items, scenarios, or answer options;
- scoring keys, rubric keys, or which option in any item scores highest;
- held-out evaluation sets or anything derived from them;
- any learner's data.

Pull requests or issues containing these will be closed and the content removed. If you
believe you have found such material published anywhere, email `standard@crln-learn.com`.

## Conflicts of interest

If you or your organization would be materially affected by a change you propose or review,
say so in the issue. GOVERNANCE.md section 3 explains how disclosures are handled. The
custodian's own commercial interest is disclosed there too.

## Validators and adopters are different things

A **validator** reviewed the framework; an **adopter** uses it. `ADOPTERS.md` keeps them
apart deliberately, and contributing a correction does not make you either, unless you ask
to be listed and meet the description.

## License

By contributing, you agree that your contribution is licensed under CC BY 4.0, the same as
the framework, and that you will be credited in `CHANGELOG.md` unless you ask not to be.
