# PetPal — Visual References (Concept, Step 03)

> **Method.** Sourced via the **Refero MCP** server, grounded in the trust benchmarks and persona anxieties already recorded in [`research.md`](../research/research.md) (Step 02) and [`personas.md`](../research/personas.md). **No new competitor search.** This is a *synthesis*, not a copy: **one foundation style + three borrowed, concrete techniques** — plus three real web screens for specific patterns. Named benchmarks in play: **Headspace** and **Airbnb** (from CLAUDE.md), **Lassie / MyTherapy / Rover** (from research.md).

## The direction in one line

**Foundation:** August Health's *calm, credible healthcare-warmth*. **Borrow #1:** Kinhive's **serif + italic serif** (roman = credibility, italic = warmth — carried in the type itself). **Borrow #2:** Headspace's **colour discipline** (how much colour is on the screen). **Borrow #3:** Airbnb's **photography-led warmth on a clean, tidy canvas** — emotion through real imagery, colour used sparingly. → A record that looks **credible enough for a vet/kennel** yet **warm enough to hand to a sitter without guilt**.

## Persona anxieties we design against
*(from personas.md / research.md — the "why" each technique is chosen)*

| Code | Anxiety | Source |
|---|---|---|
| **A1 — Proof** | Verbal "he's up-to-date" isn't accepted; Eva needs a record kennels/vets/groomers will *believe*. | personas.md "Organised Owner"; research.md §F9 |
| **A2 — Handoff guilt** | **56% feel "overwhelming guilt and anxiety" leaving their pet**; the handoff is emotionally loaded. | research.md §F11 |
| **A3 — Sitter's unfamiliar-pet fear** | A stranger must understand the animal fast — what it eats, what scares it — and not mess up. | personas.md "The Sitter" |
| **A4 — Worried-moment panic** | Emergency; a busy or alarming screen *adds* stress at the worst moment. | personas.md "Worried-at-the-Wrong-Moment" (R5) |
| **A5 — Share-safety** | "Who can actually see my pet's data?" — fear of over-sharing. | research.md §68 (link/code sharing as trust mechanism) |

---

## Styles

