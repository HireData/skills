# Case studies

Condensed worked examples showing how the principles play out on real products. Each lists the framing, then the most instructive moves as `before → after — why`. Use them for calibration: how much to change, what to keep, and how to reason. They illustrate the reasoning; they are not specifications of the real products.

## Contents
- Full-app redesigns: YouTube, Spotify, Steam, IMDb, Instagram, Apple Music, VLC
- Partial redesigns: X (Twitter), Discord, Wikipedia (monetization), a wallpaper app
- Shipped redesigns of established tools: Audacity 4, MuseScore 4
- Systems and concepts: Minecraft (unified UI), a search-engine concept, desktop theming
- Evaluations: browsers, food delivery, design tools, a phone OS skin

---

## YouTube
**Framing:** Redesign, not rebrand (kept the red and the font). Built from collected viewer complaints. Accepted engagement goals but refused friction tactics.
- Mixed icon styles, the same icon for different things → one standard icon family — consistency is the foundation.
- Three disconnected "subscriptions" entries (feed, long sidebar list, near-empty page) → one sidebar dropdown + one useful page; the subscription feed becomes a home filter — one concept, one place.
- Unexplained blue dot → numeric new-content counts — numbers explain themselves.
- Mobile bottom bar with Upload in the center → Search in the center slot; account moved to an avatar — frequency + thumb reach; upload is rare and gets misclicked.
- Opaque algorithmic home → editable tags (filter, add, mute, exclude Shorts), suggestions the user confirms — personal space belongs to the user, and feedback is visible.
- Watch Later as a playlist popup → one-click toggle plus an end-of-video reminder to clear it — interaction weight matches intent.
- Flat comments with a "creator replied" badge → threaded replies, the creator's reply shown under the comment, sort/filter and search.
- Shrunken mini-player dismiss target → reverted — making leaving harder only annoys; the mini player is also the exit.
- Video quality buried → on the control bar; extras merged into one overlay button.
- Search diluted by recommendations, filters in a closing popup → real results; filters always visible and richer.
- Sharing to a friend without DMs → reuse mutual subscriptions + notifications — reuse existing mechanics instead of building messaging.
- **Kept:** the watch-page layout (a tested side-by-side alternative lost room for comments and was disliked; fix the familiar layout instead).

## Spotify
**Framing:** Core experience degraded by "secondary missions". Kept the rounded, fun style. Defined the core jobs first: Home, Search/Browse, Library, Profile, Now Playing.
- Premium tab permanently in the mobile bar → removed; profile and settings moved into the bottom bar — stop the constant upsell; reach.
- Search needs a sidebar click, then a field → the tab turns into a focused field — one step.
- Ungrouped browse tiles → grouped under headings (genres, moods…).
- Albums, playlists, podcasts and books look identical → subtle shape differences per content type — recognition without reading.
- Artist page with an endless discography → tabs, albums collapsed by default, grid/list views, "songs you play most" next to "popular".
- Home rows truncate into separate pages → rows scroll in place; pin/move/hide rows; preview clips moved to a separate Discover tab — home is personal.
- Like merged with add-to-playlist → split into two controls — "where minimalism stops": one ambiguous control costs steps.
- No lightweight save → a "Saved" bucket separate from favorites.
- Desktop now-playing panel that kept popping open → a full song page; the panel freed for friends/queue — a settings toggle was a band-aid for a bad default.
- AI DJ as a playlist in the library → an extension of Now Playing with skip, feedback and an off switch.

## Steam
**Framing:** A ten-year-old UI; website and client scoped, mobile and big-screen out. Kept the font, type sizes and the brand blue. Asked "what is this product?" and "what do people want when it loads?".
- Client and website as two separate designs → one design; desktop-only features hidden on the web.
- 41 color styles → 12 (2 text, 5 background, 2 brand blues, 3 accents); one component list.
- Six client regions with repeated options → audited, grouped into top-level sections, duplicates removed; the big-screen mode button tucked into a dropdown — misclick prevention.
- Categories repeated in the menu, sidebar and page → three pages: Store, Browse, Discover.
- Discovery Queue (one page per game, click next) → an infinite discovery feed.
- A hover-expanding card that moves the target button → a static card; the wishlist icon shows its state.
- "Mostly Positive" verdict labels → a percentage bar per review type — show data, let users judge.
- Filters labeled "Narrow by", with options returning zero results → "Filter", a reset, zero-result options hidden.
- Library split old vs new → combined; list/grid/detail views; the first game auto-opens; global search.
- A download manager where items jump between sections → a stable list with concurrent downloads.
- Market: listings and orders mixed, no current price → tabs, current-price and 24h-change columns, edit price in place.
- **Rejected own idea:** add-to-cart on store cards; buying a game needs details first.

