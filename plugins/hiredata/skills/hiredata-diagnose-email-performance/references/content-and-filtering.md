# Content and filtering

How to tell a content problem from a placement problem, and what to inspect once you suspect
content. Source: Lettermint's deliverability knowledge base
(<https://lettermint.co/knowledge-base/deliverability>) plus HireData casework.

---

## The content problem hides in the envelope

"Content problem" almost never means the body is bad. It usually means the *envelope* — subject
line, sender, preview text — has stopped earning the open, while the body is fine for whoever
gets that far.

This matters because the two have opposite fixes and opposite evidence:

| | Body problem | Envelope problem |
|---|---|---|
| Open rate | Normal | Falling |
| Click-to-open | Falling | Flat or rising |
| Unsubscribes / complaints | Rising | Flat |
| Fix | Rewrite the offer | Rewrite subjects, preview text, targeting |

## The click-to-open test

**Click-to-open (clicks ÷ opens) is the clean measure of content relevance**, because it is
computed only over people who actually received and opened the mail. It is unaffected by
placement.

Compute it on **human opens** — machine and MPP opens have no click behind them and will crush
the ratio in a way that varies with Apple's share rather than with the content.

- **Click-to-open falling** → the offer or the body is losing relevance. A real content problem.
- **Click-to-open flat or rising while open rate falls** → the body is fine and possibly
  improving. What has failed is getting opened: envelope, targeting, or placement. Look at the
  subject lines and the audience, not the copy.

Read it alongside unsubscribe and complaint rates. Genuine fatigue produces *rising*
unsubscribes and complaints. If those are flat while opens fall, people are not annoyed — they
are not seeing it.

## Read the actual email

Do not diagnose content from behavioural metrics alone. Fetch the template with
`searchEmailTemplates (operation: show)` and read it. Large templates exceed the response limit
and are written to a file — query that file with `python3` or `jq` rather than giving up.

What to extract and judge:

- **The subject line**, and whether it is unique. Compare across segments in the same week and
  across weeks. Identical subjects across every branch or segment, repeated weekly, is a pattern
  both the provider and the recipient learn to skip.
- **The first ~150 words.** This is what the provider shows as preview text. If it is boilerplate
  that never changes, the most compelling thing in the email is invisible in the inbox.
- **Text-to-image ratio.** Count image blocks and URLs against visible copy characters.
  Image-heavy mail draws more filtering and renders as near-blank with images off.
- **Whether a plain-text alternative exists.** HTML-only mail is distrusted; multipart is
  expected.
- **Targeting.** Does every recipient in a segment get identical content regardless of their
  profile? That is usually the largest available lift and the hardest to fix by copywriting.

## Spam-score contributors

Lettermint's named triggers, worth checking against a real template:

- `SUBJ_ALL_CAPS` — all-capital subject lines.
- Urgency and hype phrasing — FREE, CLICK HERE, LAST CHANCE, "don't miss out", multiple
  exclamation marks. Emoji-heavy subjects compound it.
- `FROM_DN_EQ_ADDR` — display name identical to the email address.
- `R_SUSPICIOUS_URL`, `RSPAMD_URIBL` — flagged or blacklisted links. URL shorteners and Google
  Forms links are common offenders; use direct domain links.
- `MSBL_EBL`, `RBL_SPAMHAUS_DROP`, `DBL_PHISH` — sender domain on a blocklist or with phishing
  history.
- `MIME_BAD_EXTENSION` — dangerous attachments.
- Verification codes in subject lines.

Lettermint's own **Policy Rejected** status means their scanner blocked a send before it left,
because the spam score was too high. It is not a provider verdict, but it is a strong signal
about the same content.

## Structural causes of spam placement

Lettermint's eight causes, condensed, with the diagnostic for each:

1. **Authentication missing or wrong** — SPF, DKIM, DMARC absent or typo'd. Check DNS.
2. **Poor domain reputation** — complaint rate above 0.3%, bounce above 2%. Recovery takes weeks
   to months. Separate bulk from transactional by subdomain.
3. **New domain with no history** — start small, grow gradually, build engagement first.
4. **Spam-triggering content** — see above. Filters tighten during holiday periods.
5. **High complaints and hard bounces** — suppress bounced addresses; keep the unsubscribe link
   prominent.
6. **Poor structure** — HTML-only, broken markup, bad text-to-image ratio, newsletter-style
   formatting on transactional mail.
7. **Low engagement** — remove inactive contacts; smaller engaged lists beat large inactive ones.
8. **Poor IP reputation** — recycled or shared-with-abusers IPs; check blocklists.

## List quality

Bot signups and purchased or harvested lists poison a domain: recipients who never subscribed
report the mail as spam, and every complaint counts against reputation for *all* mail including
transactional. If a customer has open web forms feeding their candidate list, check for signup
spikes paired with rising complaints, and recommend CAPTCHA, honeypot fields and IP reputation
checks on the form.

Hard bounces must be suppressed permanently — never resend. Dead mailboxes accumulating in a
list is itself a reputation signal, and a large `Mailbox Unavailable` count at one provider is a
list-hygiene finding rather than a filtering one.

## Delivery statuses

Distinguish carefully; they mean different things and imply different actions:

- **Delivered** — accepted by the recipient's mail server. Says nothing about inbox versus spam
  folder placement.
- **Hard bounce** — permanent. Suppress, never retry.
- **Delayed / soft bounce** — temporary: full mailbox, server offline, greylisting, oversized
  message. Retried automatically.
- **Suppressed** — deliberately not sent because the address is on the exclusion list after
  bounces, an unsubscribe or a complaint.
- **Spam complaint** — the recipient previously reported mail as spam. Remove, and treat a rising
  trend as a content signal.

**Greylisting** is a temporary rejection used to filter bots; legitimate senders retry and get
through. It explains delayed arrival, not failure — do not report it as a defect.

## Writing the content recommendation

Rank by expected lift, and be concrete enough to act on this week:

1. **Put the substance in the subject line** — the actual role, place, price, whatever the
   product is. Unique per segment, unique per send. This usually fixes repetition, urgency
   phrasing and emoji in one move.
2. **Move substance above the boilerplate**, or cut the intro, so preview text shows the offer.
3. **Segment by engagement** — and explain that this is not only about the segment, because the
   unengaged tail suppresses delivery for everyone else.
4. **Clean dead addresses.**
5. **Rebalance text and images**, and confirm the plain-text alternative renders.
6. **Target the content itself** — the structural fix, and the one worth a product conversation.

Quote the customer's own good content back to them when it is good. A recommendation that opens
by acknowledging four well-written vacancies lands very differently from one that starts with
what is wrong — and if click-to-open is rising, the good content is a fact, not a courtesy.
