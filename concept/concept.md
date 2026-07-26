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
- **← Technique:** a **verification / "up-to-date" badge placed next to the section or block** — August Health's fully-pill badge + Finn's small warm trust-accent (star/checkmark), sitting where the eye already is, never buried in a menu.

### 3 · Real imagery — pet photography + purposeful illustration — not grey-gradient placeholders
- **← Data:** [jtbd.md R2](../research/jtbd.md) — *"make a stranger understand my pet fast"* (the strongest match to Rover's care card); the sitter *"has never met this animal and needs to understand it fast"* (personas.md · A3). A real photo of *this* pet is both recognition and emotional anchor.
- **← Technique:** **Finn's expressive real-pet photography** as the emotional/social-proof anchor + **August Health's soft circular photo mask**; *serious* flat illustration (Endel / Headspace register) reserved for empty states and onboarding — **never** a grey gradient standing in for a missing image.
- *Taste-consistent:* reconciles both likes — **Airbnb** (photography carries the screen) for the pet, **Endel** (serious illustration) for the light moments — against the **grey-gradient** anti-reference.

### 4 · Icon-supported, not text-only
- **← Data:** the record must be *scannable* — the sitter reads fast (A3), the worried owner acts fast in an emergency (personas.md · A4), and [voice.md](../research/voice.md) treats each section as a recognizable *place*. Icons let a dense health record be read at a glance.
- **← Technique:** **August Health's monoline outlined icons** (consistent stroke, functional not decorative) beside each section label. Functional glyphs (`✓` complete, `✕` close) are allowed by voice.md — but as **icons, never as emoji**.
- *Taste-consistent:* directly answers the **"screens without icons"** and **"emoji"** anti-references — icons yes, emoji no.

### 5 · Warm and credible, not cosy-cliché nor clinical  ⚠
- **← Data:** [voice.md](../research/voice.md) — *"calm confidence — warm by default, precise when it matters,"* and *own "trusted," not "complete."* PetPal must read as a record credible enough for a vet (A1) yet warm enough to hand to a friend without guilt (A2).
- **← Technique:** August Health's system + **Kinhive's italic serif** headline (warmth in the letterforms, reserved for hero/emphasis) on the clean near-white base + Headspace's **restraint** (one action colour).
- **Resolved → (b):** base is a **near-white `#faf8f4`**; Warm Sand stays only as a *secondary* section surface — warm, but never a cream ground. (See the decision below.)

### ✓ Where research and taste diverged — decided: (b)
[`references.md`](references.md) had committed the base surface to **Warm Sand `#f8f3eb`** (a warm cream), inherited from August Health. Your **#1 anti-reference** is exactly that warm-cream "cosy" look — a genuine tension.

**Decision (b), 2026-07-26.** The three references this direction is built on — **August Health, Airbnb, Headspace** — are all in fact **white / near-white based** (August's page base is `#ffffff`, with Warm Sand only a *secondary* surface; Airbnb is white; Headspace is `Cloud Whisper #f9f4f2`). A cream page ground pulls *away* from them, and it fights Airbnb-style photography. Resolved to:

- **Base → near-white `#faf8f4`** — Headspace's whisper-warm off-white register. Clean and credible, not clinical.
- **Warm Sand `#f8f3eb` → secondary surface only** — section bands and the panel behind floating cards, exactly how August Health uses it.
- **Warmth is carried by** the pet photography, the warm brown ink `#321004`, and the serif headline — layered on, not painted across the background.

This keeps pair #5's sweet spot (*warm and credible, not cosy-cliché nor clinical*) and can't read as the AI cosy-cream reflex. One rule holds regardless: **never cream + terracotta.** Locked into [`references.md`](references.md) and the design system.
