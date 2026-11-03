# Mapping scan findings to HireData use cases

Propose only use cases that exist in the product. The names below match the public examples on hiredata.com/examples and the template library; use them verbatim so the customer recognizes the same thing in the message, on the website, and in the app. Describe each one in the product's four-part structure: **Starts** (trigger) · **Does** (what the agent does) · **Writes** (what goes back into the ATS) · **You get** (the outcome).

When the HireData MCP is connected, check the template library for the current template that implements the use case before naming it; the library is the source of truth, this table is the fallback.

| Scan finding | Use case to propose | Default channel |
|---|---|---|
| Dormant candidates (no activity 180+ days), unknown availability | Database reactivation | WhatsApp, email fallback |
| Candidates whose contracts end soon; mid-term dormant | Database reactivation, triggered on contract end | WhatsApp |
| New candidates not screened; high applicant inflow | Pre-screening | WhatsApp |
| Leads from Meta campaigns | Ad inflow | WhatsApp |
| Matches without a score or next step | Matching (fit score, intake invite for strong fits) | AI, WhatsApp |
| Matches without candidate response; stalled procedures | Job alerts or a Matching follow-up nudge | WhatsApp |
| Shortlisted candidates waiting for an interview | Interview scheduling | WhatsApp, email |
| Qualified candidates waiting for an intake | Intake scheduling | WhatsApp |
| Candidates without a CV | CV collection | WhatsApp, email |
| Open vacancies with few matches | Talent pool first, then Job alerts | WhatsApp, email |
| Strong candidates available; clients who hire that profile | Candidate alerts | Email |
| Dormant clients (no placement or contact in 12 months) | Client reactivation | Email, in the account manager's name |
| Placements without feedback | NPS survey | Email, WhatsApp |
| Expired publications | Fresh vacancies (republish and translate) | Job boards |
| Low consent percentage; consent not recorded | GDPR consent | WhatsApp |
| Unreachable or outdated client contacts | Contact enrichment | Email, form |
| Conversations held outside the ATS | Conversation logging | WhatsApp |
| Unassigned candidates, no active owner, uneven office distribution | Ownership and distribution cleanup (internal data-hygiene step, not a public use case) | Internal |

## Business-model defaults

Use these only when the scan does not make the lead opportunity obvious.

- **Temporary staffing:** Database reactivation first, Job alerts second.
- **Secondment / detachering:** Database reactivation on contract end first, Client reactivation second.
- **Permanent contingency:** Matching and Pre-screening first, Candidate alerts second.
- **Contract / interim:** availability-driven Database reactivation first, Candidate alerts second.

## Sequencing rule

Recommend one automation to start with, one to add in month two, and one for later. Start with the automation that needs the least data preparation from the customer and the fewest approvals (usually one WhatsApp template and one audience decision).