## IMDb
**Framing:** Looked stuck in 2015; kept the yellow and the font. Most pages repeat a few templates: fix the unique core pages and let the rest inherit.
- Random light/dark pages → the theme follows user preference, with proper light and dark palettes.
- A niche pro tool in the main navigation → moved to the profile dropdown.
- Cards readable only by reading → preview-image backgrounds and per-movie color glow.
- "Go elsewhere" buttons → the missing content shown on the page — show, don't link.
- Recommendations based on the watchlist (unseen) → based on watched and rated titles.
- Every sub-page a full reload → a sticky table of contents; sub-pages as full-screen modals with their own links.
- An ambiguous "check-in" → Watchlist / Watching / Watched lists with a stateful button.
- No where-to-watch → a stream/rent/buy table with prices across all services, not just the owner's.

## Instagram
**Framing:** Keep the old, loved layout and add features on top. Ran a small survey before deciding ("I need numbers").
- Reels took Activity's bottom slot; Activity moved to the top → Reels out of the bar (most rarely used the tab); Activity + Messages merged as a swipeable Inbox tab — reach, no sixth tab.
- Explore with a search icon → an explore icon; Photos and Reels as swipeable tabs inside.
- Forced suggestions on home → a following-only home ending in "you're caught up" with a button to Explore — a business goal reached without hijacking the personal space.
- Overlapping tap zones (caption vs comments) → separated zones; the comment preview as one box that opens comments.
- Swipe direction depending on who sent the message → one mapping for all messages; timestamps visible.
- Camera and gallery as near-duplicate buttons → one media button.
- The oldest posts unreachable → a grid bottom sheet with sort options.

## Apple Music
**Framing:** Fix how it works, not how it looks; native styling per platform kept, structure kept identical across platforms.
- A library copy vs the catalog album (two versions of one object) → one canonical album; "Add to Library" becomes "Save".
- Menus of random order and length → an action row (Save, Favorite, Add, Download) on top and a fixed list below, the same on every platform.
- Hover-revealed favorite star; download indicators that look tappable but aren't → real buttons on each row with progress in place.
- Bottom search bar (reachability trend) with filters still at the top → search at the top with filters beneath, as a normal tab — a navigation-heavy app needs search and filters together.
- Album page with empty space while actions hide in a menu → artwork color, metadata on top, play/shuffle/save/search/filter.
- Artist page without search; a short top-songs list that stops playback → search and filters; playback continues.
- A volume slider duplicating system volume → removed; the space goes to lyrics; a mode menu shows the shuffle/repeat state.
- Mini player with a skip button despite swipe-to-skip → progress plus a useful control instead.

## VLC
**Framing:** Keep it simple and keep its identity: the cone, orange plus neutrals, rectangular shapes. "Old" isn't the problem; usability issues are.
- A centered play button (the trend) → rejected; play stays on the left, slightly bigger — centering enlarges the bar, covers video and erases identity; most people pause with the keyboard.
- Fullscreen on the left → bottom right with the settings, where people expect it.
- "Toggle playlist" that is actually a queue → a queue icon, with saved playlists separate.
- Subtitles three menus deep → a subtitle icon bottom right; an audio icon beside it with tracks and the output device.
- A thin seek bar → a thicker bar at the bottom with thumbnail preview.
- An effects dialog covering the video → a right sidebar with tabs; a subtitle timeline you drag; sliders instead of typed values.
- Re-adding subtitles per episode → apply to the file, folder or playlist; per-show presets.
- "Simple" vs "All" settings modes with repeats → one page per category, basics then advanced, info icons, word dropdowns.
- Feedback that hides its cause → an on-screen message that shows the shortcut pressed.
- **Kept:** the right-click menu (habit), the equalizer (with presets for casual users), limited customization (onboarding instead).

## X (Twitter)
- An unfinished rebrand, generic black-and-white → a refresh derived from the logo's meaning, with a restrained palette and color as user customization.
- 14 desktop nav items, customization only for paying users → user-chosen navigation items for everyone.
- Threads built for short posts → replies under each post with "continue thread", plus sorting.
- Paywalled accessibility features → free; self-expression (profile themes) can be paid.

