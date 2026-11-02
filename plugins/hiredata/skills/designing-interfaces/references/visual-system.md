# Visual system

Rules for color, dark mode, typography, layout, icons, shape, effects, motion and build quality. Use when a redesign touches the look, or when the user asks a visual question directly.

## Contents
- Color: building a palette
- Contrast
- Dark mode
- Typography and layout
- Icons
- Accessibility
- Dense visual output
- Shape and corners
- Effects playbook (blur, glass, glow, grain, shaders, 3D)
- Motion
- Trends and minimalism
- Build and handoff
- AI and templates

## Color: building a palette

1. **Start from context, not a mood board.** If the brand has a color, it becomes primary. Only rule out colors that clearly don't fit the industry or purpose; color psychology is unreliable without context.
2. **Define roles and name tokens by purpose:** background, surface, text, muted text, primary (main CTA), secondary, accent, and semantic colors (success, warning, error, disabled). Never name them by hue ("blue-500" as a role).
3. **Keep it lean.** Mostly neutrals plus one vivid primary. Distribute roughly 60% neutral, 30% secondary and 10% accent; with more colors, subdivide those shares rather than adding new ones. Example of a cleanup: 41 ad-hoc colors became 2 text, 5 background, 2 brand and 3 accent colors.
4. **Generate candidates from the primary:** monochromatic (minimal), analogous (calm), or complementary / split-complementary (most vibrant). Alternatively lock the colors you like and randomize the rest, or sample from imagery that will appear on the site.
5. **Build shade scales in OKLCH**, not HSL. HSL drifts in hue (blue tints turn purple) and its lightness isn't perceptually even across hues; OKLCH keeps steps even and on-hue and gives smoother gradients.
6. **Run the filters:** fits the industry? fits the purpose? sits well on the background in light *and* dark? too saturated (a slightly muted version usually looks better)? harmonious neighbors? enough contrast between roles?
7. **Test on a realistic UI** (dashboard, article, landing page) with real copy, on more than one device. Swatches alone lie.
8. **Fix a failing color by adjusting lightness or saturation** before abandoning the hue.
9. **Don't let the brand color sit in one loud place.** Use it with intent across the product, not as one saturated bar.
10. **Implement as variables or styles** (CSS custom properties at the root; design-tool styles or variables with light and dark modes). Ship light and dark together with `prefers-color-scheme`.

## Contrast

- Measure against WCAG, don't eyeball it. AA: 4.5:1 for body text, 3:1 for large text (about 24px, or 18.7px bold). AAA: 7:1 and 4.5:1. Icons, borders and meaningful shapes: at least 3:1 (thin ones should aim higher).
- Maximum contrast is not the goal: pure black on pure white, or the reverse, causes halation (text looks fuzzy). Use a near-black and an off-white.
- Never signal state with color alone; pair color with a symbol, label or shape.
- Beauty never excuses illegibility. For glass or translucent UI with low contrast, increase the blur or reduce the transparency.

## Dark mode

Design it as its own theme, not an inversion:

1. Re-check every role's contrast; light-mode colors often fail on dark backgrounds.
2. Fix contrast by raising lightness, or desaturating and raising lightness. Never fix it by adding saturation. **Verify it numerically**: compare the old and new color in OKLCH (or HSL). Lightness must go up and chroma (saturation) must stay the same or go down. A "brighter" neighbor from a standard palette is often *more* saturated than the brand color, so it fails this check even though it looks lighter. For a filled button that must stay vivid, keep the brand fill and give it a lighter border or ring for edge contrast, or use a lighter, less saturated tint with dark label text.
3. Mute vivid colors (slightly darker, less saturated); colors look brighter on dark backgrounds.
4. Don't use pure black backgrounds; use a dark neutral, and keep text slightly below pure white.
5. Shadows barely work on dark surfaces. Show elevation by making higher layers lighter, or with subtle borders or gradients.
6. Keep color usage minimal; the point is focus. Headings and body text use the neutral text colors; the brand or accent color is reserved for interactive elements and states (primary actions, links, selection, focus, the current item). Brand presence on headings, if wanted, is a small marker (a bar or dot), never the text color of every heading. Glow, gradients and blur are fine on landing or showcase pages, not on reading or text-heavy pages.
7. Follow the system preference by default, and never mix themes randomly across pages (no "flashbangs").

