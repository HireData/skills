# Review call prep — permanent recruitment agency, scan of 29 October

Note: the HireData MCP is unavailable, so I could not pull the scan record itself. Normally I would call `getContext` / `queryStatistics` on the workspace (or `searchPlatformOrganizations` → `queryPlatformStatistics` on the platform side) to verify the figures and see which automations the hours estimate is built from. Everything below is based on the numbers you gave me.

## 1. What the scan actually says

**This is a young, fast-growing, under-worked database — not a dormant one.**

- 994 of 1,143 candidates (87%) were added in the last 12 months. Dormant 180+ is only 5.7%. There is almost nothing to reactivate; the classic "wake up your old database" story does not apply here.
- 114 placements by 9 consultants = ~12.7 per consultant per year, roughly one a month each. Healthy for perm.
- 723 of the 994 new candidates (73%) have never been screened. They are adding candidates far faster than they are working them.
- 6,095 matches without candidate response on 1,143 candidates = ~5.3 unanswered matches per candidate. That is not a response problem, that is a match-hygiene problem: matches are being created in bulk (auto-match, job alerts, or shortlisting without contact) and never closed out.
- 1,155 companies without an account manager. On a 9-consultant team that is ~128 orphaned companies per person. The client side is where the ownership gap is.
- Data health 69/100 is dragged down by completeness 37.2%, reachability 55% and consent 46.3%. Half the database cannot be reached on WhatsApp and less than half has consent on record.

**Why the placement number is +0 / +0 (assumption: optimistic / conservative scenario).** The placement model is driven by reactivation and re-engagement automations, which need reachable, consented, dormant candidates. This agency has almost no dormant pool (5.7%), and of what exists, only ~half is reachable and consented. So the model has nothing to attribute placements to. The zero is a consequence of the data profile, not a verdict that HireData cannot produce placements here. The hours figure (+11.7 / +6, assumed per week) comes from the operational automations — matching follow-up, account-manager assignment, pre-screening — which do not depend on consent.

## 2. The opening — and why not the placement number

Do not open with a placement figure. There are two ways that goes wrong:

1. If the rep quotes an invented or borrowed placement uplift, the agency will ask where it comes from, look at the scan, see +0 / +0, and the rest of the call is about credibility rather than their database.
2. If the rep quotes the honest +0, the call opens on a negative and the hours story never recovers.

**Open instead with a number that is real, theirs, and bigger than their placement count:**

> "You placed 114 people last year with 9 consultants. You also added 994 candidates in that same year, and 723 of them have never been screened. That is more than six times your annual placements sitting in the database with nobody having had a first conversation with them."

Second beat:

> "On the client side, 1,155 companies have no account manager. Nobody owns them, so nobody is calling them."

Third beat, where the placement conversation belongs:

> "The scan does not yet model placements for you, and I want to be straight about why: it only counts placements it can attribute to reactivating reachable, consented candidates, and you have a young database where half the records have no usable mobile number or consent. Fix that and the placement model switches on. The hours it can already model — about 6 to 12 a week — are what we would start with."

That is honest, it still leads with a big number, and it turns the data gap into the first thing HireData fixes rather than a reason to say no.

## 3. Suggested call structure (30 minutes)

| Time | Block | Goal |
|---|---|---|
| 0–3 | Context | Confirm the ATS, who the 9 consultants are, who owns BD. Confirm the scan date and that nothing major changed since 29 Oct. |
| 3–8 | The headline | 723 unscreened + 1,155 orphaned companies. Get them to react before showing anything else. |
| 8–15 | Data health | Walk completeness 37%, reachability 55%, consent 46%. Ask how candidates come in (job boards, LinkedIn, referrals) and why phone/consent is missing. Explain the placement model honestly here. |
| 15–23 | The three opportunities | Pre-screening (723), match follow-up (6,095), account-manager assignment / client reactivation (1,155). Hours per week per item. |
| 23–28 | Proposed first 90 days | See section 5. Agree on one or two to start. |
| 28–30 | Next step | Pilot scope, data owner on their side, date for the activation session. |

