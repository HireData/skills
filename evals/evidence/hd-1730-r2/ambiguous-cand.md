Happy to QA it — but I can't actually look at it from here yet, and I'd rather tell you that than guess at what's wrong.

## Two things blocking me

**1. I can't reach your workspace.** The HireData MCP connection isn't authorized in this session, so every read I'd need to do is unavailable. You'll need to authorize it before I can inspect anything — via your claude.ai connector settings if it's set up as a connector, or with `/mcp` in an interactive Claude Code session. I can't run that authorization flow from here.

**2. I don't know which form you mean.** "Reference-check form" could point at a few different things, and the audit changes depending on which:

- the **form** a referee fills in (fields, validation, branching), or
- the **email template** that invites the referee to fill it in (variables, fallbacks, greeting/signature duplication), or
- both, as one flow — which is usually where the real bugs live, because the email promises something the form doesn't deliver.

If you can tell me the form/template name (or paste the link), I'll go straight at it. If there's more than one reference-check form in the workspace, the name matters — a stale duplicate that nobody retired is itself a common cause of "something feels off."

## What I'd run once I have access

Read-only inspection, in this order:

- `searchForms (operation: show)` on the reference-check form — I'd read the field list, required flags, validation rules, option sets, and the branching logic, all at the current revision.
- `searchEmailTemplates (operation: show)` on the invite template, if it's in scope — content, every translation, and diagnostics.
- `searchEmailTemplates (operation: capabilities)` on that same template — this returns the exact variable keys valid *for this template*, each with its type and source. That response is the only authority I'll use for checking variables; I won't validate tokens against a remembered list of key patterns, because HireData's valid set legitimately mixes dot-paths, `template::` system keys, and bare custom keys, and any shape rule I invented would flag real variables as broken.
- `searchAutomationTriggers (operation: list/show)` to see what actually sends this and what consumes the response. This one is Super Admin–gated, so it may just come back empty or refused — if it does, I'll report the recipient-type and downstream-behavior checks as *needs manual verification* rather than assuming nothing downstream depends on the form.

Then I'd build a scenario matrix — every variable, field, and branch gets a normal row, a missing/ambiguous row, and an invalid row — and report findings as evidence + severity + suggested fix, with each row and each finding marked either **Verified** (I read the actual config and confirmed it) or **Needs manual verification** (things like cross-client rendering or native-fluency translation review that a read-only audit genuinely can't settle).

## Where I'd look first, given it's a reference check

These are hypotheses to check, not findings — I haven't seen your form, so treat them as a shortlist rather than a diagnosis:

- **Recipient context.** Reference-check content goes to a *referee*, not the candidate. If `{{recipient.first_name}}` or the copy's framing assumes it's the candidate reading it, the whole thing reads wrong to the person who actually receives it. In my experience this is the single most likely cause of "feels off but I can't say why" on this specific form type — the copy is grammatical and the variables all resolve, so nothing looks broken, it's just addressed to the wrong person.
- **Fallbacks on candidate data.** The referee's form usually interpolates the candidate's name, role, or dates. Any of those being empty gives you dangling text ("their time at ," "the role of ___") rather than an error.
- **Required fields routed around by a branch** — e.g. a "would you rehire?" question that a particular answer path skips entirely, making it optional in practice.
- **Duplicated greeting or sign-off.** HireData auto-inserts a greeting and signature; a manual "Dear ..." or "Kind regards" in the content block doubles it. Easy to introduce in a content edit, easy to miss on a skim.

Also worth saying: if what feels off is the *tone* — reference checks sit awkwardly between formal and friendly — that's a judgment call I can give you an opinion on, but it won't show up as a technical finding. Tell me if that's the itch and I'll read it that way instead.

One boundary: this covers forms and email templates. If the referee is contacted over WhatsApp, that's a message template and outside what I'd audit here — I'd flag it rather than quietly extending the review.

I won't change, publish, activate, or send anything as part of the audit. If a fix or a live test send turns out to be the way to settle something, I'll propose it and wait for you to okay that specific action.

So: authorize the connector, and tell me which form (and whether the invite email is in scope). Then I'll run it properly.
