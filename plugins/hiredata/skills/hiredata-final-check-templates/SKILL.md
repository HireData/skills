---
name: hiredata-final-check-templates
description: Audit HireData email and WhatsApp templates immediately before approval, launch, or automation activation. Use for final checks, pre-live QA, launch readiness, provider sendability, or a go/no-go review. Do not use to draft a template from scratch or diagnose post-send performance.
---

# Final-check HireData templates

Give a defensible go/no-go verdict for the exact saved template revision that would go live. Review the template and its immediate delivery dependencies; do not silently redesign it.

## Establish the release candidate first

Before judging wording, identify:

- workspace, template ID, latest full saved revision, channel, and internal name;
- trigger moment, recipient object, sender, brand, purpose, and intended next action;
- required locales and which locale is the default;
- connected form, URL, button, or reply path;
- provider approval and sendability state when relevant.

Use the HireData MCP to re-read the saved template and current status. Do not treat an editor preview, screenshot, earlier revision, or prior provider state as current evidence. If live access is unavailable, perform a static review but do not return a passing verdict; state exactly what remains unverified.

## Check in risk order

### 1. Identity, audience, and sendability

Block launch when the wrong template or revision is selected, the trigger cannot supply the expected recipient context, sender or brand is wrong, a required locale is absent, or the provider says the template cannot send. `PENDING`, `REJECTED`, and `isSendable: false` are not ready states.

### 2. Variable and rendering contract

For every variable, modifier, and AI variable, verify its source object, availability at the trigger moment, type, formatting, and fallback. Render or preview each locale with:

- normal representative data;
- missing, null, and empty optional data;
- unusually long values;
- special characters and realistic URLs;
- unavailable related objects or downstream destinations.

Block unresolved tokens, empty required values, broken grammar caused by fallbacks, unsupported modifiers, or AI output that may invent facts, commitments, dates, salary, eligibility, or legal conclusions.

Check fallbacks explicitly for every variable used in recipient-visible content. Recommend a concrete, type-safe fallback for every editable custom variable, including variables that are expected to be supplied by the automation. For non-editable system or runtime variables, recommend a supported inline default modifier when one is appropriate. Do not silently add fallbacks during the audit. First list the variables without fallbacks and the proposed values in the chat, then offer the user the option to add them. Apply them only after the user explicitly chooses that option and after re-reading the current saved revision.

Compare variable keys and meanings across the template, connected form fields, and automation mappings. Flag discrepancies such as `likelihood_to_process` in an email versus `likelihood_to_proceed` in its form, even when both tokens validate independently. A different key is not automatically wrong because an automation may map between names: state what is confirmed, what remains unverified, and the possible impact. First show the mismatch in the chat and offer the user the option to rename or align it. Before changing anything, explain which side should change, check downstream mappings, and obtain explicit authorization.

### 3. Message and locale integrity

Check that the recipient can understand why they are receiving the message, who sent it, what to do next, and what happens afterward. Confirm factual consistency, tone, spelling, dates, promises, and one clear primary action.

Unless the user explicitly narrows the scope, expect English as the default plus Dutch, German, and French. Preserve the same purpose, facts, links, variables, and action across locales; natural adaptation is preferable to literal translation.

### 4. Actions and immediate dependencies

Open and verify every link, button, connected form, and reply path. Confirm that button labels match their destinations, forms are usable by the intended recipient, responses route to the right workflow, and the copy does not describe a capability the channel lacks. Flag unverified cadence, duplicate-send prevention, subscription or consent handling, or unavailable dependencies as launch risks rather than assuming they work.

### 5. Channel-specific gates

For email, verify subject, preheader when supported, from identity, reply-to behavior, brand, body, signature, CTA destination, and the appropriate unsubscribe or preference mechanism for the message type. Inspect desktop and mobile rendering when the tooling supports it.

For WhatsApp, verify language code, current category, header/body/footer, variable numbering and examples, and every button. No locale may begin or end with a variable. Confirm response and no-response behavior. Do not describe a linked file-upload field as a native WhatsApp upload button; use a direct attachment prompt or a tested web-form URL. Treat current Meta policy as live evidence only when an authoritative source was checked in the current turn.

## Verdict

Return one of these exact outcomes:

- **READY** — every launch-blocking check was verified on the saved revision and no blocker remains.
- **READY WITH WARNINGS** — all launch-blocking checks passed; list only genuine non-blocking risks or improvements.
- **BLOCKED** — at least one blocker exists, or a required live check could not be performed.

Report:

1. the verdict and one-sentence rationale;
2. the exact template IDs, revisions, channels, locales, and provider states checked;
3. blockers first, each with evidence, impact, and the smallest safe fix;
4. warnings and optional improvements separately;
5. tests performed and anything still unverified.

When fallbacks or semantic key mismatches are found, include a short proposed-changes section before the verdict handoff. It must name each affected variable, show the recommended fallback or key alignment, and give the user a clear option to apply all recommendations or select individual changes. Do not treat an offered change as authorized until the user accepts it.

Do not call a template ready based only on copy quality. Do not edit, submit, activate, send a test, or send a live message unless that separate action is explicitly authorized. A test email or message also requires an explicitly approved recipient.
