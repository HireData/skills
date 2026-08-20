# Number hygiene

Every figure in a results readout will be checked by someone who wants it to be wrong. Check it
first.

## Re-derive before you print

For each number you intend to publish, reconstruct it from its components and confirm it agrees.
Where a surface shows both a total and its parts, add the parts up. Where it shows a percentage,
divide the two numbers it claims to relate.

Common failures, all observed in real reporting surfaces:

- **The same metric reported two ways.** A modelled figure derived from task volume and a
  measured figure derived from logged activity, both labelled "time saved", differing several
  fold. Prefer the measured one, and if you must show both, label them `measured` and
  `modelled`.
- **A per-unit figure that does not divide.** A team total and a per-person average that
  disagree with the population size printed next to them.
- **Funnel stages with identical volumes** and 100% step conversion, or a stage total that
  exceeds the outcome count above it.
- **Percentages of a hidden subset.** Shares that sum to 100% across a slice representing a
  small fraction of the population, presented under a heading that says "all". Always state the
  base.
- **Two denominators in one card.** A headline pool of one size and impact figures computed from
  a different, smaller pool.
- **A ratio label that does not match its own arithmetic.** Divide the two numbers on screen and
  see whether you get the printed percentage.
- **Placeholder values leaking.** The same estimate appearing on several unrelated
  recommendations is a default, not an estimate.

## Diagnose, do not just exclude

A number that fails its own arithmetic tells you something is wrong upstream, and the cause usually
decides how to report it. Before dropping a figure, work out which of these it is, naming the query
that settles each:

| Symptom | Likely causes | What settles it |
|---|---|---|
| Attributed outcomes truncate earlier than go-live | retention limit on the tier; outcome write-back connected late; trigger rebuilt so outcomes attach to the current version only; backfill never run | first sync date and backfill state of the data source; trigger created and last-modified timestamps; whether replies exist in the unmeasured period |
| Totals disagree with the sum of their parts | test sends and internal addresses counted; deduplication differs between views; one view is all-time and the other is windowed | recount per component with the same filter and window; check whether one figure is a stock and the other a flow |
| A rate moves without the underlying work changing | the reachable pool shrinks as it is worked; seasonality; a population change under the denominator | the denominator population at the start of each period, not just the end |

The recoverable cases are worth the extra hour. A backfill that was never run turns a caveated
partial figure into the real full-period number, which is a better outcome than any amount of
careful labelling.

## Modelled projections

If the workspace has an observed rate for something, never publish a modelled assumption about
the same thing. An observed reply rate sitting two clicks from a projection that assumes a
higher one is an argument the customer will win, and it costs you the credibility of every
figure around it.

Prefer expected-replies over expected-outcomes when the outcome projection depends on a
conversion assumption you cannot evidence. Where you keep a projection, show it as a range and
name the assumption's source.

## Report hygiene

- After the summary or cover, no statistic should appear twice in the written body. Assert this
  programmatically over the extracted text rather than by eye.
- Captions on appendices and screenshots carry no figures. A number in a caption is a number
  nobody checked.
- Round consistently and use thousands separators everywhere, including in generated summary
  prose.
- Never state a headcount of recruiters or users unless one authoritative source exists. Seats,
  active users, ranked users and synced users are four different populations and they will
  disagree.

## The rejected-numbers note

Keep a running list of every figure you excluded, with the arithmetic that excluded it. Deliver
it to the product owner as a separate artefact, not inside the customer report.

Each entry should carry: where the figure appears, what it claims, the re-derivation that
contradicts it, and the consequence if a customer had seen it. Rank by how badly it would land
in front of a paying customer, not by how hard it is to fix.

This note is not a complaint. It is the highest-signal product feedback the reporting surface
will ever get, because it comes from someone who tried to stake a customer relationship on the
numbers.
