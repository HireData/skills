# Formatting Linear text

Linear issues, comments, and documents are read by the whole team: support, sales, customer success, leadership,
developers, and AI agents. The first part of this file describes how Linear renders text. Those facts hold for every
writer. The second part recommends a style that keeps text easy to read for everyone.

## How Linear renders text

These facts were measured in the Linear web app on a wide window in November 2026. The pixel and character figures are approximate and can differ on other surfaces or window sizes; the rules about line breaks and mentions hold everywhere. Re-check the figures when Linear changes its layout.

### Line width

- **Body column:** an issue body is a 791 px column of 15 px text when the window is at least about 1600 px wide.
  A line of normal prose wraps after 103 to 113 characters, depending on the words.
- **Indents:** each bullet or checkbox level costs about 3 characters. A quote costs about 2.
- **Headings:** an H2 line holds about 83 characters and an H3 line about 92.
- **Comments:** the comment column is about 2 characters narrower than the body.
- **Visible text:** a Markdown link counts as its link text, not its URL.

### Line breaks

- **One source line per block:** write each paragraph, bullet, and checkbox on one Markdown line. Linear wraps it.
  A newline inside a paragraph shows as a forced line break.
- **Wrap jumps:** when a block runs a few words past a full line, those words sit alone on the next line. To
  predict this, count the visible characters, subtract the line width once per full line, and look at the rest.
  When fewer than about 25 characters remain, shorten the block slightly or extend it so the last line carries a
  clause. Several jumps in a row make a text look untidy.

### Mentions

A mention is a clickable chip that links to the item. An agent can write some mention types through the Linear MCP.
The others become plain links.

- **Issue key:** a bare `HD-123` becomes a chip that shows the key and the full issue title. It also adds the issue
  as a Related relation. Do not repeat the title next to it.
- **Issue link:** `[HD-123](<https://linear.app/<workspace>/issue/HD-123>)` stays a short link. It adds no relation
  and shows no title. Use it inside a sentence.
- **User:** `@displayName` becomes a user mention and notifies the person, also when it is added in an edit. Look up
  the display name; the full name does not work.
- **Date:** `<linear-date date="2026-11-14">2026-11-14</linear-date>` becomes a date chip, such as "Nov 14th".
- **Customer, project, document, and label:** only the Linear UI creates these mentions, through the `@` menu. When
  an agent writes them, Linear stores a plain link. Write a masked link to the item's Linear URL, and ask the user to
  insert the mention in the UI when it matters.
- **Existing mentions:** rewriting a whole issue body turns its customer, project, document, and label mentions into
  plain links. Change an existing body with the Linear MCP's partial-update option when it offers one, instead of
  sending the whole body again.

### Markdown

- **Supported:** headings, bold, italic, `~~strike~~`, inline code, code blocks, quotes, bullets, numbered lists,
  checkboxes, tables, horizontal rules, and emoji shortcodes such as `:rocket:`.
- **Collapsible section:** `+++ Title`, the hidden content, then `+++`.
- **Not supported:** `==highlight==`, `<u>underline</u>`, subscript, and superscript stay visible as raw characters.
- **Title:** the issue title already displays as the main heading. Start the body with a paragraph, not a heading.

## Recommended style

These recommendations make Linear text easy to read for every role. Adapt them to the issue and the reader.

- **Line length:** aim for about 110 characters per visible line, and about 5 fewer for each indent level.
- **Plain words:** use the product's own labels for screens, steps, and fields. Explain terms that a support
  colleague would not know.
- **Neutral voice:** describe the problem and the product. Keep customer-specific detail in the Linear customer
  request, and keep the customer out of the subject of body sentences.
- **Lists over comma chains:** when a sentence joins three or more facts, split them into bullets.
- **One sentence per bullet:** put a second sentence in a nested bullet. Keep nesting shallow.
- **Bold lead:** start bullets with a bold subject when they describe different things. Bold the core statement
  of each acceptance criterion.
- **Exact numbers:** write the count instead of "many" or "several".
- **Tables:** use them for short structured data, such as statuses, counts, or benchmark numbers. Use bullets when a
  cell would hold a sentence.
- **Notices:** for a scope note that every reader must see, use a quote that starts with an emoji and a bold title.
- **Code:** keep code, file paths, and class names in implementation issues or attached documents, not in issues
  that the whole team reads.
- **Linear features over text:** put related issues in relations, links in Resources, and customer context in
  customer requests instead of body sections.
