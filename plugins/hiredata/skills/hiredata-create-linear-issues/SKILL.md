---
name: hiredata-create-linear-issues
description: Draft, refine, or rewrite HireData-compatible issue reports so they are understandable, correctly scoped, and ready for intake, refinement, implementation, or delivery review. Use when turning a bug, customer request, prototype, recording, meeting note, or technical prompt into an issue report, or when repairing an issue that developers or coding agents cannot act on safely.
---

# Write HireData issue reports

Create the smallest issue report that is complete for its current maturity. Do not turn every request into a build-ready specification.

## Choose the operating mode

- **Customer or partner:** produce a report the user can send to HireData. Do not guess HireData's internal priority, status, assignee, estimate, cycle, or planning decision.
- **Authorized HireData workspace:** use the connected Linear MCP or other available Linear tooling to inspect live issues and relations. Create or update an issue only when the user explicitly requests that action.

If access or authority is unclear, draft only and state what remains unverified.

## Workflow

1. Read [references/issue-writing-guide.md](references/issue-writing-guide.md).
2. Collect the affected user or account, environment, source message, URLs, screenshots or recordings, reproduction steps, actual result, expected result, frequency, impact, workaround, and last-known-good state when available.
3. Search for duplicates and related work when the connected tools permit it. Distinguish a blocker from related or follow-up work.
4. Choose one route and read its template:
   - intake: [references/intake-template.md](references/intake-template.md);
   - product specification: [references/specification-template.md](references/specification-template.md);
   - implementation: [references/implementation-template.md](references/implementation-template.md);
   - delivery: [references/delivery-template.md](references/delivery-template.md).
5. Separate known facts, decisions, assumptions, and open questions. Do not invent product behaviour, technical decisions, customer importance, or acceptance criteria.
6. For a complex feature or prototype-led request, also read [references/refinement-guide.md](references/refinement-guide.md).
7. Return a complete draft before any live mutation unless the user already approved the exact issue action in the current conversation.
8. After an authorized live change, reopen the issue and verify its title, content, relations, and requested metadata. Summarize what changed and what was deliberately left untouched.

## Readiness

- **Intake-ready:** another person can understand, reproduce, and route the report.
- **Refinement-ready:** product intent, scope, evidence, dependencies, and blocking decisions are visible.
- **Build-ready:** no blocking product questions remain and engineering has supplied or verified the implementation direction and test plan.

When blocking questions remain, collect them in one section. Do not disguise assumptions as requirements or technical choices.

## Guardrails

- Treat prototypes as visual and workflow references, not as the product contract.
- Keep reusable HireData behaviour separate from customer-specific configuration and verification.
- Separate deterministic behaviour from model-judged behaviour when both exist.
- State whether related capabilities coexist, are mutually exclusive, or run in order.
- Cover or explicitly defer configuration, execution, storage, presentation, reporting, automation, failure handling, regression, and rollout when those surfaces matter.
- Keep acceptance criteria observable and outcome-level. State each rule once.
- Retain source artifacts as evidence even when they are not authoritative.
- Do not infer urgency from tone, company size, a customer name, or an arbitrary deadline.

## Output

Provide:

1. proposed title;
2. route and honest readiness level;
3. issue description using the selected template;
4. missing information or open decisions;
5. duplicate, relation, or dependency recommendations when verified;
6. proposed metadata only where an approved source supports it;
7. for rewrites, a short change summary and the metadata left untouched.

The reporter remains accountable for the facts and evidence. AI-assisted does not mean automatically approved.
