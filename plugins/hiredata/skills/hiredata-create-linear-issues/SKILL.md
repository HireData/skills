---
name: hiredata-create-linear-issues
description: Draft, refine, or rewrite HireData Linear issue content so it is correctly routed, refinable, estimatable, and usable by developers and coding agents. Use when turning a bug, customer request, prototype, demo, meeting note, or technical prompt into a Linear issue; when writing or repairing an issue description, scope, acceptance criteria, implementation plan, or delivery note; or when preparing an issue for refinement. Do not trigger merely because an HD-#### issue is mentioned or for routine status, assignment, priority, or relationship changes.
---

# Write HireData Linear issues

Create the smallest issue that is complete for its current maturity. Do not turn every request into a build-ready specification.

## 0. Determine access and authority

This is one HireData-specific skill for the HireData team and approved partners. Do not weaken the issue-writing method based on audience. Instead, use the sources the user is authorized to access:

- **HireData team:** use the live HireData Linear workspace and internal Notion SOPs when connected.
- **Approved partner:** use any HireData project, Linear, or Notion pages shared with that partner, plus the bundled references. A partner may help refine or manage issues where HireData has explicitly granted access.
- **No live workspace access:** use the bundled references to produce a complete report for the agreed HireData support or partner channel. Mark live metadata, duplicates, relationships, and policy freshness as unverified.

Never broaden access, share a page, or mutate Linear merely because this skill is installed. Existing HireData, Linear, and Notion permissions determine what the user can read or change.

## 1. Read before writing

Use the connected Linear MCP or other available Linear tooling for live operations. Read the current issue, relations, comments, attachments, customer request, and relevant related issues before rewriting or creating anything.

Always read:

- `references/issue-sop.md`
- `references/house-conventions.md`

Before assigning priority, read `references/prioritization-matrix.md`.

The reference files identify their canonical Notion sources. When Notion is connected and the user can access them, fetch the live source if the cached reference may be stale—especially for status, priority, ownership, or workflow metadata. Follow the designated canonical source. If a page is inaccessible, use the bundled snapshot and mark policy-dependent metadata as unverified. If live pages conflict and neither is designated canonical, identify the conflict and preserve the current issue metadata until the process owner confirms the governing source.

Search Linear for duplicates and related work before creating an issue when the user has access. Discuss whether to relate, block, supersede, or update existing issues. Do not create or mutate Linear unless the user requested that action and has authority in that workspace.

## 2. Route the issue by maturity

Choose one route and read its template:

| Route | Purpose | Reference |
|---|---|---|
| Intake | Capture and route a bug, request, or improvement | `references/intake-template.md` |
| Product specification | Define the product intent and refinement decisions | `references/specification-template.md` |
| Implementation | Record the engineering plan, affected layers, migration, tests, and rollout | `references/implementation-template.md` |
| Delivery | Record what actually changed and what must be verified or communicated | `references/delivery-template.md` |

Do not combine specification and implementation merely to make an issue look complete. A large feature can have a product specification plus one or more linked implementation issues.

## 3. Match the readiness level

- **Intake-ready:** another person can understand, reproduce or route it.
- **Refinement-ready:** product intent, scope, evidence, dependencies, and blocking decisions are visible. Refinement can focus on decisions instead of reconstructing the request.
- **Build-ready:** no blocking product questions remain; engineering has a credible implementation and test plan.

If blocking questions remain, collect them in one section and recommend a refinement state. Do not disguise assumptions as requirements or move an issue toward implementation readiness prematurely.

## 4. Apply feature-refinement guardrails

For product specifications and complex improvements:

1. Describe the behaviour so it remains understandable without opening a prototype. Treat prototypes as visual/workflow references, never as the product contract.
2. Separate generic product behaviour from customer-specific wiring and verification.
3. State whether related capabilities are independent, mutually exclusive, or ordered.
4. Cover the relevant path: configuration, execution, storage, presentation, reporting, automation, failure handling, regression, and rollout. Mark irrelevant or deferred surfaces explicitly out of scope.
5. Name required refactors that materially affect scope, but leave schema and implementation choices to engineering unless engineering supplied them.
6. Verify dependencies. Distinguish `blocked by` from `related to` and from a customer delivery sequence.
7. Decide product terminology before it becomes API/schema naming. Keep HireData display vocabulary separate from customer ATS values.
8. State each rule once. Keep acceptance criteria outcome-level rather than repeating the full description.

For AI-, rule-, mapping-, or input-type-dependent features, additionally:

- separate deterministic/mechanical behaviour from model-judged behaviour;
- state when each runs and how failures differ;
- show the decisions that affect the data model, preferably as a configuration matrix by input/output type;
- identify what steers the model and what remains deterministic;
- call out prototype content that is inconclusive or likely invented instead of making it binding.

Read `references/refinement-feedback.md` when refining a complex feature or when a prototype was the primary source. Read `references/worked-example.md` when the distinction between product specification and implementation is unclear.

## 5. Apply metadata and workflow

Follow the approved SOP and prioritization matrix for status, priority, assignee, project, label, cycle, customer request, source links, and evidence.

For partners, apply internal metadata only when the governing page or shared project workflow explicitly authorizes it. Otherwise describe impact, reach, workaround, and time sensitivity and leave HireData's internal routing decision to Triage.

Default safeguards:

- leave assignee empty unless ownership is known;
- leave cycle empty unless instructed;
- use Triage for new intake issues unless the team workflow says otherwise;
- use Medium priority when the SOP explicitly permits it and no approved matrix result is available;
- attach screenshots, videos, URLs, and customer/source links;
- retain prototypes and signed-off artifacts as evidence even when they are no longer the implementation contract.

## 6. Final check

Before submitting, verify:

- Is the issue using the correct route and template?
- Can it be understood without reconstructing intent from linked artifacts?
- Are known facts, decisions, assumptions, and open questions distinguishable?
- Are customer use cases separated from reusable behaviour?
- Are dependencies and related issues accurate?
- Is the requested readiness level honest?
- Can refinement focus on product/technical decisions rather than decoding the issue?
- For build-ready work, can a developer or coding agent start without inventing missing requirements?
- Did the output use only sources and live actions available within the user's existing permissions?

When updating an existing issue, summarize what changed and which metadata was deliberately left untouched.
