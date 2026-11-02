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

## Languages

Unless the user narrows scope, use English as the default and include Dutch, German, and French. Translate the meaning and next action rather than mirroring sentence structure mechanically. Across locales, keep the same facts, variable contract, CTA destination, and expectation of what happens next.

Check that each subject and preheader is written naturally for its locale, not copied from the default language. A fallback must keep the surrounding grammar valid in every language where that variable appears.

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

## Brand, forms, and actions

Confirm the active workspace before interpreting a brand error. Read available brands and the saved template's selected brand through the MCP. Confirm any connected form or URL is the intended asset and that the button label describes its real destination. Do not infer a form from a similarly named resource or promise an action the destination cannot perform.

Keep one primary action. If no action is required, do not add a decorative button. If a linked form or URL is unavailable, change the preview or mark the email incomplete rather than leaving instructions such as "click below" without a working destination.

## Email-safe layout

Use the editor's supported formatting primitives and a simple single-column flow. Prefer standard email-safe font stacks, readable body sizing, comfortable line height, left-aligned paragraphs, and consistent vertical spacing. Avoid layout that depends on custom fonts, absolute positioning, background images, or builder-only styling.

Use separate paragraph or content blocks when line separation matters; newline characters inside one block may collapse in compiled output. Check the platform's branded scaffold before adding greetings, signatures, or spacer blocks so they are not duplicated.

When the design contains repeated cards, columns, headings, or buttons, build every instance from the same email-safe table or editor-supported structure. Use the same inline font stack, text alignment, padding, card height strategy, and button dimensions. Test the longest title and body copy; a fixed height that works only for short content is not robust. Confirm that intended columns remain side by side at a wide desktop viewport and stack deliberately on narrow screens.

CSS `border-radius` alone does not guarantee rounded buttons in classic desktop Outlook. Use an editor or compiler capability that provides an Outlook VML fallback when available. If HireData's compiled output does not provide one, record that square Outlook corners remain a compiler limitation instead of claiming exact inbox parity. Do not replace editable content with custom HTML unless the user accepts the maintenance tradeoff.

## Compiled-output review

Treat the builder as an authoring view, not proof of delivery output. Re-read the saved revision and inspect the compiled or rendered subject, preheader, body, and links for every locale.

Check for:

- unresolved or silently empty variables;
- visible typos, broken words, or inconsistent factual details;
- fallback grammar and punctuation;
- duplicated greeting, signature, or spacing from the brand scaffold;
- collapsed line breaks, excessive gaps, or broken alignment;
- consistent fonts, heading sizes, card heights, button dimensions, and text alignment across repeated blocks;
- correct rendering of emoji, currency signs, accents, smart punctuation, and other special characters, with no mojibake;
- long names and URLs disrupting the mobile reading flow;
- CTA labels that no longer match their destination, and repeated CTAs that accidentally reuse the wrong URL;
- working HTTPS destinations for every CTA—not merely syntactically valid links—including their final destination when redirects can be checked, plus appropriate `mailto:` and `tel:` protocols, the current privacy URL, and the expected unsubscribe link;
- language content or links leaking from another locale.

Structural validation and a compiled browser preview do not prove Gmail or Outlook inbox rendering. If compiled output cannot be inspected with the available MCP operations, say so explicitly and do not present builder appearance as verified rendering. State which actual inbox clients were or were not tested.

## Test matrix

- all variables populated;
- optional name or company missing;
- object relationship missing;
- long vacancy or recruiter name;
- special characters and URLs;
- longest repeated-card title and body copy;
- every repeated CTA, contact, privacy, and unsubscribe destination;
- wide desktop and narrow mobile layout;
- alternate language;
- every required locale in compiled output;
- AI generation failure or unsafe source text;
- CTA destination unavailable.
