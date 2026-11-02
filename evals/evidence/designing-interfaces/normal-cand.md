The light theme was inverted, not designed as a dark theme, and that causes most of the problems. Keep your purple. Give every color role its own dark value, show elevation with lighter surfaces instead of shadows, and use purple only on things people can click or that are selected or current. Concrete values are below. I measured every contrast ratio; none of them are eyeballed.

**Read of the brief**: This is a redesign of the dark theme only. I assume it is a product UI (tool or app) and not a showcase page. I also assume the purple #6C2BD9 is your brand color and must stay recognizable.

**Top problems** (ranked)
1. **The primary buttons don't stand out from the background.** #6C2BD9 on #000000 is only 2.99:1, which is below the 3:1 minimum for UI shapes. The button edge disappears, mostly for people with low vision or on dim screens. (P7, P20)
2. **Pure white on pure black causes halation.** At 21:1, text looks fuzzy and glows, and long reading is tiring. (P20)
3. **Every section header is purple.** On dark surfaces, color looks louder. Headers that share the button color make it hard to tell what is clickable, because the color no longer means "interactive". (P7, P3)
4. **The card shadows do nothing.** You can't see a dark shadow on black, so the cards look flat. They also don't separate from the page. (P20)

**Redesign**

- **Background and surfaces** (elevation comes from lightness, not shadows)
  - `#000000` → `--bg: #121116` (OKLCH 0.18 0.01 294) — this near-black has a hint of your purple's hue, so it stays on-brand without looking tinted. (P19)
  - Cards: shadow → `--surface-1: #1E1D25` (OKLCH 0.235 0.015 291) plus a 1px border `--border: #2E2C38` — the lighter surface shows that the card sits above the page. The border keeps cards apart where they touch.
  - Popovers, menus and modals → `--surface-2: #26242E` (OKLCH 0.27 0.02 294) — each higher layer is a little lighter. Remove `box-shadow` from cards in dark mode. You can keep one soft, large shadow on modals only.
  - Borders that must be visible (inputs, checkboxes) → `--border-strong: #6B6878` (3.47:1 on bg, 3.08:1 on surface-1). Inputs need 3:1. Decorative dividers don't, so they use `#2E2C38`.

- **Text**
  - `#FFFFFF` → `--text: #ECEAF2` (15.8:1 on bg, 14.0:1 on surface-1) — this is still far above AAA (7:1), with no halation.
  - Secondary text → `--text-muted: #A6A3B0` (7.6:1 on bg, 6.2:1 on surface-2) — it passes AA on every surface.
  - Don't go below `#8E8B98` for any text that people must read. It is 4.58:1 on surface-2, which is the AA limit.

- **Primary button** (keep the brand fill and fix the edge)
  - `#6C2BD9` fill with no edge → keep the `#6C2BD9` fill and white label (7.0:1). Add a 1px inner ring in `--primary-ring: #A793F4`. You keep the exact brand purple and the label stays very legible. The ring gives the button an edge that you can see on the dark page (7.3:1).
  - Hover → `#7746E0` (OKLCH 0.54 0.22 292) — lightness goes up and chroma goes down from 0.239. White label still 5.6:1.
  - Focus ring → 2px `#A793F4` with a 2px `--bg` offset.

- **Purple as accent** (links, selection, current item)
  - Use `--accent: #A793F4` (OKLCH 0.72 0.139 292) for links, active tab and nav indicators, toggles that are on, and focus. It is 7.3:1 on bg and 6.5:1 on surface-1.
  - I checked it against the brand: lightness goes up (0.49 → 0.72), chroma goes down (0.239 → 0.139), and the hue is the same (292). This is the correct way to make a brand color lighter in dark mode. Don't use a "brighter" purple from a stock palette. Those are usually more saturated, and they glare.
  - Selected row or chip background → `--accent-subtle: #2F2452` with `--text` (11.8:1) or `--accent` text (5.4:1).

- **Section headers**
  - Purple text → `--text` (#ECEAF2) in a heavier weight or larger size. Make them different from body text through size and weight, not color. (P7)
  - If you want the brand on headers, add a small marker: a 3px × 16px bar or a dot in `--accent` before the title. Don't color the text.

**Token sheet**

```css
:root[data-theme="dark"] {
  --bg: #121116;
  --surface-1: #1E1D25;
  --surface-2: #26242E;
  --border: #2E2C38;
  --border-strong: #6B6878;
  --text: #ECEAF2;
  --text-muted: #A6A3B0;
  --primary: #6C2BD9;
  --primary-hover: #7746E0;
  --primary-ring: #A793F4;
  --on-primary: #FFFFFF;
  --accent: #A793F4;
  --accent-subtle: #2F2452;
  --shadow-card: none;
}
```

Define these as role tokens next to the light values, and switch them with `prefers-color-scheme`. Every role must have its own dark value. Don't derive the dark values from the light ones with a filter or an inversion.

**Kept on purpose**
- The exact brand purple stays the fill of the main call to action. Your brand color is still the color of the most important action. (P19)
- Your layout, components and type scale don't change. Only the color roles and elevation change.

**Trade-offs**
- **Brand fill with a ring, or a light purple fill with a dark label** (`#A793F4` fill with a `#121116` label, 7.3:1). The light fill is a little calmer, and Material-style dark themes use it. But it changes how your main button looks. I'd ship the brand fill with a ring, because it keeps the purple people know, and both options pass.
- **Semantic colors** (success, warning, error): your current values were not in the message, so I couldn't check them. Apply the same rule to them: raise lightness, keep or lower chroma, and check 4.5:1 for text or 3:1 for icons on `--bg` and `--surface-1`. Always pair them with an icon or label.
