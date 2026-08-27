Happy to audit it — but I have to be upfront about two blockers before I can tell you anything real about *your* form.

## I can't read the form right now

The HireData MCP connection isn't authorized in this session, so I can't fetch your reference-check form. Everything in a QA audit worth acting on comes from the actual current revision — field IDs, branch targets, variable spellings, required flags. Guessing at those would just give you a plausible-sounding report about a form I've never seen.

To fix that: authorize the HireData connector (claude.ai connector settings, or `/mcp` in an interactive Claude Code session). Once it's connected I can run the audit end to end.

## I also need to know which form

"Reference-check form" could be a few different things in a typical workspace, and they have different risk profiles:

- a form the **referee** fills in about the candidate,
- a form the **candidate** fills in to supply referee contact details,
- an internal form a **recruiter** completes after a reference call.

Which one — or just the form name as it appears in HireData, plus the workspace if it isn't your default — and I'll go straight to it.

## Exactly what I'd run

1. `getContext (operation: identity)` — confirm the connected user and default workspace.
2. `searchForms (operation: list)` — locate the form by name; I'd check the results for more than one near-match, because auditing the wrong revision of the right-sounding form is a real failure mode.
3. `searchForms (operation: show)` on that form — this is the audit's source of truth. I'd read: the ordered field list with IDs and types, per-field required flags and validation rules, option sets, every logic rule (field / operator / value / jump target), confirmation and help text, and the current revision.
4. `searchAutomationTriggers (operation: list/show)` — to see what actually sends this form and what consumes the response. This read is Super Admin–gated, so it may just be unavailable; if it fails or returns nothing, I'd record that as "couldn't verify" rather than "no automation exists."

Then I'd build a scenario matrix — every variable, every field, every branch, each with a **normal**, **missing/ambiguous**, and **invalid** row — and fill it in via the category checks (variables, modifiers, fallbacks, branching, required fields, recipient context, language, spacing, downstream behavior). Findings come back as evidence + severity + suggested fix, each tagged **Verified** or **Needs manual verification**.

## Where "feels off" usually turns out to be, on this form type specifically

These are hypotheses to check, not findings — I have no evidence for any of them yet on your form. I'm listing them because "something feels off" on a reference-check form has a few common causes, and your gut may recognize one:

- **Recipient context mismatch.** This is the single most common one here. The form or its covering email goes to a **referee**, but the copy was written as if the candidate were reading it — `{{recipient.first_name}}` resolves to the referee, while questions say "your experience" meaning the candidate's. It reads fine in the builder and reads wrong to the person who actually receives it.
- **A required field that a branch routes around.** E.g. "Would you rehire?" is marked required, but a "did not directly manage this person" path skips past it — so it's effectively optional on that path, and your data has holes you can't see in the schema.
- **Missing fallbacks on optional data.** Anything like "Please comment on {{...}}'s time at [company]" that only parses when populated, or an empty variable leaving dangling punctuation.
- **Duplicated greeting/sign-off.** HireData auto-inserts a greeting and signature on the covering email; a manual "Dear ..." or sign-off in the content block doubles it. Very easy to introduce in a content edit, very easy to skim past.
- **A stale translation.** If the form has multiple locales, one may be carrying content from before the last edit.
- **A branch wired to the wrong field or with an inverted operator.** Looks correct in a summary view; only shows up when you re-derive from the raw condition what a respondent must actually answer to trigger it.

If one of those rings a bell, tell me and I'll start there — but I'd still run the full matrix, since "feels off" is often a symptom of something adjacent to what you noticed.

Nothing I do in the audit changes anything: it's all read-only inspection. If a finding calls for a live test send, a duplicate to test a fix in isolation, or an actual edit, I'll propose it and wait for your explicit go-ahead on that specific action first.
