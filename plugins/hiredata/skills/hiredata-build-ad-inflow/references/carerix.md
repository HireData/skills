# Carerix wiring

A Candidate is the person. A Match is the application linking that Candidate to a Vacancy/Job. A Publication is an advertisement for a vacancy. Resolve the vacancy reference before creating the Match. One candidate can have several matches.

## Build against the destination

Resolve the workspace, Carerix connection, source connection, trigger scope, automation revision and editability. Use the current MCP automation catalog and inspect the node contract, connected app objects and flow-position fields. The lookup field vocabulary can differ from the create/update field vocabulary. Inspect the corresponding purpose for each. Fetch live option lists, including later pages and dependent parent fields.

A visible legacy Job Application task can combine candidate and match writes. Verify whether that task is addable or editable on the destination engine. For a new draft, prefer verified current actions for exact vacancy lookup, candidate lookup or create/update, then match handling. Wire the candidate identifier from its actual output, or re-read by a proven unique criterion if required. Verify the writable Match relation to the exact vacancy. Preserve a legacy source or same-workspace shared resource when the request is for an independent draft.

## Lead and candidate fields

For Meta, preview the selected page and the exact form selection. Inspect the current all-forms option when requested and reread the saved trigger. It must retain the destination page and connection while permitting all intended forms. Never substitute a sampled form for a page-wide selection. If the event only contains a lead identifier, use an authorized source lookup supported by the configured integration, then map the retrieved answers. Use the request's actual scope and avoid unrelated trigger filters.

On a candidate create path, map separate first and last names and exactly one email destination. A collection-based email write needs one correctly shaped item. The lookup email can also be the search criterion. Do not add a second private/business email write. An existing-candidate ID-only path may need no candidate write. If the form supplies only a full name, settle how name parts will be obtained. If several forms use different source keys, normalize verified aliases and explicitly handle missing or conflicting values. Verify the phone collection's expected shape and omit empty input when the agreed update policy preserves existing values.

Check the saved mapping for required name fields. A conditional write on a required creation name can suppress a populated value. Prefer a direct mapping on the create path. Where update needs a nonempty-source condition, verify its create and update behavior separately or use distinct supported mappings. Preserve blank protection for unrelated fields.

## Application identity and writeback

A fixed job, dynamic job field or a verified vacancy number in the lead form name can identify the vacancy. Accept an extracted number only when it satisfies the agreed identifier pattern and uniquely resolves to the intended accessible vacancy. Preserve the form's actual vacancy reference through the write. Never infer a substitute vacancy from an unrelated number or AI ranking.

Resolve the exact match stage and source field from the destination. Candidate owner and match owner may follow different rules. For existing matches, confirm whether new answers, attribution or stage may change and which recruiter-managed stages are protected. Map any summary to the agreed Match destination. Use the actual Carerix option identifiers for structured answers. Keep blank, unknown and ambiguous answers distinct from an explicit negative. If consent is in scope, establish stage, period, date basis and whether existing consent can change.

For a replay or interrupted write, inspect the source event identity and existing candidate–vacancy pair. Use a source lead identifier on the application if the customer has approved a writable destination and its semantics. Reuse or update an existing Match only under the agreed policy. If the only lookup can return a best-scoring result or a capped list, establish whether it can prove uniqueness. A successful Candidate task and a skipped Match task is a partially completed intake. Identify the pending action and its retry conditions.

A non-writing preview may produce a candidate creation plan without a persisted record ID for the next Match step. Exercise the Match mapping separately with synthetic input where supported and report the remaining dependency on a real persisted ID. For authorized runtime verification distinguish candidate created, candidate updated, existing candidate reused, Match created, Match updated and intentional skips. A finished run alone does not prove the intended pair or external ATS state.
