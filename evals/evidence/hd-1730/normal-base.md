Happy to give it a look before you flip it on. Quick heads-up first: my connection to the HireData tools isn't active in this session, so I can't actually pull up the live template right now — I can't show you real content or confirm real data. What I can do is tell you exactly what I'd check and how, so you can either let me run it once the connection's back, or walk through it with me now by pasting the template content here.

Here's what I'd do and what I'd be looking for:

**1. Find the template**
- Call `searchEmailTemplates` with a query like "Interview Confirmation" to locate the exact template (and check there isn't more than one candidate with a similar name — duplicate/draft copies are a common source of "we edited the wrong one" bugs).

**2. Review the content itself**
- **Merge fields / personalization tokens**: candidate name, job title, interview date/time, interviewer name(s), location or video-call link, company name. I'd cross-check these against `searchFields` to confirm each token maps to a real field in your data model and isn't a leftover placeholder (e.g. `{{candidate_first_name}}` actually resolving, not a typo like `{{cadidate_first_name}}`).
- **Fallback behavior**: what renders if a field is blank — e.g. no interviewer assigned yet, or no video link generated. Blank tokens or literal "undefined"/"null" text going out to candidates is the single most common thing that slips through on templates like this.
- **Timezone handling**: interview time should either show a timezone explicitly or be rendered in the candidate's local timezone — ambiguous times are a classic no-show cause.
- **Links**: calendar/ICS attachment or "Add to calendar" link, video meeting link, reschedule/cancel link — all need to resolve to real, non-placeholder URLs, not staging/test URLs.
- **Subject line**: clear and specific enough that it doesn't get lost or filtered as spam (avoid ALL CAPS, excessive punctuation, spammy phrasing).
- **Sender / reply-to**: confirm it's coming from an address candidates can actually reply to if they need to reschedule, not a no-reply black hole (unless that's intentional and a reschedule link is provided instead).
- **Branding/formatting**: logo, colors, footer consistent with your other candidate-facing templates; check mobile rendering since a large share of candidates open on phone.
- **Compliance footer**: unsubscribe/preferences link and any required company address, if your org's other templates include one — for consistency and deliverability.
- **Copy/tone/grammar**: read it end-to-end as if you were the candidate — is it clear when/where to show up and what to do if something changes?

**3. Check what triggers it**
- Look at `searchAutomationTriggers` for whatever trigger is wired to this template (e.g. "on interview scheduled") to confirm it fires at the right stage, only once per interview (not once per reschedule causing duplicate emails), and isn't scoped to the wrong pipeline/stage.

**4. Test send**
- Before flipping it live, I'd run `testEmailTemplate` to send a live-rendered test to your own inbox (or a real sample candidate record) so you can see actual field values in place of placeholders, check spam-folder placement, and view it on both desktop and mobile mail clients.

If you want, paste me the template's subject line and body text (or reconnect the HireData tools) and I'll go through it against this checklist and flag anything that looks off before you turn it on.