## 4. Discovery questions to ask

Candidate intake
- Where do the 994 new candidates come from? Job board applications, sourced, referrals? (Determines whether a first-contact WhatsApp is appropriate and whether consent can be captured at the point of entry.)
- Who screens today, and what happens to a candidate nobody screens within a week?
- Why is phone/consent missing on half the records: is it not collected, or collected and not entered in the ATS?

Matches
- What creates a match in their ATS: a consultant shortlisting, auto-matching, job alerts? Are the 6,095 real shortlists or system noise?
- Is there a status they would consider "closed, no response" so these can be cleaned up?

Clients
- Is the 1,155 a real orphan list or a data artefact (e.g. account manager field never used, or companies imported from a legacy system)?
- How many of those companies have had a placement or job in the last 2 years? (That subset is the real reactivation list.)

Team
- 12.7 placements per consultant: is the constraint candidate supply, client demand, or consultant time? Their answer tells you which opportunity to lead the pilot with.

## 5. Recommended activation order

1. **Pre-screening on new candidates (first 30 days).** Triggered on candidate creation; WhatsApp where a mobile exists, email otherwise; screening form captures availability, salary, location, and — critically — mobile number and consent. This both works the 723 backlog and starts repairing reachability and consent on every new record. It is the automation that eventually turns the placement model on.
2. **Match follow-up (days 30–60).** Triggered on match creation or match stale for N days; asks the candidate to confirm interest; auto-closes on no response after two nudges. Saves the 23 min/week and, more importantly, stops the 6,095 pile from growing.
3. **Account-manager assignment and client reactivation (days 60–90).** First a one-off rule to assign the 1,155 companies (by region, sector or last consultant who placed there), then a reactivation message to the subset with a placement or job in the last 24 months. This is the biggest hours item (1.5 hrs/wk) and the most likely to produce new jobs — which, for a perm agency, is where placements actually come from.
4. **GDPR consent run** in parallel with step 1 for the existing base: a single consent request to the ~54% without consent, so the database becomes usable for outbound.

Deliberately not recommended as a first move: database reactivation on WhatsApp. With 5.7% dormant and 55% reachable it would send a few dozen messages and prove nothing.

## 6. Objections to prepare for

- "Your own scan says zero placements." → "Correct, and here is why" (section 2, third beat). Offer to re-run the scan after 90 days of pre-screening and consent capture and show the model change.
- "11 hours a week is not much across 9 people." → Reframe: it is ~1.3 hours per consultant per week, but the real value is the 723 candidates and 1,155 companies that currently get zero hours. Hours saved is the floor; coverage is the point.
- "We do not have mobile numbers for half our candidates." → That is exactly what the pre-screening form collects. Email is the fallback channel from day one.
- "Our consultants will not trust automated screening." → Automation does the first contact and the form; the consultant gets a filled profile and decides. Nothing is rejected automatically.

## 7. Things I could not verify (check before the call)

- Whether +11.7 / +6 is per week and which automations it sums; and whether the two figures are optimistic/conservative or two different scopes. Pull this from the scan detail (`queryStatistics` on the scan workspace).
- Whether "matches without candidate response" counts open matches only or all historical ones. If historical, the 6,095 is a clean-up job, not a follow-up job.
- Whether the 1,155 companies include inactive or legacy records. Ask for a count of companies with a job or placement in the last 24 months.
- The ATS. If it is Carerix, account-manager assignment and match-status rules are straightforward; if not, confirm the fields exist before promising the third automation.

**One-line brief for the rep:** lead with 723 unscreened candidates and 1,155 unowned companies, be upfront that the placement model is off because of data and that pre-screening is what turns it on, and sell the first 90 days on coverage, not on hours.
