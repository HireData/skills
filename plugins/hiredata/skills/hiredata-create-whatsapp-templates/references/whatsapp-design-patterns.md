# WhatsApp design patterns

## Write for the channel

- Identify the sender or agency when the recipient may not recognize the number.
- Explain why the message is timely in the opening sentence.
- Keep one primary purpose per template.
- Prefer short sentences and direct actions.
- Use quick replies for a small, mutually exclusive decision; use a form when more information or branching is required.
- Make every URL or button destination clear.
- Specify what happens after the recipient responds.

## Reason about category

Use current Meta policy as the source of truth. At a high level:

- Utility messages normally follow a specific user action, transaction, request, account event, or agreed service process.
- Marketing messages normally promote, recommend, reactivate, nurture, or initiate a new opportunity, even when useful to the recipient.
- Authentication is a distinct category for supported verification flows.

When uncertain, choose the more conservative category and explain why. Category selection affects approval and delivery; do not optimize it merely for lower cost or easier approval.

## Variables

Use variables only where recipient-specific data is necessary. Provide realistic examples when the review system requires them. Verify that every variable has a reliable source, sensible fallback, and no surrounding text that becomes misleading when the value is absent.

## Test matrix

- normal data;
- missing first name or job title;
- unusually long company or vacancy name;
- correct language and locale;
- each quick-reply response;
- form or URL unavailable;
- no response;
- duplicate or recently sent message;
- current category and formatting policy.
