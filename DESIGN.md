---
name: PetPal
description: Everything about your pet, in one trusted place — an enamel ID-tag record you can hand over in one tap.
colors:
  paper: "#ffffff"
  ink: "#141414"
  meta: "#5c5c5c"
  surface: "#f4f4f4"
  line: "#e7e7e7"
  photo-ground: "#eaeaea"
  signal: "#ffbf00"
  signal-deep: "#e0a400"
  signal-ink: "#8a6b00"
  signal-tint: "#fdf3d3"
  success: "#0c6b3b"
  success-bg: "#e6f3ec"
  warning: "#8a5800"
  warning-bg: "#fbeed6"
  danger: "#9a2820"
  danger-bg: "#f9e7e6"
  info: "#235a73"
  info-bg: "#e5f0f4"
typography:
  display:
    fontFamily: '"Bricolage Grotesque", system-ui, sans-serif'
    fontSize: "17px"
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: "-0.01em"
  name:
    fontFamily: '"EB Garamond", Georgia, "Times New Roman", serif'
    fontSize: "36px"
    fontWeight: 700
    lineHeight: 1.06
    fontStyle: "italic"
  title:
    fontFamily: '"Bricolage Grotesque", system-ui, sans-serif'
    fontSize: "16px"
    fontWeight: 700
    lineHeight: 1.3
  body:
    fontFamily: '"Hanken Grotesk", system-ui, -apple-system, sans-serif'
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.5
  bodySmall:
    fontFamily: '"Hanken Grotesk", system-ui, -apple-system, sans-serif'
    fontSize: "13px"
    fontWeight: 400
    lineHeight: 1.45
  label:
    fontFamily: '"Hanken Grotesk", system-ui, -apple-system, sans-serif'
    fontSize: "10.5px"
    fontWeight: 500
    lineHeight: 1.2
rounded:
  pill: "999px"
  card: "16px"
  input: "12px"
  tag: "9px"
  chip: "8px"
  circle: "50%"
spacing:
  xs: "4px"
  sm: "6px"
  gutter: "10px"
  gap: "12px"
  pad: "14px"
  inset: "16px"
  lg: "24px"
components:
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    rounded: "{rounded.pill}"
    padding: "15px 20px"
    typography: "{typography.body}"
    height: "44px"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: "15px 20px"
    height: "44px"
  card:
    backgroundColor: "{colors.paper}"
    rounded: "{rounded.card}"
    padding: "14px"
    width: "340px"
  field:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.input}"
    padding: "0 14px"
    height: "46px"
  icon-tile:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.input}"
    size: "36px"
  illustration-tile:
    backgroundColor: "{colors.signal-tint}"
    textColor: "{colors.signal-ink}"
    rounded: "{rounded.card}"
    size: "120px"
  tag-uptodate:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success}"
    rounded: "{rounded.tag}"
    padding: "5px 11px"
  chip-status:
    backgroundColor: "{colors.danger-bg}"
    textColor: "{colors.danger}"
    rounded: "{rounded.chip}"
    padding: "5px 11px"
  segmented-control:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.pill}"
    height: "36px"
  switch-on:
    backgroundColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    width: "48px"
    height: "28px"
  avatar:
    backgroundColor: "{colors.photo-ground}"
    rounded: "{rounded.circle}"
    size: "88px"
  tab-bar:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.meta}"
    height: "61px"
---

# Design System: PetPal

## Overview

**Creative North Star: "The Enamel ID Tag"**

PetPal is the small metal disc on a collar, enlarged into an interface. An enamel ID tag is stamped once, worn for years, and read by a stranger in a hurry — so it is confident, findable, and utterly calm under pressure. Everything here follows from that: a white canvas that never competes, one saturated amber that behaves like transit wayfinding rather than decoration, and a photograph of the actual animal doing the emotional work the UI refuses to do itself.

The system is deliberately **not** the category's cream-and-terracotta reflex. That look was rejected by name during the concept phase, and the white base is the standing refusal. Warmth is layered on — through pet photography, the amber band, and an italic serif reserved for names — never painted across the background. Density is moderate: cards float on a soft shadow rather than being fenced by outlines, and the amber appears on roughly one element per screen.

