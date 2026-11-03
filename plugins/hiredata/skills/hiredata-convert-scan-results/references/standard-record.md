# Standard scan record

Normalize every input into this record before producing any output. It mirrors the acquisition sheet partners and HireData use to track scanned accounts, so the final block of every answer can be pasted as one row. Use `n/a` for anything the scan does not provide. Never fill a gap with an estimate.

## Account

| Field | Source | Notes |
|---|---|---|
| Company | user, sheet | Legal or trading name as the customer uses it |
| Name in HireData | MCP workspace, sheet | Workspace name; `n/a` when no workspace exists |
| ATS | MCP connection, user | Carerix, Spott, Salesforce-based, Vincere, OTYS, other |
| Website | sheet, user | |
| Business model | sheet, user | temporary staffing · contract/interim · secondment/detachering · permanent contingency · RPO/other |
| Partner CSM / Partner sales | sheet, user | The people who own the relationship on the partner side |
| Scan status | MCP, sheet | Scanned · Connection inactive · Connection broken · No workspace |
| Scan date | scan | |
| Scan type | scan | Prospect (potential) or Customer (results shown) |
| In a sales conversation (Yes/No) | sheet | |
| Converted (Yes/No) | sheet | |

## Scope

Candidates total and new in the last 12 months · Clients total and new · Contacts total and new · Vacancies total and new · Matches total and new · Placements total and in the last 12 months · Recruiters · Offices · scan window (start and end dates). The 12-month figures are the ones to lead with; totals are context.

## Health

Data Health Score (/100) · Reachability (%) · Profile completeness (%) · Dormant 180+ (% and count) · Consent recorded (%) when present

## Opportunities

- Top opportunity #1, #2, #3: finding, count, projected effect, exactly as the scan states them.
- Priority use case and Recommended template #1, as the scan states them.
- Researched use cases #1, #2, #3 (qualitative, from business model, sector and public signals) with the reasoning and an evidence rating (high, medium, low), when the acquisition sheet provides them. When they disagree with the scan's ranking, say which you followed and why.
- Recommended automation #1, #2, #3: use case name, channel, projected effect.

## Outcome

- Potential placements per year: expected · conservative.
- Potential hours per week: expected · conservative.
- Scan summary: the scan's own two-sentence summary when present, otherwise two neutral sentences built only from the fields above.
- Notes / flags: anything that weakens a claim (see Flags below).

## Results so far (customers only)

Assisted placements · time saved · data-health change since the previous scan. Leave out for prospects.

## Flags that must be recorded

- Scan older than 30 days.
- Connection inactive or broken, or no workspace: nothing can be claimed about the data.
- "No placement upside" verdicts (for example a database that is mostly less than twelve months old): lead with hours, not placements.
- Reachability or consent low enough that outreach cannot run before a fix.
- Shares above 100 %, counts that contradict the scope, empty objects on a live tenant, or a workspace that may belong to a different legal entity.
