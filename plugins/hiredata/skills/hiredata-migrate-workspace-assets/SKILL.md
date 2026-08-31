---
name: hiredata-migrate-workspace-assets
description: Migrate or replicate a proven HireData setup (data sources, forms, WhatsApp or email templates, triggers, automations) from one workspace to another, typically sandbox to customer. Use when copying a build across workspaces or ATS tenants, re-mapping tenant-specific fields and values, or promoting a validated flow to production.
---

# Migrate HireData assets between workspaces

Rebuild the setup in the target workspace against the target tenant's own data; never copy tenant-specific identifiers verbatim.

## Workflow

1. Inventory the source: data sources, form fields with options, logic, evaluation and translations, message and email templates, the trigger, the automation's tasks, and every token any of them uses.
2. Map the target's equivalents with the MCP before building: reference fields per object (custom-field identifiers differ per tenant), data-source items and their values, connections, channels, and locales. Keep a source-to-target mapping for every token and every expectation value.
3. Rebuild in dependency order: data sources, then the form with re-mapped tokens, translations and expectations, then the message template linked to the form and synced for provider approval, then the trigger, then the automation.
4. Link the form's data references (job, match, candidate) in the form editor before per-record configuration or token resolution, then confirm with the MCP that the keys saved.
5. Rebuild the automation in the workflow builder when the MCP only creates trigger templates: recreate each task, re-pick every token from the target workspace, name the automation, and leave it inactive.
6. Configure the designated test record so questions whose vacancy data is missing are switched off per record rather than rendered with empty tokens.
7. Test before handover: provider approval on a fresh read, a real-channel run through the builder's test-with-a-user flow, and the evaluation output of a completed response. A manual or test template send does not attach the automated conversation.
8. Hand over a gap list: fields, stages, or values missing in the target tenant, deferred write-backs, and everything the customer must create before go-live.

## Guardrails

- Never reuse tenant-specific tokens, custom-field identifiers, data-source item values, or expectation values across tenants without re-mapping them from the target's own reference data.
- Keep migrated triggers and automations inactive until the owner explicitly approves activation.
- Do not write answers into target fields with a different meaning just because the intended field is missing; report the gap and defer that write-back.
- Read [references/migration-playbook.md](references/migration-playbook.md) for re-mapping, builder, testing, and conversation-takeover specifics.
- Confirm live state after every consequential step by re-reading the resource; never claim provider approval, a saved reference, or a delivered message without a fresh read.
