# Intake issue template

Use the sections that hold something for this report. Leave out the rest, and fit the shape to the kind of issue
described in `SKILL.md`. The title is the heading, so start the body with a paragraph.

## Opening paragraph

State the reported problem or request, who it affects, and why it matters, in two or three sentences. Do not put a
"Summary" heading above it.

## Current behaviour

Describe what happens now. Leave this out for a new feature.

## Expected behaviour

Describe the observable outcome the reporter expects. Do not invent the implementation.

## Steps to reproduce

For bugs, include the environment, the account or object, exact steps, the actual result, frequency, and the
last-known-good state when available. Leave this out when the problem is obvious without steps.

## What goes outside the body

Linear has a place for most intake details. Put them there instead of in a body section.

- **Evidence:** attach screenshots, recordings, run links, and source conversations as Resources or inline images.
  Keep a short pointer in the body only when a reader needs it to understand the problem.
- **Open questions:** ask each missing fact, suspected duplicate, or scope question in its own comment thread, so it
  can be answered and resolved. Remove questions from the body before the issue moves to Ready to Plan.
- **Metadata:** set the status, priority, project, label, assignee, cycle, and relations as issue properties. Leave
  unsupported fields unset. Explain a priority choice in a comment when the reason is not obvious.
- **Customer:** link the customer request, and put the customer's own words and any deadline there.
- **Identifiers:** keep long IDs, such as run or record IDs, in a comment or a Linear document for developers.
  A body that lists many IDs is hard for the rest of the team to read.
