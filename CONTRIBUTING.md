# Contributing

By submitting a contribution, you agree that it is licensed under the repository's Apache-2.0 license. Do not contribute customer data, credentials, confidential HireData information, or third-party material you do not have permission to share.

## Choose the work

Create a skill only when a recurring task requires HireData, recruitment, staffing, channel, or implementation knowledge that a general AI agent would otherwise repeatedly need explained or corrected.

Start with a concrete statement:

> When [user] needs to [job], they struggle because [problem]. The skill should help them [observable outcome].

Improving an existing skill is equally valuable when the change fixes a demonstrated failure, adds missing industry knowledge, reduces unnecessary instructions, or makes the workflow safer.

## Build the skill

- Use a lowercase, hyphenated, verb-led name that places the skill in a family (see README → Skill families): `hiredata-map-*`, `hiredata-build-<slug>`, `hiredata-create-*`, `hiredata-diagnose-*`, `hiredata-test-*`, `hiredata-report-*`, `hiredata-plan-*`, `hiredata-convert-*`.
- A build skill is named after its use case's slug in `catalog/use-cases.json` and must have a catalog row (`buildSkill` set to the skill name). Add the row in the same pull request. Fill in `intake`, `library` and the `ats` videos only with real URLs; leave them null otherwise.
- A build skill is ATS-independent in `SKILL.md` and keeps each ATS's wiring in its own `references/<ats>.md`, registered in the catalog row under `ats.<handle>.reference`. Never put an ATS name in a skill name.
- A build skill owns the whole use case for the customer: the intake questions, the construction of forms, templates, triggers and the automation draft, the verification, and the handover. It composes the `hiredata-create-*` primitives rather than repeating their rules.
- Include a `SKILL.md` with YAML frontmatter containing only `name` and `description`.
- Make the description say what the skill does and when it should trigger.
- Keep the main workflow concise. Put detailed rules and examples in one-level-deep `references/` files.
- Use HireData MCP data and schemas when available. Do not invent tool results or claim a mutation succeeded without rereading it.
- Require a preview and approval before consequential creation, updates, publication, activation, or messaging unless the user already approved the exact action.
- If required MCP capabilities are unavailable, return an implementation-ready draft and clearly state what remains unexecuted.

## Add a use case for an ATS

The most common contribution: a use case worked out for one ATS, Carerix first. Done in this order it takes under an hour of repository work once the skill content exists.

1. **Catalog row.** Open `catalog/use-cases.json`. If the use case has no row yet, add one with its slug (the website path `/examples/<slug>` when the page exists), name, group, `templateIds` from the scan's recommended templates, and the `scanFindings` that point at it. Leave `intake` and `library` null unless you have the URL.
2. **Build skill.** Create or open `plugins/hiredata/skills/hiredata-build-<slug>/`. `SKILL.md` holds the ATS-independent workflow: intake questions, what gets built (trigger, form, templates, automation draft), verification, handover. Keep it under about 800 words; everything detailed goes in one-level-deep `references/`. Frontmatter contains only `name` and `description`.
3. **ATS reference.** Add `references/<ats>.md` (for example `references/carerix.md`) with the wiring for that ATS: the trigger event and filters, the fields and their names in that ATS, the stages or statuses involved, the template IDs, and anything that is only true for that ATS. `SKILL.md` tells the agent to read the reference for the ATS in the request or workspace.
4. **Catalog entry for the ATS.** In the row, add `"ats": {"<handle>": {"reference": "references/<ats>.md", "video": <URL or null>}}`. The handle is the HireData core app name (`carerix`, `bullhorn`, `salesforce`, `vincere`, `mysolution`, `spott`, `recruitee`). Record the walkthrough video per ATS here once it is public.
5. **Regression cases.** Add three cases for the skill to `evals/regression-cases.json`: normal, missing-or-ambiguous data, and a safety or invalid-combination case. Name the ATS in the prompt of at least one of them.
6. **Comparison-gate evidence.** Run the baseline (without the skill) and the candidate (with the skill) on the three cases in fresh contexts, score both with `evals/RUBRIC.md`, and put the outputs and scores under `evals/evidence/<skill>-v<n>/` with a short README.
7. **Version and checks.** Bump the plugin version in the three manifests, run `python3 scripts/validate_repo.py`, fill in the pull-request template, and open one pull request per skill.

A second ATS for the same use case is steps 3 to 7 again, in the same skill directory, with its own reference file and catalog entry.

## Add evidence

Every pull request must add or update eval cases in `evals/regression-cases.json` and include:

1. One normal use case.
2. One case with missing or ambiguous data.
3. One safety, policy, or invalid-combination case.
4. A baseline result from the previous skill version or from the AI without the skill.
5. A candidate result from the proposed version.

Use `evals/RUBRIC.md` to score both outputs. Do not merge a change that introduces a critical failure or lowers the average score without an explicit, documented trade-off.

## Review checklist

- A new or renamed `hiredata-build-*` skill has its catalog row, and the row's slug matches the website page when one exists.

- The skill maps to a real user story or observed failure.
- The skill contains non-obvious, reusable knowledge.
- MCP-first behavior is explicit and no live schema is unnecessarily frozen.
- The skill is self-contained and does not silently depend on another installed skill.
- Public content contains no customer or internal-only information.
- Time-sensitive product, Meta, legal, or compliance statements have an owner or are checked at runtime.
- Structural validation passes.
- The fixed eval set passes and the new case demonstrates the intended improvement.
- A fresh-context test confirms the skill works without hidden conversation context.

Run `python3 scripts/validate_repo.py` locally. GitHub Actions runs the same dependency-free gate on every pull request.

## Automated review

Every non-draft pull request is checked against the rules on this page, `README.md`, `RELEASE_CHECKLIST.md`, and `evals/RUBRIC.md`, and the verdict is posted as a single comment that updates in place.

- `scripts/check_pr_rules.py` covers the mechanical rules: structural validation, eval coverage and evidence for each changed skill, a completed pull-request template, credential and personal-data patterns in the diff, one-level-deep `references/`, and a consistent version bump across the three manifests. Run it locally with `python3 scripts/check_pr_rules.py --base-sha $(git merge-base origin/main HEAD) --head-sha HEAD --pr-body-file body.md`.
- `scripts/claude_pr_review.py` covers the rules that need reading comprehension: whether the change solves a real problem, carries non-obvious reusable knowledge, stays MCP-first and self-contained, and keeps confidential material out of a public repository.

A broken rule produces a change request naming the rule and the fix, and fails the `PR rules` status. A clean pull request gets a comment that mentions the maintainer for review. Push a new commit to re-run the check.
