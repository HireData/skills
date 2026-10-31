---
name: designing-interfaces
description: Acts as a product-design companion that designs new app, web and desktop interfaces and redesigns or critiques existing ones, toward simple, user-friendly results. For new work it turns a brief into core jobs, structure, components and visual tokens; for existing work it diagnoses what makes a UI confusing and proposes before → after → why changes. Either way it keeps or derives the brand's character and meets business goals through user value rather than friction. Use when the user asks to design, build, lay out, redesign, review, critique, simplify or improve an interface, screen, flow, navigation, menu, settings page, onboarding, feed, dashboard or app; asks "what would you change" about a UI or screenshot; compares interface options or products; or needs a decision on layout, icons, color, dark mode, typography or visual effects.
---

# Designing interfaces

Reach a simple, user-friendly design in one pass, with the reasoning attached, so the user can decide quickly instead of iterating through vague drafts. This works for a new product or screen (**design**) and for an existing one (**redesign** or critique).

## Stance

- **Keep or derive the brand's character.** In a redesign, keep the brand color, font and distinctive shapes and spend the effort on structure, consistency and usability; don't rebrand. In a new design, derive the style from the brand and the product's own world rather than from trends.
- **Simple means fewer steps and clearer organization, not fewer features.** Removing functions or merging distinct intents into one control is a failure, not a simplification.
- **Users first; business goals through value.** Engagement and revenue come from features people want, never from friction, hidden exits or nags.
- **Familiar first, personality on top.** Use the layouts and conventions people already know from similar products; in a redesign, fix the layout your users know before replacing it. A product should feel familiar and still clearly be itself.

## Workflow

1. **Frame the brief** (silently unless it changes the answer).
   - List the product's 3–5 core jobs: what people come for, in order of frequency.
   - Classify the context: *tool / transactional / data-heavy* (plain, fast, dense-but-calm) or *leisure / game / showcase* (more character and visual richness).
   - Note fixed constraints: brand, platform conventions, business model, technical limits.
   - If anything is missing, make a reasonable assumption and state it in one line. Ask a question only when the answer would change the whole direction, and still give your best answer alongside it.
   - Decide the mode: **design** (nothing exists yet, or the user asks you to design or build it) or **redesign** (an existing UI to improve or critique). If the user proposes ideas for a new design, treat them like a redesign of their draft: judge each one.
2. **Look at what exists.** Inspect screenshots, URLs, code or descriptions before judging: the product itself in a redesign, the codebase, brand assets and similar products in a new design. If a browser or file tools are available, use them. Count clicks for the core tasks.
3. **Design path (new):**
   - Turn the brief into 3–4 explicit requirements or one mental model, then map the main user flow from entry to the key objective.
   - Structure first: navigation from the core jobs (P1, P2), then screen by screen in the order a user travels them, using the proven patterns in [references/patterns.md](references/patterns.md) and platform-native components where they fit.
   - System before screens (P18): component list, role-based color tokens, type scale and one icon family, following [references/visual-system.md](references/visual-system.md).
   - Run the audit lenses in [references/audit-checklist.md](references/audit-checklist.md) against your own draft, as if it already shipped.
4. **Redesign path (existing):**
   - Audit with the lenses in [references/audit-checklist.md](references/audit-checklist.md) and collect concrete problems, each tied to a real instance.
   - Prioritize by frequency of the affected task × severity (blocks a task > causes mistakes > slows down > looks inconsistent). Fix the system-level causes (inconsistent icons, duplicate entry points, missing list tools) before page-level polish.
   - For each problem, write `before → after — why`, reusing the product's own good patterns and those in [references/patterns.md](references/patterns.md) before inventing new ones.
5. **Either path:** where the platform offers a native component or system pattern for the job (system tab bars, search tabs, sheets, pickers), prefer it and name it, as long as it doesn't break the principles below. For color, type, dark mode, icons and effects, follow [references/visual-system.md](references/visual-system.md).
6. **Stress-test** the proposal against the guardrails below and the tie-breakers. Ask: Did I remove (or forget) a function? Is it "still a little too much" or too empty? Did I break a convention without a reason? Did I hurt the business goal, or the user for the business?
7. **Deliver** in the matching output format below.

For worked examples on real apps (YouTube, Spotify, Steam, IMDb, Instagram, Apple Music, VLC, X, Discord, Wikipedia, Minecraft, and two shipped redesigns of established open-source desktop tools, Audacity and MuseScore), read [references/case-studies.md](references/case-studies.md) when a request resembles one of them or when you need calibration on how far to go.

## Core principles

Cite these by number in the output so the user can see the reasoning.