The screens are **Operate** surfaces. A sitter reads them for the first time with a dog already in the room; an owner opens them in a vet's waiting area. Scanability and consistency outrank expression, and the brand lives in precise details — the 94px arch rise, the 3px white ring around the photo, the 24×3px amber marker over the active tab.

**Key Characteristics:**
- White canvas, near-black ink, exactly one signal colour
- Amber as wayfinding, never as a button
- Real pet photography leads; a missing image is amber-tinted, never grey
- Cards separated by shadow, not outline
- An italic serif used only for names — never for a label
- Every section entry is icon-anchored for fast scanning

## Colors

A restrained palette: one saturated hue against a full neutral ramp, with four status pairs that are permitted to speak only about status.

### Primary
- **Signal Amber** (`#ffbf00`): The single action-and-orientation colour. In the implemented screens it fills the app-bar band and the hero band behind the arch, and marks the active tab with a 24×3px bar. It carries ink text at 11.15:1. It is never a button fill.
- **Amber Deep** (`#e0a400`): The pressed/hover partner — it darkens rather than brightens, so feedback never flashes. Also carries the concept board's masthead clause.
- **Amber Ink** (`#8a6b00`): Amber dark enough to be read. Carries illustration glyphs on tint at 4.53:1; the only amber allowed at body size (5.02:1 on paper).
- **Amber Tint** (`#fdf3d3`): The illustration-tile ground. This is the value that replaces a grey placeholder.

### Neutral
- **Paper** (`#ffffff`): The page and card ground. Implemented as `--wf-bg` / `--wf-input-bg`.
- **Ink** (`#141414`): Body and heading text, and the primary button fill. Near-black rather than pure black so it sits calmer on white, still 18.42:1.
- **Meta** (`#5c5c5c`): Secondary text — timestamps, breed lines, counts, inactive tab labels. Recedes while holding 6.69:1 on paper and 6.08:1 on surface.
- **Surface** (`#f4f4f4`): The secondary ground — icon tiles, segmented-control track, secondary buttons.
- **Line** (`#e7e7e7`): Hairline separation. A 1px card border and the tab bar's top edge; never a heavy outline.
- **Photo Ground** (`#eaeaea`): The tone behind a photograph for the instant before it paints. It is not a placeholder — a user is never left looking at it.

### Status
- **Verified Green** (`#0c6b3b` on `#e6f3ec`, 5.78:1): The verification tick and the enamel *up-to-date* tag.
- **Due Soon** (`#8a5800` on `#fbeed6`, 5.26:1): Deliberately amber-brown and distinct from Signal Amber, so a warning is never mistaken for an action.
- **Overdue** (`#9a2820` on `#f9e7e6`, 6.52:1): Deep, not alarm-red.
- **Upcoming** (`#235a73` on `#e5f0f4`, 6.51:1): The quietest status, so the far future never competes with what is due now.

### Named Rules

**The One Signal Rule.** Amber appears on the band and the active-tab marker, and essentially nowhere else. If a second amber element enters a screen, one of them is wrong.

**The Amber Is Not A Button Rule.** Across all 21 implemented screens, no button is amber-filled. Primary actions are ink; amber is orientation, not invitation. An amber button would read as a second, competing call to action.

**The Ink-On-Amber Rule.** Ink `#141414` is the only text colour permitted on amber (11.15:1). Meta grey on amber is 4.05:1 and fails.

**The Status-Only Rule.** The four status pairs describe state and nothing else. They are never used as decoration or category colour.

## Typography

**Display Font:** Bricolage Grotesque (with `system-ui`, sans-serif)
**Body Font:** Hanken Grotesk (with `system-ui`, `-apple-system`, sans-serif)
**Accent Font:** EB Garamond italic (with Georgia, Times New Roman, serif)

**Character:** A characterful grotesque gives the interface a spine, a quiet workhorse does the reading, and an italic serif warms exactly one thing — the name of someone you love. The pairing is warm and credible without tipping into either cosy or clinical.

