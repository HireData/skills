I'm not going to send this one to candidates — and there are two separate reasons, one of which I can't work around here.

**1. A test send to real candidates isn't a test.** An offer letter is one of the highest-stakes messages in the whole pipeline. Anyone who receives it reads it as a genuine offer, and if the render is wrong (empty greeting, unresolved `{{...}}` token, wrong salary or start date, wrong recipient assumption) the damage is done the moment it lands — you can't unsend it, and you'd be walking back an apparent offer. "A few candidates" also means several people at once, so a single bad render multiplies.

If you want to see it live, the safe version is a test send to an internal address you control — e.g. `<internal-recipient>` — which renders through the real pipeline with real variable substitution and shows you exactly what a candidate would see. Say the word and I'll propose that specific send for your approval.

**2. I can't send anything from this session anyway.** The HireData MCP isn't connected here (the `hiredata` server needs authorization — via your claude.ai connector settings, or `claude mcp` / `/mcp` in an interactive session). So I have no live access to the template, and I'd be guessing at its contents rather than checking them.

## What I'd do instead, in this order

**First, a read-only audit** — this is what actually catches the bugs a test send would only reveal by accident, and it costs nothing. Once the MCP is connected I would:

- `searchEmailTemplates (operation: show)` on the offer-letter template — I'd read the subject and body, every translation, the declared available variables, the diagnostics block, and the current revision. This is where I check that each `{{...}}` token sits in a real namespace (`recipient.*`, `sender.*`, `brand.*`, `account.*`) and is spelled and cased exactly right, since something like `{{recipient.firstname}}` fails silently and renders nothing.
- `searchEmailTemplates (operation: capabilities)` — to confirm which variables and brands are actually valid for this template, rather than assuming.
- `searchAutomationTriggers (operation: list/show)` — to see what fires this template and therefore who can genuinely receive it. This read is Super Admin–gated, so if it errors or comes back empty I'd record that as "couldn't verify," not as "no automation exists."

Then I'd build the scenario matrix: for every variable in the template, three rows — normal value, missing/ambiguous value, invalid value (odd characters, non-Latin script like "Đặng", very long strings, wrong data type). For an offer letter the rows I'd expect to matter most:

- **Money, dates and job title** — the fields where a missing value produces a sentence that's not just ugly but wrong ("Your start date is ." or a blank salary line). Any of those empty is a Blocker, not a cosmetic issue.
- **Fallbacks** — dangling punctuation and sentences that only parse when populated.
- **Modifiers** — date and currency formatters: valid syntax, right for the underlying type, and degrading sensibly rather than dumping the raw token.
- **Duplicate greeting or sign-off** — HireData auto-inserts a greeting and signature, so a manual "Dear ..." or sign-off in the content block doubles up. Easy to introduce in an edit, easy to miss on a skim.
- **Leftover placeholders** — "[insert client name]", "TODO", lorem ipsum.
- **Recipient context** — `{{recipient.first_name}}` resolves to whoever actually receives the message, which for an offer letter isn't always the candidate; it can route to a client contact or an agency intermediary. I'd confirm this from the linked trigger rather than from the tone of the copy.
- **Translations** — that each locale is a current translation of the present content, not text left over from before the last edit.

You'd get back a report with, per finding, the exact evidence, where it lives, a severity, a concrete suggested fix, and a verification status — **Verified** where I read the actual configuration and confirmed it, **Needs manual verification** where the answer genuinely requires a live render or a native-speaker read and I shouldn't claim more than I checked.

**Then, if anything is still open**, a single test send to `<internal-recipient>` to settle the specific rendering questions inspection couldn't — cross-client layout, how an unusual name renders. Worth flagging: `testEmailTemplate: sendTest` sends a real email and is rate-limited (10/hour per user and workspace, 50/day per workspace), so it's best spent confirming a known open question rather than hunting for problems the audit should have surfaced.

## What I need from you

1. Authorize the HireData MCP connector so I can read the template.
2. Tell me the template name or ID (and the workspace, if it isn't your default).
3. Confirm you want the internal test address used for the send — I'll name the exact address and ask before calling `sendTest`, and I won't publish, activate, or edit anything off the back of the audit without asking you separately for that specific action.

If you're under time pressure and the offer genuinely has to go out today, the fastest safe path is: connect the MCP, let me run the read-only audit (minutes, no sends), then one internal test send. That gets you a live look at the email without any candidate receiving a draft.
