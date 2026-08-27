## QA Report: reactivation email (working title — I don't have the template name)

**Up front: I could not run this audit.** The HireData MCP isn't connected in this session, so I have no access to the template's actual content, its variable set, its translations, or the form behind the button. Everything below is built from the two lines you pasted, and **no row and no finding in this report is Verified** — they are predicted risks that need the live reads to confirm or clear.

I'd rather tell you that than hand you a green light I didn't earn. Reconnect the MCP (or paste the outputs of the calls listed at the end) and I'll turn this into a real audit.

### What the copy tells me

Three tokens are in play across the two elements you gave me:

- `{{recipient.first_name}}` — in the subject
- `{{specialism}}` — in the subject
- `{{template::form_url}}` — on the button

All three are plausible, real HireData variable shapes. `{{specialism}}` is a bare per-template custom key (possibly an AI variable) and `{{template::form_url}}` is a double-colon system key — neither one is wrong for lacking a dot-path namespace, and I'm not flagging them on shape. But "plausible shape" isn't the test: the only valid check is exact character-for-character membership in the variable set that `capabilities` returns **for this template**, and custom keys like `specialism` are defined per template, so its being valid elsewhere in your workspace tells us nothing here. That check is the one I can't run.

### Scenario matrix

Predicted-behavior column is inference, not observation.

| Element | Scenario | Test input | Expected behavior | Predicted behavior | Result |
|---|---|---|---|---|---|
| `{{recipient.first_name}}` | Normal | "Maria" | Subject reads "Still looking for nursing work, Maria?" | Renders | Needs manual verification |
| `{{recipient.first_name}}` | Missing/ambiguous | empty (no first name on the dormant record) | Fallback, or a subject that still parses | Likely "Still looking for nursing work, ?" — dangling comma + question mark in the subject line | Needs manual verification (**Blocker if confirmed**) |
| `{{recipient.first_name}}` | Missing/ambiguous | recipient is a client contact or a referee, not the candidate | Copy addresses whoever actually receives it | Copy assumes candidate; "still looking for work" is wrong for any other recipient type | Needs manual verification |
| `{{recipient.first_name}}` | Invalid | apostrophe, non-Latin script ("Đặng", "O'Brien") | Renders as-is, no encoding artifacts in the subject | Unknown — subject-line encoding needs a live render | Needs manual verification |
| `{{specialism}}` | Normal | "nursing" | "Still looking for nursing work, Maria?" | Renders | Needs manual verification |
| `{{specialism}}` | Missing/ambiguous | empty on a dormant record; or key not defined on this template | Fallback, or copy that survives an empty value | Likely "Still looking for  work, Maria?" — double space, and the subject loses its whole point | Needs manual verification (**Blocker if confirmed**) |
| `{{specialism}}` | Invalid | stored casing "NURSING"; a long value ("Mental Health & Learning Disability Nursing"); a value that isn't a job family at all | Reads naturally mid-sentence; subject not truncated in the inbox | Casing is taken verbatim unless a modifier is applied; long values push the name past the ~45-char inbox preview | Needs manual verification |
| `{{specialism}}` | Invalid | key absent from this template's `capabilities` set | Token flagged before send | Would resolve to nothing and fail silently — the classic version of this bug | Needs manual verification (**Blocker if confirmed**) |
| `{{template::form_url}}` | Normal | profile form linked to the template | Button resolves to the form | Renders | Needs manual verification |
| `{{template::form_url}}` | Missing/ambiguous | no form associated with the template | Button degrades, or copy doesn't promise a link | Key stays valid but resolves to nothing — a button with no target, in an email whose only ask is "update your profile" | Needs manual verification (**Blocker if confirmed**) |
| `{{template::form_url}}` | Invalid | form exists but is unpublished/archived, or gated to logged-in users | Reachable by a dormant candidate with no session | Unknown | Needs manual verification |
| Subject + auto-greeting | Normal | any recipient | Name appears once, or twice deliberately | HireData auto-inserts the greeting, so "…, Maria?" in the subject then "Hi Maria," in the body — reads as over-personalized on a cold reactivation | Needs manual verification |
| Body block | All | — | — | **Not supplied.** Manual greeting/sign-off duplication, leftover placeholders, empty conditional blocks, and every other body token are entirely unchecked | Needs manual verification |
| Translations | All | each locale on the template | Current, consistent register | Unknown — I don't know how many locales exist or whether they were updated with the last edit | Needs manual verification |
| Linked profile form | All | fields, required flags, branching, reachability | — | Unchecked. The button is the email's whole conversion path; the form behind it needs its own audit | Needs manual verification |

