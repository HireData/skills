Happy to QA it before you activate — but I have to flag up front that I can't actually inspect it from here.

## Why the audit can't run yet

The HireData MCP connection isn't authorized in this session, so I have no read access to the template. Everything a real pre-activation audit rests on — the actual content, the translations, and critically the exact set of variable keys that are valid *for this specific template* — has to come from live reads. I'm not going to guess at it: an "Interview Confirmation" email could contain almost anything, and a QA report built on assumed content would be worse than no report, because it would look complete.

To unblock: authorize the HireData connector (claude.ai connector settings, or `/mcp` in an interactive session). Then re-ask and I'll run the full audit.

## What I will do, exactly, once connected

**Step 1 — read the template (read-only):**
- `searchEmailTemplates (operation: show)` on the "Interview Confirmation" template — content, all translations, available variables, diagnostics, current revision.
- `searchEmailTemplates (operation: capabilities)` on that same template. This one is mandatory, not a nice-to-have: it returns the authoritative set of variable keys valid for this template, each with a `type` and a `source` (`system` or `custom`), plus available brands. Every variable and modifier check is validated against that response and nothing else — I won't validate tokens against a remembered list of namespaces, because the valid set legitimately mixes dot-paths (`recipient.first_name`), double-colon system keys (`template::form_url`), and bare per-template custom keys with no namespace at all (`specialism`). Any shape-based rule would reject real variables.
- `searchAutomationTriggers (operation: list/show)` to see what actually sends this email and therefore who actually receives it. This read is Super Admin–gated, so it may be unavailable — if it fails or returns nothing, I'll record "couldn't verify," not "no automation exists."

**Step 2 — scenario matrix.** Every variable and conditional in the template gets three rows: normal, missing/ambiguous, and invalid, with expected vs. predicted/observed behavior and a pass/fail per row. It's built from the real token list, not a generic one.

**Step 3 — the checks that catch the actual bugs in interview-confirmation emails.** For flavor of what I'll be looking for (not findings — I haven't seen your template):
- **Variables**: exact character-for-character membership against the `capabilities` set. Near-misses like `{{recipient.firstname}}` for `{{recipient.first_name}}` resolve to nothing and fail silently at send time.
- **Fallbacks**: what renders when the date, time, location, or interviewer name is empty. Interview confirmations are unusually exposed here — "Your interview is at" with a blank tail, or "Hi ," is a blocker, not a cosmetic issue.
- **Modifiers**: date/time formatting checked against the `type` the capabilities response reports for that key, not against what the key's name suggests. A date-looking custom key that comes back as a `string` behaves differently under a date modifier.
- **Recipient context**: `{{recipient.first_name}}` resolves to whoever the recipient actually is. If a trigger also sends this to a client contact or a hiring manager, candidate-facing copy reads wrong. I'll confirm recipient type from the trigger where I can read it, rather than inferring it from tone.
- **Spacing/formatting**: HireData auto-inserts a greeting and signature, so a manual "Hi {{...}}," or sign-off in the content block duplicates it — and leftover placeholders or blank lines from false conditional blocks.
- **Language**: consistent register, and whether each translation is genuinely current rather than stale content from before the last edit.
- **Downstream behavior**: whether this send feeds another template's variables or fires a follow-up automation.

**Steps 4–5 — report.** Each finding gets evidence (exact quote or field), severity (Blocker / Major / Minor / Info), a suggested fix, and a verification status: **Verified** only where I directly confirmed it against retrieved content, **Needs manual verification** otherwise. Things that will land in that second bucket regardless of access: how it renders across email clients, and native-fluency judgment on translations.

## Current status

**Verdict: cannot assess — no checks have been run.** Not "looks fine," and not "ready to activate." Zero of the checks above are Verified right now, so please don't read this message as a green light.

Two other notes:
- If it also involves a WhatsApp/message template, that's outside what I audit — I'd flag it rather than quietly extending the review.
- I won't send a test email, duplicate anything, edit content, or activate the template as part of the audit. If a live test send turns out to be the only way to settle a specific rendering question, I'll ask you first and name that exact action — and test sends are rate-limited per user and per workspace, so I'd only spend one on something reading the template can't answer.
