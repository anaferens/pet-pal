# PetPal — Concept

Concept-phase decisions for the visual design. Companion to [`references.md`](references.md) (the Refero visual direction) and grounded in [`../research/personas.md`](../research/personas.md), [`../research/jtbd.md`](../research/jtbd.md), [`../research/voice.md`](../research/voice.md).

---

## Designer's Taste

Captured from the designer directly — the fixed reference points every visual decision is checked against.

### Likes — named products, not adjectives
- **Headspace** — mental health is a serious subject, but they make it *fun and calming*. Seriousness and lightness in the same screen.
- **Airbnb** — *photography carries the screen*. Real images do the emotional and informational work; the UI recedes around them.
- **Endel** (ambient / mental-health background music) — an *illustration language that stays serious at the same time*: expressive, systematic, never childish.

### Anti-references — do NOT want
- **Warm cream background + terracotta** — AI's first reflex the moment it reads "cosy." The default we refuse.
- **Grey gradients instead of photography** — placeholder fills standing in for a real image.
- **Emoji** — as decoration or content. *(Also forbidden by [voice.md](../research/voice.md) — taste and research agree here.)*
- **Screens without icons** — bare text lists with no visual anchors to scan by.

---

## Attributes

Five opposing pairs for PetPal. Each is **`X, not Y ← data point (source); technique — borrowed technique`** — a research anchor *and* a concrete technique from [`references.md`](references.md). None contradicts the Designer's Taste above. One place where research and taste diverge is flagged at the end for you to decide.

### 1 · Calm, not anxiety-inducing
- **← Data:** the owner is *already* anxious — the handoff is emotionally loaded (**56% feel "overwhelming guilt and anxiety" leaving their pet**, personas.md · A2), and the job is emotional before it's functional: *"peace of mind"* is the single most-repeated feeling in real reviews ([jtbd.md E1](../research/jtbd.md)). The UI must lower the temperature, not raise it.
- **← Technique:** Care.com's **well-structured caregiver card** (one calm free-text field + inline helper tip) for the sitter handoff, over **Headspace's colour discipline** (warm-neutral base, one action colour, saturated hue only in small accents) — so nothing on screen *reads* urgent unless it truly is.
- *Taste-consistent:* Headspace ("serious… but calming").

### 2 · Trust signals visible, not hidden
- **← Data:** [jtbd.md R3](../research/jtbd.md) — *"give a professional an accurate picture quickly… facts, not guesswork,"* and the Main job is *"somewhere I **trust** and can pass on."* Verbal "he's up-to-date" isn't accepted by kennels/vets (personas.md · A1 proof).
- **← Technique:** a **verification / "up-to-date" badge placed next to the section or block** — August Health's fully-pill badge + Airbnb's small trust badges (a compact verified / checkmark mark), sitting where the eye already is, never buried in a menu.

