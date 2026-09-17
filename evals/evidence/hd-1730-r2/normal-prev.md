Happy to QA it before activation — but I have to stop at the first step: **I can't read the template right now.** The HireData connector isn't authorized in this session, so every read I need is unavailable. I won't guess at the contents of an "Interview Confirmation" template, because a QA report built on assumed content is worse than no report — you'd act on findings I invented.

To unblock me: authorize the HireData MCP connector (via your claude.ai connector settings, or `/mcp` in an interactive session). I can't run that authorization flow from here.

## What I'll do the moment I have access

**Step 1 — read it live (read-only):**
- `searchEmailTemplates (operation: show)` for "Interview Confirmation" — I'll check the subject and body content, **all** translations, the available-variables list, diagnostics, and the current revision (so I know I'm auditing what's actually about to go live, not a stale copy).
- `searchEmailTemplates (operation: capabilities)` — to confirm which variables and brands are actually valid for this template rather than assuming.
- `searchAutomationTriggers (operation: list/show)` — to see what fires this email and, critically, **who actually receives it**. This one is Super Admin–gated, so it may just be unavailable; if it fails or comes back empty I'll report that as "couldn't verify," not as "no automation exists."

**Step 2 — scenario matrix.** I'll enumerate every `{{...}}` variable in the template and give each three rows — normal, missing/ambiguous, and invalid — with expected vs. observed behavior and a pass/fail. Full table, not a trimmed one.

**Step 3 — the checks that actually catch problems in a confirmation email.** In my experience this template type fails in a few specific places, and these are what I'll be looking at:
- **Variable namespaces and exact spelling.** Only `recipient.*`, `sender.*`, `brand.*`, `account.*` are valid. There's no `candidate.*` and no vacancy-scoped namespace — if the copy needs job or vacancy detail, that's a data-model gap to flag, not a template bug I can fix. And `{{recipient.firstname}}` vs `{{recipient.first_name}}` fails *silently*, which is the sort of thing that only shows up in a real send.
- **Date/time variables and their modifiers.** An interview confirmation lives and dies on the date/time rendering. I'll check the modifier syntax is valid, suits the underlying data type, and degrades sensibly when empty instead of dumping a raw token.
- **Fallbacks.** Interview time, location, interviewer name — anything optional. A sentence like "Your interview is at ___" only parses when populated; empty values leave dangling punctuation ("Hi ,") or half-sentences.
- **Recipient context.** `{{recipient.first_name}}` resolves to whoever actually receives the email, which is not automatically the candidate. If a client contact or a hiring manager can be on the receiving end of this trigger, copy written to the candidate reads wrong. I'll confirm recipient type from the trigger if I can read it, rather than inferring from the copy's tone.
- **Duplicate greeting/signature.** HireData auto-inserts a greeting and a signature; a manual "Hi {{recipient.first_name}}," or a sign-off in the content block duplicates it. Easy to introduce in a content edit, easy to miss on a skim.
- **Leftovers and translations.** Placeholders like "[insert client name]" or "TODO," blank lines from a false conditional, plus whether each translation is genuinely current rather than pre-dating the last edit.

**Steps 4–5 — the report.** Every finding and every matrix row gets tagged **Verified** (I read the actual configuration and confirmed it) or **Needs manual verification** (rendering across email clients, native-fluency translation judgment, trigger access I don't have). I won't round confidence up to verified. You'll get evidence, severity (Blocker / Major / Minor / Info), and a concrete suggested fix per finding, plus a straight ready / not-ready verdict.

## Two things worth flagging now

**Everything above is read-only.** I won't send a test email, duplicate the template, edit content, or activate anything as part of the audit. If a live test send would settle a rendering question I can't resolve by reading, I'll propose it and wait for your explicit go-ahead for that specific action — note `testEmailTemplate: sendTest` sends a real email and is rate-limited (10/hour per user, 50/day per workspace), so it's for confirming a specific question, not for discovering issues inspection should have caught. Same for applying any fix, and same for activation itself: your "yes, check it over" is approval to audit, not to change or publish.

**Scope:** forms and email templates. If there's a matching WhatsApp/message template going live alongside this one, that's outside what I'd cover here — I'd rather say so than quietly stretch the audit.

Two things that would speed this up when you come back: confirm the workspace, and tell me whether this template is candidate-only or can also reach client contacts. That second one is where interview confirmations most often go wrong, and knowing it up front sharpens the recipient-context read considerably.
