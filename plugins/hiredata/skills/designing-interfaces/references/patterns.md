# Pattern library

Proven moves, grouped by area. Each says when to use it and why. Prefer the product's own existing good patterns first; reach for these next.

## Contents
- Navigation
- Menus and context menus
- Search
- Lists, collections and filters
- Entity pages (album, artist, product, profile, title)
- Home, feeds and discovery
- Settings
- Onboarding
- Media players
- Comments, chat and messaging
- Notifications and inbox
- Commerce and ordering
- Status, feedback and errors
- Mobile gestures and reach
- Customization
- Monetization
- Editing and creation tools
- Integrations
- Shipping a redesign
- Themed and concept briefs

## Navigation

- **Inventory → sections → sort → delete duplicates.** List every option from every region, define the top-level sections, sort options into them, remove duplicates and dead regions. Use for any app with sprawling navigation.
- **Bottom bar of about five core destinations** on mobile. Remove upsell, creation and rarely used tabs. Put the most frequent action (often search) in the easiest-to-reach slot. Move account to an avatar or to a profile tab.
- **Need a sixth tab? Merge two related ones** into one tab with swipeable sub-tabs (Activity + Messages = Inbox; Photos + Reels = Explore). This keeps the bar within reach and in balance.
- **Desktop: collapsible sidebar with optional compact top navigation.** Let it resize from wide (full names) to hidden (reveal on edge hover) so people can reduce density.
- **Expose menu items when space allows** (a top bar with hover dropdowns that transition smoothly) instead of hiding everything in a hamburger.
- **Tuck modes and niche tools** (big-screen mode, pro tools, upload) into a dropdown or the profile menu to prevent misclicks.
- **Tabs as the modular structure** for main sections; browser-like tabs on desktop when users juggle several views.
- **Sticky back navigation.** A back button must not scroll away.

## Menus and context menus

- **Action row + list.** The top row holds the 3–4 most frequent actions as icons (for example Save, Favorite, Add, Download). The rest are listed beneath in a fixed order, identical on every platform.
- **Merge left-click and right-click menus** that differ for no reason; keep the right-click menu where it is an established habit.
- **One menu, not a duplicate top menu** that repeats the context menu.
- **Shuffle, repeat and similar modes** go in one menu whose icon reflects the current combined state.

## Search

- **Search is reachable in one step.** The tab or icon turns into a focused field immediately (keyboard opens), but the user can still browse instead.
- **Keep search, filters and results together.** Don't split a bottom search bar from top filters and top-down results.
- **Answer on top, then category chips, then full results.** For question-like queries, show a quick answer first.
- **Group results by type, most likely intent first** (songs before albums for a music app). Feature the exact entity match (the band) with its top items.
- **Ambiguous queries:** show both interpretations, each one click from full results; never force a re-query.
- **Results are results.** Don't dilute them with recommendations after the first few.
- **Filters always visible and rich** (custom date ranges, duration, media type, exclude users, location). Usable together with a text query, not mutually exclusive. On mobile, filters come before secondary actions in the overflow menu.
- **Search in every large page** (artist, channel, playlist, server, profile, comments), with autocomplete and a clear (×) button.
- **Show matching items with key data** (dish + price + photo; item + rating), not only their containers.

## Lists, collections and filters

- **The list-tools recipe.** Search + sort + filters + view switch (list / grid / detail / timeline) + multi-select bulk actions. Apply it to every collection: history, saved, playlists, library, followers, comments, reviews, worlds, servers.
- **Filter sidebar.** Label it "Filter", trim the text, add a reset, show counts, and hide options that would return zero results.
- **Stable lists.** Items don't jump between categories or reorder under the user (download managers). Completed items stay until cleared.
- **Collapsed by default instead of infinite.** Album groups collapse and the user expands the one they want; use pagination instead of an endless "load more" for reviews.
- **Per-row actions** (play, edit, delete, download, favorite) on the right of each row, with inline progress.
- **Pins, recents and "continue where you left off"** at the top of libraries and home screens.
- **Collections / smart lists.** User-defined groups (channels by topic) or saved filters that update themselves (dynamic playlists).
- **Content-type shapes.** Make albums, playlists, podcasts and books distinguishable by tile shape or detail even without cover art.

