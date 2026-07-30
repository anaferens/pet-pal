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

### Colour

| Token | Value | Serves | Why this value |
|---|---|---|---|
| `--paper` | `#ffffff` | 5 · Warm and credible | The white canvas decided above — refuses the cream-and-terracotta anti-reference. |
| `--ink` | `#141414` | 1 · Calm | Near-black, not pure black: sits calmer on white while holding 18.4:1. |
| `--surface` | `#f4f4f4` | 5 | The neutral secondary surface — the two-surface rhythm, de-creamed from Warm Sand. |
| `--line` | `#e7e7e7` | 1 · Calm | Hairline separation instead of a border. Cards are told apart by shadow, not outline (Shape: *no black outlines*). |
| `--meta` | `#5c5c5c` | 1 · Calm | Secondary text that recedes but still clears AA on white (6.7:1). |
| `--signal` | `#ffbf00` | 2 · Trust signals visible | The one action colour. Headspace's discipline: saturated hue only in small accents. |
| `--on-signal` | `#141414` | 2 | Ink is the only text colour allowed on amber — 11.2:1. Muted grey on amber is 4.05:1 and **fails**. |
| `--signal-deep` | `#e0a400` | 1 · Calm | Hover/pressed for amber. Darkens rather than brightens, so feedback never flashes. |
| `--signal-ink` | `#8a6b00` | 3 · Real imagery | Amber dark enough to be *text or a glyph*. Carries illustration glyphs on tint at 4.5:1. |
| `--signal-tint` | `#fdf3d3` | 3 · Real imagery | The illustration-tile ground. Warmth without a grey placeholder — the anti-reference this replaces. |
| `--success` / `--success-bg` | `#0c6b3b` / `#e6f3ec` | 2 · Trust signals visible | The verified mark and the enamel *up-to-date* tag. The designer approved green as the one supporting accent. |
| `--warning` / `--warning-bg` | `#8a5800` / `#fbeed6` | 1 · Calm | *Due soon.* Amber-brown, distinct from `--signal` so a warning is never mistaken for a button. |
| `--danger` / `--danger-bg` | `#9a2820` / `#f9e7e6` | 1 · Calm | *Overdue* and destructive actions. Deep, not alarm-red — [voice.md](../research/voice.md) P2 asks for precise, never panicked. |
| `--info` / `--info-bg` | `#235a73` / `#e5f0f4` | 1 · Calm | *Upcoming.* The quietest status, so the far future doesn't compete with what's due. |

**Semantic colour is status only, never decoration.** All four pairs clear AA on their own ground (5.3–6.5:1).

### Type

| Token | Value | Serves | Why |
|---|---|---|---|
| `--disp` | Bricolage Grotesque 600/700 | 5 · Warm and credible | Headings. Confident without shouting. |
| `--body` | Hanken Grotesk 400–700 | 4 · Icon-supported | UI and body. Neutral, highly legible at 13px. |
| `--serif` | EB Garamond italic 700 | 5 · Warm and credible | **Names only** — pet and owner. Kinhive's italic serif carrying the warm clause. Never a label: Me.html's app bar reads "Owner", which is a label, so it stays sans. |

### Shape

| Token | Value | Serves | Why |
|---|---|---|---|
| `--r-pill` | `999px` | 2 · Trust | Buttons and the segmented switcher. The committed *pill* shape. |
| `--r-card` | `16px` | 1 · Calm | Cards, sheets, illustration tiles. |
| `--r-input` | `12px` | 1 · Calm | Inputs, selects, icon tiles, calendar tiles — anything you act on inside a card. |
| `--r-tag` | `9px` | 2 · Trust | The flat enamel *up-to-date* tag. The enamel ID-tag radius the direction is named for. |
| `--r-chip` | `8px` | 2 · Trust | Status chips (*Overdue*, *Due soon*). |
| `--r-thumb` | `12px` | 3 · Real imagery | Photo thumbnails. |

### Elevation

| Token | Serves | Why |
|---|---|---|
| `--sh-card` | 1 · Calm | Cards float on a soft shadow instead of an outline. Offset + blur, never a zero-offset halo. Lightened once on the designer's note that the first value was too intense. |
| `--sh-pop` | 1 · Calm | Confirm sheets and the QR sheet — one step above a card. |
| `--sh-phone` | — | Prototype chrome only (the device frame), not product UI. |

### Standing rules

- **Tap targets ≥ 44×44** (WCAG 2.5.5). Buttons are `15px 20px` for a 44px box.
- **Every form control needs a programmatic label** — `id` + `for`, not a visually adjacent `<label>`.
- **Icons are Solar only.** Where Solar has no glyph — it has no bare checkmark and no bowl — draw it in CSS rather than importing a second family.
- **No grey placeholder fills.** A missing image is the `--signal-tint` illustration tile with one content-matched Solar glyph; a real photo where the content is a pet or a person (Attribute 3).
