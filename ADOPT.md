# Adopting CRLN-TRG-001

A guide for an organisation that wants to use this framework in its own training,
assessment or hiring — without CRLN's involvement and at no cost.

CRLN-TRG-001 is licensed **CC BY 4.0**. You may use, adapt, translate and build on
it commercially. You must credit it. You do not need permission, a contract, or a
conversation with us.

Concept DOI: [10.5281/zenodo.22049550](https://doi.org/10.5281/zenodo.22049550) ·
Change log: `CRLN-TRG-001-CHANGELOG.md`

---

## What you are adopting, and what you are not

**Licensed to you (CC BY 4.0):**
- The ten canonical competency domains (D-01…D-10)
- The crosswalk to the JTF framework and ICH E6(R3)
- The four-level performance scale and its level descriptors
- The regulatory jurisdiction mapping
- The machine-readable spec, `crln-trg-001.json`

**Not licensed, and deliberately so:**
- The measurement engine, item parameters and calibrations
- The scenario items themselves
- CRLN learner data

That boundary is the honest one: you can adopt the *framework* and score against it
however you wish. You cannot obtain CRLN's psychometric calibrations, because they
are the part that took real work and the part we sell. Nothing about the framework
requires them — the scale is designed to be applied by a human rater.

## Before you adopt: what is provisional

Adopting a standard means inheriting its maturity. As of the 1.0 publication:

- **The JTF and ICH crosswalk is provisional**, pending independent SME review. If
  you rely on a specific domain mapping for a regulatory or accreditation purpose,
  verify that mapping yourself.
- **39 of 200 regulatory jurisdictions are verified** against primary sources. The
  other 161 record an inference. Check your own jurisdiction before citing it.
- **0 of 31 assessment items have been independently attested.**

We would rather you discover this here than after building on it. If you need a
mapping firmed up for your jurisdiction, tell us — that is useful pressure and it
is how the provisional set shrinks.

## Four ways organisations use it

**1. As a curriculum spine.** Map your existing training modules to D-01…D-10 and
you can state coverage and gaps in terms an auditor or sponsor recognises. This is
the lowest-effort adoption and needs nothing from us.

**2. As an assessment rubric.** Use the four-level scale to score your own
scenarios, OSCEs or competency reviews. The level descriptors are written to be
applied by an experienced rater without training on our engine.

**3. As a common language between organisations.** A site network and a sponsor that
both express competency in D-01…D-10 can compare staff readiness without agreeing
on a shared training provider. This is the point of publishing it openly.

**4. As a credential others can verify.** If you would like your learners to earn a
CRLN-verifiable credential from your own programme, that requires integration
rather than adoption — see below.

## How to attribute

Minimum attribution under CC BY 4.0:

> Competency framework adapted from CRLN-TRG-001 (Clinical Research Learning
> Network), licensed CC BY 4.0. DOI: 10.5281/zenodo.22049550

If you adapt the domains or the scale, say so, and say how. An unmarked adaptation
that people take for the original is the one use that damages everybody, including
the next adopter.

## Implementation checklist

1. Read `CRLN-TRG-001-Standard-v1.1.md` (human) and `crln-trg-001.json` (machine).
2. Note the version you are adopting and record it. Published versions are
   immutable, so a stated version is a stable reference.
3. Check the crosswalk rows and jurisdiction rows you depend on, and note which are
   marked provisional.
4. Map your own material to D-01…D-10. Expect gaps; the gaps are the finding.
5. Add the attribution line wherever competency levels are reported.
6. If you publish your mapping, we would like to link to it. Openly published
   adoptions are how a standard becomes one.

## Integrating rather than adopting

If you want your learners assessed by CRLN's engine, or want to issue credentials
that resolve against CRLN's public verification endpoint, that is an integration
and not something the licence covers. It is free and it is not yet self-service:
`jwebber@crln-learn.com`.

## Reporting a problem with the framework

Errors in the crosswalk or the jurisdiction mapping are the most useful thing you
can send us, and they are why it is published in a flagged state rather than a tidy
one. Email `jwebber@crln-learn.com` with the domain or country, what you believe is
correct, and a primary source. Corrections are recorded in the change log and
credited unless you ask otherwise.

## Are you using this?

Please tell us: **standard@crln-learn.com**, or open a pull request against
[`ADOPTERS.md`](ADOPTERS.md).

We are asking because we genuinely cannot tell. CC BY 4.0 means you may use, adapt and
translate this without permission, without a contract and without notifying anyone, which is
the right licence and is not changing. The consequence is that **we cannot count our own
adoption.** Someone could be teaching from this framework today and we would never know.

So any adoption figure we publish is a floor rather than a count, and `ADOPTERS.md` is the only
evidence behind it. That matters beyond vanity: "how many organisations use it" is the first
question a ministry, a funder or a standards body asks, and "we don't know" is a worse answer
than a small number.

Being listed means you use the framework. It is **not** an endorsement of CRLN, it does not
imply you use our platform, and it creates no obligation. One row: organisation, country,
version, and one line on how it is used. Ask to be removed at any time and it happens the same
day, no questions.

A correction is just as welcome as a listing. If a mapping is wrong for your jurisdiction or
your practice, that is more useful to us than agreement.
