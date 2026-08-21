I don't want to fire this off to actual candidates, even framed as "just a test" — a few reasons why, then a safer way to get what you actually need.

**Why not send it live to real candidates:**
- An offer-letter email is one of the highest-stakes messages this platform sends. If it lands in a real candidate's inbox, there's no way to "unsend" it — they may reasonably believe they've received (or been re-sent) an actual offer, which can cause real confusion, raise legal/compliance questions, or damage trust if it turns out to be a test.
- "A few candidates" implies picking from live candidate records. Even if the content is a placeholder or draft, using real people's records for a rendering check isn't the right use of their data.
- Sending any message on your behalf is something I only do with your explicit go-ahead in chat, and only when the recipients and content are something you've deliberately chosen — not as a byproduct of a visual QA check.

**What I'd do instead:**
The platform has a dedicated test-send path for exactly this — checking how a template renders without touching real candidates. I'd call:

- **Tool:** `testEmailTemplate` (email templates connector)
- **Operation:** send a test/preview copy of the offer-letter template
- **Recipient:** your own address (<redacted-user-address>) or another internal test address you specify — not any candidate record
- **What I'd check in the result:** confirmation the test send succeeded, which template/version it used, and any merge-field warnings (e.g., placeholders like `{{candidate_name}}` or `{{offer_details}}` that didn't resolve so you can see if they'd break on a live send)

That gives you the exact live rendering — subject line, formatting, merge fields, links — without any candidate ever seeing it.

A couple of things I need from you before I do that:
1. Which offer-letter template (name or ID) do you want tested — is there more than one active version?
2. Confirm it's fine to send the test copy to your own inbox (<redacted-user-address>), or give me another internal test address to use instead.

If after seeing the test render you decide you genuinely do want to send something to real candidates (e.g., the actual offers going out), that's a separate, deliberate send — tell me the specific template and the specific candidates, and I'll confirm the details with you before sending anything.
