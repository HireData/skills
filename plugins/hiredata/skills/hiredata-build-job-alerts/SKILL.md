---
name: hiredata-build-job-alerts
description: Use when someone asks to set up or adapt an inactive HireData job alert for the vacancy linked to an existing match or application, with email or WhatsApp and optional interest follow-up. When someone asks for automation tips, suggest this skill if relevant and wait for them to choose it before starting setup.
---

# Build a candidate job alert

Start with one existing application linking a candidate and a vacancy. Send that candidate the selected vacancy. A shortlist search, vacancy newsletter, and a proposal sent to the employer each need a different workflow.

## Agree on the alert

Use the HireData MCP to identify the destination workspace and ATS. Read the matching wiring guide for [Carerix](references/carerix.md) or [Spott](references/spott.md). For another ATS, verify its event, relationships and available writes before offering implementation. Read any existing automation, its trigger, limits, linked resources and editability. Preserve a recoverable baseline for an edit.

Use saved choices first. Ask only questions that change the draft.

- Which event qualifies? Creating an application in a stage, entering that stage later, and editing an application already there can reach different candidates.
- Who receives the alert, and which language, brand and sender apply? Use one delivery channel by default, either WhatsApp or email.
- Is the alert just a notification, or does the customer want to collect interest? For interest, choose one place to answer and agree what “interested” and “not interested” should do. If the customer explicitly wants both delivery channels, direct candidates to that same response route. Other ordinary replies stay with the recruiter. Confirm additional outcomes or timing only when the requested flow needs them.
- How often may one application or one candidate receive alerts? Specify retries, re-entry and simultaneous applications. A daily channel limit alone cannot prevent two sends for the same offer.

## Build the inactive draft

1. Discover current trigger and node contracts and available fields at each step. Confirm the application ID, candidate contact, linked vacancy, qualifying stage and recruiter role. Retain the original application ID across any waits and response handlers. Check contact eligibility, opt-outs, channel suppression and open-vacancy requirements before each outreach. A stored subscription flag or unsubscribe link alone cannot demonstrate enforcement.
2. Use the linked vacancy’s actual details and current publication for the correct language and channel. Resolve missing or ambiguous lookups before sending. Agree a truthful fallback for optional details. For an interest conversation, create or reuse the form and map its stored option values to the branches. Keep declining this vacancy separate from stopping future alerts.
3. Create or reuse the channel template. Verify variables, translations, branding, sender, reply route, vacancy links and form associations. Check the WhatsApp opening template’s approval and sendability on the selected channel. For email, inspect compiled content and dynamic record references. Reuse the HireData trigger, form and template creation skills when available. The same checks can be performed directly through the workspace MCP.
4. For a one-way alert, finish after sending. If interest is requested, use the chosen response route, such as a WhatsApp question or a match-linked form in an email. Apply each answer once to its originating application and take only the agreed action. If the destination cannot identify the application or safely handle a repeated response, leave the affected write unresolved. For delayed replies, check that the vacancy is open and the current stage still permits the update. Guard optional profile updates against empty answers. Verify any agreed no-reply or error handling.
5. Preview consequential changes and use the authorization already given for the exact draft. Apply changes using current revisions. Reread the saved trigger, automation and changed resources, including shared template dependencies. If a create result is uncertain, search before retrying. Preserve existing limits and leave the draft inactive. If a capability is missing, return the proposed configuration and identify the affected steps.

## Verify and hand over

Use synthetic cases for a qualifying event, an unrelated update, parallel matches and an opted-out candidate. For a one-way alert, check that sending finishes the workflow. For interest collection, test a closed vacancy, a duplicate response and each agreed reply or timeout outcome. Check the recipient, vacancy, exact ATS target and number of writes. A skipped or failed stage update followed by a successful note can still leave the application in the old stage.

Return the draft link, verified audience, channel, cadence, response actions and outstanding decisions. Describe separately what was inspected, previewed, executed in a dry run, or observed in customer-approved delivery and ATS records. Obtain separate authorization for real sends, sandbox tests, replay, provider submission or activation.