### 3 · Real imagery — pet photography + purposeful illustration — not grey-gradient placeholders
- **← Data:** [jtbd.md R2](../research/jtbd.md) — *"make a stranger understand my pet fast"* (the strongest match to Rover's care card); the sitter *"has never met this animal and needs to understand it fast"* (personas.md · A3). A real photo of *this* pet is both recognition and emotional anchor.
- **← Technique:** **Airbnb's photography-carries-the-screen approach** (real, emotional imagery doing the social-proof work) + **August Health's soft circular photo mask**; *serious* flat illustration (Endel / Headspace register) reserved for empty states and onboarding — **never** a grey gradient standing in for a missing image.
- *Taste-consistent:* reconciles both likes — **Airbnb** (photography carries the screen) for the pet, **Endel** (serious illustration) for the light moments — against the **grey-gradient** anti-reference.

### 4 · Icon-supported, not text-only
- **← Data:** the record must be *scannable* — the sitter reads fast (A3), the worried owner acts fast in an emergency (personas.md · A4), and [voice.md](../research/voice.md) treats each section as a recognizable *place*. Icons let a dense health record be read at a glance.
- **← Technique:** **August Health's monoline outlined icons** (consistent stroke, functional not decorative) beside each section label. Functional glyphs (`✓` complete, `✕` close) are allowed by voice.md — but as **icons, never as emoji**.
- *Taste-consistent:* directly answers the **"screens without icons"** and **"emoji"** anti-references — icons yes, emoji no.

### 5 · Warm and credible, not cosy-cliché nor clinical  ⚠
- **← Data:** [voice.md](../research/voice.md) — *"calm confidence — warm by default, precise when it matters,"* and *own "trusted," not "complete."* PetPal must read as a record credible enough for a vet (A1) yet warm enough to hand to a friend without guilt (A2).
- **← Technique:** August Health's system + **Kinhive's italic serif**, used to *carry the message itself* — roman for the credible/clear clause, italic for the warm one (the hero pairs both) — on the clean white base + Headspace's **restraint** (one action colour).
- **Resolved → white canvas:** base is a **white canvas `#ffffff`**; a **light neutral grey** stays only as a *secondary* section surface — never a warm or cream ground. (See the decision below.)

### ✓ Where research and taste diverged — decided: (b)
[`references.md`](references.md) had committed the base surface to **Warm Sand `#f8f3eb`** (a warm cream), inherited from August Health. Your **#1 anti-reference** is exactly that warm-cream "cosy" look — a genuine tension.

**Decision (b), 2026-07-26.** The three references this direction is built on — **August Health, Airbnb, Headspace** — are all in fact **white / near-white based** (August's page base is `#ffffff`, with Warm Sand only a *secondary* surface; Airbnb is white; Headspace is `Cloud Whisper #f9f4f2`). A cream page ground pulls *away* from them, and it fights Airbnb-style photography. Resolved to:

- **Base → white `#ffffff`** — clean and neutral. (Refined from the earlier warm near-white `#faf8f4`, which read too creamy and warm.)
- **Secondary surface → light neutral grey `#f4f4f4`** — section bands and the panel behind floating cards (the two-surface rhythm, neutralised from Warm Sand so nothing reads cream).
- **Warmth is carried by** the pet photography, the warm-orange accent + arched hero, and the serif headline — layered on, not painted across the background. (Body ink is a neutral near-black `#1a1a1a`.)

This keeps pair #5's sweet spot (*warm and credible, not cosy-cliché nor clinical*) and can't read as the AI cosy-cream reflex. One rule holds regardless: **never cream + terracotta.** Locked into [`references.md`](references.md) and the design system.

---

## Directions — selected: C · The Signal *(2026-07-27)*

From the three worlds explored in [`directions.html`](directions.html) (via the impeccable flow + slop test), the designer chose **C · The Signal**. This **supersedes** the earlier synthesis's *"Committed direction"* table in [`references.md`](references.md) — that phase stays as evidence/anti-reference. The durable token set is recorded in [**Tokens**](#tokens) below, and rendered live in [`concept.html`](concept.html), which is the source of truth for component values.

- **World:** enamel ID-tag / transit wayfinding — confident, findable, calm under pressure. Not the category's cream-and-terracotta reflex, nor the generic pastel health-app.
- **Colour (Restrained):** white `#ffffff` · ink `#141414` · **one signal amber-gold `#FFBF00`** (black text as on-accent) · light-grey `#f4f4f4` secondary · `#5c5c5c` meta.
- **Type:** Bricolage Grotesque (display) + Hanken Grotesk (body) + **EB Garamond** italic (names — pet + owner).
- **Shape:** **pill** buttons; flat enamel "up-to-date" tag (`--r-tag`, built as `.uptodate` — on the pet card under the name); cards float on a soft shadow — **no black outlines**.
- **Icons:** Solar **bold**.
- **Imagery:** real pet photography leads the card (Airbnb-style); icons for fast scanning.

### Alternatives — documented, not selected *(kept for reference; see [`directions.html`](directions.html))*

**A · The Passport** — *Committed colour strategy.* The EU pet passport / official vet record: a deep **passport-ink** field (`#0B3A4A`) carrying the header and ID band on white, with machine-readable **mono IDs**, security guilloche hairlines, an official stamp accent, and a validation-green tick. Type: Schibsted Grotesk + Hanken Grotesk + Spline Mono. Reads *credible / official* — leans hardest into A1 (proof). Set aside as too document-formal for the warmth PetPal wants at the handoff.

**B · The Field Guide** — *Drenched colour strategy.* A naturalist specimen catalogue: a deep **herbarium-green** ground (`#1B3A2C`) with **bone** text and **antique-gold** classification labels, an engraved oval plate for the pet photo, Latin binomial, and a specimen number. Type: Bodoni Moda (engraved-plate display) + Hanken Grotesk. Reads *heritage / scientific* — warm via illustration, not surface. Set aside as too dark/editorial for a fast, calm records tool — but a strong reference for empty states or a premium tier.

Both remain viable worlds: if The Signal ever needs more gravitas (A) or more heritage warmth (B), the material is here.

---

## Tokens

The full set in use, each tied to the **Attribute** it serves. Anything on a PetPal screen must resolve to a token below; a value that can't is a decision invented from scratch and gets removed. Live in [`concept.html`](concept.html) `:root`.

> **This section follows the layouts.** The 21 implemented screens are the design; this table describes them. Values below were measured from computed styles on the live pages (see [`../DESIGN.md`](../DESIGN.md), generated from the same screens), not transcribed from intent. Where the wireframes name a token differently from the concept board, **the wireframe name is the one that ships** and is given in the *In the layouts* column.

### Colour

| Token | In the layouts | Value | Serves | Why this value |
|---|---|---|---|---|
| `--paper` | `--wf-bg`, `--wf-input-bg` | `#ffffff` | 5 · Warm and credible | The white canvas decided above — refuses the cream-and-terracotta anti-reference. |
| `--ink` | `--wf-text`, `--wf-btn` | `#141414` | 1 · Calm | Near-black, not pure black: sits calmer on white while holding 18.42:1. Also the primary button fill. |
| `--surface` | `--wf-surface`, `--wf-btn-sec` | `#f4f4f4` | 5 | The neutral secondary surface — icon tiles, the segmented-control track, secondary buttons. De-creamed from Warm Sand. |
| `--line` | `--wf-border` | `#e7e7e7` | 1 · Calm | Hairline separation instead of a border. Cards are told apart by shadow, not outline. |
| `--meta` | `--wf-muted` | `#5c5c5c` | 1 · Calm | Secondary text that recedes but still clears AA — 6.69:1 on paper, 6.08:1 on surface. |
| `--signal` | `--signal` | `#ffbf00` | 2 · Trust signals visible | The one signal colour. **Implemented as orientation, not as an action fill** — see the rule below. |
| `--signal-ink` | `--signal-ink` | `#8a6b00` | 3 · Real imagery | Amber dark enough to be *text or a glyph*. Carries illustration glyphs on tint at 4.53:1. |
| `--signal-tint` | `--signal-tint` | `#fdf3d3` | 3 · Real imagery | The illustration-tile ground. Warmth without a grey placeholder — the anti-reference this replaces. |
| `--photo-bg` | `--wf-placeholder` | `#eaeaea` | 3 · Real imagery | The tone behind a photo for the instant before it paints. **Not a placeholder fill** — it is never what a user is left looking at. |
| `--success` / `--success-bg` | same | `#0c6b3b` / `#e6f3ec` | 2 · Trust signals visible | The verification mark and the enamel *up-to-date* tag. 5.78:1. |
| `--warning` / `--warning-bg` | same | `#8a5800` / `#fbeed6` | 1 · Calm | *Due soon.* Amber-brown, deliberately distinct from `--signal` so a warning is never mistaken for an action. 5.26:1. |
| `--danger` / `--danger-bg` | same | `#9a2820` / `#f9e7e6` | 1 · Calm | *Overdue* and destructive actions. Deep, not alarm-red — [voice.md](../research/voice.md) P2 asks for precise, never panicked. 6.52:1. |
| `--info` / `--info-bg` | same | `#235a73` / `#e5f0f4` | 1 · Calm | *Upcoming.* The quietest status, so the far future doesn't compete with what's due. 6.51:1. |

**Semantic colour is status only, never decoration.** All four pairs clear AA on their own ground (5.26–6.52:1, verified against the shipped values).

**Amber is orientation, not invitation.** In all 21 screens amber fills the app-bar band and the hero band behind the arch, and marks the active tab with a 24×3px bar — and fills **no button anywhere**. Primary actions are ink `#141414`. *Rationale:* the direction is transit wayfinding, and a band that says *where you are* cannot also be the thing that says *press me* without the screen growing two competing voices. This is what the layouts do; the amber pill button on the [`concept.html`](concept.html) board is a swatch of the token, not a shipped pattern.

**Ink is the only text colour on amber** (11.15:1). Meta grey on amber is 4.05:1 and fails.

#### Declared only on the board, not in the layouts

| Token | Value | Status |
|---|---|---|
| `--on-signal` | `#141414` | A *rule* rather than a variable in the wireframes — the ink-on-amber pairing is written literally. Kept because the rule it names is load-bearing. |
| `--signal-deep` | `#e0a400` | Hover/pressed for amber, and the board's masthead clause. No shipped screen has an amber hover surface yet, so it appears only in `concept.html`. Darkens rather than brightens, so feedback never flashes. |
| `--disabled` | `#8a8a8a` | Inactive control text. Ships in the wireframes as `--nav-cap`, where it styles the **prototype sidebar** only, not product UI. |
| `--board` | `#ececec` | The language board's own page ground. Documentation chrome, never product UI. |

The four status pairs and `--signal-tint` are declared on the 10 pages that use them rather than globally — a page carries the tokens it needs. Every `var()` reference in all 21 pages resolves on its own page; there are no dangling references.

#### The tab bar's own set

The wireframes carry `--nav-bg` `#ffffff`, `--nav-line` `#e7e7e7`, `--nav-text` `#5c5c5c`, `--nav-text-active` `#141414`, `--nav-active-bg` `#f4f4f4`. *Rationale:* these are aliases of the neutral ramp, kept separate so the tab bar can be restyled without touching page surfaces. `--nav-cap` `#8a8a8a` belongs to the prototype sidebar and is not product UI — its 3.45:1 is therefore not a product accessibility finding.

### Type

| Token | Value | Serves | Why |
|---|---|---|---|
| `--disp` | Bricolage Grotesque 600/700 | 5 · Warm and credible | Headings. Confident without shouting. |
| `--body` | Hanken Grotesk 400–700 | 4 · Icon-supported | UI and body. Neutral, highly legible down to 13px. |
| `--serif` | EB Garamond italic 700 | 5 · Warm and credible | **Names only** — pet and owner. Kinhive's italic serif carrying the warm clause. Never a label: Me.html's app bar reads "Owner", which is a label, so it stays sans. |

**The roles as implemented.** Measured on the live screens; each is a role, not a free size.

| Role | Value | Where | Why this value |
|---|---|---|---|
| Name | EB Garamond italic 700 · 36px · 1.06 | Under the arch, on the pet card and owner profile | The single most expressive element on a screen. Large enough to be the thing you see first, italic so it reads as *a name* rather than a heading. |
| App bar | Bricolage Grotesque 600 · 17px · 1.5 · −0.01em | The title inside the amber band | Small and calm — the band already does the orienting, so the title does not need to shout. **Switches to EB Garamond 700 when the title is a name** (the pet card), because a name is a name wherever it appears. |
| Section title | Bricolage Grotesque 700 · 16px · 1.3 | The heading on every listing card | Byte-identical across `home-success`, `Whats-due` and `Shared-pet-view` — this is the most repeated component in the product, so its spec is the one that must not drift. |
| Body | Hanken Grotesk 400 · 14px · 1.5 | Descriptions and record values | The default reading size. |
| Body small | Hanken Grotesk 400 · 13px · 1.45 | The meta line under a section title — counts, "Updated N days ago" | One step down so the count recedes behind the section name without becoming unreadable. 6.69:1 in `--meta`. |
| Tab label | Hanken Grotesk 500 · 10.5px | Tab bar captions | Caption scale; the active tab steps to 700 and `--ink` so the current place is legible at a glance. |

**A meta line nested inside a heading must restate its own font.** `font-family` **and** `font-weight` both — otherwise it inherits the display face and 700 from the enclosing heading and renders as a second title. *Rationale:* the section-title/meta-line pair is the most repeated component in the product; when the meta inherits, every card on the screen reads as two competing headings.

**Standing rule — set the serif 1.25× when it sits inline with the grotesque.** EB Garamond's x-height is 42.1 per 100px against Bricolage's 52.5, so at a shared `font-size` the serif reads about 20% short. Multiply by `52.5 / 42.1 = 1.25` to match x-heights and the two faces look one size; pair it with `line-height:1` so the taller inline box doesn't inflate the line. Cap-heights already agree (66 vs 65.4), which is why only the lowercase looks wrong. Applied to the masthead clause and to the Garamond type specimen (56px against the two 46px sans specimens). A name standing on its own — `.petcard .n`, the row names, the 26px name spec — needs no correction, because nothing sits beside it to be short against.

**The masthead clause is the one deliberate contrast exception.** It is set in `--signal-deep`, which is `1.88:1` on `--board` — below the 3:1 large-text bar. It is expressive display type on a decorative headline and is documented as an exception, not a pattern: amber that has to be *read* uses `--signal-ink` (`5.02:1` on `--paper`). Nothing else in the system takes an exception.

### Shape

The scale is real and consistent in the layouts, but it ships as **literal `px`, not as `--r-*` custom properties** — none of the six radius tokens is declared on any of the 21 pages. They are named here because the *scale* is the durable decision; the variables exist only on the [`concept.html`](concept.html) board. Radius encodes **what a thing is**, which is why the set is small enough to memorise.

| Token (board) | Value | Serves | Why |
|---|---|---|---|
| `--r-pill` | `999px` | 2 · Trust | Buttons and the segmented switcher. The committed *action* shape. |
| `--r-card` | `16px` | 1 · Calm | Cards, sheets, illustration tiles — the containers. |
| `--r-input` | `12px` | 1 · Calm | Anything you act on *inside* a card: fields, selects, icon tiles, calendar tiles. |
| `--r-tag` | `9px` | 2 · Trust | The flat enamel *up-to-date* tag. The enamel ID-tag radius the direction is named for. |
| `--r-chip` | `8px` | 2 · Trust | Status chips (*Overdue*, *Due soon*). One step tighter than the tag, so status reads as smaller than proof. |
| `--r-thumb` | `12px` | 3 · Real imagery | Photo thumbnails. Same value as `--r-input` — kept as a separate name because it answers a different question. |
| *(no token)* | `50%` | 3 · Real imagery | Photographs of a living thing, and round icon buttons. A circle is reserved for faces. |

**The arch is the signature geometry.** A white panel cut into the bottom of the amber band: `border-radius: 50% 50% 0 0 / 94px 94px 0 0`. The **94px rise is constant** on every screen that uses it — `home-success`, `Me`, `Shared-pet-view` — and only the band height above it changes (160px on the pet card and owner profile, 188px on Share, 224px on the shared card). *Rationale:* the arch is the one shape a returning user recognises before reading anything, so its curvature is fixed and the band flexes instead. The band must stay at least as tall as apex + rise, or the curve clips flat at the edges.

**The photo sits 50/50 on the arch line.** An 88px circle with a 3px `--paper` ring, centred so exactly half crosses the arch. *Rationale:* it belongs to both the amber band and the white card, which is what makes the pet — not the chrome — the subject of the screen.

### Layout

| Attribute | Value | Why |
|---|---|---|
| Canvas | `372px` | Mobile-first; the prototype's device frame. Desktop is a later phase. |
| Side inset | `16px` | Gives a `340px` content measure that **every** card, field and button shares — one measure, no exceptions, so nothing looks hand-placed. |
| Card padding | `14px` | Tight enough to keep a section row at 72px, loose enough that the 36px icon tile does not touch the edge. |
| Card gutter | `10px` | Cards in a group read as one list; the group is then separated from the next block by `24px`. |
| Row gap | `12px` | Icon tile → text inside a card row. |
| Field height | `46px` | Above the 44px tap-target floor with 2px to spare. |
| Tab bar | `61px` | Pinned bottom on every owner-facing screen. **Absent on the recipient's shared card** — a sitter has no account, so there is nowhere to navigate. |

### Elevation

| Token | Value as shipped | Serves | Why |
|---|---|---|---|
| `--sh-card` | `0 10px 24px -18px rgba(20,20,20,.13), 0 2px 6px -4px rgba(20,20,20,.05)` | 1 · Calm | Cards float on a soft shadow instead of an outline. Two stacked shadows — a wide, deeply-inset ambient one and a tight contact one — so the card lifts without a visible edge. Never a zero-offset halo, which reads as a glow. Lightened once on the designer's note that the first value was too intense. Identical on all 21 pages. |
| `--sh-pop` | `0 26px 50px -22px rgba(20,20,20,.34), 0 6px 16px -10px rgba(20,20,20,.16)` | 1 · Calm | Confirm sheets and the QR sheet — exactly one step above a card. Declared on the 17 pages that have a sheet. |
| `--sh-phone` | — | — | Prototype chrome only (the device frame), not product UI. |

Cards also carry a `1px --line` hairline alongside the shadow. *Rationale:* shadow alone disappears against `--surface`; the hairline guarantees the edge is findable on either ground without becoming an outline.

### Standing rules

- **Tap targets ≥ 44×44** (WCAG 2.5.5). Buttons are `15px 20px` for a 44px box; fields are 46px.
- **Every form control needs a programmatic label** — `id` + `for`, not a visually adjacent `<label>`.
- **Icons are Solar only.** Where Solar has no glyph — it has no bare checkmark and no bowl — draw it in CSS rather than importing a second family. All 189 icons ship **inlined as base64 data URIs**, not fetched from the Iconify CDN. *Rationale:* the pages render with no network dependency and no icon flash; the trade is that family provenance is no longer machine-checkable from the file, so it must be enforced at authoring time.
- **No grey placeholder fills.** A missing image is the `--signal-tint` illustration tile (120×120, `--r-card`) with one content-matched Solar glyph; a real photo where the content is a pet or a person (Attribute 3).
- **Amber fills no button.** Primary actions are `--ink`. See the colour section.

---

## Where this file sits

[`../DESIGN.md`](../DESIGN.md) is generated from the layouts and records **what is implemented**. This file records **why** — the taste, the attributes, and the reasoning behind each value. When the two disagree, the layouts are the design and this file is corrected to follow them.
