I can't actually run this audit right now — the HireData MCP connection isn't attached to this session, so I have no read access to your workspace's forms/email templates. I don't want to hand you a QA report that looks complete but is actually just guesswork, so here's exactly what I'd do the moment the connection is back, plus a couple of options if you want something useful in the meantime.

### What I'd call, and why

1. `searchEmailTemplates` (operation: `show`) for "Interview Confirmation" — pulls the current revision's subject, body, every translation, and the variables it declares as available. This is the core read the whole audit depends on.
2. Same tool, operation: `capabilities` — confirms which variable namespaces and modifiers are actually valid for this template, so I'm checking spelling/casing against ground truth rather than assumption.
3. `searchAutomationTriggers` (operation: `list`/`show`) filtered to this template — tells me who actually receives it (candidate vs. client vs. referee) and what, if anything, downstream consumes the send. This one is Super Admin–gated, so it may come back empty or fail even when connected; if it does, I'll flag recipient-context and downstream-behavior as "needs manual verification" rather than assuming candidate-only or assuming no automation exists.

### What I'd check once I have that content (per the QA skill)

- **Variables** — every `{{...}}` token in subject/body/translations resolves to `recipient.*`, `sender.*`, `brand.*`, or `account.*`, spelled exactly right (e.g. `{{recipient.first_name}}`, not `firstname`).
- **Fallbacks** — for anything tied to optional data (interview date/time, location, interviewer name, video link), what renders if it's blank — dangling punctuation, a sentence that only makes sense when populated, etc.
- **Recipient context** — "Interview Confirmation" is exactly the kind of template that's easy to write candidate-voiced but that could also fire to a client contact confirming from their side, or to both with different copy needed. I'd confirm via the trigger, not the copy's tone.
- **Language/spacing** — consistent register across the body and every translation; no manual greeting/sign-off duplicating HireData's auto-inserted ones; no leftover placeholders like "[insert time]" or stale translation text from a prior edit.
- **Downstream behavior** — whether a confirmation reply, click, or the send itself updates an ATS record or fires another automation.

Each finding would get a severity (Blocker/Major/Minor/Info) and a verification tag (Verified vs. Needs manual verification), per the usual format, and I would not touch `saveEmailTemplate` or `testEmailTemplate` (sendTest) without asking you first for that specific action.

### To actually get this done

Two options:

- **Reconnect the HireData MCP tools** and re-ask — I'll run the real inspection and give you a full scenario-matrix report before you flip it on.
- **Paste the template content here** (subject, body, all translations, and — if you know it — what triggers the send and who receives it). I can do a content-level read-through against the same checklist right now, but I'd flag the branching/recipient/downstream items as unverifiable without the live configuration and trigger data, since those need the actual system state, not just the text.

Given this is about to go live, I'd lean toward the reconnect-and-verify path rather than a text-only read, since recipient context and downstream automation are exactly the kind of thing that looks fine in the copy and breaks at send time.
