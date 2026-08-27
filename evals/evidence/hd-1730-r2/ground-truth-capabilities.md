# Ground truth: real `searchEmailTemplates (operation: capabilities)` response

Retrieved 2026-08-27 from the live HireData workspace `hiredata` (id 1), read-only, for an
existing email template. Abridged: the `variables` array is 300+ entries; the shapes present
are what matters.

Every entry has `key`, `label`, `type`, and `source` (`system` or `custom`). The `key` is used
in content as `{{key}}` — the response's own `guidance` field states: "Use variable keys as
{{key}} placeholders."

Shapes actually returned:

- Dot-paths: `recipient.first_name`, `recipient.address.city`, `sender.email`,
  `brand.email_signature`, `account.brand.location.address.zip`, ... (`source: system`)
- Double-colon system keys: `template::form_url`, `template::subject`,
  `template::unsubscribe_url` (`source: system`, `type: string`)
- Bare keys with NO namespace, defined per template: `specialism`, `work_location`,
  `last_contact_date`, `last_known_role`, `yes_no` (`source: custom`), and
  `profile_recap` (`source: custom`, `type: ai` — an AI variable)

Namespaces present in this template's set: `recipient.`, `sender.`, `brand.`, `account.`.
No `candidate.` namespace in this template's set — but other templates in the same workspace
have live content using `{{candidate_name}}` and `{{meeting.title}}` in their subject lines,
i.e. the custom-variable set differs per template and the namespace inventory is not fixed.

Therefore: `{{template::form_url}}` and `{{specialism}}` are BOTH valid variables. Any check
that requires a token to begin with `recipient.`, `sender.`, `brand.`, or `account.` produces a
false positive on them. `template::form_url` is the variable that renders a link to the
template's linked form — the most common variable in this workspace's form-driven emails.
