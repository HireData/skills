Here's the draft. I haven't created anything in Linear.

---

**Title:** Messaging: Send One WhatsApp Template to a Whole Talent Pool

**Body:**

Customers ask to send one WhatsApp template to every candidate in a talent pool in a single action. Today this works by sending to candidates one at a time in a loop, which times out after about 200 candidates. Larger pools can't be reached in one go.

## Current behaviour

- **Sending to a pool:** the template is sent by looping over the pool's candidates one by one.
- **Timeout:** the loop times out after about 200 candidates.
  - It is not known whether the candidates after that point get no message, or whether some get it twice when the send is retried.

## Expected behaviour

A user can send one WhatsApp template to a whole talent pool, or to a chosen list of candidates, and every eligible candidate receives it once, whatever the pool size.

## Acceptance criteria

- [ ] **A pool larger than 200 candidates is sent to in full** without timing out.
- [ ] **Each eligible candidate receives the message exactly once**, including when part of the send fails or is retried.
- [ ] **The sender can see the result:** how many messages were sent, how many failed, and how many candidates were skipped as ineligible.

> 💡 **Scope note:** the reporter suggested a bulk endpoint that takes a list of candidate IDs. That is one possible solution. It is recorded here as a suggestion for engineering to assess, not as the agreed scope.

## Triage questions

- **Where does the loop run?** Is it a customer integration calling our API, a HireData automation, or an action in the HireData app? The answer decides who hits the timeout and where the fix belongs.
- **What happens after the timeout?** Do the remaining candidates get nothing, and does a retry send duplicates?
- **Which customers are asking, and how big are their pools?** We need the customer requests linked and the typical and largest pool sizes.
- **Meta limits:** how do WhatsApp messaging tier limits and rate limits apply to a send of this size?
- **Eligibility:** which candidates should be skipped, for example those without opt-in, without a valid number, or already messaged?
- **Duplicates:** is there an existing issue for bulk WhatsApp sending or for this timeout?

## Evidence and links

- Source: colleague report in team chat. A link still needs adding.
- No customer requests, run links or example pools are attached yet.

---

**Proposed metadata (none of it checked against live Linear):**

| Field | Proposal |
|---|---|
| Status | Triage |
| Priority | Not set. Leave it for Triage to decide with the prioritisation matrix. The case for it is that this is customer-requested, there's a hard ceiling of about 200 candidates, and the only known workaround is splitting pools by hand. That points to Medium, or High if Triage counts it as a workflow being materially impaired. |
| Project | Messaging |
| Label | Feature, or Improvement if bulk sending already exists in some form |
| Assignee / Cycle | Empty |
| Customer | Link the customers who asked, plus the original Intercom/Discord threads |
| Relations | None yet. Search for duplicates first. |

**Notes on the draft:**

- **Request, not spec:** I wrote this as a customer request, not a spec for the bulk endpoint. The colleague's endpoint idea is a sensible guess, but who runs the loop and what happens at the timeout are still unknown. Both could change the solution.
- **Readiness:** the issue is ready for Triage. It isn't ready for refinement until the first two questions are answered.
- **Not checked:** with no Linear access in this session, I couldn't search for duplicates, check project or label names, or link customers. Those are listed above for whoever files it.
