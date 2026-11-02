# Comparison-gate evidence: `hiredata-create-linear-issues` formatting and shape update

Records the `evals/RUBRIC.md` comparison gate for the change that adds `references/formatting.md`, makes the issue
templates fit the kind of issue, moves open questions to comment threads, adds a write step with anchored patches,
reshapes the delivery template around update comments, and refreshes the status list.

## Why the change was needed

- **Kind drift:** the previous version routed every new request through the intake template, so feature requests
  got a "Steps to reproduce" section and empty template sections.
- **Rendering:** the skill said nothing about how Linear renders text. Measured in the Linear web app: a body line
  wraps after 103 to 113 characters, a newline inside a paragraph shows as a forced break, a bare issue key adds a
  Related relation, and rewriting a whole body turns customer, project, document, and label mentions into links.
- **Updates:** the delivery template had no guidance for update comments, which is where delivered work is recorded.
- **Statuses:** the cached status list named statuses that no longer exist and missed To Be Tested and the
  Done variants.

## Method

- **Arms:** **prev** is the skill as committed on `main`; **cand** is the proposed version. Each arm got the same
  prompt and a copy of its own skill folder, with no Linear or other tools connected.
- **Contexts:** twelve independent `claude -p` runs, one per case per arm.
- **Randomization:** a `/dev/urandom` coin flip per case decided which arm became Output A. Map in
  `blinding-map.txt`.
- **Review:** one fresh context per case, given only the rubric, the case's `must`/`must_not`, the prompt, and the
  two anonymized outputs. The three new cases also got three Linear rendering facts as ground truth. Verdicts are in
  `scores/`.
- **Redaction:** one output named the requester in an attribution line; it is replaced with `[requester]`.
  Names of former process owners that the outputs copied from the skill are replaced with `[process owner]`.

## Scores (0 to 2 per dimension, 12 max)

| Eval case | Previous | Candidate | Critical failures |
|---|---:|---:|---|
| `linear-issue-feature-shape` (new) | 7 | 11 | Previous: bug template on a feature. Candidate: none. |
| `linear-issue-update-numbering` (new) | 6 | 11 | Previous: edits an earlier update, no attribution. Candidate: none. |
| `linear-issue-rewrite-keeps-mentions` (new) | 5 | 11 | Previous: says mentions survive a full rewrite. Candidate: none. |
| `linear-issue-normal` | 11 | 10 | None either arm. |
| `linear-issue-prototype-ambiguity` | 11 | 12 | None either arm. |
| `linear-issue-false-urgency` | 10 | 11 | None either arm. |
| **Average** | **8.33** | **11.00** | |

The candidate improves every new case and two of the three stable cases. On `linear-issue-normal` it scored one
point lower on efficiency because its reply was slightly longer; this is a single sample, not a workflow error.
The candidate introduces no critical failure.
