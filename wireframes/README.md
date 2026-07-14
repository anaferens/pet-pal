# PetPal — Interactive Wireframe Prototype

Mid-fidelity, clickable wireframes for the whole PetPal product — mobile **and** desktop in one page each. Every screen is reachable, every interactive element is wired, and there are **no dead ends** (see the guarantee at the bottom).

**Live:** [anaferens.github.io/pet-pal/wireframes/](https://anaferens.github.io/pet-pal/wireframes/My-Pets.html)
**Traces to:** [sitemap.md](../research/sitemap.md) (screens & jobs) · [flows.md](../research/flows.md) (user flows) · [ia.md](../research/ia.md) (unified tree) · [personas.md](../research/personas.md).

---

## How to use it

Every screen has:
- a **left sidebar** — the full screen catalog, a **Mobile / Desktop** toggle, and three **Persona flows**;
- a **state bar** at the top of the device — *Success / Empty / Loading / Error* for that screen;
- a **flow step tooltip** (only when entered through a persona flow) — a step counter, the task to do on this screen, and ‹ › to move through the journey.

### Persona flows (guided walkthroughs)

Pick one from the sidebar, or add `?flow=…` to any URL. In flow mode, in-page buttons keep you *inside* the journey, loading screens auto-advance, and the tooltip narrates each step.

| Flow (`?flow=`) | Persona | Path |
|---|---|---|
| **`owner`** — Pet owner (Ana) | ⭐ Organised Owner | My Pets → Miso's dossier → Health & jabs → Documents → Personality & care → Share a pet → What's due |
| **`setup`** — New pet setup (full journey) | ⭐ Organised Owner, first run | Empty state → Set up a pet → *(Add photo)* → new-pet dossier → **+ Add info** → Health, Documents, Insurance, Personality, Vet, Emergency → Share → Sitter view *(13 steps)* |
| **`sitter`** — Pet sitter (recipient) | ◦ Receiving Caregiver | Shared pet view → Emergency & what I'm allowed to do |

---

## Screen catalog

Each base screen also has **Empty / Loading / Error** variants (`*-empty.html`, `*-loading.html`, `*-error.html`) where the flow needs them. **★ = new in v2** (added while building the interactive prototype — see [sitemap.md §"Screens realized in the interactive wireframes"](../research/sitemap.md)).

**Owner — pets & dossier**
- `My-Pets.html` — pet list (Miso + Cheetah); each card opens *that* pet's dossier.
- `Set-up-a-pet.html` — create a pet (name, species, breed, sex, microchip, photo).
- ★ `Upload-photo.html` — **Add photo** (take photo / choose from library); reused by *Edit pet identity*.
- `home-success.html` — populated **Pet dossier** (multi-pet, with switcher).
- ★ `home-success-single.html` — **single-pet dossier** (no switcher — the 0-tap auto-land case).
- `home-success-cheetah.html` — the second pet's dossier (switcher target).
- ★ `home-new.html` — **brand-new pet dossier** empty state: encouraging copy + **"+ Add info"** → *"What do you want to add?"* section-picker modal.
- `Edit-pet.html` — edit identity & lifecycle (photo, microchip, archive/delete).

**Owner — dossier sections**
- `Health-and-jabs.html` — vaccinations + health records; floating **+** (Add vaccine / Add health record); each row edits *its own* entry.
- `Documents-and-passport.html` — documents; each opens its own **Document view**.
- ★ `Document-view.html` — view / download / re-share / replace one stored document.
- `Insurance.html` — policy details + policy document.
- `Personality-and-care.html` — care notes (food, temperament, not-friendly-with, behaviour, routines, special); each note edits *its own* entry.
- `Vet-and-appointments.html` — vet clinic + upcoming/past appointments.
- `Emergency-info.html` — vet contact, meds, conditions, emergency contacts.

**Owner — add / edit records**
- `Add-record.html` — generic add form; **record type pre-selected** from the launching card (documents / insurance / vet).
- ★ `Add-health-record.html` — typed *Add health record* variant.
- `Add-care-note.html` — add a care note; **category pre-selected** (e.g. Behaviour).
- ★ `Edit-health-record.html` — **edit an existing** record, pre-filled + delete (per-record via `?rec=`).
- `Edit-care-note.html` — edit an existing care note, pre-filled (per-note via `?note=`).

**Owner — reminders & sharing**
- `Whats-due.html` — cross-pet reminders (vaccinations, renewals, appointments).
- `Share-a-pet.html` — scope + role + link/QR (QR is a centered modal).
- `Who-has-access.html` — manage grants; each **Edit/Revoke** opens *that* grant.
- `Edit-access-grant.html` — edit/revoke one grant (per-person via `?person=`).
- `Emergency-auth-setup.html` — emergency authorization (deep action).

**Recipient (no account)**
- `Shared-pet-view.html` — the sitter's read-only projection of the dossier.
- `Emergency-allowed.html` — emergency contacts, vet, and what the sitter may do.

---

## Prototype mechanics

- **Context-carried pre-selection.** Add/Edit forms and detail pages read a URL param and pre-fill accordingly — `?type=` (record type), `?cat=` / `?note=` (care-note category / which note), `?doc=` (which document), `?rec=` (which record), `?person=` (which grant). Clicking "Edit" on *Annual checkup* opens *Annual checkup*, not a blank form.
- **One add affordance.** A floating **+** action button on every dossier section (expands on Health & jabs) — replacing the old, inconsistent header "Add/Upload/Edit" text buttons.
- **State-truthful setup.** During *new pet setup*, each section shows what a brand-new pet actually has: its **empty** state, then after the first entry a **first-run** view with **only that one entry** — never the fully-populated demo. Realized as `*-firstrun.html` for Health & jabs, Documents, Personality, Vet, and Emergency (Insurance already shows a single policy).
- **State variants** for every screen the flows touch (Empty / Loading / Error), each with a recovery path (retry / back-to-dossier / show owner contact).
- **Responsive.** One file renders both mobile and desktop; toggle in the sidebar.

## No-dead-ends guarantee

The prototype is checked by four repeatable audits (scripts kept alongside the build):
1. **Structural** — no button/anchor without an action, no broken file links (both mobile & desktop).
2. **Semantic** — no set of distinct list items collapsing to one hardcoded destination.
3. **Entity match** — a link's label matches where it goes (no "Cheetah → Miso").
4. **Inert controls** — every interactive-looking element (toggles, scope pickers, chips) actually responds.

All four currently pass at **zero findings**.
