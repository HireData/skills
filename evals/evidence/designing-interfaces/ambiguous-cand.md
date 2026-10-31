The biggest problems are moving a candidate to another stage, which is the most frequent task, and losing your place after you open a profile. Fix those first, then the filters and the stage colors. The nav is fine apart from the orange upgrade button.

**Read of the brief**: Your users are recruiters working a pipeline every day. Their core jobs, most frequent first: move candidates through stages, find a specific candidate or group, review a profile, check a job's pipeline, and pull reports. This is a data-heavy tool, so it should stay plain, dense and calm. I'm assuming you want to keep the current top nav, the table and your brand, and that the "Upgrade to Pro" button stays in some form for revenue.

**Top problems** (ranked by how often the task happens × how much it hurts)

1. **Changing a stage takes 4 clicks, through a modal.** You tick the checkbox, click Actions, click Change stage, then pick in a modal. That is a select-then-act flow for the most common action on the page (P4, P11).
2. **Opening a profile throws away your place.** The profile opens as a new page, and when you come back the scroll position and filters are gone. With 2,000 candidates, people have to rebuild the list after every profile they check (P5, P6).
3. **Filters fight you.** They sit behind "More", and the popup closes after every pick. Building a filter like "Interview + LinkedIn + Frontend job" means opening the popup three times, and you can't see which filters are on (P13, P10).
4. **The stage colors mislead.** Interview, Offer and Hired are all green, so you can't spot Hired, the outcome that matters most (P8, P18; visual system: one meaning per state color).
5. **Search looks global but only matches names.** People will type an email, phone number or job title, get no results, and conclude the candidate doesn't exist (P8).
6. **"3 weeks ago" hides the real date.** You can't tell 15 days from 27, and the relative wording doesn't sort or compare well (P8).
7. **The bright orange "Upgrade to Pro" button takes a prime nav slot.** It's the loudest thing on every screen, and nobody uses it daily, including paying customers (P2, P21).

**Redesign**

- **Stage changes**
  - Tick → Actions → Change stage → modal → **click the stage pill in the row → dropdown of stages → pick**. That's 2 clicks, with no modal and no selection step. Why: the action lives on the object (P4), and a quick intent takes a light interaction (P11).
  - Keep the checkbox + Actions → Change stage path for **bulk** moves, and show a selection bar ("12 selected · Change stage · Reject · Email") in place of the table header while rows are selected. Why: bulk still matters, it just shouldn't be the only path (P12).
  - After a change, show a toast like "Moved Sam Lee to Offer · Undo". Why: visible feedback with a way back (P10).
- **Profile**
  - New page → **a side panel that slides in from the right, over the right part of the table**. The list, scroll position and filters stay put underneath. The panel has its own URL, so you can share and bookmark it, plus "Open full page" for deep work. Why: opening in place with a deep link (P5, the "new page vs in place" tie-breaker).
  - Add **↑/↓ (or K/J) and "Next / Previous candidate"** in the panel to step through the current filtered list without closing it. Why: reviewing a list is a run of candidates, not one (P12).
  - Even when people use the full page, **keep filters, sort and search in the URL and restore the scroll position** on Back (P6).
- **Search and filters**
  - "More" popup → **an always-visible filter row above the table** with Stage, Job, Source, Owner and Last activity. Each is a multi-select dropdown that **stays open while you tick options**, shows counts, and hides options that would return 0. Active filters show as removable chips, with "Clear all" (P13, P9).
  - Search for name only → **search name, email, phone, job and tags, with the placeholder saying so** ("Search name, email, phone, job…"). Results combine with the active filters (P8, P13).
  - Add **sortable column headers** and a result count ("Showing 214 of 2,031"). Why: a collection of 2,000 needs the full list-tools set (P13).
  - Add **saved views** ("My candidates in Interview", "New this week") as tabs above the filter row. Why: recruiters run the same filters every day (P12).
- **Stage colors**
  - All green → **one color per stage group, always shown with the text label**: Applied/Screening neutral gray, Interview blue, Offer amber, **Hired green (used only for Hired)**, Rejected/Withdrawn muted red. Why: a state color has to be reserved for its state, and color is never the only signal (P8, P18).
- **Last activity**
  - "3 weeks ago" → **"28 Sep" (with the year when it's not this year) plus the activity type** ("28 Sep · Email sent"). The relative time goes in the tooltip. Why: show the data, not an interpretation (P8). The column sorts by real date.
- **Top bar**
  - Bright orange "Upgrade to Pro" next to the nav → **a quiet "Upgrade" text link next to the avatar (and in the avatar menu), hidden entirely for Pro customers**. Show Pro features **at the moment they're relevant** instead, for example a "Pro" badge on a Pro-only filter or report, with one line on what it does. Why: frequency decides position, and the upsell should be related to the task and gone for people who already pay (P2, P21, P22).

Wireframe of the Candidates page:

```
[Logo] Dashboard  Jobs  Candidates  Reports            Upgrade  (?)  (avatar)
---------------------------------------------------------------------------
Candidates                                              [+ Add candidate]
[All] [My candidates] [New this week] [+ Save view]
[Search name, email, phone, job…      ]  Stage ▾  Job ▾  Source ▾  Owner ▾  Last activity ▾
Stage: Interview ×   Source: LinkedIn ×   Clear all            Showing 214 of 2,031
---------------------------------------------------------------------------
[ ] Name ▲        Job applied        Stage            Source     Last activity
[ ] Sam Lee       Frontend Dev       [Interview ▾]    LinkedIn   28 Sep · Email sent
[ ] Ana Ruiz      Data Analyst       [Offer ▾]        Referral   2 Oct · Note added
...                                             ┌── Side panel: Sam Lee ─────┐
                                                │ ‹ Prev   Next ›   Open full│
                                                │ Stage [Interview ▾]        │
                                                │ Contact · CV · Activity    │
                                                └────────────────────────────┘
```

**Kept on purpose**

- **The top nav (Dashboard, Jobs, Candidates, Reports).** It maps to the core jobs and is familiar (P1, P15).
- **The table layout and its columns.** Recruiters scan dense lists, and this one already shows the right data (P15).
- **Checkboxes and the Actions menu**, now for bulk work only.
- **Your logo, brand color and fonts.** This is a structure fix, not a rebrand (P19).

**Trade-offs**

- **Side panel vs the full profile page.** The panel covers part of the table. I'd ship the panel as the default for clicking a name, because people mostly check and move on, and keep "Open full page" one click away. If your users mostly do long edits on the profile, swap that default.
- **The quieter upgrade button may lower clicks on it.** I'd accept that cost. The in-context Pro badges reach people at the moment the feature has value, which tends to convert better than a permanent orange button, and paying customers stop seeing a nag.

**Suggested order**: start with the quick wins, which are the stage colors, real dates, the search scope and placeholder, and the quieter upgrade button. Then do the inline stage dropdown with undo. After that, make filters persist and open profiles in the side panel. Saved views come last.
