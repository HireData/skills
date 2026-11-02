# Comparison-gate evidence: attribution at the end of agent comments

Records the `evals/RUBRIC.md` comparison gate for the change that moves the agent attribution line from the top
of a comment to the end, like a commit message trailer.

## Why the change was needed

Agents opened every comment with the attribution, so readers saw who wrote it before what it said. Attribution
belongs after the content.

## Method

- **Arms:** **prev** is the skill on `main`; **cand** is the proposed version. Each ran in a fresh `claude -p`
  context with its own skill copy and no tools connected.
- **Case:** `linear-issue-update-numbering`, with updated expectations: end with a plain attribution line, and do
  not open with it.
- **Review:** one fresh blind context with the rubric, the case expectations, and the two outputs as A and B.
  Map in `blinding-map.txt`.
- **Redaction:** the requester's name in the attribution lines is replaced with `[requester]`.

## Scores (0 to 2 per dimension, 12 max)

| Eval case | Previous | Candidate | Critical failures |
|---|---:|---:|---|
| `linear-issue-update-numbering` | 7 | 11 | Previous: opens the comment with the attribution. Candidate: none. |