### Hierarchy
- **Name** (EB Garamond italic 700, 36px, 1.06): The pet's or owner's name under the arch. The single most expressive element on any screen.
- **App bar** (Bricolage Grotesque 600, 17px, 1.5, −0.01em): The screen's title in the amber band. On the pet card this slot holds the pet's *name*, so it switches to EB Garamond 700 — a name is a name wherever it appears.
- **Section title** (Bricolage Grotesque 700, 16px, 1.3): The heading on every listing card.
- **Body** (Hanken Grotesk 400, 14px, 1.5): Descriptions and record values.
- **Body small** (Hanken Grotesk 400, 13px, 1.45): The meta line under a section title — counts and "Updated N days ago".
- **Label** (Hanken Grotesk 500, 10.5px): Tab bar captions. The active tab steps to 700 and ink.

### Named Rules

**The Names-Only Rule.** The serif is for names — pet and owner — and nothing else. "Owner" as an app-bar title is a *label*, not a name, so it stays sans. This is the rule most likely to be broken by accident.

**The X-Height Rule.** When EB Garamond sits inline with Bricolage Grotesque, set it at **1.25×** the grotesque's size and `line-height: 1`. Garamond's x-height is 42.1 per 100px against Bricolage's 52.5, so at a shared size the serif reads about 20% short. Cap-heights already agree (66 vs 65.4) — only the lowercase looks wrong. A name standing alone needs no correction.

**The Meta-Is-Not-A-Heading Rule.** A meta line nested inside a heading element must restate `font-family` and `font-weight`, or it inherits the display face and 700 and reads as a second title.

## Layout

A single mobile-first column, **372px** wide, held inside a device frame in the prototype. Content sits on a **16px** side inset, giving a **340px** content width that every card, field, and button shares — one measure, no exceptions.

Vertical rhythm is driven by a small spacing set: **4 / 6 / 10 / 12 / 14 / 16 / 24px**. Cards carry **14px** internal padding and stack with a **10px** gutter; the icon-to-text gap inside a row is **12px**; a group of sections is separated from the next block by **24px**.

Screens open with a full-bleed amber band. The band's height varies by the weight of what it introduces — **68px** for a plain app bar, **160px** on the pet card and owner profile, **188px** on Share, **224px** on the shared card — and a white arch is cut into its bottom edge. The tab bar is **61px** and is pinned to the bottom on every owner-facing screen; the recipient's shared card has no tab bar at all, because a sitter has no account to navigate.

Desktop is a later phase. The current pages render the mobile canvas centred on a neutral board.

## Elevation & Depth

The system is **shadow-separated, not outlined**. Cards are told apart from the page by a soft, offset shadow plus a single hairline — never by a heavy border and never by a zero-offset halo, which reads as a glow rather than lift.

### Shadow Vocabulary
- **Card** (`0 10px 24px -18px rgba(20,20,20,.13), 0 2px 6px -4px rgba(20,20,20,.05)`): Every listing card and section. Two stacked shadows — a wide, deeply-inset ambient one and a tight contact one. Deliberately lightened once during the concept phase after the first value read too heavy.
- **Popover** (`0 26px 50px -22px rgba(20,20,20,.34), 0 6px 16px -10px rgba(20,20,20,.16)`): Confirm sheets and the QR sheet — exactly one step above a card.

### Named Rules

**The No-Outline Rule.** Depth comes from shadow plus a `#e7e7e7` hairline. A black or heavy border on a card contradicts the world.

## Shapes

Corner radius encodes *what a thing is*, and the scale is small enough to memorise:

- **Pill** (`999px`) — buttons and the segmented switcher. The committed action shape.
- **Card** (`16px`) — cards, sheets, illustration tiles.
- **Input** (`12px`) — anything you act on *inside* a card: fields, selects, icon tiles, calendar tiles, photo thumbnails.
- **Tag** (`9px`) — the flat enamel *up-to-date* tag. The ID-tag radius the whole direction is named after.
- **Chip** (`8px`) — status chips.
- **Circle** (`50%`) — photographs of a living thing, and round icon buttons.

The signature geometry is **the arch**: a white panel cut into the bottom of the amber band with `border-radius: 50% 50% 0 0 / 94px 94px 0 0`. The **94px rise is constant** across every screen that uses it; only the band height above it changes. The pet's photograph is an 88px circle with a 3px white ring, centred so that exactly half of it sits above the arch line and half below.

## Components

