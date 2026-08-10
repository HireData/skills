---
name: hiredata-create-email-templates
description: Design, validate, create, translate, or improve HireData email templates for recruitment and staffing workflows. Use when an email needs the right recipient context, subject, copy, brand, variables, modifiers, AI variables, calls to action, and measurable downstream behavior.
---

# Create HireData email templates

Design an email around the recipient's context and the next useful action.

## Workflow

1. Determine the trigger moment, recipient, sender, desired outcome, language, brand, and downstream action. Inspect any related trigger, form, message, or user story.
2. Use the HireData MCP to inspect current templates, available variables, related objects, brands, editor capabilities, translations, and duplicates.
3. Read [references/email-design-patterns.md](references/email-design-patterns.md) for structure, variable selection, modifiers, AI variables, and review criteria.
4. Decide whether the email is transactional, informational, or relational. Use buttons only when they clarify a meaningful action; do not force them into every email.
5. Show a plain-language preview containing:
   - internal name and purpose;
   - recipient and sender;
   - subject and preheader when supported;
   - complete copy and CTA destinations;
   - variables, modifiers, and AI variables with their data sources and fallbacks;
   - brand and language;
   - expected signal or next step;
   - assumptions and missing data.
6. Test the preview with complete, missing, null, unusually long, and wrong-language data. Treat AI-generated text as untrusted until it meets the stated constraints.
7. Create or update only after the exact preview is approved, unless already approved in the current conversation.
8. Re-read the saved template and verify rendering, variable resolution, links, recipient context, translation, status, and test-email behavior. Sending a test email requires an explicitly approved address.

## Guardrails

- Use MCP-supported editor operations; do not emit raw ProseMirror JSON unless the tool explicitly requires it.
- Prefer deterministic variables for facts. Use AI variables only for bounded transformation or generation where the source, instruction, tone, output length, and fallback are explicit.
- Never let an AI variable invent dates, salary, legal status, job facts, or commitments.
- Use modifiers for deterministic formatting, defaults, casing, lists, dates, or similar transformations supported by the current product.
- Do not publish, activate, or send beyond an approved test as an incidental step.
- If the MCP is unavailable, return an implementation-ready template and list unresolved variables or capabilities.
