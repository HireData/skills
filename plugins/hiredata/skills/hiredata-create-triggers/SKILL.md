---
name: hiredata-create-triggers
description: Design, validate, create, or improve HireData automation triggers for ATS events, dates, birthdays, schedules, and manual starts. Use when a user wants an automation to start at the right recruitment moment, needs filters or object relationships, or needs help diagnosing an unreliable or overly broad trigger.
---

# Create HireData triggers

Design the trigger around the business event and the data later workflow steps require.

## Workflow

1. Determine the outcome, source app, source object, trigger type, timing, population, and downstream steps. Ask only when a missing choice materially changes the configuration.
2. Use the HireData MCP to inspect available trigger capabilities, connected apps, objects, fields, relationships, and existing triggers. Use returned schemas as the source of truth.
3. Read [references/trigger-patterns.md](references/trigger-patterns.md) for naming, trigger-type selection, filtering, and relationship guidance.
4. Check whether the same or a materially overlapping trigger already exists.
5. Produce a preview containing:
   - name and purpose;
   - source app, object, event or schedule;
   - timing and timezone;
   - filters in plain language;
   - relationships needed downstream;
   - expected frequency and duplicate controls;
   - missing data and risks.
6. Resolve invalid field values, ambiguous relationship chains, and unsupported combinations before creation. Do not silently translate a user's business intent into a different population.
7. Create or update only after the user approves the exact preview, unless they already clearly approved it in the current conversation.
8. Re-read the saved trigger, compare it with the preview, and report its identifier and inactive/active state. Keep new or changed triggers inactive unless activation was explicitly requested.

## Guardrails

- Do not hard-code a connection name, source schema, or object ID.
- Do not activate an automation or trigger as an incidental part of creation.
- Do not broaden a filter because a field is missing. Report the gap.
- Preserve the source system's canonical values; translate labels for the user without changing stored values unless the MCP confirms the mapping.
- If the MCP cannot create triggers, return an implementation-ready configuration and identify the unsupported step. Never claim it was created.
