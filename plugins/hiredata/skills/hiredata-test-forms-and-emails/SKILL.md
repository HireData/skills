---
name: hiredata-test-forms-and-emails
description: Use when someone is about to activate, publish, or hand over a HireData form or email template, or asks for one to be checked, reviewed, QA'd, or tested before it goes live. Audit a HireData form or email template before activation by inspecting it live via the HireData MCP, building a scenario matrix of normal, missing-or-ambiguous, and invalid inputs, and checking variables, modifiers, fallbacks, branching, required fields, recipient context, language, and spacing; returns evidence, severity, and a suggested fix per finding, marks each check as verified or needing manual verification, and never activates, publishes, sends, or mutates anything without separate explicit approval for that exact action.
---

# Form & Email QA (HireData)

Recruitment forms and emails almost always *look* correct in the builder — the bugs show up at runtime, when a real recipient with a real (and sometimes incomplete or malformed) data context opens the message. This skill audits a form or email against a deliberate matrix of inputs — not just the happy path — and reports findings as evidence + severity + fix, so someone can act on the output without re-deriving your reasoning.

Two things matter more than any individual check:

1. **Read-only by default.** This skill's job is to find problems, not fix them live. Every step below uses list/show/capabilities/describe operations only. `saveForm`, `saveAutomationTrigger`, `duplicateResource`, `deleteResource`, and `testEmailTemplate (sendTest)` are mutating or externally-visible actions — never call any of them as a side effect of "doing the QA." If a fix or a test send would help, say so in the report and ask. Approval to run the audit is not approval to act on its findings; each mutating action needs its own explicit go-ahead, for that exact action, at the time you're about to take it.
2. **Say what you actually checked.** "I read the content and it looks fine" and "I traced this exact path and confirmed X" are different claims. Every finding and every scenario-matrix row carries a verification status (see Step 4) so the report never implies more confidence than the check actually earned.

## Step 1: Inspect via MCP (read-only)

- Forms: `searchForms (operation: show)` — fields, options, logic, configuration, current revision.
- Emails: `searchEmailTemplates (operation: show)` — content, all translations, available variables, diagnostics, current revision. Call `capabilities` too if you need to know what variables/brands are valid for it.
- If it's useful for the recipient-context or downstream-behavior checks (Step 3), also try `searchAutomationTriggers (operation: list/show)` to see what triggers or consumes this form/email — this is read-only, but it's Super Admin–gated, so it may simply be unavailable. If it fails or comes back empty, don't treat that as "no automation exists" — treat it as "couldn't verify" and say so.
- If the resource was just edited, re-fetch. A revision you reasoned about earlier in the conversation may already be stale.
- Stay in scope: forms and email templates only. If the user asks about message/WhatsApp templates, that's outside this MVP — say so rather than quietly extending the audit.

## Step 2: Build the scenario matrix

Before running category checks, enumerate the elements that carry runtime risk — every variable, every form field, every conditional rule — and give each one three rows: **normal**, **missing/ambiguous**, and **invalid**. This is the artifact that makes the audit systematic rather than a vibes-based read-through; category checks in Step 3 are how you fill it in, not a separate activity.

| Element | Scenario | Test input | Expected behavior | Predicted/observed behavior | Result |
|---|---|---|---|---|---|
| `{{recipient.first_name}}` | Normal | "Maria" | Greets "Hi Maria," | Renders correctly | Pass |
| `{{recipient.first_name}}` | Missing/ambiguous | empty string; or recipient is a client, not the candidate | Either a defined fallback, or copy that still makes sense | No fallback defined; renders "Hi ," | **Fail** |
| `{{recipient.first_name}}` | Invalid | value with an apostrophe or non-Latin script ("Đặng") | Renders as-is, no encoding artifacts | *(needs live render to confirm)* | Needs manual verification |
| Field "Interview date" (required) | Normal | valid future date | Accepted, flows to next field | Accepted | Pass |
| Field "Interview date" (required) | Missing/ambiguous | left blank | Form blocks submission | Form blocks submission | Pass |
| Field "Interview date" (required) | Invalid | past date / malformed string | Validation error shown | No validation rule defined — accepts past dates | **Fail** |
| Branch: "Has certification?" = No → skip to Q9 | Normal | "No" selected | Jumps to Q9 | Jumps to Q9 | Pass |
| Branch: "Has certification?" = No → skip to Q9 | Missing/ambiguous | question skipped entirely (upstream branch bypasses it) | Defined default path | Field becomes unreachable in that path | **Fail** |

Define what "invalid" means per element type as you build the matrix — it isn't one thing:
- **Variables**: wrong data type substituted, unexpected characters (emoji, RTL script, very long strings), an unresolvable namespace.
- **Form fields**: malformed format (bad date, invalid email), out-of-range values, a value technically valid but nonsensical for the question.
- **Branching conditions**: the boundary/edge value of whatever the condition tests (e.g. exactly the cutoff date, an option added after the logic was written).

For a large form or email with many variables, this table can get long — that's fine, it's meant to be exhaustive. If it exceeds what's useful inline, still produce it in full and let the report (Step 5) surface only the rows that failed or need attention; don't shrink the matrix to make the response shorter.

## Step 3: Category checks

Run these to populate the matrix. Each maps to specific rows above.