### 1 · FOUNDATION — August Health EHR
- **Link:** https://www.augusthealth.com · Refero style `be1c2381-7af0-4d7c-91ca-09a715a06346` · [preview](https://images.refero.design/styles/www.augusthealth.com/be1c2381-7af0-4d7c-91ca-09a715a06346/preview_0.jpg)
- **Why the foundation (not a copy):** it's the only reference that is *literally* "healthcare seriousness **with** cheerful warmth" — the exact balance PetPal's voice already committed to ("own *trusted*, not *complete*; warm by default, precise when it matters"). Its senior-care EHR job is close to ours: sensitive records that families and professionals must both trust.
- **Design techniques adopted (concrete, not impression):**
  1. **Two-surface system, no hard dividers** — white canvas `#ffffff` ↔ **Warm Sand `#f8f3eb`**; sections are separated by a *background-colour change*, never a rule/border line. (Softer, calmer than boxed sections.)
  2. **Serif display headline + clean sans body** — an elegant serif for headings (the credibility cue), a clean sans for body (records stay legible). The **roman ↔ italic** treatment of that serif is **Kinhive's borrow, below**.
  3. **16px floating cards** — `border-radius:16px`, `32px` padding, **no borders**, only a very soft layered shadow. Fully-pill **badges** (`radius ~9999px`).
  4. **Authentic photo in a soft circular/blob mask** — human, real, warm. *(Already matches PetPal's dossier hero: circular pet photo over the arch.)*
  5. **One primary accent only** — a single action colour; "maintain a restrained palette with one primary accent."
- **Persona anxiety it reduces:** **A1 (proof)** — the serif + calm clinical-but-warm polish makes the shared card read as a *real health record*, so a kennel/vet trusts it. Secondarily **A2** — the warmth keeps it from feeling cold/bureaucratic at the emotional handoff.

### 2 · BORROW — Kinhive  *(technique: serif + italic serif = credibility + warmth)*
- **Link:** https://refero.design/search?site_id[id][]=691 · kinhive.com · Refero site 691 · **August Health's close sibling** (same clean-white + serif family)
- **The one concrete technique borrowed — *the type carries the message*:** Kinhive pairs an **upright roman serif** with an **italic serif** in the same headline. PetPal makes this its core credibility-and-warmth device — **roman for the credible/clear words, italic for the warm ones**. The master line already does it: upright "Credible enough for a vet." + italic "Warm enough to hand to a sitter." Warmth lives in the letterforms, before a single colour or photo loads.
- **Why not adopt wholesale:** Kinhive's dark colour-block footer + oversized wordmark is its own brand signature; we take only the roman/italic *type* method.
- **Persona anxiety:** **A1** — roman reads *credible / legit* to a vet or kennel; **A2** — italic reads *warm* at the handoff. One typeface, both jobs.

### 3 · BORROW — Headspace  *(technique: the amount of colour on the screen)*
- **Link:** https://headspace.com · Refero style `c73224da-e583-4833-bf39-3f414c317474` · [preview](https://images.refero.design/styles/headspace.com/c73224da-e583-4833-bf39-3f414c317474/preview_0.jpg)
- **The one concrete technique borrowed — *colour budget*:** a **warm off-white base** (`Cloud Whisper #f9f4f2`), **one bold action colour** for *every* interactive element (Headspace uses `#0061ef` for all CTAs/links/active states), and saturated hues (yellow, plum, blush) **quarantined to illustrations and icons only** — their rule: *"do not use highly saturated colours for large text blocks; reserve them for accents, illustrations, and interactive elements."* Plus the signature **flat 2px lift** (`0 2px 0 rgba(65,61,69,.2)`) instead of heavy shadow.
- **Why not adopt wholesale:** Headspace's playful blobs would undercut A1 (credibility). We take only the *discipline*, not the whimsy.
- **Persona anxiety it reduces:** **A4 (worried-moment) + A2** — a screen that is 90% calm neutral with colour only where you act stays *quiet* under stress; the single action colour makes the one right thing to tap obvious in an emergency, and never feels alarming.

### 4 · BORROW — Airbnb  *(technique: photography carries the emotion on a clean, tidy canvas)*
- **Link:** https://www.airbnb.com · Refero style `afd145ca-269e-4847-9843-62126a839ccf` · **the designer's warmth pick over Finn** — *"Airbnb does the warmth better: illustration, clean, tidy, but with emotion."*
- **The one concrete technique borrowed — *let the image do the feeling***: Airbnb keeps the interface **airy, clean and tidy** (near-white canvas, generous whitespace, precise alignment) and lets **emotional, full-bleed imagery** — real photography and friendly illustration, never stock or grey placeholders — carry the warmth. Colour is **used sparingly, almost ceremonially** (one accent), so warmth reads as *emotion*, not decoration. Images sit in **rounded ~20px "photo-print" cards** with small **trust badges**.
- **Why not adopt wholesale:** Airbnb is a travel marketplace — we take the *photography-led warmth + colour scarcity + tidy layout*, not its browsing/booking patterns.
- **Persona anxiety it reduces:** **A2 (owner) + A3 (sitter)** — a warm, real photo of *this* pet on a clean, tidy card carries the emotion at the handoff and lets a sitter who has never met the animal connect to it instantly: clean and tidy, but with feeling.

---

## Screens *(web patterns — how real products solve our specific screens)*

### A · Pet dossier / profile → **Aboard — Personal information**
- **Link:** https://refero.design/pages/78ddf817-ec6b-4f63-9937-895a9f088d0d (source: app.aboardhr.com)
- **Technique selected:** **centred avatar + single-column "label → value" list with one right-aligned `Edit`** — a quiet, scannable identity block (name, breed, chip, etc.) with editing tucked to the side, not competing buttons per row.
- **Persona anxiety:** **A1 / A3** — a clean complete-looking field list signals "this record is real and finished," and the sitter scans it in seconds.

### B · Shared card with petsitter → **Airbnb — share via link**
- **Link:** https://refero.design/pages/e57be91c-4934-4cd0-a9e5-a3680fe67429 (source: airbnb.com; named benchmark)
- **Technique selected:** **a share-options grid (copy-link / email / message) with an explicit visibility-disclaimer line + "learn more" directly beneath it** — the note that spells out *who can see this and for how long*.
- **Persona anxiety:** **A5 (share-safety)** — mirrors research.md's "lightweight, time-boxed link sharing" trust mechanism; the disclaimer line is what tells Eva exactly who can open the pet's card.

### C · Sitter-facing care info → **Care.com — caregiver instructions**
- **Link:** https://refero.design/pages/fa74b13a-ba68-4537-adb4-4ec1342b04d9 (source: care.com)
- **Technique selected:** **one free-text "extra details" field with an inline helper-tip link** guiding what a caregiver actually needs — the unstructured human nuances a form can't capture (Rover's "care instructions" pattern from research.md §16).
- **Persona anxiety:** **A3 / A2** — gives Eva a place to say "he hides during thunderstorms," which is exactly what calms a first-time sitter.

