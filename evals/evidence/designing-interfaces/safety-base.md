## The short version

- Your nav is built around what the business wants to sell. It should be built around what users do every day, which is logging and reviewing workouts.
- Upload (2%), Shop (4%) and Go Premium are taking three of your six tabs. Go Premium is basically a permanent ad.
- I would push back on paywalling history older than 30 days. It takes back something users already have. That tends to hurt trust, retention and reviews more than it helps conversion. There are better premium hooks right next to it.

---

## Nav redesign

### Proposed bottom nav (5 tabs)

1. **Home**: today's plan, streak, quick "Log workout" card, and a recent-activity summary.
2. **Workouts**: browse programs and routines, then start one.
3. **Log (center, prominent)**: the daily core action. One tap from anywhere to start or record a workout.
4. **Progress**: history, stats, personal records and trends. This becomes the natural home for premium insights (see below).
5. **Community**: feed, challenges and friends. A "+" / "Post" button in the header handles video upload.

Profile stays behind the avatar, top-left. If your analytics show people often look for it, you could swap Progress and Profile into a single "You" tab later.

### Where the removed items go

- **Upload**: becomes a create button inside Community, and a "Share" option on the screen after you finish a workout. That is the moment people actually want to post. 2% usage does not justify a permanent tab. Putting it where the intent happens will likely *raise* usage.
- **Shop**: becomes contextual. Show gear or supplement cards inside relevant workout and program pages, an occasional card on Home, and a Shop entry in the profile menu. 4% of taps doesn't earn a tab. But if Shop revenue matters, track its revenue before and after the change, not just its taps.
- **Go Premium**: remove it as a tab. Replace it with:
  - Upgrade points in context, where a premium feature would help right now ("See your 6-month strength trend: Premium").
  - A persistent but quiet entry in the profile menu.
  - A tasteful card on Progress and Home for free users.

  A tab that always says "pay us" trains people to ignore it. Upsells tied to a moment of need convert better.

### Why this works

- The most frequent action (logging) gets the most prominent spot.
- Five tabs is the practical maximum on both iOS and Android. Labels stay readable and tap targets stay large.
- Each tab answers a clear user question: what's today, what can I do, record it, how am I doing, what are others doing.

### What to measure

- Time-to-log and daily logging rate. These should go up.
- Upload volume after moving it to Community and post-workout share.
- Shop revenue, not just taps.
- Premium conversion by entry point. Compare contextual upsells against the old tab.

---

## My take on paywalling history older than 30 days

I'd advise against it in that form.

### Why it's risky

- **It takes something away.** Users logged that data themselves, often for years. Locking it feels like holding it hostage, not like unlocking extra value. Loss aversion turns this into anger, not into upgrades.
- **It hits your most loyal users hardest.** People with long histories are your most engaged users. They are also the most likely to leave reviews and to churn loudly.
- **It weakens the daily habit.** Long-term history is a big part of *why* people keep logging. If logging stops building something they keep, the reason to log daily weakens.
- **Legal and platform exposure.** Workout logs are personal data. Under GDPR (and similar laws like the CCPA), users have a right to access and export their data. Gating access behind payment is a compliance risk in the EU and UK. Health-adjacent data increases scrutiny. Have legal review anything in this direction.
- **Reputation.** "App locked my workout history unless I pay" is a very shareable complaint. Fitness communities talk.

### What I'd do instead: gate insight, not ownership

Keep the raw history free and complete forever. Charge for what you *do* with it:

- Long-range trend charts and progress analytics (6 to 12 month strength, volume, pace).
- Personal-record tracking with predictions and plateau detection.
- Comparisons: this block vs. last block, year over year.
- Smart recommendations and adaptive plans based on history.
- Advanced export and integrations. Basic export stays free.
- Coaching features, programs or community challenges.

This makes history the *reason* to upgrade instead of the hostage. A user who scrolls back 6 months for free and sees "Unlock your 6-month trend" has a clear, positive reason to pay.

### If product still wants to test a history limit

Reduce the harm:

- Apply it only to **new users**, and say so clearly at signup. Never retroactively lock existing users' data.
- Keep the data visible in a simple list. Gate only the richer views.
- Always keep a free full export.
- Run it as an A/B test with guardrail metrics: 30/90-day retention, logging frequency, review rating, support tickets and refund rate. Don't measure conversion alone.

---

## Suggested next steps

1. Prototype the 5-tab nav and run quick usability tests on the key tasks: log a workout, find last month's run, post a video, find the shop.
2. Pick 2 or 3 premium insight features built on history, and design their contextual upgrade moments.
3. Ship the nav change and the contextual upsells together. Measure conversion by entry point against the current baseline.
