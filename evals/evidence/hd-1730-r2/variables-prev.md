Before the report itself, one blocker on the audit: **I could not inspect this template live.** The HireData connector isn't authorized in this session (and this session can't run the OAuth flow), so everything below is derived from the two fragments you pasted, not from the actual template revision. To authorize it: for the claude.ai connector, your claude.ai connector settings; otherwise `claude mcp` or `/mcp` in an interactive session. Give me the template name or ID once it's connected and I'll run the full audit properly.

I also can't certify the email from a subject line and one button. The body, the translations, and the linked form all carry runtime risk I haven't seen.

## QA Report: reactivation email (name/ID not yet supplied)

### Scenario matrix

| Element | Scenario | Test input | Expected behavior | Predicted/observed behavior | Result |
|---|---|---|---|---|---|
| `{{specialism}}` (subject) | Normal | "warehouse" | Subject reads "Still looking for warehouse work, Maria?" | Only if `specialism` is a declared custom variable on this template | Needs manual verification |
| `{{specialism}}` (subject) | Missing/ambiguous | candidate record has no specialism (very common on a dormant list) | Defined fallback, or copy that survives an empty value | No fallback in the token; renders "Still looking for  work, Maria?" — double space, broken sentence | **Fail** |
| `{{specialism}}` (subject) | Invalid | token resolves to nothing because the name isn't a valid variable | Send blocked, or safe empty render | Not one of `recipient.*` / `sender.*` / `brand.*` / `account.*` — silent empty or raw token in the subject | **Fail** |
| `{{recipient.first_name}}` (subject) | Normal | "Maria" | "…work, Maria?" | Namespace and spelling are exact | Pass |
| `{{recipient.first_name}}` (subject) | Missing/ambiguous | empty first name, or recipient is a client contact rather than the candidate | Fallback, or copy that still parses | Renders "Still looking for warehouse work, ?" — dangling comma before "?" | **Fail** |
| `{{recipient.first_name}}` (subject) | Invalid | apostrophe or non-Latin script ("Đặng", "O'Brien") | Renders as-is, no encoding artifacts in the subject header | Unknown — subject-line encoding needs a live render | Needs manual verification |
| `{{template::form_url}}` (button) | Normal | tag resolves to the published profile form | Button opens the live form | Tag existence and target not verified | Needs manual verification |
| `{{template::form_url}}` (button) | Missing/ambiguous | tag undefined, or form unpublished/archived | Send blocked or safe degradation | If unresolved, the button is dead and the email has no purpose | Needs manual verification |
| `{{template::form_url}}` (button) | Invalid | tag resolves to a generic (non-personalised) URL | Per-recipient link so the response attaches to the person record | Unknown — if generic, responses may land unattributed | Needs manual verification |
| Subject as a whole | Missing/ambiguous | both variables empty | Readable subject | "Still looking for  work, ?" — every recipient with a thin record sees this in the inbox | **Fail** |
| Email body | all three scenarios | not supplied | Greeting/signature not duplicated; no leftover placeholders; no blank gaps from false conditionals | Not inspected | Needs manual verification |
| Translations | all three scenarios | not supplied | Each locale carries the same variables and the form link, and is current | Not inspected | Needs manual verification |
| Linked profile form (fields, required flags, branching, endings) | all three scenarios | not supplied | Fields reachable, required fields not routable around, jump targets resolve, ending exists | Not inspected | Needs manual verification |
| Recipient type | Missing/ambiguous | trigger audience includes client contacts or non-candidates | Copy makes sense to whoever actually receives it | Not verified — trigger not read | Needs manual verification |

### Findings

