# HireData Linear house conventions

Use the maintained team SOP and prioritization matrix as the source of truth. These conventions supplement them.

## Content

- Prefer plain, factual language and short sections.
- Match the workspace's established Title Case convention. Prefer **Area: Outcome or Problem** when a stable product area makes the backlog easier to scan, for example **Automations: HTTP Request Task** or **Responses: Add Score Calculation**. Do not force a prefix when the concise product name is clearer, such as **Form Evaluations**.
- Put each rule in one place; avoid repeating the description in the To do and acceptance criteria.
- Keep acceptance criteria outcome-level and testable.
- Separate facts, decisions, assumptions, and open questions.
- Link source material; do not make a prototype or AI-generated mock binding.
- Preserve customer-specific stages, field names, and values as customer configuration rather than HireData product vocabulary.

## Relations

- `blocked by`: work cannot proceed or complete without the other issue.
- `blocks`: the inverse of `blocked by`.
- `related to`: useful context or complementary work without a hard dependency.
- `duplicate/superseded`: confirm residual scope before closing or replacing an issue.

## Workflow

- Intake belongs in Triage unless instructed otherwise.
- An issue with unresolved blocking product decisions is refinement-ready, not build-ready.
- Implementation issues may name files, migrations, APIs, refactors, tests, and rollout steps when engineering supplied or verified them.
- Do not assign owners, dates, estimates, cycles, or priorities without a source or explicit authorization.

## Estimation readiness

The current HireData Linear scale is **XS = 1, S = 2, M = 3, L = 5, XL = 8**. Treat these as the workspace's relative estimation values, not as time commitments.

Do not assign or change an estimate unless engineering supplied it or the user explicitly requested the change. An issue is ready for **To Be Estimated** when:

- the user outcome and observable behaviour are clear;
- in-scope and out-of-scope work are explicit;
- blocking product decisions are resolved or deliberately deferred;
- dependencies, affected surfaces, required refactors, and material risks are visible;
- acceptance criteria and relevant evidence are present;
- engineering can size the work without reconstructing intent from a prototype or chat.

If these conditions are not met, recommend **To Be Refined** rather than inventing detail or an estimate.

Use the live [How Linear Statuses Work](https://www.notion.so/2dc00d874868809ca942d7f0382d29e4) page when status meaning matters. Current meanings:

- **Backlog:** valid work that is not planned.
- **Triage:** awaiting completeness, duplicate, and routing review.
- **To Be Refined:** missing product or technical information.
- **To Be Estimated:** approved and awaiting estimate.
- **Ready to Plan:** approved and awaiting scheduling.
- **To Do:** selected for the current cycle.
- **In Progress:** active implementation.
- **On Staging (Review):** code and functional review.
- **On Production (QA):** production verification.
- **Done – No Update:** complete without a public product update; notify relevant customers directly.
- **Done – Draft Update:** complete and awaiting a public update draft.
- **Ready to Publish / Published:** product update publication states.
