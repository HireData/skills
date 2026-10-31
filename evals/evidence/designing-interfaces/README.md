# Comparison-gate evidence — `designing-interfaces`

Records the `evals/RUBRIC.md` → Comparison gate for adding the `designing-interfaces` skill.
The skill is new, so the baseline is the same model answering without any skill.

## Method

- **Arms.** Baseline: the case prompt answered from the model's own knowledge, with skills disabled. Candidate: the same prompt answered after reading this skill and its references.
- **Contexts.** Six independent fresh contexts, one per case per arm. No context saw the other arm, the other cases, or this repository.
- **Randomization.** Per case, a `/dev/urandom` coin flip decided which arm became Output A. The map is in `blinding-map.txt`. All three draws happened to put the candidate in A; no reviewer saw the map.
- **Review.** One fresh context per case, given only the prompt, `evals/RUBRIC.md`, the case's `must` and `must_not` lists, and the two outputs as A and B. Reviewers scored "HireData and industry correctness" as interface-design correctness and "MCP use" as avoiding invented facts and stating assumptions, because the cases involve no HireData workspace. Verdicts are in `scores/`.
- **Un-blinding.** Done only after all three verdicts were written.

## Scores (0–2 per dimension, 12 max)

- **`designing-interfaces-dark-mode-fix` (normal):** baseline 10, candidate 12. Both met 7 of 7 must items. No critical failures.
- **`designing-interfaces-candidate-list-screen` (ambiguous):** baseline 10, candidate 11. Baseline met 6 of 8 must items and candidate 8 of 8. No critical failures.
- **`designing-interfaces-fitness-nav-and-paywall` (safety):** baseline 10, candidate 11. Baseline met 7 of 8 must items and candidate 8 of 8. No critical failures.
- **Average:** baseline 10.0, candidate 11.33.

## What separated the arms

- The candidate stated its assumptions up front and answered without stalling; the baseline ended the ambiguous case with clarifying questions.
- The candidate showed real dates in the candidate list and gave a reason for every change; the baseline kept relative times and left table basics unexplained.
- The candidate addressed thumb reach for profile and history in the fitness nav; the baseline kept the top-left avatar without discussing reach.
- Both arms rejected paywalling existing workout history, so neither introduced a safety failure.

## Known trade-off

Two reviewers lowered the candidate's efficiency because it cites principles as bare `P#` codes that mean nothing to a reader without the skill. This is the skill's documented output format; a later revision could name the principle alongside the number.
