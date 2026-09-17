I don't think I should send this the way you've described, and I want to flag why before doing anything else.

**The core issue: real candidates, not a test list.** `testEmailTemplate (sendTest)` is a live send — the recipient gets an actual email in their inbox indistinguishable from the real thing. If it goes to actual candidates, you're not testing the offer letter, you're *sending* it. That's risky in a few concrete ways:

- If the content has any of the bugs this audit is designed to catch — a dangling `{{recipient.first_name}}`, a leftover `[insert start date]` placeholder, a stale translation, wrong salary/role variables — real candidates now have that in writing, from a system that looks authoritative.
- An "offer letter" landing in a candidate's inbox can read as a real offer regardless of your intent, with HR/legal implications (expectation-setting, even good-faith confusion about whether it's binding) that a test send to internal addresses doesn't carry.
- It also burns real send quota (`testEmailTemplate` is rate-limited — 10/hour per user+workspace, 50/day per workspace) on people who can't be un-sent to if something's wrong.

This falls squarely under "send any message on the user's behalf," which needs your explicit, specific approval before I'd trigger it at all — but even with approval, sending live offer-letter content to real candidates as a "test" isn't something I'll do. I'd send it to *you*, a teammate, or a designated internal test address instead — that gets you the live rendering check without exposing candidates to unverified content.

Here's what I'd suggest instead, in order:

1. **Run the read-only QA audit first.** I'd call `searchEmailTemplates (operation: show)` on the offer-letter template to pull its current content, all translations, and available variables, and `capabilities` to confirm the valid variable/brand namespaces. Then I'd build the scenario matrix from the skill — every `{{...}}` variable checked for correct namespace/spelling, fallback behavior when a field is empty (e.g. does it render "Hi ," if a name is missing), auto-inserted greeting/signature duplication, leftover placeholders, and tone/register consistency across translations. If it's accessible, I'd also check `searchAutomationTriggers` to confirm who actually receives this (candidate vs. a client contact) rather than assuming from the copy.
2. **Report findings with severity and verification status**, per the skill's format — anything I can't confirm by reading (e.g. exact rendering in a real email client, native-fluency check on a translation) gets flagged as "needs manual verification" rather than glossed over.
3. **Then, if you still want a live rendering check**, I'd propose sending via `testEmailTemplate (sendTest)` to your own email address or a short internal list you name — not to candidates — and I'd wait for your explicit go-ahead on that specific action before sending.

(One environment note: the HireData MCP connection isn't attached in this session, so I can't actually execute any of the calls above right now — I'm describing exactly what I'd run and what I'd look for once it's available, not reporting results.)

Want me to go ahead with the read-only audit of the offer-letter template first?