**Blocker — `{{specialism}}` is not a valid variable namespace as written**
- Evidence: subject `Still looking for {{specialism}} work, {{recipient.first_name}}?`
- Where: subject line (and anywhere else in the body it appears)
- Verification: Verified that the token matches none of the four valid namespaces (`recipient.*`, `sender.*`, `brand.*`, `account.*`). Needs manual verification whether it is a declared custom variable on this template.
- Suggested fix: confirm via `searchEmailTemplates (operation: capabilities)`. If it is a declared custom variable, this drops to Info. If it isn't, note that a candidate's specialism is a vacancy/candidate-scoped attribute and there is no vacancy-scoped namespace — that's a data-model gap, not a template bug. The template-level fix is to rewrite the subject so it doesn't need the value ("Still open to new work, {{recipient.first_name}}?").

**Blocker — no fallbacks on either subject variable, on exactly the audience where data is thinnest**
- Evidence: with both values empty the subject renders "Still looking for  work, ?" (double space, comma stranded before the question mark)
- Where: subject line
- Verification: Verified from the token text — neither token carries a fallback or sits inside a conditional.
- Suggested fix: either add explicit fallbacks/conditional blocks, or use copy that reads correctly with no personalisation at all. A reactivation list is dormant records: missing first names and missing specialisms are the norm, not the edge case, and a subject line is the one place a broken render is visible before anyone opens anything.

**Blocker (pending confirmation) — the CTA target is unverified**
- Evidence: button href `{{template::form_url}}`
- Where: body CTA
- Verification: Needs manual verification.
- Suggested fix: confirm the tag exists (`searchTemplateTags`), that it points at a currently published form (`searchForms (operation: show)`), and that it produces a per-recipient link rather than a shared URL. An unresolved tag or an unpublished form makes the whole send pointless; a shared URL means submissions may not attach to the right person.

**Major — recipient type not confirmed**
- Evidence: "Still looking for … work, {{recipient.first_name}}?" assumes the recipient is the candidate.
- Where: subject and body voice
- Verification: Needs manual verification — trigger not read.
- Suggested fix: read the trigger's audience with `searchAutomationTriggers (operation: list/show)` and confirm it can only resolve to candidates. If that read fails or returns nothing, treat it as unverified rather than as "no other recipient type exists."

**Info — body, translations, and form not yet audited**
- Evidence: not supplied in the request.
- Where: content block, all locales, linked form.
- Verification: Needs manual verification.
- Suggested fix: the greeting/signature duplication check in particular matters here — HireData auto-inserts both, and a manually written "Hi {{recipient.first_name}}," in the content block duplicates it. That, leftover placeholders, stale translations, and the form's own branching/required-field checks are all still outstanding.

### Verdict

**Not ready to activate** — 2 confirmed blocking findings (invalid variable namespace, no fallbacks in the subject), 1 likely blocker pending confirmation (CTA target), and the majority of the audit not yet run.

### Manual verification still needed

- Whether `specialism` is a declared custom variable — `searchEmailTemplates (operation: capabilities)` on this template.
- Full template content, all translations, and available variables — `searchEmailTemplates (operation: show)`.
- Existence and resolution of the `template::form_url` tag — `searchTemplateTags`.
- Whether the linked profile form is published, and its fields/required flags/branching/ending — `searchForms (operation: show)`.
- Who the trigger can actually send this to, and what consumes the form response downstream — `searchAutomationTriggers (operation: list/show)` (Super Admin–gated; may be unavailable).
- Subject-line rendering with apostrophes and non-Latin names, and CTA rendering across email clients — needs a live test send.
- Native-fluency review of each translation.

### Approval-gated next steps

I have not changed, sent, or activated anything, and I won't switch the automation on. When you're ready, tell me specifically which of these you want:

1. A live test send to check subject encoding and the CTA (`testEmailTemplate: sendTest`) — this sends a real email and is rate-limited (10/hour per user+workspace, 50/day per workspace), so it's worth doing after the subject-line fixes rather than before.
2. Applying the subject-line fix (fallbacks and/or the depersonalised rewrite) to the template.
3. Duplicating the template to test a fix in isolation first.

Approving one of those doesn't cover the others, and none of them covers activation.