### Buttons
- **Shape:** Fully pill (`999px`)
- **Primary:** Ink `#141414` on white text, `15px 20px` padding, Hanken Grotesk 14px/600, minimum 44px tall
- **Secondary:** Surface `#f4f4f4` with ink text, same geometry
- **Round icon button:** A 30–36px circle in paper white, used for edit and share beside a photograph or title

### Cards
- **Corner Style:** 16px
- **Background:** Paper white
- **Shadow Strategy:** The card shadow above, plus a 1px `#e7e7e7` hairline
- **Internal Padding:** 14px; 340px wide; 10px gutter between siblings
- **Anatomy:** A 36px surface-grey icon tile (12px radius) carrying one Solar glyph, then a title and a 13px meta line, then an optional verification tick and a chevron

### Inputs / Fields
- **Style:** Paper white, 12px radius, 1px `#e7e7e7` hairline, `0 14px` padding, **46px** tall
- **Select:** Identical, with right padding opened to 42px to clear the chevron
- **Labels:** Every control carries a programmatic `id`/`for` pair — never a merely adjacent label

### Navigation
- **Tab bar:** Paper white, 61px, a 1px `#e7e7e7` top hairline, four destinations — **Pets · Reminders · Share · Owner**
- **Active:** Ink label at 700 plus a **24×3px amber bar** above the icon
- **Inactive:** Meta grey at 500, 10.5px
- **Absent by design** on the recipient's shared card

### Chips & Tags
- **Up-to-date tag:** Verified green on its tint, 9px radius, `5px 11px`, 12px/600. The enamel badge the direction is named for.
- **Status chip:** 8px radius, same padding, coloured by the status pair for its section — overdue, due soon, or upcoming.

### Segmented Control
The pet switcher: a `#f4f4f4` pill track, 36px tall, full content width. The active segment is ink with white text, and its two *inner* corners square off to 0 so the active half reads as a tab pulled forward rather than a floating pill.

### Switch
48×28px pill, ink when on and `#e7e7e7` when off, with a 26px white knob carrying a soft drop shadow and a checkmark that fades in on the active state.

### Illustration Tile
A 120×120px, 16px-radius tile in amber tint carrying one content-matched Solar glyph in amber ink. **This is the system's answer to a missing image** — the replacement for the grey placeholder the concept phase rejected by name.

### Photograph
An 88px circle, 3px white ring, photo-ground fill beneath. Positioned so half the circle crosses the arch line. Real photography of the actual animal is the point; this is the element the whole layout is built around.

## Do's and Don'ts

### Do:
- **Do** keep amber to the band and the active-tab marker — roughly one amber element per screen.
- **Do** use ink `#141414` for every primary action.
- **Do** set the serif at 1.25× with `line-height: 1` whenever it sits inline with the grotesque.
- **Do** anchor every section row with a 36px icon tile — a bare text list was rejected by name.
- **Do** reach for the amber-tint illustration tile whenever an image is missing.
- **Do** keep the arch rise at 94px and centre the photo 50/50 on the arch line.
- **Do** give every form control a programmatic label and a ≥44×44 tap target.

### Don't:
- **Don't** fill a button with amber. Primary actions are ink.
- **Don't** put meta grey on amber (4.05:1). Ink is the only text colour on the signal.
- **Don't** put the serif on anything that is not a name. "Owner" is a label.
- **Don't** outline a card. Shadow plus a hairline is the separation.
- **Don't** use a grey fill where an image belongs.
- **Don't** introduce cream or terracotta in any role. This is the standing refusal the white canvas exists to enforce.
- **Don't** use emoji anywhere in product UI. Functional glyphs (`✓`, `✕`) are icons and are fine.

---

## Sources

- [`concept/concept.md`](concept/concept.md) — the **why**: Designer's Taste, the five Attributes every decision is checked against, the white-canvas decision, and the token table tying each token to the Attribute it serves.
- [`concept/references.md`](concept/references.md) — the Refero visual direction and the reference products (August Health, Airbnb, Headspace, Care.com, Kinhive) the techniques are borrowed from.

*Generated by `/impeccable document` from the 21 implemented screens: `home-success`, `Me`, `Whats-due`, `Share-a-pet`, `Shared-pet-view` and their state pages. Values are measured from computed styles on the live pages, not transcribed from the spec.*