## Entity pages (album, artist, product, profile, title)

- **Header formula.** Artwork-derived color, key metadata at the top (date, duration, contributors, total length, counts), primary actions (play/shuffle, save, buy) grouped together, and in-page search/sort/filter. Reuse the same formula across all entity types.
- **Tabs for depth** (Main, Albums, About; Posts, Media; Store, Community). The main tab shows a curated summary with "see all".
- **Personalize the entry.** "Songs you listen to most" next to "popular"; play starts with the user's favorites.
- **Sticky table of contents** for long info pages; sub-sections (photos, cast, reviews, trivia) open as full-screen modals with their own links instead of page reloads.
- **Photos: grid first**, then click into a smooth gallery.
- **Related content at the end**, like "related articles" on a blog, not in the middle of the main content.
- **Explicit state lists.** Want / doing / done (watchlist, watching, watched). The button reflects the current state, which also gives profiles meaning.
- **Where-to-get table** (stream / rent / buy with prices) across all providers, not just the owner's.
- **Explain editions** (what premium includes) and surface add-ons (DLC) at the top.

## Home, feeds and discovery

- **Home is personal; discovery is separate.** Move previews, trending clips and algorithmic experiments into a Discover or Explore surface.
- **User-editable feed tags.** The system proposes tags; the user filters by them, adds their own, mutes topics and excludes content types (for example no short videos). Inline cards ("based on recent watching") let them confirm or reject an interest.
- **Rows the user controls.** Pin, move or hide rows, add a row from the library, toggle dynamic rows. Rows scroll horizontally in place rather than opening a separate page.
- **"In case you missed it" sections** for creators' recent posts or videos.
- **"You're all caught up"** at the end of the followed feed, with a button to Explore.
- **Pull to refresh** for fresh recommendations; feeds should never just stop.
- **Category rows on one Explore page** with "view all", which gives smaller categories visibility.
- **An infinite discovery feed** instead of click-next-per-item queues for casual browsing.
- **Show, don't link.** Put real content on the home page instead of buttons that send people elsewhere.

## Settings

- **One page per category, basics first, advanced lower down in the same place.** Avoid separate "simple / all" modes.
- **Categories by the user's mental model** (General, Interface, Privacy, Controls, Playback, Video, Audio, Subtitles, Library, Network, Performance), about 10. No category holds a single setting, and nothing repeats.
- **Each setting next to its input; details behind an info icon**, not long hover tooltips or paragraphs.
- **Toggles, not checkboxes, for on/off.** Human-word dropdowns, not numeric levels. Sliders for continuous values, with live preview.
- **Privacy settings in account settings**, and also surfaced at the moment they matter (when joining a server).
- **Presets** for combinations (per-show subtitle settings, equalizer presets with preview icons for casual users).
- **Settings persist** across items, episodes and sessions.
- **Visible settings entry.** One obvious place, not duplicated across menus.

## Onboarding

- Short: ask 2–3 real preferences (theme with a live preview, layout options such as tab position), then leave the user alone.
- Ask questions a new user can answer (moods and styles, not "pick 5 of these 14 unnamed artists"), and land them on the personalized result.
- Teach interactively and gradually (sections appear as introduced); briefly introduce key shortcuts.
- Offer customization in onboarding instead of forcing everyone through it.
- Never set defaults or pin the app stealthily during install.
- **Setup wizards:** open on the essential choice (the path most users take), keep alternatives such as templates as a tab that remembers the last one used, offer "Done" right after the essentials, and merge optional steps onto one page. Don't open with questions users can't answer yet (title, metadata); insert editable placeholders into the result instead.
- **Existing users after a big redesign:** offer a "Classic" layout or style at first launch, alongside the new default.
- Announce new features in-product; don't silently ship them.

## Media players

