I'm not going to send this to candidates — and I can't send anything at all right now. Two separate reasons, both worth knowing:

**1. A test send to real candidates isn't a test — it's an offer.**
A test send from HireData (`testEmailTemplate: sendTest`) delivers a real email to a real inbox. If the recipients are candidates, what lands in their inbox is an offer letter from your agency. There's no "this is only a test" wrapper on it. Candidates who haven't been offered anything will read it as an offer; ones who have may read a placeholder salary or start date as the real number. That's a retraction conversation, a trust problem, and potentially a legal one — for a rendering question that an internal recipient can answer just as well.

Test sends also draw on a small per-user and per-workspace quota, so they're worth spending on a specific question, not a general look.

**2. The HireData MCP isn't connected in this session.**
The HireData connector needs to be authorized before I can call it — via your claude.ai connector settings, or `/mcp` in an interactive session. Until that's done I can't read the template, and I can't send. So nothing has gone out.

## What I'd suggest instead

**First, a read-only audit — it catches most of what a "see how it looks live" send is really looking for.** Once the connector is up, the exact calls I'd make:

- `searchEmailTemplates (operation: show)` on the offer-letter template — content, every translation, and the current revision. I'd check for a manual greeting or sign-off duplicating the one HireData auto-inserts, leftover placeholders ("[insert client name]", TODO), and blank gaps left by conditional blocks.
- `searchEmailTemplates (operation: capabilities)` on that same template — this returns the exact set of variable keys valid for it, each with a type. I'd check every `{{...}}` token in the subject, body, and each translation against that set, character for character. Near-misses are the classic offer-letter bug: `{{recipient.firstname}}` for `{{recipient.first_name}}` resolves to nothing and fails silently. I'd also read each key's reported type before trusting a date or currency modifier on it.
- Then the fallback trace: for salary, start date, job title, manager name — whatever's optional or conditional — what actually renders when the field is empty. An offer letter with "Your start date is ___" or "Hi ," is exactly the failure a live send would expose, and I can find it by reading.
- `searchAutomationTriggers (operation: list/show)` to confirm who actually receives this template. Worth checking on an offer letter specifically — if a trigger routes it to a client contact or a hiring manager as well as the candidate, copy written for the candidate reads wrong to them. This call is Super Admin-gated, so if it fails I'd mark recipient context as needing manual verification rather than assume.

**Then, if a rendering question genuinely survives that** — how a logo or a table renders in Outlook, say, which no amount of reading resolves — I'd propose one test send to an internal address, e.g. `<internal-recipient>`, and wait for you to approve that specific send before making the call. Internal inbox, real render, no candidate involved.

## What I need from you

1. Authorize the HireData connector so I can read the template.
2. Confirm the template name or ID, and the workspace if it isn't your default.
3. Tell me whether you want the internal test send proposed after the audit, or whether the audit alone is enough.

If you'd rather show the offer letter to colleagues live rather than just check it, the internal-recipient send does that too — forward it, or add a couple of your own team's addresses. Same render, no candidate on the receiving end.

One thing I'd flag either way: if what you actually want is a stakeholder sign-off on the wording before this goes live, a test send is a weak way to get it — nobody can comment on an email. I can pull the rendered content and the findings into a page your team can read and mark up instead. Say the word.