**Variables** — Extract every `{{...}}` token (subject, body, every translation, every form field label/help/confirmation text). Check the namespace is one of `recipient.*`, `sender.*`, `brand.*`, `account.*` (there is no `candidate.*` or vacancy-scoped namespace — an implied need for one is a data-model gap, not a fixable form bug, flag it as such) and that spelling/casing is exact (`{{recipient.firstname}}` vs `{{recipient.first_name}}` fails silently).

**Modifiers** — If a variable is passed through a formatter/filter (date formatting, casing, truncation), check the modifier syntax is valid, suits the underlying data type, and degrades sensibly when the value is missing rather than throwing or rendering the raw token.

**Fallbacks** — For every variable tied to optional or conditional data, trace what renders when it's empty: dangling punctuation ("Hi ,"), sentences that only parse when populated ("Your interview is at ___"), whether an explicit fallback/conditional block exists versus a silent gap.

**Branching** (forms) — Every jump/skip target must resolve to a field that exists in the current revision. Jump-to-end must target an explicit `ending`-type field. Every field should be reachable by some path and every path should terminate. Re-derive from the raw condition (field/operator/value) what a respondent must answer to trigger each branch, and check it matches the branch's evident purpose — a branch is easy to wire to the wrong field or with an inverted operator and still look right in a summary view.

**Required fields** — Identify which fields are marked required, then check whether any branch can route around a required field entirely (making it effectively optional on that path) — and whether that's intentional or an oversight. Also check the inverse: a field that's optional but that later logic or a variable in an email treats as if it's always present.

**Recipient context** — `{{recipient.first_name}}` resolves to whoever the actual recipient is, not necessarily the candidate. For each template: identify who can actually receive it (from linked triggers/forms, not just what the copy assumes), then read the content as that recipient. A "reference check response" may go to a referee; an "interview feedback" form may go to a client contact. If the automation-trigger read succeeded in Step 1, use it to confirm recipient type directly rather than inferring from copy tone.

**Language** — Consistent register throughout (not mixing "Dear" with "Hey" in one template); tone appropriate to the moment; every translation is a genuine current translation, not stale content from before the last edit.

**Spacing/formatting** — HireData auto-inserts a greeting and signature on emails; a manual greeting or sign-off in the content block duplicates it — check explicitly, it's easy to introduce during a content edit and easy to miss on a skim. Also check for leftover placeholders ("[insert client name]", "TODO", lorem ipsum) and blank lines left behind by a conditional block whose condition is false.

**Downstream behavior** — What consumes this response or send: does it feed another template's variables, update a Carerix/ATS record, or fire an automation? Trace this via `searchAutomationTriggers` if that read succeeded; if it didn't (no access, or nothing found), don't guess — mark it as needing manual verification rather than assuming there's no downstream dependency.

## Step 4: Verification status

Tag every finding and every matrix row with one of:

- **Verified** — you read the actual current content/configuration and directly confirmed this (e.g., namespace check against known list, branch target resolution against actual field IDs, required-flag read from the form schema).
- **Needs manual verification** — the check requires something this audit can't do read-only: visual rendering across email clients, native-fluency judgment on a translation you can't fully evaluate, confirming an automation trigger you don't have access to read, or actual behavior with live production data.

Don't round "Needs manual verification" up to "Verified" because you're fairly confident — confidence isn't the bar, having actually run the check is. A report that's honest about its gaps is more useful than one that looks more complete than it is.

## Step 5: Report

```
## QA Report: [Template/Form name]

### Scenario matrix
[full table from Step 2 — or a link/artifact to it if long, with only
non-pass rows summarized inline]

### Findings

**[Severity] — [short title]**
- Evidence: [exact quote, field ID, or condition that shows the problem]
- Where: [element/field/branch/locale]
- Verification: Verified / Needs manual verification
- Suggested fix: [concrete change, or "requires a data-model change" /
  "requires manual review" if it's not a template-level fix]

[repeat per finding, ordered by severity]

### Verdict
Ready to activate / Not ready — [N] blocking finding(s)

### Manual verification still needed
- [item] — [what would resolve it: live test send, native speaker review,
  automation-trigger access, etc.]
```

**Severity scale** (use this unless the user specifies a different one they already use, e.g. matching Linear labels):
- **Blocker** — a real recipient sees wrong/broken content, or a form path dead-ends or lets a required answer be skipped.
- **Major** — wrong in an edge case that will occur in production (a specific locale, a specific recipient type, a specific branch) but not on the default happy path.
- **Minor** — cosmetic or polish; doesn't misinform or dead-end anyone.
- **Info** — an observation with no required action (e.g., "this variable will need a new namespace once one exists").

If the same class of issue recurs across several templates in a batch (e.g. multiple templates assume recipient = candidate), say so once at the top of the response instead of repeating it per template — it's a systemic fix, not N separate bugs.

## Approval-gated actions

Everything above is read-only. If, based on findings, it would help to:
- send a live test email (`testEmailTemplate: sendTest`),
- duplicate a form/template to test a fix in isolation (`duplicateResource`),
- apply a fix directly (`saveForm`, or editing email content),
- or activate/publish anything,

— propose it and wait for explicit approval naming that specific action before calling the tool. Approval for one action (e.g. "yes, send the test") doesn't extend to others (e.g. it doesn't also authorize publishing). Note also that `testEmailTemplate: sendTest` sends a real email and is rate-limited (10/hour per user+workspace, 50/day per workspace) — don't spend that quota discovering issues Step 3 should have already found by inspection; use it to confirm a specific rendering question you couldn't resolve by reading.
