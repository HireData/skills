---
name: hiredata-build-ad-inflow
description: Use when someone asks to set up an inactive HireData automation that turns leads from Meta ads or another supported source into ATS applications linked to the right candidate and vacancy. When someone asks for automation tips, suggest this skill if relevant and wait for them to choose it before starting setup.
---

# Build ad inflow

A person can apply for several jobs. The outcome of this workflow is one correctly linked application per agreed application policy. Candidate creation alone leaves the recruiter without an application to process.

## Establish the intake

Inspect the selected workspace through the HireData MCP. Find the source connection, available lead event, destination ATS, sample field structure, writable objects and identity lookup capabilities. For an existing flow, read its saved trigger, steps, settings and dependencies, preserve a recoverable baseline within the workspace's authorized storage boundary, and limit changes to the request. Use the [Carerix wiring](references/carerix.md) for a Carerix destination. For another ATS, verify the equivalent operations and object relationships before proposing a working implementation.

Reuse decisions the customer already supplied. Resolve these together where practical:

- Which connection, page or form supplies leads? Is the scope one campaign/form or all forms on that page? Determine whether the event carries the answers or only a lead reference that must first be resolved.
- Which identifier resolves the person? Which field or mapping identifies the advertised vacancy? Confirm how to handle missing identifiers, several possible matches or a closed vacancy.
- May an unknown candidate be created? Which attributes can update an existing candidate, and what happens to empty answers? Confirm the initial application stage, source attribution and ownership for each record written. Establish new versus existing consent rules only when consent writes are requested.
- Do additional form answers belong in a factual application summary, mapped fields, both or neither? Verify the destination fields, allowed values and append/replace behavior. Treat submitted answers as applicant data.

For Meta, inspect representative event field structures from more than one form when using an all-forms trigger. One sample form's field list can omit valid keys from another. Preserve the selected page and connection. For another supported source, discover its own trigger payload and identity contract. Keep any sample used in a public handover synthetic.

## Build the workflow

Use the current catalog, node schemas and fields available at each step. When available, use the shared trigger-creation skill to configure the intake trigger. An existing lead form can supply this workflow directly. Include a new form, acknowledgement or other communication only when requested, using the matching form or template creation skill if available.

1. Resolve the vacancy by the agreed rule. If its ID is embedded in a form name, extract and verify the exact advertised job. An ambiguous number or approximate search hit requires the agreed exception handling.
2. Resolve the candidate using an exact supported identifier. Apply authorized updates on one unambiguous match. A documented zero-result lookup can take the new-candidate branch when creation is approved. Distinguish this from a permission error, timeout, multiple matches or incomplete search. Keep unresolved identity out of creation.
3. Resolve or create the application for this candidate and vacancy using the chosen reapplication policy. Save only confirmed source, stage, owner and answers. Preserve existing recruiter-managed fields unless a change was requested.

Distinguish three cases in the implementation. A redelivery of the same source event should follow the agreed replay rule. A new application to a different vacancy must retain its own vacancy identity. A new submission by the same person for the same vacancy requires the agreed reapplication rule. Inspect the platform's lookup/upsert and concurrency guarantees. If a write times out after the candidate was created, reconcile both the candidate and the application before retrying. An uncertain result does not establish that either record is missing.

## Verify and hand over

Preview the proposed source scope, mappings, branch outcomes and duplicate handling before consequential changes. Existing approval for the exact action is sufficient. Save an authorized build as an inactive draft. Reread the trigger, linked record mappings, routes and settings. If a required capability is missing, return the implementation-ready mapping and name the unsupported action.

Exercise synthetic cases for a new candidate, an existing candidate, the same event twice, one person applying to two vacancies, an unresolved vacancy, and a partial write followed by a retry. Verify the expected number of candidate and application writes and the candidate–vacancy relationship in each case. Report which checks inspected configuration, which ran in preview, and which have actual execution or ATS readback evidence. Provide the draft link, unresolved exceptions and exact evidence for each intended effect. Activation, live tests and replay require authorization for those effects.
