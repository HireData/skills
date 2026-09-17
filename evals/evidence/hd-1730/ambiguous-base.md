Happy to dig into this, but I should flag one thing up front: my connection to the HireData tools isn't active in this session, so I can't actually pull up your form right now and click through it. What I can do is tell you exactly what I'd check and how, so we can either walk through it together or I can run it properly once the connection is back.

"Something feels off" could mean a few different things, and they point to very different places:

1. **Structural/field issue** — a question is worded oddly, a field type is wrong (e.g., free text where you wanted a dropdown), required/optional flags are off, or the field order doesn't match how references actually read it.
2. **Logic/routing issue** — conditional branching (e.g., skip logic based on relationship-to-candidate) isn't firing right, or the form routes to the wrong next step/owner.
3. **Response quality issue** — you're getting responses back, but they're low-effort, incomplete, or inconsistent, which usually points to unclear question wording or a confusing layout rather than the form config itself.
4. **Delivery issue** — the form itself might be fine, but the invite email or link tied to it is what's actually broken (wrong merge fields, dead link, going to spam).
5. **Data/mapping issue** — the form works fine for the reference but the answers aren't landing in the right fields on the candidate/person record afterward.

If I had tool access right now, here's the sequence I'd run:

- `searchForms` — locate the exact reference-check form (there may be more than one version if it's been duplicated/edited over time) and confirm which one is actually live/linked.
- On the matching form, review its field list and any conditional logic, comparing question order and required/optional settings against what you'd expect for a reference check.
- `searchFormResponses` scoped to that form — pull the most recent submissions and look for patterns: blank fields that are "required," oddly short answers, or the same field getting misinterpreted across multiple respondents (a strong signal the wording or field type is confusing).
- `searchAutomationTriggers` — check whether anything triggers on form submission (e.g., moving a candidate stage, notifying the recruiter) and whether that's firing correctly.
- `searchEmailTemplates` / `searchMessageTemplates` — check the invite that carries the form link, since a broken merge field or stale link often gets misdiagnosed as "something wrong with the form" when it's actually the send.

To speed that up when the connection is back, it'd help to know:
- Is this about the questions themselves, how references are responding, or something downstream (data not syncing, notifications not firing)?
- Did this start recently, or after any edits to the form/template?
- Do you have a specific response or candidate where it went wrong that I could use as a concrete example?

Once I have tool access again, I'll pull the actual form and responses rather than going off memory — just wanted to be upfront that I haven't done that yet.
