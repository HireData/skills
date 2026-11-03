---
name: hiredata-convert-scan-results
description: Turn HireData Scan results for a recruitment agency on any ATS into the next step with that customer - an outreach message to open the conversation, a guide to walk through the results together, or a proposal to sell HireData - plus a standardized record for the acquisition sheet. Use when someone has scan findings (from the HireData MCP, a scan report, a PDF or a screenshot) and asks what to say to the customer, how to run the review call, which automations to propose, or what to log. Do not use for running or diagnosing automations, or for anything that needs person-level data.
---

# Convert scan results

The Scan already did the analysis. This skill does the translation: pick what matters, say it in the customer's words, map it to automations HireData actually offers, and hand the person something they can send, run or paste within a minute. It works for any ATS and any partner; say "your ATS" and "your account manager" unless the user names them.

## First decide which job you are being asked to do

- **Open**: get into a conversation. First contact after a scan. Output: a five-line brief, a message under 120 words, a log line.
- **Review**: go through the results together. A call is planned. Output: a 20 to 30 minute call guide with questions and objections.
- **Sell**: proposal or business case. The customer asked for a proposal, or the review call happened. Output: a one-page proposal.

Default to Open when nothing indicates otherwise. Ask only when the mode genuinely cannot be inferred.

## Workflow

1. **Get the scan.** Prefer the HireData MCP: `searchScans` (operation `show`, no scanId) returns the latest completed scan's findings for the workspace: counts with 12-month deltas, Data Health, projection with baseline placements and the value-model assumptions behind it, ranked opportunities, recommended templates and the summary. Use `searchScans` operation `section` (candidates, clients, contacts, vacancies, matches, placements, activity, team) for the breakdown behind a finding, and operation `team` for per-recruiter or per-office figures. Never call operation `placements`, which returns person identifiers. Starting a new scan is `saveScan` operation `create`, which requires the user's explicit confirmation (`confirmStart`) and can take minutes to hours; otherwise accept a scan report, PDF, screenshot or a row from the acquisition sheet, and say which you used. If the scan is older than 30 days, say so and offer a refresh. If there is no scan, or the connection is inactive or broken, say exactly that and stop. Never estimate numbers to fill the gap.
2. **Establish the context you need**: customer, business model, language of the relationship (Dutch for NL/BE by default), whether they are a prospect or a customer with live automations (the scan type usually says), and who is sending (partner CSM, partner sales, or HireData). Messages go out in the sender's name.
3. **Normalize into the standard record.** See [references/standard-record.md](references/standard-record.md). It mirrors the acquisition sheet; every output ends with it so it can be pasted as one row.
4. **Find the one number.** The finding with the best mix of size, reachability and ease of action. Usually dormant-but-reachable candidates. Two exceptions: when the scan says there is no placement upside (a young database), lead with hours saved; when reachability or consent is the blocker, lead with that, because nothing else runs until it is fixed.
   Prefer the last-12-month figures over lifetime totals when both exist: "61 placements last year" says more about the agency today than "514 placements ever". Use the business model and sector (researched, not from the scan) to choose between use cases the numbers alone cannot separate; the scan's own ranking leans towards reactivation and job alerts whenever dormant candidates or open vacancies exist, so treat it as one input, not the verdict.
   The findings expose the assumptions behind the projection (`valueModel`: dormant reply rate, reply-to-placement rate, recruiters in scope, hours per recruiter per week) and the baseline (`baselineAnnualPlacements`, `upliftPct`). Quote the assumption when you quote the projection.
   Sanity-check every projection against last year's placements before quoting it: if the expected uplift exceeds roughly half of the placements made in the last 12 months, or placements are missing, quote only the conservative figure and flag the expected one in Caveats as not credible for this agency. When the scan returns no conservative figure (the MCP projection currently gives only the expected one), quote no placement number at all: lead with the finding itself, and with hours only if they pass the same check. Never derive a conservative figure yourself, for example by halving the expected one.
5. **Pick two supporting findings**, ideally one on data quality and one on the client or vacancy side. Three findings in total. The customer hears one; the brief and the proposal hold three.
6. **Translate to outcomes with the scan's own figures.** Always give expected and conservative. Label them as projections. Never add, round up or extrapolate.
7. **Map each finding to a use case** using [references/use-case-mapping.md](references/use-case-mapping.md), expressed as Starts / Does / Writes / You get. When the MCP is connected, confirm the current template in the library before naming it. Recommend one automation to start with, one for month two, one for later; start with the one needing the least preparation.
8. **Produce the mode output** from [references/mode-templates.md](references/mode-templates.md), then the standard record, then a `Caveats` line when any flag applies.

## Rules

- Aggregates only. Never include names, email addresses, phone numbers or record identifiers in any output, even when the input contains them.
- Quote the scan. Projections stay projections: "could" and "projected", never "will". The conservative figure always sits next to the expected one; when the scan gives no conservative figure, the expected one is not quoted either.
- One opportunity per message; three per review or proposal.
- Use the product's use-case names and the Starts / Does / Writes / You get structure so the customer sees the same thing on the website, in the message and in the app.
- Do not mention plans, prices, discounts or contract terms the sender did not supply. For prospects, the next step is seeing their scan together, never buying.
- Flag instead of building on bad data: inactive or broken connections, no workspace, scans older than 30 days, "no placement upside" verdicts, shares above 100 %, counts that contradict the scope, a workspace that may belong to a different entity. Flags go in the record and in the `Caveats` line.
- Do not run, create, activate or send anything. This skill produces text for a person to use.
