---
name: hiredata-map-staffing-lifecycle
description: Apply staffing-agency and ATS domain knowledge (actors and ownership, the Carerix-style object model, match lifecycle stages, candidate- vs job-driven market context, communication cadence, and the data that actually matters) before reasoning about or acting on recruitment work. Use when a request touches candidates, contacts, companies, jobs, matches or applications, placements, talent pools, publications, or when deciding the right next step, audience, or timing — especially to tell a person apart from an application or a placement.
---

# Apply staffing lifecycle and ATS domain knowledge

Recruitment requests are easy to misread: the same word ("close the candidate", "the placement ended") can point at a person, an application, or a placement, and the right next step depends on the lifecycle stage, the market, and who owns the record. Use this domain judgment to interpret the request correctly, then act through the relevant creation skill and the live HireData MCP.

This skill supplies reasoning, not data. Never freeze schema or stage names from here — treat them as the *pattern* and confirm the workspace's actual fields, stages, and values through the MCP.

## Workflow

1. **Identify the actors and owners.** A staffing workspace has four actors: the **candidate** (looking for / being placed in a job), the **company** (where the candidate would work), the **contact** (a person at that company who hires — the hiring manager), and the **recruiter/user** (the person operating HireData). Candidate, contact, and company each have an **owner** (a user). Establish who is who and whose record it is before proposing an action. See [references/actors-and-objects.md](references/actors-and-objects.md).

2. **Place the request in the object model — and disambiguate.** Map the request onto the objects: person records (candidate, contact, company, user), the **application** (in Carerix, a **match** = a specific candidate + a specific job, moving toward a placement), **jobs**, **publications** (a job made public), **talent pools** (reusable candidate lists), and **placements** (the hire). The most common mistake is confusing a **person** with an **application/match** or a **placement**. Relationships are many-to-many — one candidate has many matches and many placements over time — so "the match/placement" is rarely unique to a person; confirm *which* one. A placement ending does not close the person — the person persists (often for redeployment). Also check ownership: candidate, contact, and job may have different owners. When a request is ambiguous, state which object you believe it means and confirm before mutating.

3. **Find the current stage and the event that should advance it.** A match moves through configurable stages (roughly: application → selection → proposal → interview → success/unsuccess → placement). Identify the stage the record is actually in and the event that legitimately moves it forward. Flag contradictions (e.g. a *Rejected* match cannot trigger onboarding or "role filled"). Note the **placement type**: temp/interim (assignment with an end date → redeployment) versus permanent/CDI (a one-time hire with a guarantee/fall-off window) imply different next steps — confirm which applies.

4. **Read the market context and pick the right journey side.** In a **candidate-driven** market (more jobs than candidates) speed and relevant candidate outreach dominate — job alerts to well-matched candidates, fast contact before competitors. In a **job-driven** market (more candidates than jobs) the recruiter sells candidates to contacts. Many steps have a **client-side** mirror (intake → submission → interview feedback → offer → placement → aftercare) whose audience is the contact/hiring manager, not the candidate; chasing client feedback and post-placement aftercare drives repeat vacancies. This changes the right action, audience, and message. See [references/lifecycle-and-communication.md](references/lifecycle-and-communication.md).

5. **Check the data that matters and name the gaps.** For candidates, **availability** is often the single most decisive field (you cannot propose someone who is not available), alongside work experience, education, and salary expectation. For jobs, the **requirements** (licenses, experience) and the offered **salary** matter most. Before acting, check these via the MCP; if a decisive field is missing, ask the one question that changes the outcome rather than guessing.

6. **Choose audience, timing, channel, and cadence — avoid the anti-patterns.** Keep contact regular from proposal through placement and beyond; a good call followed by two weeks of silence loses trust. Don't over-send: bulk email/WhatsApp that is irrelevant or too frequent annoys people, gets ignored, and risks spam flags that damage sender reputation. Add a follow-up (agenda or automated message) after phone contact. NPS surveys between stages are a normal quality signal.

7. **Inspect before proposing; preview before mutating; verify after.** Use the HireData MCP as the source of truth for current names, stages, fields, and workspace state. Never invent workspace facts, and never claim a mutation succeeded without re-reading it. Hand consequential creation (triggers, forms, emails, WhatsApp) to the relevant creation skill, which owns preview-and-approval.

## Quick disambiguation

- "Close / archive the candidate" after a placement ends → almost always means end the **placement** (and maybe update match status), **not** delete the person. Confirm.
- "Send the placement message" on a *Rejected* or non-placed match → contradiction; surface it and ask which candidate was actually placed.
- "Message the candidate about the job" → check the **match stage** and the candidate's **availability** first; wrong-stage or unavailable outreach is an anti-pattern.
- "Do the placement follow-up" → depends on **type**: temp/interim points at assignment end + redeployment; permanent/CDI points at the guarantee/fall-off window. Confirm which.
- "We can contact them, they're in our system" → an ATS record is not blanket consent; surface the purpose/consent question rather than assuming.
- Terms vary by ATS. These names are Carerix's; confirm the workspace's actual vocabulary via the MCP before using them in output.

## Guardrails

- This skill must not be silently required by other skills; it improves their reasoning but they must function without it.
- Do not perform consequential actions (create, send, publish, activate, invite) here — defer to the creation skill and its approval step.
- Do not present the stage names, market rules, or fields above as workspace fact; they are portable defaults to be verified against live MCP data.
- Treat consent, privacy, and channel policy as context-dependent; flag uncertainty instead of giving legal advice.