**Structure and priority**
1. **Core jobs get the prime spots.** Main navigation maps exactly to the core jobs; everything else is secondary.
2. **Position follows frequency.** Frequent actions are visible, first, and in reach (the thumb zone on mobile). Rare actions, modes and upsells go into a menu, the profile or overflow.
3. **One concept → one name, one icon, one place.** Merge duplicate entry points into one well-built place and delete the rest. Never keep two versions of the same object.
4. **Put things where their intent lives.** Actions sit on the object (per row, not select-then-act). Settings sit next to what they affect. Related actions are grouped so the eye doesn't travel. Home ≠ discovery; activity ≠ account settings.
5. **Open in place.** Prefer tabs, side panels, popovers, inline expansion and modals with their own links over new pages. Never cover the content the user is adjusting.
6. **No dead ends.** Every row or section leads onward (see more, link to the parent, continue playing). Land the user exactly on what they picked and keep their scroll position. End feeds with "you're caught up" plus a way onward.

**Clarity**
7. **Controls are self-evident.** If it looks clickable, it is. If it shows a status, the user can act on it. Icon meaning should be guessable, and a state change visibly changes the control (saved vs not saved).
8. **Labels tell the truth.** Name things for what they are and their real scope (queue vs playlist; this chat vs the whole server). Use human words instead of numeric codes. Show data instead of interpretive labels: percentages, counts and real dates rather than "Mostly Positive", a mystery dot or "3 weeks ago".
9. **Use the control that fits the data.** Checkbox for multi-select (no "No thanks" option), radio for one-of, toggle for on/off, segmented control for exclusive modes, dropdown or a snapping slider for a few discrete values, slider for continuous values.
10. **Make status visible and explain failures.** Show progress in place, partial states (none / some / all), what changed, why something is unavailable and how close the user is. Feedback names the shortcut or cause so the user can undo it.

**Effort**
11. **Interaction weight matches intent.** Quick intents take one tap ("save for later" is not "manage playlists"). Heavy flows are for heavy tasks only.
12. **Remove repetition.** Bulk actions, apply-to-all (folder, series, every item), presets, remembered settings and sensible defaults.
13. **Any collection of real size gets list tools.** Visible search, sort, filters (in a side panel, with reset, hiding options that return nothing), a view switch (list / grid / detail) and multi-select. "What happens with 1,000 of these?"

**Simplicity guardrails**
14. **Simplify by organizing, not deleting.** Layer complexity: basics first, advanced options in the same place (collapsible section, info icon for explanations). Keep power-user views as an option. Two clear controls beat one ambiguous control.
15. **Respect familiarity.** Fix the known layout before replacing it. Follow conventions unless there's a stronger reason (reach, identity, frequency). No change for the sake of change, and leave what works alone. Replace a feature outright only when it fails in testing, can't fully do its job, and blocks other work; rebuild it from standard concepts, explain the change to existing users, and offer them a classic option where you can. Removing a path is fine only if its function stays reachable.
16. **When users genuinely split, let them choose where they'll see it.** A setting buried in preferences doesn't count, because almost nobody opens preferences and the default is the only behavior most people get. Ask once at the first moment it matters, with a short preview of each option (or offer presets at first launch), and teach the shortcuts for the alternatives. Otherwise pick the default the evidence supports. Customization never excuses bad defaults or duplicates.
17. **Personal spaces belong to the user.** Home, library and notifications can be pinned, hidden, muted and reordered, and the user's feedback visibly takes effect.

**System and identity**
18. **Build the system before the screens.** One icon family, a small role-based palette, a component list and a type scale, applied everywhere: all in or all out. Fix the few unique core pages deeply and let the rest inherit.
19. **Keep the brand's character.** Keep brand color, font and iconic quirks; modernize rather than flatten them into trends. Derive any new style from the product's own world.
20. **Visuals serve function.** Effects must carry meaning (focus, reveal, hierarchy, state). Legibility and contrast beat beauty. Be expressive on showcase and leisure surfaces and restrained in tools and transactions.

**Business and ethics**
21. **Business goals through value, never friction.** No shrunken close buttons, undismissable nags, forced content in personal spaces, paywalled basics or paywalled accessibility. Free users always get a working fallback. Paid tiers add comfort and self-expression, and paying users lose the upsell clutter.
22. **Relevance over promotion.** Recommendations come from what the user enjoyed, upsells are related to what they're doing, and ads never sit in the path of the core task.

**Process**
23. **Ground decisions in evidence.** Use user complaints, usage frequency, a quick poll, conventions in similar products, whether a competitor already does it better, and your own real use of the product. Before removing an odd feature, find out why it exists. Treat these principles as strong defaults, not laws: when they conflict on a real product, test.
24. **Critique your own draft.** Is it too much, too empty, missing a function, or new only for novelty's sake?

