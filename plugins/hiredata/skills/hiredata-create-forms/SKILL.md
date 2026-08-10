---
name: hiredata-create-forms
description: Design, validate, create, or improve HireData forms for recruitment and staffing workflows. Use for screening, availability, interview feedback, intake, consent, NPS, or other forms that need appropriate fields, validation, branching, language, context, and a useful next step.
---

# Create HireData forms

Create the shortest form that captures the decision or signal the workflow needs.

## Workflow

1. Identify the audience, use case, preceding trigger or message, language, required decision, and what should happen after submission.
2. Use the HireData MCP to inspect existing forms, current field types, schemas, theme and brand options, connected workflow context, and duplicate candidates.
3. Read [references/form-design-patterns.md](references/form-design-patterns.md) for recruitment form patterns and branching guidance.
4. Do not ask again for data already known from the trigger, person, application, meeting, vacancy, or preceding quick reply.
5. Show a preview before creating:
   - form name, audience, context, and language;
   - ordered fields with type and required/optional status;
   - choices and validation;
   - branching paths and endings;
   - submission outcome and owner;
   - assumptions and data or consent concerns.
6. Test the preview mentally against positive, negative, empty, invalid, and unexpected answers. Confirm every branch reaches an appropriate ending.
7. Create or update only after approval of the exact preview, unless the user already approved it in the current conversation.
8. Re-read the form and verify field order, stable identifiers, required flags, options, validation, branching, language, status, and preview link.

## Guardrails

- Use the current MCP schema instead of manufacturing raw editor JSON.
- Mark a field required only when the form's purpose cannot be fulfilled without it.
- Keep feedback forms short and screening forms decisive.
- End every path with a clear next step, not an unsupported promise.
- Do not assume an existing record proves valid consent for a new purpose. Follow the customer's policy and flag legal uncertainty.
- Keep a created form unpublished or inactive when the MCP supports drafts, unless publication was explicitly approved.
- If creation is unavailable, return the approved form specification and clearly state what remains unexecuted.
