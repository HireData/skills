**Short answer:** Logging gets the tab bar. Upload, Shop and Go Premium leave it but stay easy to find. Workout history stays free. Sell premium as extra insight on top of that history, not as a fee to get it back.

**Read of the brief**: This is a tool-type app used daily, so it should feel plain, fast and encouraging. Core jobs by how often people do them: (1) log today's workout, (2) find or follow a workout, (3) see progress and history, (4) community. Assumptions: logging today takes a few taps from Home or Workouts, and history sits somewhere under Profile. Shop revenue matters but isn't the core business.

**Top problems** (ranked)
1. **The most frequent job has no tab.** Nearly everyone logs daily, but logging competes for space with features 2–4% of people use (P1, P2).
2. **Two of six tabs are business slots, not destinations.** Shop and Go Premium take prime thumb-zone space. Upload sits in the bar for about 2% of users, which also invites mis-taps. Six tabs is also more than the comfortable maximum of about five (P2, P21).
3. **Progress and history are buried.** Seeing your streak and improvement is the main reason people keep logging. Right now it lives behind a top-left avatar, the hardest spot to reach one-handed (P1, P2).
4. **Upload is cut off from where posts appear.** Posting is a Community action, but it sits in its own tab (P4).

**Redesign**
- **Bottom bar**
  - Home · Workouts · Upload · Community · Shop · Go Premium → **Today · Workouts · Log (+) · Progress · Community** — five tabs, each mapped to a core job (P1). Log sits in the center slot, the easiest one to reach, because it's the daily action (P2).
- **Log (+)**
  - Logging spread across screens → **one bottom sheet** that opens over the current screen (P5, P11). It opens with smart defaults: today's planned workout, otherwise "Repeat last workout", otherwise a search. You can save in one tap with a "Done" button, and add details later (P12, P27).
- **Today (was Home)**
  - A general home screen → **a personal screen**. It shows the planned or suggested workout with Start and Log, your streak and this week's summary, then friends' recent activity with a link to Community (P4, P6).
- **Progress (new tab, history moves here)**
  - History behind the avatar → **its own tab**. It shows your streak, personal records and a full history list. The list gets search, filters by type, sort and a calendar/list switch, because daily loggers end up with hundreds of entries (P13).
- **Upload**
  - A tab of its own → **a "+ Post" button in the Community header**. You can also share straight from a finished log ("Share this workout") (P4). Same function, out of the prime slot (P15).
- **Shop**
  - A tab → **a "Shop" row in the profile menu**, plus **"Gear used in this workout"** on the workout pages where it's relevant (P22). That moves Shop from random taps to purchase intent, which usually sells better per visit.
- **Go Premium**
  - A permanent tab → **a "Premium" row in the profile menu**, plus a small "Premium" tag on locked features where people run into them (P21, P22). Paying users see none of this.
- **Profile and settings**
  - Avatar at the top left → **keep it**, because people already know it (P15). Make the menu order: account, Premium, Shop, settings, help.

```
┌───────────────────────────────┐
│ (avatar)   Today       (bell) │
│ Today's workout  [Start][Log] │
│ Streak 12 days · This week 4/5│
│ Friends' activity  → see all  │
├───────────────────────────────┤
│ Today Workouts (+) Progress Community │
└───────────────────────────────┘
```

**Your take on the history idea: I'd recommend against it.**
- **Locking it takes away something users already have.** Daily loggers built that history themselves, and it was free. Locking it the moment it turns 30 days old will feel like ransom, not an upgrade. That's the kind of thing that ends up in 1-star reviews and churn (P21).
- **It weakens the habit that drives conversion.** A long visible record is the reason people keep logging. A habit they can no longer see breaks more easily, and someone who has left the app won't convert.
- **It's a legal and policy risk.** In many markets users have a right to access their own personal data. A fitness log plausibly counts. Check with legal before locking it at all.

**Do this instead (same goal, through value):**
- **Free forever:** the full history list, streaks and personal records, as a simple working version (P21).
- **Premium:** what people can't easily do themselves. Long-range trend charts, comparisons ("this month vs. last year"), plateau and recovery insights, adaptive plans built from their history, and export or health-app sync with advanced metrics.
- **Upsell at moments of value, not a wall.** At a 30-day streak or a new personal record, show a preview: "Here's your 3-month trend — see the full year with Premium." On the Progress tab, show a blurred preview of the long-range chart above the free list. Never put it in place of the list (P22).
- If Product still wants a limit, put it on the **advanced views of older data**, never on the raw entries, and grandfather everything already logged.

**Kept on purpose**: the brand look, the avatar profile entry, Workouts and Community as they are, and every function. Upload, Shop and Premium are each still at most one tap from where they're used.

**Trade-offs**
- **Fewer taps on Go Premium and Shop.** Removing their tabs will cut raw taps. Measure conversion instead (premium upgrades, shop orders per visit). Run the new nav as an A/B test against the current one, with conversion and 30-day retention as the success metrics. I'd expect the contextual entries to win on conversion.
- **Upload creators lose a top-level button.** That's 2% of users. Share-from-log and the Community "+ Post" button should keep or raise posting. If posting drops, move "Post" into the Log sheet as a second option instead of bringing the tab back.
