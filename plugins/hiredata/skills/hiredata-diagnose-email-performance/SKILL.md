---
name: hiredata-diagnose-email-performance
description: Diagnose why a customer's email open rate, click rate or deliverability has fallen, and turn it into advice they can act on. Use when someone says their opens or clicks have dropped, that performance was better in their previous system, that mail is landing in spam, that a domain is blocked, blacklisted or flagged by Microsoft or Google, or when they ask what their delivery, bounce, unsubscribe or complaint rates are. Also use when a customer implies HireData made their email worse. Do not use this to diagnose a broken workflow, a failing step or a message that never sent — that is hiredata-diagnose-automations.
---

# Diagnose HireData email performance

Separate "the mail did not arrive" from "the mail arrived and nobody cared". They feel identical
to a customer and they have nothing in common.

Almost every "our open rate dropped" is one of six things, and the order you rule them out
matters:

| Cause | Signature |
|---|---|
| Sending infrastructure | `Reputation` blocks at one provider; a dedicated IP or legacy pool; bulk and transactional sharing an identity |
| Inbox placement shifted at one provider | One large provider's engagement diverges sharply while others stay flat |
| Authentication or bulk-sender compliance | Gmail decline with no reputation blocks; DMARC or one-click unsubscribe incomplete |
| Send frequency went up | Delivered ÷ distinct recipients rose, and engagement fell in step with it |
| The audience or content went stale | Decline is uniform across every provider |
| The comparison is not like-for-like | The old system counted opens differently, or transactional is being compared to bulk |

Infrastructure sits at the top because it is the most consequential, the least visible to the
customer, and frequently ours rather than theirs. Content sits near the bottom because it is the
easiest to blame and the hardest to prove.

## Workflow

1. **Read the account history first.** Check the account's known history — CRM notes, the account
   record, past support tickets — before touching the data. Prior blocklist events, domain changes,
   IP moves and expert consultations are almost never in the statistics, and diagnosing without
   them produces confident nonsense. If the history describes a past incident, the current problem
   is usually its continuation.
2. Get the claim precisely: workspace, period, what they are comparing against, and whether they
   have shared their old figures. Confirm the workspace ID — customers often have a
   `(testomgeving)` or `(to delete)` twin.
3. Read [references/email-queries.md](references/email-queries.md) for query shapes and
   constraints, then run the first pass it opens with.
4. Establish the health baseline (§ below). If delivery is healthy, say so early and plainly.
5. Strip machine opens before claiming any trend, then run both tests below.
6. Split blocks by provider *and* classification. Read
   [references/deliverability-architecture.md](references/deliverability-architecture.md) for
   the infrastructure knowledge that turns a symptom into a fix, and
   [references/content-and-filtering.md](references/content-and-filtering.md) for the content
   side — including how to read a template and what to check in it.
7. Open at least one real template before saying anything about content, in either direction.
8. Write advice in effect order, separating what HireData will do from what the customer must do.

## Check the baseline is real

Before comparing any two periods, verify the earlier one is a period rather than an artefact.

Look at the first month day by day. A customer who migrated recently may have a first month that
is one blast to a fresh list — the most flattering data point that can exist, and not comparable
to anything. In one migration case, 94% of the apparent baseline month came from a single send on
the second day of sending.

Rule: if the earlier period contains a first-ever send, a fresh list, or a fraction of the later
volume, it is not a baseline. Say so and compare from the first steady month instead.

## The two tests that decide the diagnosis

Run both before attributing a decline to anything. Either one alone will mislead you.

### Test 1 — human-only open rate per provider per month

- **Decline concentrated at one provider, others flat** → placement. But **do not read this as
  ruling out content.** Gmail adapts placement to engagement; Ziggo, KPN and most static ISPs do
  not. So a content-driven decline surfaces as a *Gmail-only* decline, and flat ISP lines only
  tell you the audience's underlying interest is unchanged.
- **Decline uniform across every provider** → audience or content reaching everyone. Frequency
  and fatigue become live hypotheses.
- **Microsoft falling with `Reputation` blocks** → sending pattern, IP consistency, or a
  domain flagged as spam-sending. Architecture reference, not content advice.
- **Google falling with zero reputation blocks** → placement. Check bulk-sender compliance before
  speculating, and say plainly that placement is not observable.

### Test 2 — click-to-open on human opens

Clicks ÷ human opens is computed only over people who received *and* opened, so it is unaffected
by placement. It separates the body from the envelope:

- **Falling** → genuine content or offer decay. Read it with unsubscribes and complaints, which
  rise together in real fatigue.
- **Flat or rising while the open rate falls** → the body works and may be improving. What failed
  is getting opened: subject lines, preview text, targeting. Do not tell the customer their
  content is stale when this ratio is climbing.

Content and placement are usually not competing explanations. A repetitive envelope depresses
engagement; Gmail responds by deprioritising; the decline then looks provider-specific. Content
is the cause and placement is the mechanism. Say so, rather than picking one.

### Test 3 — a control customer, when "it's just the market" is raised

Customers and colleagues will propose that inboxes got noisier and nobody reads mail any more.
It is testable: run the same per-provider human open rate for another customer on the same
platform over the same months. Flat or rising engagement there means the decline is
customer-specific, not market-wide.

