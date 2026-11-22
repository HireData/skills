# Carerix wiring

Use the workspace MCP to check current events, relationship fields, value types and write settings. The field names below are discovery starting points.

| Role | Where to look |
| --- | --- |
| Alert identity | The triggering Match and its `_id` |
| Candidate recipient | The Match’s `toEmployee` relationship |
| Vacancy | The Match’s `toVacancy` relationship |
| Stage | The Match’s `statusInfo` with a workspace-specific value |
| Recruiter | Match owner, candidate owner or modifying user according to the requested role |

For entry into a phase, inspect the updated-Match event, its condition target and the stage rule. Check the saved condition as well as the trigger setup, especially on older engines. Exercise a record already in the phase, a genuine entry, and creation in the phase. An event that changes only the candidate or a sibling match should leave this offer untouched.

Load the candidate, vacancy and agreed recruiter relationships at the send step. Inspect vacancy-specific links and any publication lookup for its medium and language. Treat an integration user as a possible modifying user when choosing a reply owner.

Target the triggering Match ID for the response note, task or change of phase. Write candidate availability only when agreed and the answer is present. Before a delayed update, verify the match still belongs to the original candidate and vacancy and its current stage allows the change. Ensure the automation’s own updates cannot qualify the same alert again.

For an existing flow, read `editable` and `readOnlyReason`. An exact same-workspace duplicate may retain its engine and shared linked resources. Verify inactivity, independent node IDs and dependencies. When an adaptation needs a new draft, discover the current record-update and person-mapping contracts instead of reusing legacy step settings.