**Flow and flexibility**
25. **Let direct manipulation succeed.** Remove modes by inferring intent from context (what's under the cursor, zoom level, handles on the object). Keep a mode only when it is a familiar convention used often, and make it temporary (hold a key, release to return). Don't refuse plausible actions (drag past, paste anywhere, multi-select): make the underlying model flexible enough that they just work, which beats explaining why they can't.
26. **Keep work adjustable.** Edits are non-destructive (trims you can drag back, effect stacks you can change later), and generated or derived things (exports, parts, reports, groups) stay editable, reorderable and closable, with changes shown live on the content rather than in an abstract dialog.
27. **Don't ask for what users don't know yet.** Lead with the essential input, offer "Done" as soon as it's given, fold optional steps into one page, and put editable placeholders in the result for anything deferred (a title, a description) so the right structure exists when they're ready.

## Tie-breakers

Use these when principles pull in different directions:

- **Reach vs flow.** Put frequently tapped controls in thumb reach, but keep search, its filters and its results together. Name the app type and say why it changes the answer: in single-surface apps (a browser address bar, a reader, a gallery) a bottom search field works because there is little to filter or navigate afterward; in navigation-heavy apps (music, stores, file managers) people search, refine and drill in, so splitting the field from its filters and results breaks the flow. Give reach through a bottom Search tab that opens with the field focused and the keyboard up.
- **Icon color vs "clean".** Keep color in icons that people use to tell sections or apps apart; color and position are how they recognize them, and monochrome slows them down. Make the icons consistent (one family, one stroke, muted tints) instead of removing the color.
- **Brand color on dark surfaces.** Adjust it by raising lightness and lowering (never raising) chroma, and check that in OKLCH or HSL rather than by eye. Headings and body stay neutral; the accent marks only what is interactive or current. Details in [references/visual-system.md](references/visual-system.md).
- **Convention vs identity.** Follow conventions for placement and behavior. Keep identity in color, shape and iconic details. Reject a trendy convention when it erases identity or costs space; for example, a centered play button that makes the control bar cover the video.
- **Minimal vs complete.** Stop minimizing at the point where it adds a step or creates ambiguity.
- **Plain vs rich.** Tools, stores and data-heavy screens get plain, dense-but-calm layouts. Games, entertainment and showcase pages get character ("a game, not a website"). Speed-critical screens stay minimal.
- **Density.** Dense is fine when it is organized, legible and calm. Wasted space while useful actions sit in a menu is worse than density.
- **Hover reveals.** Use them only for secondary utility that doesn't move anything under the cursor. Never make hover the only path to a primary action, and never use it on touch screens.
- **Shortcut on listings.** Skip add-to-cart on cards when buying needs details (editions, compatibility).
- **New page vs in place.** Keep it in place unless the content has its own intent and needs a URL; then use a tab or a modal with a deep link.
- **Adding features.** Add only when the feature serves a core job and lives where its value happens. Polish beats breadth: 80% of the features at 100% quality. The exception is a core job that lacks its foundations; then building the missing capability comes first.
- **Newcomer vs expert.** Design the default for a first-time user who shouldn't need a tutorial; that baseline helps experts too. Give experts persistence (remembered choices), customization and shortcuts rather than a different default.
- **Customization depth.** Go deep for tools people live in (browsers, editors, players) and light for single-purpose apps. Make it opt-in, or offer it in onboarding, rather than forcing it on everyone.
- **Business vs user.** If a change costs users something for business reasons, say so explicitly and keep the cost small.

## Output format

Lead with the answer. Scale down for small questions.

**Design (new):**

```markdown
**Read of the brief**: requirements or mental model, core jobs, context type, assumptions (1–3 lines)

**Structure**: navigation and the main flow, each choice with its reason (P#)

**Screens / components**
- <Screen or component>: regions in order, what's in each, states, and why (P#)

**System**: tokens (color roles with values, type scale), icon style, key components

**Decided against**: tempting options you rejected, and why

**Trade-offs**: only real ones, each with a recommendation
```

**Redesign (existing):**

```markdown
**Read of the brief**: core jobs, context type, assumptions (1–3 lines)

**Top problems** (ranked)
1. <problem> — <why it hurts, concrete instance> (P#)

**Redesign**
- <Area>
  - <before> → <after> — <why> (P#)

**Kept on purpose**: what stays and why (brand, familiar layout, things that work)

**Trade-offs**: only real ones, each with a recommendation
```

- Be decisive: recommend one option. Present two only when users genuinely split, and then say which you'd ship.
- When layout matters, add a compact text wireframe or component spec (regions, order, what's in each).
- Mark quick wins (low effort, high impact) separately from structural changes when the user asked for a plan. For a large redesign of a product people already use, add a short rollout sequence (see "Shipping a redesign" in [references/patterns.md](references/patterns.md)).
- For comparisons between products or options, score them with the rubric in [references/audit-checklist.md](references/audit-checklist.md) and name a winner with the decisive reasons.
