# PetPal — Wireframe conventions

Rules every wireframe screen must follow. Read this before drawing anything.

---

## 1. Level of detail

Wireframes show **structure, hierarchy, and zones only**.

| Include | Exclude |
|---|---|
| Layout grid and content zones | Brand colours, gradients, shadows |
| Grey fills for placeholder areas (photos, thumbnails, illustrations) | Real images or icons |
| Text hierarchy (heading vs body vs caption — via size and weight) | Typeface selection, font pairing |
| Interactive element shapes (buttons, inputs, toggles, cards) | Final border-radius, elevation, micro-interactions |
| Status indicators as labelled text ("Up to date", "Overdue") | Colour-coded badges (green/amber/red) |
| Navigation bar with labelled items | Icon design, active-state colour |

**Greyscale palette (CSS variables used across all wireframes):**

```
--wf-bg:       #ffffff       page background
--wf-surface:  #f5f5f5       card / section background
--wf-border:   #e0e0e0       borders, dividers
--wf-text:     #1a1a1a       primary text
--wf-muted:    #757575       secondary / helper text
--wf-placeholder: #d0d0d0   image placeholders, skeleton blocks
--wf-input-bg: #fafafa       form input background
--wf-btn:      #333333       primary button fill
--wf-btn-text: #ffffff       primary button text
--wf-btn-sec:  transparent   secondary button (outline only)
```

---

## 2. Viewport

**Mobile-first.** All wireframes are designed for a **375 × 812** viewport (iPhone-class). Desktop adaptation is a later phase.

```css
max-width: 375px;
min-height: 100vh;
margin: 0 auto;
```

---

## 3. Markup

Semantic HTML — not nested `<div>` soup. Every wireframe must use the elements below for their intended purpose:

