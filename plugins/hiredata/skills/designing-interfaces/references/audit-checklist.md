# Audit checklist

Use these lenses to find problems in an existing interface, then the rubric to compare products or options. Not every lens applies to every screen; skim for the ones that do.

## Contents
- How to audit
- Lenses: structure and navigation; consistency; controls and affordances; content and truthfulness; lists and collections; flows and effort; feedback and status; personal space and control; platform and reach; visual system; business and ethics
- Severity guide
- Comparison rubric

## How to audit

1. **Inventory first.** List every navigation item, menu option and region (sidebar, top bar, bottom bar, overflow). Mark duplicates, dead regions and items in the wrong group. This often reveals the real structure problem faster than looking at screens one by one.
2. **Walk the core journeys in order**, the way a real user would: launch → find something → act on it → come back later. Fix problems as you "bump into" them.
3. **Count.** Clicks for each core task, distinct icon styles, color values, button variants, settings that appear more than once. Numbers make the case (for example, "41 colors → 12").
4. **Check edge cases.** What happens with the longest title, 1,000 items, an empty state, a first-time user, dark mode, a small phone, keyboard only?

## Lenses

### Structure and navigation
- What are the 3–5 core jobs? Does the main navigation map exactly to them?
- What should people see the moment it loads?
- Is any concept reachable from several places, such as a feed, a sidebar list and a page all for "subscriptions"? Can they become one?
- Do low-frequency or business-driven items (upload, premium, pro tools, mode switches) sit in prime slots?
- Is anything placed by tab rather than by what it relates to (account items in a messages tab)?
- Are there two design generations live at once (old and new pages, client vs web)?
- Do duplicate panels for one object fall out of sync (a change in one not reflected in the other)?
- Do users actually receive updates, or are many running years-old versions?
- Is there a catch-all "More" tab, or a category with one item? Are there too many categories, or categories you have to scroll to see?
- Does the navigation keep changing between versions? Is a primary path only reachable by a hidden gesture?

### Consistency
- Does each icon mean one thing everywhere? Is one icon used for two things, or two icons for one thing?
- Are icons from one family (all outlined or all filled, same stroke, same container size and padding)?
- Do menus have a predictable order and length? Do frequent items sit in the same place every time?
- Are fonts, sizes, paddings and corner radii consistent across pages and platforms?
- Is the brand or design language applied completely, or 20% branded and 80% default?
- Is a state color reserved for its state? If everything is green, "added" is invisible.

### Controls and affordances
- Would a user have to press something to find out what it is (a slider that looks like a divider, tags that are really results)?
- Do decorative indicators look like controls, or controls look like decoration?
- Are primary actions hover-only or hidden in a right-click menu?
- Is the control type right for the data (checkbox / radio / toggle / segmented / dropdown / slider)?
- Are hit targets big enough and separated? Does anything move or grow under the cursor or finger?
- Does a destructive action use the conventional icon and spot (trash) and offer undo or confirmation?

### Content and truthfulness
- Do labels match what the thing is and its scope ("Replies" tab that shows posts, "Theme" that only toggles dark mode, search that looks local but is global)?
- Are interpretive labels hiding data ("Very Positive", "Personalized", a blue dot, relative dates)?
- Is key info buried at the bottom or styled like body text (dates, views, duration, price, reviews)?
- Is copy in the product's voice, not leaked corporate tone ("customer")?
- Are settings explained? Are numeric levels used where words would do?

### Lists and collections
- Can you search, sort, filter, switch view, and multi-select? Can you reach the oldest item?
- Are filters visible, labeled as filters (not "Narrow by"), resettable, and free of options that return nothing?
- Does sort live under the right label (not under "Filters")?
- Is a long list paginated or collapsed sensibly, rather than an infinite expanding scroll?
- Do results show the matching item itself (dish + price + photo), not just its container (the restaurant)?

### Flows and effort
- How many steps does the common task take? Is there a prerequisite in the way (download only after adding to the library)?
- Is it select-then-act where an action could live on the row?
- Does the user have to leave or cover the content to adjust it, or bounce to another app and lose their place?
- Does the user repeat work (per episode, per item) that could apply in bulk or be remembered?
- Does a simple action open a heavy dialog?
- Does the user have to switch modes to do ordinary things? Can they get stuck in one, or fail because they're in the wrong one?
- Does the app refuse plausible actions (drag past, paste here, multi-select) instead of just making them work?
- Are edits destructive, or outputs locked once generated, so changing one step means starting over?
- Does a setup flow ask for information the user doesn't have yet, or force every optional step before "Done"?
- Do shortcuts have a visible equivalent?

