I can run this QA, but I need to flag a limitation up front: my connection to the HireData tools isn't active in this session, so I can't actually pull your reference-check form's current configuration right now. I haven't looked at any real data — everything below is either "what I'd run" or a generic risk list for this form type, not a confirmed finding. I don't want to hand you something that reads as a completed audit when it isn't one.

Here's exactly what I'd do once the connection is back:

**1. Inspect (read-only)**
- `searchForms (operation: show)` — pull the reference-check form itself: fields, options, branching logic, and confirm which revision is current. If more than one form matches "reference check," I'd ask you which one before going further, or pull all candidates.
- `searchAutomationTriggers (operation: list/show)` — see what actually triggers this form to be sent and to whom. This is the check I'd prioritize first, because for reference-check forms the single most common defect is a recipient-context mismatch (see below), and this is the only way to confirm it rather than infer it from the copy. It's Super Admin–gated, so it may come back empty or fail — if so I'll say "couldn't verify," not "no automation exists."
- `searchEmailTemplates (operation: show)` — if there's an invite/reminder email that carries respondents to the form, I'd pull that too, since a broken variable or fallback there is just as much a "the reference check feels off" cause as the form itself.

**2. Scenario matrix I'd build**
Once I have the real config, I'd enumerate every field, every branch condition, and every `{{variable}}` in the form and any linked email, and score each on normal / missing-or-ambiguous / invalid inputs, per the standard template. I can't fill this in with real values yet, but here's the shape of it, seeded with the risk areas that are specifically worth checking for a reference-check form based on the class of problem this form type tends to have:

| Element | Scenario | What I'd check | Why it matters here |
|---|---|---|---|
| Recipient context | Who actually opens this form | Confirm via the trigger, not the copy, whether the recipient is the referee or the candidate | Reference-check forms are the classic case where `{{recipient.first_name}}` etc. resolve to the referee, but the copy is often drafted as if the candidate will read it ("Tell us about your experience...") |
| Required "relationship to candidate" / rating fields | Missing/ambiguous | Whether any branch lets a respondent skip a required rating or comment field | A referee who selects certain answers may get routed around a field the form still treats as always-answered downstream |
| Branch: e.g. "Would you rehire this person?" = No → follow-up question | Normal / edge | Whether the "No" and "Not sure" paths both resolve to a real field, and don't silently rejoin without capturing the follow-up | Two-state branches (Yes/No) sometimes miss a "Prefer not to say" or blank submission path |
| `{{recipient.first_name}}` / candidate name variable in form intro text | Missing/ambiguous | Whether a fallback exists if the referee's name or the candidate's name field is blank | Produces "Hi ," or "...regarding 's application" if unhandled |
| Jump-to-end field | Normal | Whether every branch that should terminate the form actually targets an `ending`-type field, not a dead field | A misrouted branch can leave a respondent on a screen with no way to submit |

I'd fill this in with actual field IDs, condition logic, and pass/fail results once I can read the form — right now every row above is a hypothesis about where this form type typically breaks, not something I've verified.

**3. What I need from you to move forward**
- Is there more than one form with "reference check" in the name/tag? If so, which one (or should I check all of them)?
- Anything more specific about what "feels off" — a particular question, a specific referee's report of a weird experience, a broken-looking email — would let me jump straight to that element instead of doing a full blind audit.
- If you can paste the form's field list/branching logic or a screenshot in the meantime, I can start the variable/branching/required-field checks from that even without live tool access, though I still wouldn't be able to confirm the automation-trigger/recipient question without the tool.

### Verdict
Not yet assessed — no live data pulled. This message is scoping the audit, not reporting results.

### Manual verification still needed (once tools are available)
- Recipient identity (referee vs. candidate) via `searchAutomationTriggers` — highest-value first check for this form type.
- Full field/branch/variable matrix via `searchForms (operation: show)`.
- Any linked invite/reminder email via `searchEmailTemplates (operation: show)`.