## Discord
**Framing:** Make it less overwhelming, especially for new users, while respecting what makes it different.
- Large add/discover-server buttons above the servers people use → demoted.
- Search that looks local but is global → one unified search with filters, the chat open beside it.
- Combined vs separate direct messages split the audience → a separate tab by default, with a setting.
- Swipe-left that enters edit mode and wipes a draft → double-tap to reply; edit moved to the context menu.
- An inbox flooded with server logs → only followed threads, collapsed with counts.
- Density controls → collapsible channel list; navigation resizable to hidden; pinned conversations.

## Wikipedia (designing for revenue)
**Framing:** Deliberately optimize for business, within the organization's ethics: no ads, nothing previously free gets paywalled, show good faith first.
- Fix the free reading layout first: sticky iconized side panels, a clear namespace hierarchy, related-articles hierarchy, an ideal-width (about 80 characters) option.
- Paid = additive: font styles and themes, a topic mind map, notes and highlights, an assistant, personal translation.
- A free fallback for each (a related-pages list instead of the mind map) — never a dead end.
- Semantic search first proposed as paid → reverted to free; finding information is core.
- A pro layout that removes upsell space for paying readers.
- An honest admission: moving languages into a tools panel costs users a little, in exchange for attention on paid tools.

## A wallpaper app (day-one critique)
- Onboarding: "pick 5 of 14 unnamed artists" → pick moods and styles — ask questions a new user can answer; then land on the personalized home.
- Ads on top of an ad-gated basic download → SD free; full resolution via an ad *or* a subscription — don't charge twice.
- Tiny search, an explore icon that doesn't say search → a bigger search entry and a clearer icon.
- After download, ask lock screen / home screen / both — the obvious follow-up step.

## Audacity 4 (shipped redesign of an established audio editor)
**Framing:** A 25-year-old, widely used open-source audio editor, grown complex through layered feature requests, modernized for existing and new users alike. Research showed most use is simple editing, with sizeable podcast and production groups. The rule was not to break what people love, and the redesign shipped gradually across minor releases before one replatformed major version.
- No update awareness, a three-page download → one-step download and an in-app update check — later fixes reach most users within weeks.
- A "Time Shift" mode to move audio → draggable clip handles — the clip looks movable and is moved directly; there's no mode to enter or get stuck in.
- Six tool modes → two: the pen appears automatically at sample-level zoom, selection is always available, the envelope tool becomes a toggle, the multi-tool disappears, and a conventional split tool is added with hold-S temporary use — infer intent from context; keep a mode only when it's familiar and frequent.
- Destructive effects and trims → non-destructive trimming and real-time effect stacks in a side panel — users can experiment and change any step without undoing everything.
- "The app says no" (clips colliding like walls, paste refused, no multi-select; trim and stretch reachable only by hover and Alt) → a rebuilt clip model with free placement, multi-select, and visible trim, untrim and stretch handles.
- Four always-visible audio-device dropdowns → one button; meters and volume merged — rarely changed settings don't get prime space.
- An implicit, overloaded grouping feature (incomprehensible in testing, incomplete, a technical blocker) → explicit clip grouping plus two ripple-delete shortcuts — replaced outright from standard concepts, and explained publicly to existing users.
- One global delete behavior, with users split two to one → a one-time choice at the first delete, with animated previews and shortcuts for the alternatives — a preference nobody opens wouldn't help.
- One fixed layout → workspaces plus a three-question first launch (theme, clip style, classic vs modern) — existing users keep a familiar layout, new users get the modern one, and future audiences can get their own preset.
- **Kept:** the headphone motif in a simplified logo, envelope editing (as a toggle), a classic clip style after early feedback called the new one too alien.

## MuseScore 4 (shipped redesign of an established notation app)
**Framing:** A 15-year-old open-source notation app built from volunteer patches. The foundation and component library were rebuilt first, then the app was made easier for first-time users without discarding what worked, guided by polls, testing and the community's history of why features existed.
- Two overlapping play panels and two text panels → one of each — the duplicates fell out of sync, caused bugs, and one went unseen.
- Frequent tools missing from the main input bar → added, and the bar made user-configurable — frequency earns the prime spot, and niche tools can ship hidden by default.
- A setup wizard opening with title and metadata → it opens on choosing instruments (what most users do, per a poll), with templates as a remembered tab — the default follows the majority; the minority path stays one click away.
- Five setup steps → at most two: "Done" right after instruments, optional settings merged on one page with pop-ups.
- Skipped title fields that left users improvising plain text → editable placeholder titles inserted into the result — defer what users don't know yet without losing the right structure.
- Parts generated in a hidden dialog, then locked → a visible Parts button; parts open and close freely and are edited in a panel with instant results on the score.
- Ad-hoc colors → 12 role-based tokens with light and dark values plus an accent; high contrast, keyboard navigation and screen-reader support built into the components.
- Collisions and uneven spacing in the score → collision-free ties and beams, equal space for equal durations, optical centering — every accidental intersection is an eye snag.
- Playback that left users hand-mapping sounds through a lossy protocol → a notation-aware engine that works out of the box, keeping the old compatibility.
- **Kept:** the working input bar, panel locations, templates and metadata (demoted, not deleted). New manual and separate tutorials for existing and new users, with an in-app Learn section, because the redesign made the old help obsolete.

