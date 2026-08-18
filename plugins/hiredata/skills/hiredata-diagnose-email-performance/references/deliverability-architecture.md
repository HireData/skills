# Deliverability architecture

How sending infrastructure and domain structure cause engagement problems, and the rules that
are not negotiable.

Sources: Lettermint's deliverability knowledge base
(<https://lettermint.co/knowledge-base/deliverability>), Microsoft and Google sender guidance, and
HireData migration casework. Escalate to your email delivery provider's deliverability team when a
diagnosis lands on infrastructure.

---

## 1. Providers do not judge you the same way

The most useful fact in deliverability diagnosis, and why a provider-by-provider breakdown must
precede any conclusion.

| Provider | Weights |
|---|---|
| **Gmail** | Domain reputation, heavily, and **adapts placement to engagement** |
| **Microsoft** | Proprietary scoring across many factors, with unusual weight on **IP reputation** and sending consistency |
| **Yahoo** | Filters aggressively at IP level |
| **Dutch ISPs** (Ziggo, KPN) | Largely static rules; do not adapt to engagement at scale |

Two consequences that decide diagnoses:

- **A content or relevance problem shows up as a single-provider decline.** Gmail's filter reacts
  to falling engagement; Ziggo and KPN do not. So flat ISP engagement alongside a Gmail collapse
  is *not* evidence that content is fine — it means those ISPs still deliver to the inbox, and
  the audience's underlying interest is unchanged. Do not read it as ruling content out.
- **A Microsoft problem is often not fixed by the same lever as a Gmail problem.** Microsoft
  reacts to sending pattern and IP consistency; Gmail reacts to domain reputation and engagement.

Always split blocks by provider *and* classification before proposing anything.

## 2. Microsoft

Symptoms: `blocked` with classification `Reputation`, concentrated at `outlook.com` and
`mx.microsoft`, often with heavy `deferred` volume (throttling). Microsoft distinguishes
temporary and permanent blocklists.

Microsoft also flags **domains** as spam-sending, not only IPs. In one HireData migration the root
domain was flagged, bulk sending was moved to a dedicated subdomain, and the team pursued delisting
each time Microsoft re-flagged the subdomain despite full compliance. That combination resolved it
over several months, reducing reputation blocks by more than three orders of magnitude. Persistence
is part of the remedy; a single delisting request is often not enough.

**Pre-emptive accommodation** is the lever, and it works even when you are not currently blocked:

1. Submit the unblock request form at `go.microsoft.com/fwlink/?LinkID=614866`.
2. Microsoft replies saying you are not blocked. Expected.
3. Reply to Hotmail Sender Support using the exact phrase **"pre-emptive accommodation"**.
4. They send a table to complete: **IP / IP ranges, 1st date, anticipated traffic (messages per
   day), 2nd date, anticipated traffic, notes**. The two dates are when you want the IP online
   and when you step up volume. They also ask for the location of your posted mail practices.
5. Expect two follow-up questions: whether you see `451 4.7.652 ... has exceeded the maximum
   number of connections (S3115)` only when sending to O365/domain accounts, and whether you use
   multiple recipients on a single email.
6. If accepted, they raise the limits for your reputation.

Join **JMRP** (Junk Email Reporting Program) and **SNDS** (Smart Network Data Services) — both
free, and the only IP-level visibility Microsoft offers. Staying inside the volume you projected
is what keeps the accommodation. It is not permission to spam; the filters stay on.

Reference: <https://www.spamresource.com/2021/05/requesting-pre-emptive-accommodation.html>

## 3. Google

Google rarely hard-blocks; it deprioritises. The symptom is a falling open rate with **no
reputation blocks at all** — only `Mailbox Unavailable` blocks, which are dead addresses.

Check the binary things before speculating:

- **Bulk sender requirements.** Above 5,000 messages/day to Gmail: SPF, DKIM, DMARC, one-click
  list-unsubscribe (RFC 8058), and spam rate below 0.3%. An incomplete DMARC record or missing
  `List-Unsubscribe-Post` header produces exactly the slow slide into Promotions that reads as
  engagement decay.
- **Google Postmaster Tools.** Free, and the only direct view of domain reputation and spam rate.
  Recommend it in essentially every Gmail diagnosis, and say plainly that everything else is
  inference until it is enabled.
- **Engagement signals.** Gmail weights them heavily. Lettermint is explicit: *"focus on smaller
  engaged lists over large inactive ones"*. A large never-opening tail suppresses placement for
  the whole domain, including for people who do want the mail.

## 4. Domain and subdomain structure

Root domains and subdomains carry **separate reputations**. That is the whole point of the
split: a newsletter performing badly from `newsletter@mail.example.com` does not damage
`info@example.com`.

- **Separate bulk from transactional.** They must not share a sending identity. A bulk reputation
  problem must never be able to take down application confirmations, interview invitations or
  contracts.
- **Prefer subdomains over separate domain names.** A subdomain keeps brand association and
  controlled reputation inheritance; a fresh unrelated domain starts from nothing and reads as
  evasion.
- Lettermint's recommended structure: `transactional.example.com`, `newsletter.example.com`,
  `alerts.example.com`, and a staging subdomain so test sends never touch production reputation.
- A subdomain that has never sent has no reputation and must be warmed like any new sender.

## 5. Shared pool versus dedicated IP

The intuition that a big customer deserves a dedicated IP is usually wrong.

**Rule of thumb: under roughly 300K emails/month, a shared pool beats a dedicated IP.** Postmark
and Lettermint both give this guidance.

- Reputation is built by *consistent* volume. One customer alone on a dedicated IP sending in
  irregular weekly bursts presents no recognisable pattern, and providers — Microsoft above all —
  block what they do not recognise.
- Modern pools are load-balanced rather than segmented by customer quality, so a large consistent
  sender in the pool lifts everyone in it. Alone on a dedicated IP you carry your own reputation
  with nothing to support it.
- Each IP has its own queue. When an IP is blocklisted for a destination, that queue is suspended
  and traffic moves to another IP — a mechanism you only benefit from with more than one IP.
- Adding a *new* IP invites immediate blocking; providers distrust an address they have never
  seen. Announce it in advance with expected volume and a warm-up plan.

Check which IP or pool a customer is on before diagnosing anything as content. A customer left
on a legacy or dedicated IP while others migrated is a structural finding.

## 6. Sender addresses

**A newsletter goes from one fixed From address.** Rotating the sender dynamically — sending each
candidate's copy from their owning recruiter — is flagged as spam behaviour, by Microsoft among
others. Do not recommend it; flag it if a customer is doing it.

HireData has hit a version of this: a data inconsistency caused candidate records to be
auto-resolved as senders, since fixed by restricting sender resolution to users only. Watch for it
when a customer reports an unexpected From name.

**The two From addresses:**

- **Header From** — what the recipient sees. Can be a person's address, provided that domain is
  authenticated with the provider (sender signatures in Postmark, domains in Lettermint, sender
  authentication in SendGrid).
- **Envelope From** — the return path, a fixed domain such as `subdomain.mail.hiredata.com`. This
  carries reputation.

A named human header From per campaign is fine and often good. Varying it per recipient within
one send is not.

Also avoid `FROM_DN_EQ_ADDR` — a display name identical to the email address is a spam-score
contributor.

## 7. Warm-up and send pacing

- New IPs, domains and subdomains must be warmed: start low, increase gradually, monitor per
  provider. Use your delivery provider's published warm-up schedule rather than inventing one.
- **Ramping from tens of thousands to hundreds of thousands per month without a warm-up plan
  reliably produces a blocklist event.** Warm-up guidance at migration is HireData's job. If it
  was not given, say so.
- **Spread large sends.** An 80K blast goes out over several hours, not one minute. Split a list
  across days or batches. Lettermint's example of a red flag: 1,000/day suddenly becoming 50,000.
- Consistency matters more than volume. A steady 100K/month is a better profile than an erratic
  40–200K. **This is why cutting frequency can make a Microsoft problem worse** — never
  recommend a volume cut without checking which provider you are treating.

## 8. Thresholds

| Metric | Limit |
|---|---|
| Spam complaint rate | < 0.3% (Lettermint), ideally < 0.02% |
| Hard bounce rate | < 2% |
| Gmail bulk-sender spam rate | < 0.3%, above 5,000/day |

## 9. When to escalate

Hand to whoever owns sending infrastructure, or your delivery provider's deliverability team, when
the diagnosis lands on:

- `Reputation` blocks concentrated at Microsoft, or a domain flagged as spam-sending.
- A customer on a dedicated IP below ~300K/month, or on a legacy pool others have left.
- Bulk and transactional sharing an IP or sending identity.
- A blocklist event following a volume ramp.
- Anything whose answer is a pool migration, an accommodation request or a warm-up schedule.

Say clearly which actions are HireData's and which are the customer's. Customers accept an
infrastructure problem far better when it comes with a named owner and a plan.