- **Control bar.** Primary control slightly larger, previous/next beside it. Fullscreen, settings, subtitles and audio at the bottom right where users expect them. A thick seek bar at the bottom edge with thumbnail preview. Only show controls that matter in that context; for example, no "watch later" in fullscreen.
- **Expose what users monitor** (quality, subtitles, audio track) directly; merge extras into one overlay button.
- **Hover-reveal top and bottom bars** in fullscreen, so the title is visible without exiting.
- **Side panel instead of dialog** for effects, subtitle sync (a timeline you drag, sliders instead of typed values), bookmarks and the library, so the video stays visible.
- **Library beside the content.** A compact sidebar next to the video; "never have to leave the video".
- **Now Playing on mobile.** Lyrics and queue toggles reachable at the bottom; remove controls that duplicate system UI (volume); a mode menu reflects the current shuffle/repeat state.
- **Mini player.** Progress indicator, no redundant buttons (if swipe skips, drop the skip icon), and a generous close target; the mini player is also how people dismiss.
- **Continue prompts** appear near the playback controls with enough time to respond.
- **Dynamic color** from the artwork for bars and glows, graying out on pause.

## Comments, chat and messaging

- **Threaded replies** with clear parent/child relation and easy expand/collapse; sort (top, newest, most replied, timestamped) and search across all replies.
- **Show the creator's reply directly** under the comment instead of a badge.
- **Comment preview as one non-interactive box** that opens the full section, so tap zones don't overlap.
- **Dense chat.** Drop avatars, color usernames, give the name and message clear contrast, and make mentions distinct. Chat takes the full side panel, with tabs for related views.
- **One gesture mapping everywhere** (for example, swipe left = reply for every message). Destructive or mode-changing gestures (edit) live in the context menu.
- **Timestamps visible without gestures**; tap your own reaction to remove it.
- **One media button** (gallery + camera) instead of near-duplicates; a compact popup for emoji, stickers and GIFs.
- **Remove link previews before sending**; double-click or double-tap to reply.

## Notifications and inbox

- An "All" tab with filters (likes, follows, mentions) instead of tabs that reflect old business priorities.
- Notification choices are explicit: all / chosen types / none, not a vague "personalized".
- The inbox holds only what the user follows, collapsed with counts, not logs from every server.
- Icons per activity type so the list is scannable without reading.
- Numbers instead of unexplained dots for new content.

## Commerce and ordering

- Deep-link from a matched item straight to it inside the menu or store; keep the scroll position after adding.
- A full-page menu or catalog instead of a long horizontal category scroller.
- Reviews as their own section, sortable, with photos and the ordered item linked.
- A scannable added-state marker (a colored line on added items, a basket preview in the menu).
- Real-life options: "add another with different options", a rule for out-of-stock items, presets for notes, multiple carts, the price including fees before checkout, nutrition info, bilingual names.
- Customizable items go to a builder with pictures and clear steps instead of a quick-add plus button.
- A cart upsell offers related add-ons, not random specials.
- Show the discount end date and full sort options; show the current market price next to the user's own listings, and allow editing a price in place.

## Status, feedback and errors

- **Graded states.** Red = none, yellow = some, plus details on hover (which ingredient or step is missing).
- **Small persistent indicators** (time, coordinates, timers, active effects), each configurable on or off, rather than debug screens.
- **Exact numbers** (makes 16, not a picture of 4).
- **Undo buffers** (trash keeps the last item) for destructive actions; hold-to-confirm only for irreversible ones.
- **Feedback states the cause** ("Subtitles off (V)").
- **Loading.** Show progress, count up, accelerate to 100%, never stall at 99%; target under 3 seconds.
- **Reading progress** for long content; a skip button for long intro animations.
- **Don't signal with color alone**; pair it with a symbol or text, and keep status indicators from competing with the content being judged.

## Mobile gestures and reach

- Frequent actions in the bottom half; reachable menus put profile, switch account and settings at the bottom.
- Long-press for 2–3 quick actions (like, add to playlist, hide) without opening a full screen.
- Swipe between sibling tabs; use the platform's own gesture vocabulary.
- Keep hit zones separate (caption vs comments vs more; scrubber vs tabs).
- Never make a hidden gesture the only way to do something primary.

## Customization

- Full color picker over a few swatches; keep app colors in themed icon packs (recognition depends on color).
- Branded vs default toggle when a brand style is polarizing.
- User-chosen navigation items, for everyone rather than only paying users.
- Drag-and-drop layout editing on one canvas, with saved layouts per profile.
- Light/dark plus an accent color as basic, free settings.

