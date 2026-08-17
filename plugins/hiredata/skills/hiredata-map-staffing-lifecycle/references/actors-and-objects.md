# Actors, ownership, and the ATS object model

Names below follow **Carerix** conventions. Other ATSs (Bullhorn, Greenhouse, Ashby, Workable, Teamtailor, etc.) use different words for the same ideas. Treat these as the pattern and confirm the workspace's actual vocabulary, fields, and stage values through the HireData MCP. Do not freeze these names into output.

**The live HireData MCP `capabilities` response is the source of truth** for objects, fields, stages, and their values. The tables here are a reasoning aid, not a schema. If a value you encounter is not in these tables, treat it as **undiagnosed** — inspect it via the MCP — rather than forcing it into the closest row. Never present a name from this file as a confirmed workspace fact.

## The four actors

| Actor | Who they are | Notes |
|---|---|---|
| **Candidate** | A person looking for a job, or being placed into one by the recruiter. | Has a profile. Owned by a candidate owner. |
| **Company** | The organization the candidate would work for (e.g. "Amazon"). | Has a profile. Owned by a company owner. |
| **Contact** | A person who already works at the company and who hires the candidate — the **hiring manager**. At a small company this may be the CEO; at a large one, a whole team. | Has a profile. Owned by a contact owner. |
| **Recruiter / User** | The person operating HireData. Uses it to automate tasks and make more placements. | In most systems the recruiter is called the **user**. |

All four have their own profile and are connected to each other. Candidate, contact, and company each carry an **owner** (which user owns the relationship). Ownership matters for routing, follow-up, and who is accountable for the next step.

## The objects that connect them

- **Application** — a candidate applying for a job. It can start from either side: the candidate reaches out (calls the recruiter, applies via a website, is referred) or the recruiter reaches out (LinkedIn, cold call, purchased lists). Either direction creates the link.
- **Match (Carerix)** — a specific **candidate + specific job** that the recruiter is trying to turn into a placement. This is the core working object of the ATS. ("Application" and "match" are the same idea under different system names.)
- **Job** — a role a company needs to fill. The recruiter pairs a job with a candidate to create the match.
- **Publication (Carerix)** — a job that has been made public (e.g. posted on the agency's website).
- **Talent pool** — a reusable list the agency keeps to track candidates (e.g. "IT specialists in AI"), so they can return to it when a relevant job appears.
- **Placement** — the hire. A candidate goes through the match stages and, if the company wants to hire them, the recruiter makes the placement.

## Person vs application vs placement (the key distinction)

These are different objects with different lifespans:

- A **person** (candidate/contact) persists across many applications and placements. Ending or archiving is rare and deliberate.
- An **application/match** is one attempt to place one candidate in one job. It has stages and ends in success or unsuccess.
- A **placement** is the resulting hire; it has a start and can end (assignment finished), which does **not** remove the person — they often return to a talent pool for redeployment.

When a request says "close the candidate", "the placement ended", or "wrap this up", determine which of these three it means before doing anything. Default to the least destructive interpretation and confirm.

## Relationships are many-to-many

A single person spans many objects over time; disambiguation depends on this:

- One **candidate** can be on many **matches** at once (different jobs) and many **placements** over their history.
- One **job** can have many **matches** (competing candidates).
- A **placement** belongs to exactly one candidate + one job, but a person accumulates many placements across a career.

So "the match" or "the placement" is rarely unique to a person — when a request names a person, confirm *which* match/job/placement is meant before acting.

## Ownership and handoffs

Candidate owner, contact owner, and company owner may be **different users** (a "split desk", where one recruiter owns candidates and another owns clients/jobs; a "360" recruiter owns both sides). Before proposing a next step, check who owns the record that action touches — the right person to send, follow up, or be accountable is the owner, not necessarily the requester.

## Placement / contract type

The type of placement changes everything downstream. Confirm how the workspace models this via the MCP; do not assume. Two broad patterns:

- **Temp / interim / contract** — an assignment with a **start and end date**, often timesheets and extensions. When it ends the person is not finished: they typically return to a **talent pool for redeployment**, and re-placement is a core, repeating revenue motion. Follow-up continues through and after the assignment.
- **Permanent / CDI (direct hire)** — a one-time hire, usually with a **guarantee / fall-off period** (a window in which a leaver may be replaced or refunded). Aftercare in that window protects the placement and the fee.

An agency may run both models (e.g. an "Interim & CDI" workspace). Ask or inspect which applies before choosing the follow-up, because interim redeployment and permanent guarantee windows imply opposite next steps.

## Why an ATS, not just a CRM

A plain CRM tracks companies and contacts. A staffing **ATS** (Applicant Tracking System) additionally tracks candidates and a **pipeline** that brings jobs and candidates together (the match and its stages). That candidate + pipeline layer is what recruitment-specific tooling adds, and it is where most staffing automation lives.
