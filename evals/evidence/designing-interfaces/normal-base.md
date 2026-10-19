Inverting a light theme almost never works. All five choices you listed are common dark-mode mistakes, and each one has a simple fix. Here is what I would change, with values you can start from.

## 1. Background: stop using pure black

`#000000` with `#FFFFFF` text has the highest contrast possible (21:1). That sounds good, but it causes "halation": white text seems to glow and smear, especially for people with astigmatism. Pure black also leaves you no darker colour to show depth.

Use a near-black instead. A slight tint of your brand purple makes it feel designed rather than defaulted:

- **Page background:** `#14121A`
- **Neutral alternative:** `#121212`, if you would rather not tint it.

## 2. Use lighter surfaces instead of shadows

On a dark background you can barely see a drop shadow, so your cards blur into the page. In dark mode you show elevation with lightness: the higher a surface sits, the lighter it is.

- **Level 0, page:** `#14121A`
- **Level 1, cards and panels:** `#1C1A23`
- **Level 2, raised cards, dropdowns and popovers:** `#25222E`
- **Level 3, modals and dialogs:** `#2E2A38`
- **Borders and dividers:** `#2E2A38`, or `rgba(255, 255, 255, 0.08)`

To make cards easy to see:

- Remove the light-mode shadow.
- Use a Level 1 background and a 1px border instead.
- If a floating element (menu, modal) still needs a shadow, make it darker and softer, for example `0 8px 24px rgba(0, 0, 0, 0.5)`.

## 3. Text: off-white in three tiers

- **Primary text:** `#ECEAF0`. This gives about 15:1 on the background. That is far above the minimum, without the glare of pure white.
- **Secondary text (labels, metadata):** `#A9A5B3`. This gives about 7.7:1.
- **Disabled and placeholder text:** `#6F6B78`. This gives about 3.6:1. Use it only for text that does not need to be read.

Use a slightly heavier font weight, or slightly larger letter spacing, for small text. Light text on dark looks thinner than dark text on light.

## 4. Primary buttons: lighten the purple

`#6C2BD9` works well as a button fill in light mode. On a near-black page, though, the button itself has only about 2.6:1 contrast with the background. That is below the 3:1 minimum for UI components, so the button looks heavy and muddy.

Use a lighter, slightly less saturated tone of the same hue, with dark text:

- **Button fill:** `#A47BF0`. This gives about 5.9:1 against the background.
- **Button text:** `#140A26`. This gives about 6:1 on the fill.
- **Hover:** `#B794F6`
- **Pressed:** `#9466E6`
- **Focus ring:** `2px solid #C4B0F7`, with a 2px offset.
- **Secondary or ghost button:** transparent fill, `#C4B0F7` text, and a `1px` border in `rgba(196, 176, 247, 0.4)`.

You could keep white text on a purple fill instead. In that case, you cannot go much lighter than about `#7C3AED` before white text drops below 4.5:1. That fill is still dim against the dark background. The light fill with dark text reads better and still looks clearly on-brand.

## 5. Section headers: stop making all of them purple

When every header is purple, the brand colour stops meaning "this is important or clickable". Saturated purple text on dark is also tiring to read.

- **Section headers:** primary text colour `#ECEAF0`. Show hierarchy with size and weight, not colour.
- **Purple is for:** primary actions, links, the active nav item, selected states and focus.
- **If you want a brand accent on headers:** add a small purple element, such as a short 3px bar or an icon. Do not colour the whole heading.
- **If you need purple text (links, for example):** use `#C4B0F7`, which gives about 8.5:1, and not `#6C2BD9`.

## 6. Other things to adjust while you are at it

- **Status colours:** lighten and desaturate them the same way:
  - **Success:** `#4ADE80`
  - **Warning:** `#FBBF24`
  - **Error:** `#F87171`
  - **Info:** `#60A5FA`
- **Status backgrounds (badges and alerts):** use the colour at about 12-16% opacity over the surface, for example `rgba(248, 113, 113, 0.14)`. Do not use solid fills.
- **Images and illustrations:** check any with white backgrounds, because they will glare. Give them a surface-coloured frame, or use dark-mode versions.
- **Input fields:** Level 1 background, the border colour above, and the `#C4B0F7` focus ring.
- **Charts:** check the series colours against the new surfaces. Many light-mode palettes become too dark.

## How to roll it out

1. Define these values as semantic tokens, such as `bg`, `surface-1`, `surface-2`, `text-primary`, `text-secondary`, `primary`, `primary-hover`, `on-primary` and `border`. Do not use raw hex values in components. Then light and dark mode are only two maps of the same names.
2. Check every text and background pair with a contrast checker. Aim for 4.5:1 for body text and 3:1 for large text and UI boundaries.
3. Test on a real phone at low brightness and on an OLED screen. Problems with pure black and too-bright purple show up most there.

These values are a starting point. Adjust the purple tint in the surfaces, and the exact button tone, until they match your brand. Keep the structure the same: tinted near-black, lighter surfaces for elevation, off-white text, a lighter brand tone, and purple only where it means something.