## Monetization

- **Show good faith first.** Fix the free experience before selling anything.
- **Free stays free.** Basics, accessibility (font size, dark theme) and anything that used to be free stay free.
- **Paid = additive.** Themes and self-expression, power tools (notes, maps, assistants), richer views, profile perks (profiles double as ads for the paid tier).
- **Free fallback.** Free users get a simpler working version (a list instead of a mind map), never a dead end.
- **Choice of payment.** Watch an ad *or* subscribe; don't charge twice.
- **Paying users get less clutter.** Remove upsell space for them.
- **Fair prices** anchored to market norms.

## Editing and creation tools

- **Handles instead of modes.** Make objects look manipulable (drag handles to move, trim, stretch) so users act on them directly instead of switching tools.
- **Context-inferred tools.** Switch behavior from context: a pen appears when zoomed in near editable data, selection is always available. A "multi-tool" that already works is proof the modes aren't needed.
- **Temporary modes.** When a mode is conventional and frequent (a split or cut tool), give it a visible button plus hold-a-key-to-use, release to return.
- **Non-destructive by default.** Trims keep the hidden data and can be dragged back; effects live in a per-item stack in a side panel and can be changed or removed at any time.
- **Explicit over implicit grouping.** Let users group items deliberately (select, then Group) rather than inferring groups from overlap; provide separate, named shortcuts for related variants (ripple-delete this track vs all tracks).
- **Generated outputs stay live.** Parts, exports and derived views open and close freely and are edited in a panel with instant results on the content.
- **Configurable toolbars as a growth valve.** Let users show, hide and reorder tools, so frequent tools stay prominent and new niche tools can ship hidden by default without cluttering anyone's layout.
- **Workspaces.** Layout presets per audience (classic, modern, a future specialist workspace) inside one product, chosen at first launch and switchable later; never two parallel apps.

## Integrations

- When users must map or wire things by hand to make an integration work, fix the integration (send richer context, process ahead) so it works out of the box, and keep the old compatibility path. Prefer one general mechanism over per-partner special cases.

## Shipping a redesign

For a large redesign of a product people already use:

1. **Write the end-state vision first**, then cut it into releases. Each release is a coherent, shippable step toward that vision; avoid one release that disrupts every workflow at once.
2. **Order by dependency.** Foundations come before the features that need them (the data model before the editing features; the component library and tokens before screens).
3. **Rebuild the foundation only when it blocks the design** (every change breaks something else, the UI framework can't do what's needed), and only with experienced people.
4. **Make sure updates reach users** before investing in step-by-step improvements: a one-step download and an in-app update check.
5. **Explain changes in the product and in public**, especially removals and replacements; users don't read release notes. Offer a classic option where it's cheap.
6. **Replace obsolete help with the release:** an updated manual, separate tutorials for existing and new users, and an entry point to them inside the app.
7. **Work in public where possible.** Early designs shared with the community catch details and soften surprises; a visual design can't be argued into being good, so show it rather than explain the concept.

## Themed and concept briefs

For playful, speculative or "make it look like X" briefs:

1. **Turn the brief into 3–4 requirements or one mental model** before drawing (time as a stream; music as listen-and-feel; "fast, easy, relevant, sorted").
2. **Make the metaphor do real work.** Map every control and data point onto it: the record's position is the progress, the tonearm is pause, zippers are a progress bar, months become envelopes. Decoration-only metaphors fail.
3. **Never lose a function** while restyling; if the concept drops one, re-add it in the concept's terms.
4. **Define the visual language first** (buttons, color, icons, font, corners), drawn from the product's world, and push it to every detail (cursors, window hints).
5. **Pull back from realism** when it hurts readability, scale or speed; a stylized middle ground (cartoony rather than photoreal) usually reads better.
6. **Add subtle imperfection and consistent lighting** so stylized UI doesn't look synthetic. Light direction can encode inset (input) vs raised (button).
7. **Check for prior art** and differentiate on capability, not looks.
8. **Build from what already exists** (the platform's own features and precedents) so the concept is plausible.