## Typography and layout

- **Body text 16–18px** on the web, small text about 14px and titles about 32px, from a type scale (a minor third, 1.2, is a good default). Pick fonts for readability first and vibe second, and test them on a real UI.
- **Inter** is a safe body font when no brand font exists. Keep the brand's font and type scale in a redesign; if a licensed font must be replaced, use the closest free alternative.
- **Headings must look different from body text**, and important metadata (date, views, price) must not look like description text. Avoid back-to-back double headings; turn one into a display element.
- **Line length about 80 characters at most**; reading containers about 700–1000px wide even on large screens. Offer width options on reading products.
- **Fixed title size**: don't let a title's size vary with its length.
- **Real copy, not lorem ipsum**, when judging a layout; check the longest real title.
- **Six checks for any screen:** visual hierarchy, contrast, balance (spacing, alignment, placement), consistency, simplicity, interaction feedback.
- **Alignment and symmetry matter.** A brand flourish (a custom font on the clock) must not break alignment.
- **One primary CTA per area**: high contrast, clear label, not surrounded by other primary-styled buttons.
- **Big display text** only for one short line (a slogan or headline); never scroll-animated text the user has to scroll through to read.

## Icons

- One family: all outlined or all filled, the same stroke weight, the same container size and padding. Standard systems (Material, SF Symbols) work when they match the platform or parent company.
- One icon per concept and one concept per icon. The icon changes when the state changes (outline → filled for saved).
- Guessable meaning; if it isn't guessable, add a label. An icon that looks like another common action (settings looking like tab search) is a bug.
- Keep color in app icons; recognition relies on color and layout, so monochrome themes slow people down. For themed packs, keep the original colors.
- Color-coding categories of icons speeds navigation (activity types, enchantments, window controls).
- A two-tier set can work: detailed or two-tone icons for non-interactive menu decoration, plain monochrome for clickable controls.
- Use icons + counts instead of verbose text for repeated actions (helpful 12, funny 3).

## Accessibility

Build it into the foundation rather than bolting it on later:
- Every component ships with focus states, keyboard navigation and screen-reader labels.
- A high-contrast theme (customizable for low vision, poor contrast perception and color blindness) comes from the same role-based tokens as light and dark, alongside an accent color. These are free settings.
- Designing once for light and dark is fine *only* when every role token has its own value per theme; that is different from inverting colors.

## Dense visual output

For screens dense with marks (charts, timelines, scores, maps, diagrams):
- Remove accidental collisions and intersections: each one creates an extra shape the eye snags on, multiplied across the whole screen.
- Space by meaning: equal things get equal space, and unrelated items never sit close enough to look grouped. Uneven spacing implies a difference that isn't there.
- Don't let the densest item dictate spacing for everything aligned with it; tuck elements into free space where possible instead of pushing everything apart.
- Keep alignment independent of content length (rows start at the same x-position whatever the label length), and keep consistent padding at edges.
- Center irregular or slanted shapes (italics, asymmetric icons) by their optical center, not their bounding box.

## Shape and corners

- Preserve the brand's shape language (rectangular players stay rectangular, just slightly softened). Corners can echo content (mini-player corners match the album art radius).
- Match the medium: sharp corners for blocky or pixel worlds; rounded and playful where the brand is.
- Apply the corner decision to every nested element (windows, hints, tooltips, cursors).

## Effects playbook

Use the simplest tool that achieves the effect: CSS first, SVG filters next, WebGL shaders last.

