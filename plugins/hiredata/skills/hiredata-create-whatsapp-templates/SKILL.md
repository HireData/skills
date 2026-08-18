---
name: hiredata-create-whatsapp-templates
description: Design, validate, create, or improve HireData WhatsApp templates for recruitment and staffing workflows. Use when a user needs concise message copy, variables, buttons, language, Meta category reasoning, approval readiness, or a connected form or follow-up flow.
---

# Create HireData WhatsApp templates

Create a concise message that is useful in context and likely to pass the current channel review requirements.

## Workflow

1. Determine what triggered the message, who receives it, the intended outcome, language, consent and conversation context, and what should happen after each response.
2. Use the HireData MCP to inspect existing templates, current template capabilities, variables, languages, approval states, connected forms, and duplicates.
3. Read [references/whatsapp-design-patterns.md](references/whatsapp-design-patterns.md) for channel-specific copy, category reasoning, and testing.
4. Check current authoritative Meta guidance when category or formatting policy could have changed. Treat static examples as patterns, not policy evidence.
5. Produce a preview containing:
   - internal name, language, and proposed category;
   - trigger, recipient, and purpose;
   - header, body, footer, variables, and buttons where supported;
   - category rationale;
   - response and no-response paths;
   - connected form or URL;
   - assumptions, consent concerns, and approval risks.
6. Validate variable order and examples; keep copy understandable when variables are long or missing. Test every button and downstream path.
7. Create or update only after the exact preview is approved, unless already approved in the current conversation.
8. Re-read the saved template and verify language, category, components, variables, button targets, and approval status. Report Meta approval as pending until the platform confirms otherwise.

## Guardrails

- Never claim that a template, duplicate, connection, channel capability or provider status
  exists unless a live read returned it in the current turn. If the workspace or MCP surface is
  unavailable, mark the fact as unverified instead of inventing a plausible result.
- Do not cite or summarize Meta policy as current unless an authoritative source was checked in
  the current turn. Without that check, mark category reasoning as provisional and do not invent
  a policy link.
- Do not classify a template as utility merely because it is manually initiated. Base the category on the content and current policy.
- Do not disguise promotional or re-engagement content as transactional.
- Do not imply Meta approval before approval is returned.
- Do not send a live message or start a conversation as part of template creation unless separately authorized.
- Keep personal and job data limited to what the recipient needs.
- If the MCP cannot create the template, return an implementation-ready specification and state what remains unexecuted.