| Element | Use in wireframes |
|---|---|
| `<header>` | Screen title bar (pet name, back button, screen title) |
| `<nav>` | Global bottom navigation (Pets · What's due · Share) |
| `<main>` | Primary content area of the screen |
| `<section>` | A distinct content group (e.g. "Conditions & meds", "Vaccination history") |
| `<article>` | A self-contained content card (pet card, record entry, document card) |
| `<form>` | Any input group (Set up a pet, Add a record, Share form) |
| `<fieldset>` + `<legend>` | Grouped form fields (e.g. "Pet identity", "Vaccination details") |
| `<button>` | All tappable actions (Save, Retry, Add, Share) |
| `<input>`, `<select>`, `<textarea>` | Form controls with `type`, `placeholder`, and `required` where applicable |
| `<ul>` / `<ol>` | Lists of records, documents, appointments |
| `<figure>` | Image/photo placeholder zones |
| `<footer>` | Screen-level footer content if any (not the global nav) |

**Accessibility baseline:**
- Every `<img>` and `<figure>` gets an `alt` attribute (even if the content is a grey placeholder: `alt="Pet photo placeholder"`).
- Every form `<input>` has a visible `<label>`.
- Buttons have descriptive text, not just icons.

---

## 4. Text content

**Real, domain-specific text everywhere.** No "Lorem ipsum", no "Title here", no "Description text."

| Where | Write |
|---|---|
| Screen titles | Exact names from sitemap.md: "My Pets", "Pet dossier", "Health & jabs", etc. |
| Pet names | Use "Luna" (dog) and "Miso" (cat) as sample pets throughout |
| Section labels | Real labels: "Vaccinations", "Conditions & current meds", "Favourite food & treats" |
| Empty-state messages | Actionable copy: "No vaccinations yet. Add your first to stay ahead of what's due." |
| Error messages | Specific: "Couldn't load your pet's records. Check your connection and try again." |
| Button labels | Verb-first: "Add vaccination", "Upload document", "Share Luna's info", "Try again" |
| Form placeholders | Realistic examples: "e.g. Rabies", "e.g. Lassie Pet Insurance", "e.g. Loves belly rubs" |
| Helper text | Domain-relevant: "Only name and species are required. You can add more later." |

---

## 5. Page structure (shared across all screens)

Every wireframe page has the same outer skeleton:

```
┌─────────────────────────┐
│  <header>               │  Screen title bar
│  Back · Title · Action  │  (contextual per screen)
├─────────────────────────┤
│                         │
│  <main>                 │  Screen content
│                         │  (scrollable)
│                         │
│                         │
├─────────────────────────┤
│  <nav>                  │  Global bottom nav
│  Pets · What's due ·    │  (3 items, always visible)
│  Share                  │
└─────────────────────────┘
```

**Header rules:**
- **My Pets:** title = "My Pets", no back button (root screen).
- **Pet dossier:** title = pet name ("Luna"), back button → My Pets (hidden if single-pet auto-land).
- **Dossier sections:** title = section name ("Health & jabs"), back button → Pet dossier. Pet identity strip below header (photo + name + species).
- **Add / update a record:** title = action ("Add vaccination", "Edit record"), back button → section. Cancel = back without saving.
- **Share a pet:** title = "Share [pet name]", back button → Pet dossier.
- **Set up a pet:** title = "Set up a pet", back button → My Pets (or close if first-run).

**Bottom nav rules:**
- 3 items: **Pets** · **What's due** · **Share**.
- Always visible on every screen except full-screen modals (Add / update a record).
- Active item is indicated by text weight (bold), not colour.
- "What's due" and "Share" are present in the nav but are step 08 screens — they navigate to placeholder/stub pages in this batch.

---

## 6. File naming

Base screen = the **success** state. State variants are separate files with a suffix.

**Pattern:** `wireframes/<Screen-name>.html` (kebab-case with capital first letter of each word)

| Screen | Success (base) | Empty | Loading | Error |
|---|---|---|---|---|
| My Pets | `My-Pets.html` | `My-Pets-empty.html` | `My-Pets-loading.html` | `My-Pets-error.html` |
| Set up a pet | `Set-up-a-pet.html` | — | `Set-up-a-pet-loading.html` | `Set-up-a-pet-error.html` |
| Pet dossier | `home-success.html` | `home-empty.html` | `home-loading.html` | `home-error.html` |
| Health & jabs | `Health-and-jabs.html` | `Health-and-jabs-empty.html` | `Health-and-jabs-loading.html` | `Health-and-jabs-error.html` |
| Documents & passport | `Documents-and-passport.html` | `Documents-and-passport-empty.html` | `Documents-and-passport-loading.html` | `Documents-and-passport-error.html` |
| Insurance | `Insurance.html` | `Insurance-empty.html` | `Insurance-loading.html` | `Insurance-error.html` |
| Personality & care | `Personality-and-care.html` | `Personality-and-care-empty.html` | `Personality-and-care-loading.html` | `Personality-and-care-error.html` |
| Vet & appointments | `Vet-and-appointments.html` | `Vet-and-appointments-empty.html` | `Vet-and-appointments-loading.html` | `Vet-and-appointments-error.html` |
| Add / update a record | `Add-record.html` | — | `Add-record-loading.html` | `Add-record-error.html` |
| Share a pet | `Share-a-pet.html` | — | `Share-a-pet-loading.html` | `Share-a-pet-error.html` |

**Total: 10 base + 7 empty + 10 loading + 10 error = 37 pages.**

---

## 7. State rules

Each state is a **separate HTML page** with the same structure but different content in `<main>`.

### Success (base page)
The primary state. Content is loaded, the screen is functional. **Wireframe this first** — all other states are derived from it.

### Empty (`-empty`)
The screen's primary content doesn't exist yet. Rules:
- Show the same `<header>` and `<nav>` as the success state.
- Replace `<main>` content with: a grey placeholder illustration zone (120×120 `<figure>`), a headline explaining the empty state, a body line with context, and a primary `<button>` CTA.
- The CTA navigates to the creation flow (e.g. "Add your first vaccination" → Add-record.html).
- Never show a blank screen. The empty state IS the onboarding for that section.

### Loading (`-loading`)
Data is being fetched or an action is being saved. Rules:
- **Fetch loading (opening a screen):** show the same `<header>` and `<nav>`. Replace content cards/lists with grey placeholder blocks (skeleton pattern). Use `<div>` with `--wf-placeholder` background, same dimensions as the real content. Label one block "Loading…" in muted text.
- **Save loading (submitting a form):** keep the form visible but disabled. The submit `<button>` shows "Saving…" and is disabled. No full-screen overlay.

### Error (`-error`)
A fetch or save failed. Rules:
- Show the same `<header>` and `<nav>`.
- Replace `<main>` content with: an error headline ("Something went wrong"), a body line with specific context ("Couldn't load Luna's health records. Check your connection and try again."), and a primary `<button>` "Try again" that retries the failed action.
- For save errors on forms: keep the form visible with all data preserved. Show an inline error banner above the submit button. The user taps "Try again" — they never re-enter data.
- **No dead ends.** Every error state must have at least one recovery action.

---

## 8. Component patterns

Reusable patterns that appear across multiple screens. Build them consistently.

### Pet identity strip
Used in: all dossier section headers.
```
┌──────────────────────────────┐
│ [photo]  Luna · Dog · Husky  │
└──────────────────────────────┘
```
Grey circle (40×40) for photo, pet name in bold, species and breed in muted text. Signals "you're looking at this pet" for multi-pet owners (Q8).

### Section card
Used in: Pet dossier (section overview).
```
┌──────────────────────────────┐
│ [icon zone]                  │
│ Health & jabs                │
│ 3 records · Updated 2 days  │
│ ago                          │
└──────────────────────────────┘
```
Grey square (24×24) for icon placeholder, section name in bold, fill status in muted text.

### Record entry
Used in: Health & jabs, Documents, Insurance, Vet & appointments.
```
┌──────────────────────────────┐
│ Rabies vaccination           │
│ 12 Mar 2026 · Up to date    │
│                    [Edit] →  │
└──────────────────────────────┘
```
Record name in bold, date + status in muted text, edit action aligned right.

### Empty-state block
Used in: every `-empty` page.
```
┌──────────────────────────────┐
│        [illustration]        │
│     120×120 grey zone        │
│                              │
│   No vaccinations yet        │
│   Add your first to stay     │
│   ahead of what's due.       │
│                              │
│   [ Add vaccination ]        │
└──────────────────────────────┘
```
Centred layout. Illustration placeholder, headline, body copy, CTA button.

### Error block
Used in: every `-error` page.
```
┌──────────────────────────────┐
│   Something went wrong       │
│   Couldn't load Luna's       │
│   records. Check your        │
│   connection and try again.  │
│                              │
│      [ Try again ]           │
└──────────────────────────────┘
```
Centred. Headline, contextual body, retry button.

### Form field
Used in: Set up a pet, Add / update a record, Share a pet.
```
  Label *
  ┌────────────────────────┐
  │ Placeholder text       │
  └────────────────────────┘
  Helper text in muted
```
Label above, input with placeholder, optional helper text below. Required fields marked with `*`. Error state: border changes to dark grey, error message replaces helper text.

---

## 9. What we leave for later

These are **not** part of wireframes and must not appear in any wireframe file:

- Brand colours (the dark palette from research pages)
- Typography (Inter or any specific font — wireframes use system font stack)
- Shadows, elevation, blur effects
- Real icons (use grey squares or text labels instead)
- Real images or illustrations (use grey placeholder zones)
- Animations, transitions, micro-interactions
- Final border-radius values
- Dark mode
- Desktop / tablet layouts

---

## 10. CSS approach

All wireframe pages share one inline `<style>` block using the CSS variables from section 1. No external stylesheet, no build step.

```css
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: -apple-system, BlinkMacSystemFont, sans-serif;
  max-width: 375px; min-height: 100vh; margin: 0 auto;
  background: var(--wf-bg); color: var(--wf-text);
  line-height: 1.5; -webkit-font-smoothing: antialiased;
}
```

Keep CSS minimal — only enough to establish zones, spacing, and hierarchy. If a style choice is about aesthetics rather than structure, leave it out.
