# Carerix meeting reminders

Use a Carerix Meeting linked to the intended Candidate. Discover fields through the destination's supported HireData MCP operations before binding them. An appointment stored on another object needs its own evidence that its datetime, interviewer and candidate belong to the same occurrence.

## Trigger and identity

- Inspect the connection, catalog, saved automation, editability, source revision, loaded relationships and overlapping reminders. An exact same-workspace copy can reuse the supported duplication operation. Verify that the copy is inactive and independent, and check which templates and connections are shared. A duplicate can retain the original engine. Use a new supported inactive draft for an authorized adaptation when the old engine cannot be edited.
- Verify the custom date trigger on Meeting and the real start datetime. Check whether `startDate` includes its time, or whether the connector requires a separate time field. A display field such as `timeDisplay` can render text but does not establish timezone or scheduling semantics. Preserve the requested offset, repeat and weekend rules.
- Fetch current canonical meeting-type and status values using the connection's option lists. Check `toActivityTypeNode`, status, deleted markers and the linked candidate. Where a meeting-name convention defines eligibility, verify it on representative meetings and check a similar nonqualifying name. Do not reuse option values, cutoffs or connection IDs from other workspaces.
- Inspect occurrence identity at enqueue and send. Re-read by the stable Meeting ID, compare the current booked start instant and candidate with the queued identity, and check current deletion, cancellation and meeting type. If no reliable lookup or equivalent scheduling guarantee exists, disclose that an old queued message may survive a reschedule. Keep the draft inactive while this affects the agreed behavior.

## Recipient and content

Use the linked Candidate people preset when available and verify the subscribed destination. Inspect the Meeting's candidate relation, commonly `toEmployee`. The meeting owner, its attendees, the creator and the candidate owner can be different people. Verify which field identifies the person conducting this specific meeting. Resolve conversation ownership separately.

Inspect `meetingCallLink` or another proven source for video appointments. A `location` field can contain an address or free text. Verify the expected URL shape and provenance from permitted records or synthetic inputs without opening a private meeting link. Use approved phone or location wording for telephone or in-person appointments. Show which types a required-link guard would suppress.

Inspect `context` and `listFields` at the send node, then map the selected template's actual variable keys. Preserve the candidate name, recruiter, local start time and link mappings the user needs. Include a vacancy lookup only when a required field actually comes from that vacancy. Verify rendering with accents, apostrophes, long names and URL query parameters. For missing values, agree on a truthful alternative or hold the send.

## Timing checks

Use two synthetic appointments in the workspace timezone, one in winter and one in summer. Compare the displayed appointment time and intended reminder instant separately. If a customer uses a fixed morning dispatch, test the calendar-day boundary and the handling of meetings that start before dispatch. For a relative reminder, test a booking made shortly inside the offset and a delayed job that wakes after the meeting has begun.

For a reschedule, queue an occurrence, move the source start and evaluate the old job. Test a cancellation and a candidate change the same way. Verify a new occurrence separately. Where a preview evaluates an isolated node or a dry run bypasses trigger scheduling, record that limit. A successful message step demonstrates only the status it returned. Provider delivery needs corresponding channel evidence.
