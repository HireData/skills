---
name: hiredata-build-meeting-reminders
description: Use when someone asks to set up or adapt HireData reminders for already-booked meetings, including appointment type, interviewer, local time, link or location, and changed bookings. When someone asks for automation tips, suggest this skill if relevant and wait for them to choose it before starting setup.
---

# Build meeting reminders

Start with a booked appointment. The reminder goes to its linked candidate at the agreed time before the meeting. If the candidate still needs to choose a slot, the request belongs to interview scheduling.

## Agree what the candidate should receive

Use the workspace-scoped HireData MCP to inspect the appointment source, existing booking confirmations, and other reminders for the same audience. Open the applicable ATS wiring reference. [Carerix wiring](references/carerix.md)

Reuse the customer's wording and settled choices. Resolve only the decisions that change the reminder.

- Which booked meeting types qualify? For video, telephone and in-person appointments, confirm which details each message requires.
- What offset and timezone apply? A reminder one hour before the appointment and a batch sent every morning reach different audiences. Agree what to do with a booking made inside the offset and a meeting moved after an earlier reminder.
- Which candidate, sender, language and reply owner apply? Who conducts this appointment? Where does its confirmed joining link, telephone instruction or address come from?

## Build the draft

1. Inspect the saved source, linked templates, feature access and editability. Search for an existing task draft. Preserve a recoverable baseline for an edit. Verify current node types, fields, people presets and template choices with the automation catalog. Use the trigger and channel-template creation skills when available. If the connector lacks a required capability, return the proposed settings and identify the unsupported part.
2. Configure a date-relative trigger on the booked start datetime, for the agreed appointment types and offset. Preserve subscription requirements, limits and existing weekend settings. Choose a supported duplicate key for the agreed policy. An appointment ID identifies a meeting. Pairing it with the start instant distinguishes a rescheduled occurrence. Verify the scheduler's behavior for repeated evaluations and existing queued jobs.
3. Immediately before the message, compare the queued occurrence with the authoritative current appointment. Check that the meeting still qualifies, the candidate is still linked, the start matches the scheduled occurrence, and the send is still timely. Resolve the current interviewer and joining details. Use the connector's verified send-time check or retrieve the appointment by its stable ID. Hold the message when the appointment is missing, cancelled, moved, ambiguous or unreadable. If reliable send-time checking is unavailable, document the stale-reminder risk before activation.
4. Map the candidate's name, interviewer, displayed local time and required joining details at the send step. Keep the conversation owner as configured. Guard required values or use a customer-approved alternative message. Preserve exact supplied copy and requested locales. For WhatsApp, check the sender, template, variables, provider approval and sendability in the workspace. For email, verify the sender and rendered template. Add follow-up or ATS writes only when requested.
5. Show the proposed trigger, audience, sender, copy, mappings and change handling. Apply an already-approved build as an inactive draft. Reread the saved automation and templates. Inspect dependencies and issues. If a save result is uncertain, reread it before retrying.

## Verify and hand over

Use synthetic previews and supported dry runs. Check these cases against the saved draft.

| Case | Expected result |
| --- | --- |
| Eligible appointment in winter and summer | Correct candidate and interviewer. Offset is relative to the scheduled instant. Display reflects the local offset on each meeting date. |
| Wrong type, missing required link, unsubscribed recipient | Reminder stops or uses the agreed alternative for that case. |
| Duplicate evaluation or late booking | The agreed duplicate and lateness policies determine the outcome. |
| Meeting moves after queueing, then the old job runs | The old occurrence produces no send. Evaluate the new occurrence under the rescheduling policy. |
| Cancellation, changed attendee or failed source lookup before send | No stale message goes to the original candidate. |

Return draft links, observed status, changes, test results and any unverified behavior. Identify which checks used previews and which used actual scheduler or provider evidence. Keep provider submission, real messages, sandbox sends and activation within their explicit authorization.