### Feedback and status
- Is progress shown in place? Are loading states honest (no stall at 99%)?
- Are partial states shown (have some ingredients, not none)?
- Do one-time notifications say *what* changed?
- Does feedback name the cause or shortcut so it can be undone?
- Is status hidden in a debug screen or deep menu when it belongs in a small persistent indicator?
- Are previews live for visual settings?

### Personal space and control
- Can the user shape their home, library and notifications (pin, hide, mute, reorder, exclude a content type)?
- Does their feedback (like, dislike, "not interested") visibly change anything?
- Are recommendations based on what they enjoyed rather than on upsell or the wrong signal?
- Is owned content easy to reach, or tangled with the store?

### Platform and reach
- Are mobile and desktop structurally the same, with each platform's native style allowed?
- Is anything available on one platform but missing on the other?
- On mobile, are frequent controls within one-handed reach? Is the bottom bar limited to about five core destinations?
- Do gestures map consistently (the same swipe means the same thing everywhere) and avoid destroying work?
- Does the layout adapt to input type (touch, mouse, controller, keyboard)?

### Visual system
- How many colors, button variants and text styles exist? Can they collapse into a small role-based set?
- Is contrast measured (WCAG), not eyeballed? Is anything pure black on pure white in dark mode?
- Is there a theme "flashbang", where pages switch randomly between light and dark?
- Do components have focus states, keyboard navigation and screen-reader labels? Is there a high-contrast option?
- In dense output, do marks collide or space unevenly, implying differences that aren't there?
- Does the style fit the medium (sharp corners for blocky or pixel worlds, more character for games)?
- Do effects (blur, glass, motion, 3D) carry meaning, or are they decoration that hurts legibility or speed?
- See [visual-system.md](visual-system.md) for the rules.

### Business and ethics
- Is a business goal pursued through friction (shrunken dismiss targets, removed outbound links, forced suggestions, stealth defaults, undismissable reminders)?
- Is something basic, accessible or previously free now paywalled? Is there a free fallback?
- Are users charged twice (ads plus an ad-gated basic)?
- Do the platform owner's promotions crowd out user content?
- Could a value-based alternative reach the same goal (a "you're caught up" screen with a button to Explore instead of forced suggestions)?

## Severity guide

Rank problems by **frequency of the affected task × severity**:

| Severity | Meaning | Examples |
| --- | --- | --- |
| Blocks | User can't complete a core job, or loses work | No way to find an owned item; a gesture wipes a draft |
| Misleads | User does the wrong thing or can't tell state | Duplicate-looking icons, mislabeled tabs, an indicator that looks done but isn't |
| Slows | Extra steps, hunting, repetition | Nested menus for a frequent task, no bulk actions |
| Erodes | Inconsistency, clutter, lost trust | Mixed icon styles, nags, half-applied branding |

Fix system-level causes first: one fix (an icon family, merged entry points, a list-tools recipe applied everywhere) resolves many page-level symptoms.

## Comparison rubric

Use this when comparing products, competitors or design options. The weights reflect what most often decides the outcome.

| # | Criterion | Weight | What wins |
| --- | --- | --- | --- |
| 1 | Task efficiency | Very high | Fewest detours to the goal; lands exactly on the chosen item; keeps place |
| 2 | Self-evidence / learnability | Very high | Usable without docs or guessing; controls look like what they do |
| 3 | Consistency | High | One icon family, consistent states and colors, design language applied completely |
| 4 | Efficient density | High | Information-rich but calm; neither cramped nor wasteful |
| 5 | Customizability | High for tools people live in, low for single-purpose apps | Full pickers over presets; can remove what isn't used |
| 6 | Respect | Medium-high (heavy penalty when violated) | No nags, stealth defaults, forced AI, accounts or paywalls on basics |
| 7 | Thoughtfulness | Medium-high (strong bonus) | Anticipates real situations: ordering for two, item out of stock, bilingual labels |
| 8 | Completeness | Medium-high | Obvious companion actions exist; features are finished |
| 9 | Hierarchy and contrast | Medium | Key info (price, state, headings) stands out and is legible |
| 10 | Feedback and polish | Medium (tie-breaker) | Smooth, meaningful micro-interactions; nothing goofy or janky |
| 11 | Onboarding | Medium where relevant | Short, captures a few preferences with a live preview, then gets out of the way |
| 12 | Identity | Low-medium | Familiar layout with its own polished character; doesn't merely copy |

How to declare a winner: the one that is **familiar enough to use immediately, reaches the goal with the fewest detours, is clean but not sparse, and goes further in thoughtful features or customization**, with few consistency slips. Feature count is never penalized; disorganization is. "Generic" is not a flaw if it is clean and predictable.