Match the comparison to the claim. A customer sending transactional automations only rules out
"the platform's mail is treated differently"; ruling out "bulk recruitment mail got noisier for
everyone" needs a comparator sending bulk at similar scale. State which of the two you actually
tested, and never present the weaker one as the stronger.

Then read [references/content-and-filtering.md](references/content-and-filtering.md) and **open
the actual template**. Behavioural metrics tell you *where* the problem is; only reading the
email tells you *what* it is.

## Health baseline

| Metric | Healthy | Source |
|---|---|---|
| Delivery rate | > 95% | `delivered` ÷ `processed` |
| Spam complaint rate | < 0.1%, ideally < 0.02% | `spamreport` ÷ `delivered` |
| Hard bounce rate | < 2% | `bounce` ÷ `delivered` |
| Unsubscribe rate | < 0.5% | `unsubscribe` ÷ `delivered` |

If all four pass, HireData's sending is not defective — state that with the numbers before
moving to harder news. Customers arrive suspecting the platform, and evidence removes that
faster than assurance.

If the complaint rate approaches 0.1%, treat it as urgent: that is the level at which providers
bulk-folder an entire domain, and on shared infrastructure it affects other customers.

## Machine opens are not people

Apple Mail Privacy Protection and similar proxies pre-fetch tracking pixels. `is_machine_open`
and `is_mpp_open` exist for this.

Always report both the headline open rate and the human-only rate. A rising MPP share can hold
the headline flat while human engagement collapses underneath. And providers differ enormously
in MPP exposure — Apple/iCloud rates are structurally inflated and are never a fair comparator.
Benchmark against low-MPP providers.

## Comparisons that are not comparisons

Two traps that produce confidently wrong reports.

**Transactional versus bulk.** One-to-one mail a candidate is expecting opens at 60–90%; a list
newsletter opens at 10–20%. That gap is inherent to the product and says nothing about
placement, content or infrastructure. Do not present it as evidence — and never let it become
the recommendation "send your newsletter from your recruiters", which is itself flagged as spam
behaviour. See the architecture reference, §6.

**Their old system versus ours.** Ask how it calculated open rate. Many older systems count bot
and prefetch opens, and some divide by sent rather than delivered. Both inflate the old number,
and this is a common, entirely innocent source of a decline that never happened. Until you know,
say the comparison is unverified.

## Frequency

Compute delivered ÷ distinct recipients per month and put it beside the open-rate series. It is
a genuine and common cause — but only when the decline is uniform across providers, and only
when the trend actually rises. If frequency fell while engagement fell, it is ruled out.

Where frequency is the cause, the template library usually shows it: hundreds of near-identical
templates on a weekly cadence, the same subject-line formula repeated across every branch or
segment. Count templates, group by name prefix, count subject repetition.

One caution: reducing frequency can make a Microsoft IP problem *worse*, because Microsoft
rewards consistency of pattern. Never recommend a volume cut without checking which provider you
are treating.

## Advice, in effect order

Order by expected impact and separate ownership. A customer accepts an infrastructure problem
far better when it comes with a named owner and a plan.

**HireData's side** — pool or dedicated-IP review, Microsoft pre-emptive accommodation, send
pacing, completing bulk/transactional separation. See the architecture reference.

**The customer's side** — authentication and bulk-sender compliance, Google Postmaster Tools,
suppressing or re-permissioning non-openers, segment hygiene, relevance.

Give the advice free before proposing paid help. A customer who asked whether we broke something
and receives an invoice will conclude that we did. Offer a paid engagement as a next step.

## Guardrails

- **Own what is ours.** Missing warm-up guidance at migration, a customer left on a legacy IP, a
  remedy we recommended that did not work — say so explicitly. It costs far less than having
  them discover it.
- **Never promise a spam-placement percentage.** No platform can see inbox versus spam
  placement; providers report acceptance at the SMTP handshake and nothing after. `spamreport`
  counts only people who clicked "report spam" — a floor, not a rate. Say this plainly when
  asked, because a vague answer invites the customer to believe a vendor who claims otherwise.
- **Do not invent a cause for a placement decline.** Name the plausible drivers, say which are
  testable, and recommend Postmaster Tools. Inference presented as measurement will be
  contradicted later.
- Do not diagnose from a blended average. Segments with structurally different engagement —
  different countries, consumer versus business, cold versus warm — need separating first.
- Do not present a benchmark as a target. It depends on their list and their offer.
- A low click rate with a healthy open rate is a content and offer question, not a
  deliverability one.
- Anonymise recipient addresses in anything shared, and never carry one workspace's figures into
  another's diagnosis.
- If the diagnosis turns out to be a broken workflow rather than an engagement problem, hand off
  to `hiredata-diagnose-automations`.

## This produces a draft, not a decision

The output is material for a human to judge, not a reply to send. Whoever owns the account knows
things the data does not, and this analysis can be confidently wrong when it lacks that context
— it has been, more than once, on exactly this kind of question.

So: hand over the reasoning and the evidence, flag explicitly what is inferred rather than
measured, and let the account owner decide. When drafting customer text, write it in their
language and in a voice the sender would actually use — a reply that reads as machine-generated
undermines the credibility of the analysis behind it.