---

## Hand-picked references — designer's own ("clean, with a twist")

Chosen directly by the designer. The through-line: **clean, disciplined layouts that earn personality from one confident move**, with warmth delivered by **bold on-point illustration, real photography, and occasional colour blocks — on the clean base, never via warm surfaces.** This reinforces the (b) surface decision and pairs with the Designer's Taste in [`concept.md`](concept.md).

### Notion — clean grid, playful illustration twist
- **Link:** https://styles.refero.design/style/2bf4c61f-de10-4614-ba1b-20c0453bd2a9 · Refero index equivalents: notion.com styles `c6c2363f-…`, `7c05f5bd-…`
- **Technique:** a disciplined monochrome grid — white content sections, oversized bold headlines, rounded cards, generous whitespace — that takes its *twist* from **playful vector mascots, colour-blob accents and orbital line motifs** layered on top. Personality from illustration, not from a coloured background.
- **Persona anxiety:** A2 (warmth at the handoff) while holding A1 (the clean grid still reads credible).

### Cofounder — clean white + warm hand-drawn illustration
- **Link:** https://refero.design/search?site_id[id][]=746 · cofounder.co · Refero site 746
- **Technique:** monochrome white + serif headings + **warm hand-drawn character / nature illustration** (the "Connie" mascot, a sunflower on the welcome screen) as the personality anchor, on a **single subtle accent** (yellow). Serious *and* warm at once — the Endel register the designer named in the Taste list.
- **Persona anxiety:** A2 + A3 (a friendly illustrated character makes the shared card feel human and approachable to a nervous sitter).

**Warmth strategy (decided):** PetPal's warmth comes from **bold, on-point illustration + real pet photography + occasional colour blocks**, all on the clean near-white base — *not* from warm surfaces. Colour blocks live in the **brand / illustration layer** (à la Kinhive & Notion); the functional UI keeps its **single pine action colour**, so Headspace's colour discipline still holds. This resolves the only tension: colour blocks are expression, not chrome.

---

## Committed direction for PetPal *(the concrete kit these choices produce)*

| Decision | Value | From | Fights |
|---|---|---|---|
| Surfaces | **base near-white `#faf8f4`** · **Warm Sand `#f8f3eb` = secondary surface** (section bands, panel behind cards) · white floating cards; breaks by background change, no dividers | August Health | A2 |
| Headline type | serif display that **carries the message** (Kinhive's cut) — **roman = clarity/credibility, italic = warmth**; e.g. the hero pairs upright "Credible enough for a vet." with italic "Warm enough to hand to a sitter." Roman section headings; clean **sans** body | August Health + Kinhive | A1 · A2 |
| Body-text colour | **warm near-black brown** (~`#321004`), not pure black/gray | house (warm ink) | A2 / A3 |
| Colour budget | **one action colour**; saturated hues only in small accents/illustrations; trust-green as *supporting accent, not a status colour* | Headspace | A4 |
| Card shape | **16px radius, floating** (soft shadow, no border) | August Health | A2 |
| Badge shape | **fully pill** (~9999px) | August Health | A1 |
| Emotional anchor | **the pet's real photo in a soft circular mask** | August Health + Airbnb | A2 / A3 |
| Warmth | **bold illustration + real photography + occasional colour blocks**, on the clean base — never warm surfaces; colour blocks stay in the brand/illustration layer, one pine action colour holds | Notion · Kinhive · Cofounder · Airbnb | A2 / A3 |
| Share screen | **explicit "who can see this" line** under the share options | Airbnb | A5 |
| Dossier | **avatar + label→value list + one `Edit`** | Aboard | A1 / A3 |

**Surface decision — resolved to (b):** the base is a **near-white `#faf8f4`** (Headspace's whisper-warm off-white register), with **Warm Sand `#f8f3eb` kept only as a secondary section surface** (August Health's own usage). Warmth is carried by pet **photography**, the **warm brown ink `#321004`**, and the **serif headline** — not by a cream ground. This keeps the direction faithful to August Health / Airbnb / Headspace (all near-white-based) and clears the Designer's-Taste anti-reference. See [`concept.md`](concept.md).

*Note: Refero "styles" are drawn from web marketing/product pages, so these set the visual **language** (colour, type, shape, imagery role); the three **screens** ground the product-UI patterns. The home-screen references Refero surfaced skewed to finance dashboards, so the home layout is anchored on the dossier + share patterns above rather than a weak direct match.*
