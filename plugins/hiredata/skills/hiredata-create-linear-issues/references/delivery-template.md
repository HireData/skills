# Delivery issue/update template

Record delivered work in an update comment on the issue. Keep the issue body as it read before the work started,
and tick the to-dos and acceptance criteria that were verified.

## Update comment

A suggested shape, adapted to what the update needs:

```markdown
### Update 2

One or two sentences on what this update covers.

**Findings**
* What turned out different from the issue, in plain words.

**Added**
* One sentence per change.

**Fixed**
* One sentence per fix.
```

- **Numbering:** start with `### Update`, then `### Update 2` and onward. Read the existing comments for the number.
- **Categories:** pick from Findings, Added, Changed, Fixed, Removed, Known limitations, and Next steps. Use only the
  ones that hold something. Put Findings first when the result differs from the issue.
- **Proof of work:** show the result in the format that communicates best: screenshots, a short video, numbers, or a
  run that shows the change. When the material is dense, attach a Linear document and link it.
- **Leave out:** PR links, commit names, and release dates. Linear already shows them.
- **Replies:** put evidence and questions about the update in replies under it. Start a new thread for a later
  topic, such as metrics after a release.
- **New content:** add a new comment instead of editing an earlier one, so that readers see the change.
- **Attribution:** when an agent writes the update, end it with a plain line after an empty line, such as
  `Written by <agent and model> on behalf of <person>`. Do not open the comment with it.

## What to cover

- **Delivered:** the observable change and the issue it satisfies.
- **Behaviour and compatibility:** what changed, what stayed compatible, data effects, and known limitations.
- **Verification:** automated coverage, reviewed environments, and customer or account verification.
- **Follow-ups:** remaining product, UX, documentation, or cleanup work, as linked issues. Do not absorb them into
  the delivered scope or the acceptance criteria.
- **Communication:** whether release notes, customer communication, documentation, or internal enablement are
  required.
