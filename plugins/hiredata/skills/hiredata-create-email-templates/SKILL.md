---
name: hiredata-create-email-templates
description: Design, create, translate, or improve high-quality HireData email templates for recruitment and staffing workflows. Use when an email needs strong copy, the right recipient context, supported variables, four-language coverage, brand and form compatibility, robust formatting, or verified compiled output. Do not use for a full automation launch audit or post-send performance diagnosis.
---

# Create HireData email templates

Create an email that is clear for the recipient and reliable in HireData's rendered output. Stay focused on the email and the immediate assets it uses; do not turn this workflow into a total automation audit.

## Workflow

1. Establish the email brief: what happened, why the recipient receives this message, who sends it, what the recipient should understand or do, the default locale, the brand, and any form or URL the email must use. Inspect only enough trigger context to choose the correct recipient and available data.
2. Use the HireData MCP to inspect the current template when one exists, the exact supported variables and modifiers, related-object availability, brands, translations, connected forms, editor capabilities, saved revision, and compiled or rendered output operations. Do not infer support from token shape or from another template.
3. Read [references/email-design-patterns.md](references/email-design-patterns.md) for copy structure, variable selection, multilingual consistency, email-safe layout, and compiled-output checks.
4. Unless the user narrows the language scope, write English as the default plus Dutch, German, and French. Preserve purpose, facts, variables, links, and the primary action across locales while adapting the wording naturally.
5. Decide whether the email is transactional, informational, or relational. Use one clear primary action. Add a button only when it makes that action clearer and its destination is verified.
6. Show a plain-language preview containing:
   - internal name and purpose;
   - recipient and sender;
   - subject and preheader when supported;
   - complete copy and CTA destinations;
   - variables, modifiers, and AI variables with their data sources and fallbacks;
   - selected brand and all required locales;
   - connected form or URL and the exact button destination;
   - typography, alignment, spacing, greeting, and signature behavior;
   - expected signal or next step;
   - assumptions and missing data.
7. Test every locale with complete, missing, null, unusually long, special-character, and wrong-language data. Treat AI-generated text as untrusted until it meets the stated constraints.
8. Inspect the compiled or rendered email for every locale instead of trusting only the builder. Verify subjects, preheaders when supported, variable resolution, character encoding, every link and button destination, line breaks, spacing, repeated-block alignment, mobile-friendly flow, and that platform-managed greetings or signatures are not duplicated.
9. Create or update only after the exact preview is approved, unless already approved in the current conversation. When improving an existing email, preserve the supplied original or copy boundary. Fetch the complete current resource immediately before mutation and use its latest revision; never force an update through a stale-revision conflict.
10. Re-read the saved revision and inspect its compiled output again. Report what was verified, which inbox clients were actually tested, and any email-specific limitation that remains. Do not declare the wider automation ready from this email check alone. Sending a test email requires an explicitly approved address.

## Guardrails

- Use MCP-supported editor operations; do not emit raw ProseMirror JSON unless the tool explicitly requires it.
- Prefer deterministic variables for facts. Use AI variables only for bounded transformation or generation where the source, instruction, tone, output length, and fallback are explicit.
- Never let an AI variable invent dates, salary, legal status, job facts, or commitments.
- Use modifiers for deterministic formatting, defaults, casing, lists, dates, or similar transformations supported by the current product.
- Use editor-supported, email-safe typography and spacing. Avoid fragile layout techniques, decorative font dependencies, and formatting that works only in the builder.
- Build repeated cards, headings, and buttons from one consistent email-safe structure. Keep typography, alignment, dimensions, and spacing identical while allowing sufficient room for the longest supported content.
- Verify the selected brand and any connected form or URL against the saved template; do not silently substitute a similarly named asset.
- Do not publish, activate, or send beyond an approved test as an incidental step.
- If the MCP is unavailable, return an implementation-ready template and list unresolved variables or capabilities.
