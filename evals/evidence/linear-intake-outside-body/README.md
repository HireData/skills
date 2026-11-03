# Comparison-gate evidence: intake details outside the issue body

Records the `evals/RUBRIC.md` comparison gate for the change that rewrites the intake template. The template no
longer asks for Summary, Evidence and links, Triage questions, and Metadata sections in the body. It sends those
details to issue properties, comment threads, Resources, and the customer request.

## Why the change was needed

New Triage bugs written with the skill carried a Metadata section, a Triage questions section, and tables of IDs
in the body. The intake template still prescribed those sections after the formatting rewrite.

## Method

- **Arms:** **prev** is the skill on `main`; **cand** is the proposed version. Each ran in a fresh `claude -p`
  context with its own skill copy, renamed so that no user-level copy could shadow it, and no tools connected.
- **Case:** `linear-issue-intake-outside-body`.
- **Review:** one fresh blind context with the rubric, the case expectations, and the two outputs as A and B.
  Map in `blinding-map.txt`.
- **Redaction:** the requester's email in the attribution line is replaced with `[requester]`.

## Scores (0 to 2 per dimension, 12 max)

| Eval case | Previous | Candidate | Critical failures |
|---|---:|---:|---|
| `linear-issue-intake-outside-body` | 7 | 9 | Previous: Metadata and Triage questions sections in the body. Candidate: none. |