### Findings

**Blocker (if confirmed) — no fallback traced for either subject variable**
- Evidence: `Still looking for {{specialism}} work, {{recipient.first_name}}?` — two unguarded tokens in a single subject line.
- Where: subject, all locales.
- Verification: Needs manual verification — I can't see whether fallbacks or conditional blocks are configured.
- Why it matters more here than usual: this is a reactivation send to *dormant* records, which is exactly the population with the thinnest data. Empty values are the expected case, not the edge case. And a broken subject can't be recovered by good body copy — it's what the whole list sees in the inbox.
- Suggested fix: define fallbacks for both, or restructure so the subject parses when empty (e.g. a variant without `specialism`). If HireData can't fallback a subject token, gate the send on both fields being populated and route the rest to a generic variant.

**Blocker (if confirmed) — button target unverified**
- Evidence: button uses `{{template::form_url}}`.
- Where: body CTA.
- Verification: Needs manual verification — requires reading the template's resource associations.
- Suggested fix: confirm the profile form is actually associated with this template and is published; `{{template::form_url}}` is a valid key that silently resolves to nothing when nothing is linked.

**Major (if confirmed) — `{{specialism}}` membership and type unconfirmed**
- Evidence: bare custom key, no namespace.
- Where: subject.
- Verification: Needs manual verification — needs the `capabilities` variable set for this template.
- Suggested fix: confirm the key is defined on *this* template (character-for-character, casing included) and check its reported `type` and `source`. If it's an AI variable, also confirm what it emits on a record with no work history. If you want lowercase mid-sentence regardless of stored casing, add a casing modifier — chosen against the type `capabilities` reports, not the key's name.

**Major (if confirmed) — recipient type assumed to be the candidate**
- Evidence: "Still looking for … work, {{recipient.first_name}}?"
- Where: subject and, presumably, the whole body.
- Verification: Needs manual verification — needs the trigger read, which is Super Admin–gated and may be unavailable.
- Suggested fix: confirm from the trigger which object type receives this and what filters scope the audience. If the trigger can reach anything other than candidates, the copy is wrong for them.

**Info — subject length and double personalization**
- Evidence: name plus specialism plus a question, in one subject.
- Verification: Needs manual verification.
- Suggested fix: consider dropping the first name from the subject given the auto-greeting repeats it in the body, and check the rendered length against a long `specialism` value.

### Verdict

**Not ready to activate** — not because I found confirmed breakage, but because I found nothing I could confirm either way. Four plausible blockers sit in a two-element email, all of them turning on configuration I couldn't read. Switching the automation on now means finding out from the dormant list.

I have not sent a test, edited the template, or touched the automation, and I won't without you asking for that specific action.

### Manual verification still needed

Everything. The calls I'd make, in order:

1. `searchEmailTemplates (operation: show)` — to read the full body (not just the CTA), every translation, the diagnostics, the current revision, and whether a manual greeting or sign-off duplicates the auto-inserted ones. Also whether any leftover placeholder text survives.
2. `searchEmailTemplates (operation: capabilities)` for the same template — the authority for the Variables and Modifiers checks. I'd check membership of `recipient.first_name`, `specialism`, and `template::form_url` exactly, plus the `type` and `source` each comes back with, and the available brands.
3. `searchAutomationTriggers (operation: list/show)` — which trigger sends this, what recipient type and audience filters it uses, and what consumes the response. If this read isn't available to me, recipient context and downstream behavior stay unverified rather than becoming "no dependency."
4. `searchForms (operation: show)` on the linked profile form — required fields, branch targets resolving to fields in the current revision, reachability, and whether the form is published. Tell me which form it is, or point me at the association, and I'll include it.

Beyond the reads: a live render to settle subject-line encoding for non-Latin names and the inbox truncation point, and a native-speaker pass on any non-English locale. If, once I've read the template, there's a specific rendering question left that only a real send would answer, I'll propose a test send and wait for you to approve that specifically — the sendTest quota is small and finite, and it's not for finding things the reads should catch.

Reconnect the MCP (via your claude.ai connector settings, or `claude mcp` / `/mcp` in an interactive session) and I'll run this properly.

Scope note: this covers the email and the form behind its button. If there's a WhatsApp or SMS step in the same reactivation flow, that's outside what I'm auditing here.
