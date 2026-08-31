# Cross-workspace migration playbook

## Re-mapping tenant data

- Custom object fields (for example a vacancy's additional-info fields) carry tenant-specific identifiers. Look them up per object in both workspaces through the MCP's reference-field listing and match on label, not on identifier.
- ATS data nodes (language levels, stages, motives) have tenant-specific item identifiers too. Rebuild each needed data source in the target workspace and re-map every screening expectation to the target's item values before relying on the rules.
- Write-back targets may not exist in the target tenant. List the missing candidate, match, or vacancy fields and stages for the customer instead of repurposing semantically different fields.
- External-object records are read-only in HireData; filling missing vacancy data happens in the ATS. Until then, per-record question toggles are the supported mitigation, with token default filters as cosmetic insurance.

## Rebuilding the automation

- The MCP creates trigger templates; a full canvas automation (start, filters, tasks) is built in the workflow builder.
- The builder's token picker fuzzy search is unreliable. Search the literal question text, or type the raw token prefix, to surface the right suggestion. Question answers offer Question, Answer Label, and Answer Value variants: write stable values to external fields, not labels. Text questions expose a single answer token.
- Click into an input before typing. Stray keystrokes on the canvas trigger navigation shortcuts and can discard an unsaved task.
- The send-survey task defines the AI conversation (goal form, template, recipient, owner); the channel and sender come from the linked template's connection.

## Testing semantics

- A manual or test template send delivers the message but opens a manual conversation: candidate replies are not answered by the AI flow. The automated conversation only attaches when the automation's send-survey task starts it.
- The builder's test panel offers two modes: previewing a single item runs the automation against one record without executing tasks; testing with a user executes real actions, but only toward the selected user.
- One automated conversation stays open per person. A new send toward that person may require an explicit takeover; take over only with the owner's confirmation, re-reading the conversation immediately before.
- Provider template approval is asynchronous. Report it as pending until a fresh read returns approved, and only then run the live-channel test.

## Per-record configuration

- Per-vacancy question toggles and classification overrides live on the record's form configuration, which requires the form's data references to exist first.
- A field marked mandatory cannot be excluded per record. If the design calls for per-vacancy toggling, the field must not be mandatory.