## Minecraft (one UI across editions)
**Framing:** One style across editions; layouts may differ by input (PC vs console vs touch). "A game, not a website."
- Inconsistent button styles → one playful, textured, 3D style everywhere; sharp corners to fit the blocky world.
- "Singleplayer / Multiplayer" (inaccurate) → Worlds / Servers / Realms.
- Select a world, then press edit → actions on each row; search, sort, tags and grid view for large lists.
- World creation for both quick and deep users → visual pickers and descriptions; four tabs, with advanced settings in collapsible sections.
- Recipe book marked red when one intermediate item is missing → red (none) / yellow (some) and a blueprint on hover; exact output counts.
- Time and coordinates only in a debug screen → a small configurable on-screen indicator.
- A slider with eight discrete options → a dropdown; previews for visual settings.
- Owned skins buried in a store maze → a simple owned library.

## Search-engine concept
- Turned a vague brief into four requirements: fast, easy, most relevant, sorted sources.
- Ambiguous query → both interpretations, each one click deep; then simplified to a quick answer plus category chips when the first draft was "still a little too much".
- Results that bounce users to the browser → results inside the panel, with a way back.
- Differentiation on capability (plugins that change ranking and add personal context) rather than looks.

## Desktop theming (two personal themes)
- Wallpaper first; derive the palette from it; one base hue with lighter and darker variants.
- Push one language to every detail: a pixel font leads to pixel icons, cursors, sharp windows and sharp window hints.
- When the system can't do an effect (progressive blur, styled panels), bake it into the wallpaper.
- Keep window controls despite the trend to remove them: function and preference beat trend.
- Noted limit: a theme can't fix UX; a long settings sidebar without hierarchy still needs a redesign.

---

## Evaluations

### Browsers (about 30)
Criteria: onboarding, intrusiveness, customization, ease of navigation, clean and clutter-free, consistency, tab management.
- Top: the one with massive customization that is still neatly categorized, a sidebar that opens anything, and no need for an overflow menu.
- Penalized: installers that stealthily set defaults; undismissable "set as default" reminders; duplicate-looking icons; one long settings page with random headings; a sidebar that opens sites full screen, breaking the expectation it creates; missing obvious buttons (no "new note" on a notes page).
- Rewarded: familiar layout with its own polished identity; features that serve real behavior (tab trails for people who lose track); onboarding that asks a few preferences with a live preview.

### Food delivery (about 20 apps, one task: find fried rice and order it)
- Winner: clean, deep-links from a dish to its place in the menu, one full-page menu, reviews with photos and ordered items, attractive but non-intrusive offers.
- Rewarded: real dishes with prices shown in search; dense-but-calm layouts; anticipating real situations (ordering for two, an out-of-stock rule, note presets, multiple carts, fee-inclusive prices, nutrition).
- Penalized: "No thanks" options in checkbox lists; scroll reset after adding; reviews buried or promised but absent; one color for everything so the added state is invisible; decorative giant cards; sticky bars that don't earn it; ads at the top of results; unnecessary AI.

### Design tools (about 20)
- Rewarded: familiar layouts; labeled values; drag-to-scrub numbers; everything for the selection in one panel; timelines that show only what's animated; local use with no forced account.
- Penalized: crowded parallel toolbars eating the canvas; basic tools that don't behave as expected; docs that mention UI that isn't there; no live preview; paywalls and AI on basics.

### A phone OS skin
- "All in or all out": a design language applied 20% over a stock OS reads as an identity crisis.
- Every change from the base must be an improvement (bigger tiles that fit fewer toggles are worse).
- A brightness slider that looks like a divider fails self-evidence.
- Monochrome icons hurt recognition; offer themed icons that keep the original colors, and a full color picker instead of a few swatches.
- Place unique features where their value happens (a rear light as a selfie countdown, not a progress bar nobody sees).
