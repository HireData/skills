# Recruitment email design patterns

## Build from context

Answer these questions before writing:

1. What just happened?
2. Why is this person receiving the email now?
3. What should they understand, decide, or do?
4. What happens after they act or do not act?
5. Which facts are reliably available from the trigger and related objects?

## Structure

Use only the sections the message needs:

- specific subject;
- contextual opening;
- concise value or explanation;
- one primary action, with secondary actions only when genuinely useful;
- expectation or next step;
- appropriate sender signature.

Avoid generic enthusiasm, vague urgency, and unnecessary repetition. Do not promise response times or outcomes the workflow cannot support.

## Variables

Prefer the closest reliable source object. Use recipient variables for the person receiving the email and subject variables for the record the email is about. Check null behavior and relationship availability.

Use a modifier when a deterministic transformation is sufficient, such as a default value, date format, capitalization, truncation, or list formatting. Confirm the modifier exists in the current HireData variable reference or MCP response.

Use an AI variable only when deterministic formatting cannot produce the desired output. Define:

- source data;
- narrow instruction;
- allowed facts;
- language and tone;
- maximum length or structure;
- fallback when source data is missing or generation fails.

Examples of bounded uses include summarizing supplied vacancy text for a candidate, adapting an approved paragraph to the recipient's language, or turning structured notes into a short introduction. Do not use AI variables for identity, eligibility, compensation, legal conclusions, or promises.

## Test matrix

- all variables populated;
- optional name or company missing;
- object relationship missing;
- long vacancy or recruiter name;
- special characters and URLs;
- alternate language;
- AI generation failure or unsafe source text;
- CTA destination unavailable.