- **Layer blur:** ambient colored blobs or glows tucked into corners (40–100px+ on colored shapes). Don't blur content people need to read without a reason.
- **Backdrop blur / glass:** use it as a surface background (headers, panels over imagery), not as a stunt. Avoid a hard bottom edge on blurred headers; fade the blur with a gradient mask (`mask-image: linear-gradient(...)`). Add `-webkit-backdrop-filter` for Safari. Translucency is tuned, not maxed (for example 85% active, 75% inactive windows, which also signals which window is active).
- **Shadows and glows:** decide realistic or expressive. For a glowing border, blur a rectangle and clip out its middle with `clip-path: polygon()` using a `calc(100% - Npx)` inset so it adapts to any size.
- **Blur with meaning:** reveal (unblur on scroll), focus (blur everything but the cursor area), section transitions, blur-up image placeholders.
- **Grain:** an SVG `feTurbulence` filter (`type="fractalNoise"`, a higher `baseFrequency` gives finer grain) applied as a low-opacity overlay (for example a `body::before` pseudo-element) or over gradients. Avoid PNG noise. In design tools, use a noise plugin with exposure and contrast maxed and opacity lowered.
- **Image hover effects:** do zoom (`transform: scale` with a transition) and grayscale-to-color (`filter: saturate()`) in CSS; reserve shaders (Three.js plane + fragment shader) for distortion, RGB split or ripples on showcase sites, and optimize for unknown GPUs.
- **3D:** ask what it's for (usually showcasing a physical product). Pair it with simple, minimal UI and short copy. Keep it subtly alive (a slow linear idle spin, for example 360° over about 10s), and scrub scroll animations to scroll position.
- **Blend modes:** `mix-blend-mode: difference` for text that auto-inverts on hover; `luminosity` for grayscale-to-color.
- Combine effects in harmony. The hard part is coherence, not more technology.

## Motion

- Motion serves content: reveal, transition between states, show focus, confirm an action. Delight is welcome when it doesn't slow the task.
- Choose easing deliberately; use linear only for continuous ambient loops.
- Prefer user-controlled motion (scroll-scrubbed, hover that settles back when the cursor leaves).
- Reuse one motion language across related components.
- Remove animations made necessary by bad layout, and anything janky or goofy.
- Long intro animations get a skip button. Page transitions must never slow a basic task; nobody admires a transition while ordering food.

## Trends and minimalism

- Judge each trend by its UX and performance cost and by the site's purpose. Showcase, portfolio and brand landing pages can carry immersive effects; stores, reading and task UIs should not.
- **Bento grids:** people notice only 1–2 tiles; reveal tiles on scroll; build with nested flex/grid or auto layout.
- **Custom cursors:** fine when simple and used as a hover affordance on media; never confusing.
- **Scroll-driven navigation:** never as the primary navigation; scrollytelling only for short stories (people hold 5–7 chunks).
- **Minimalism** is good when it comes from doing exactly what users need. It becomes worse when it removes functions, hides important controls, turns sterile and soulless, or homogenizes everything into the same trendy look. Simple doesn't mean less attractive, and it doesn't mean fewer features.
- **Avoid the generic AI/trend look** (giant hero type, bento boxes, oceans of white space, glowing-blue futurism) unless the context calls for it. Style should fit the product: a bakery and a developer tool shouldn't look alike.

## Build and handoff

- Structure every group with auto layout, stacks or flex/grid, nested (row inside column inside screen), never loose placement. Use wrap for card collections and min/max sizes to bound flexible elements.
- Decide position and sizing as each element is created: relative widths over fixed, and the right position type (absolute for decoration or overlays, relative for flow, fixed for persistent UI, sticky for headers).
- Design responsively from the start: one responsive layout with breakpoints (for example ≥1200 / 810 / 390), relative units, and multiple image resolutions. Verify every breakpoint.
- Define styles and variables (color, type, shadow; modes for themes and localization) before building, and use components with variants and states (default, hover, pressed, expanded). Prefer in-place state changes (variants, Smart Animate, variables) over new screens.
- Name and group layers that code depends on; hand off with specs, tokens and assets.
- Draw shapes in a design tool, export SVG, and paste the path into code rather than hand-writing it. Keep textures editable (SVG over PNG).

## AI and templates

- Treat generated layouts, copy and images as starting points, never the finished design. They converge on the same trends and miss specifics.
- Add the research, context and intent: who it's for, what it must do, what makes it this product.
- Don't shoehorn AI into basic tasks (choosing dinner, a separate AI tab). AI earns its place when it is personal and context-aware (it knows the open tabs, the user's own data) and optional.
