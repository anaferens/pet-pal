# PetPal — User Flows

Mermaid `flowchart TD`. Every `["screen"]` node exists in [sitemap.md](sitemap.md). One new node — **Add / update a record** — was introduced by these flows and is in the sitemap with its job.

> **Revised after the [critique](sitemap-critique.md):** all 8 terminal dead ends are now **recovery branches** (retry / offline cache / back-to-dossier / re-share / show-owner-contact), and the missing **loading / empty / error** states were added (My Pets fetch, dossier open, brand-new-pet empty sections, share-link create, shared-view load).

**Shape legend**
- `["Screen"]` — a screen (named from sitemap.md)
- `{"Question?"}` — decision point
- `("Loading / Empty / …")` — a **state**, not a screen
- `(["Success / Partial …"])` — an ending

**Colour legend**
- 🟦 **blue** — screen · ⬜ decision (default diamond)
- 🟨 **amber** — loading / empty / recovery state
- 🟥 **red** — error state
- 🟩 **green** — success ending (happy path)
- 🟧 **orange** — *partial* ending: recovered, not stuck (no dead ends remain)

---

## Main job — keep everything in one trusted place: consult & pass on
*Primary persona: Organised Owner.*

```mermaid
flowchart TD
  Start("Open app") --> PetsLoad("Loading: fetching pets")
  PetsLoad --> Qp{"Pets loaded?"}
  Qp -->|no| PetsErr("Error: could not load pets")
  PetsErr -->|retry| PetsLoad
  Qp -->|yes| Pets["My Pets"]
  Pets --> Q1{"Any pets yet?"}
  Q1 -->|no| EmptyPets("Empty: no pets yet")
  EmptyPets --> Setup["Set up a pet"]
  Q1 -->|yes| DossLoad("Loading: opening dossier")
  Setup --> SaveLoad("Loading: saving pet")
  SaveLoad --> Q2{"Saved?"}
  Q2 -->|no| SaveErr("Error: could not save")
  SaveErr -->|retry| Setup
  Q2 -->|yes| DossLoad
  DossLoad --> Qd{"Dossier opened?"}
  Qd -->|no| DossErr("Error: could not open dossier")
  DossErr -->|retry| DossLoad
  Qd -->|yes| Dossier["Pet dossier"]
  Dossier --> Q3{"Everything captured and current?"}
  Q3 -->|no| Health["Health & jabs"]
  Health --> Qe{"Any records yet?"}
  Qe -->|no| EmptySec("Empty: no records yet, add the first")
  EmptySec --> AddRec["Add / update a record"]
  Qe -->|yes| AddRec
  AddRec --> RecLoad("Loading: saving record")
  RecLoad --> Q4{"Saved?"}
  Q4 -->|no| RecErr("Error: save failed")
  RecErr -->|retry| AddRec
  Q4 -->|yes| Dossier
  Q3 -->|yes| Q5{"Pass it on now?"}
  Q5 -->|no| DoneConsult(["Success: record consulted and up to date"])
  Q5 -->|yes| Share["Share a pet"]
  Share --> Q6{"Recipient and scope set?"}
  Q6 -->|no| Share
  Q6 -->|yes| LinkLoad("Loading: creating link")
  LinkLoad --> Q7{"Link created?"}
  Q7 -->|no| LinkErr("Error: could not create link")
  LinkErr -->|retry| LinkLoad
  LinkErr -->|save and try later| Dossier
  Q7 -->|yes| DoneShare(["Success: handoff sent, consult and pass on complete"])

  classDef screen fill:#e7f5ff,stroke:#1971c2,color:#0b3d66;
  classDef state fill:#fff3bf,stroke:#f08c00,color:#663c00;
  classDef error fill:#ffe3e3,stroke:#e03131,color:#7a1212;
  classDef success fill:#d3f9d8,stroke:#2f9e44,color:#14532d;
  classDef soft fill:#ffe8cc,stroke:#e8590c,color:#7a3000;
  classDef start fill:#f1f3f5,stroke:#868e96,color:#343a40;
  class Start start;
  class Pets,Setup,Dossier,Health,AddRec,Share screen;
  class PetsLoad,EmptyPets,DossLoad,SaveLoad,EmptySec,RecLoad,LinkLoad state;
  class PetsErr,DossErr,SaveErr,RecErr,LinkErr error;
  class DoneConsult,DoneShare success;
```

---

## New-pet setup — the full onboarding journey *(realized in the interactive prototype)*
*Primary persona: Organised Owner (embodied as **Ana** in the prototype). The **"New pet setup (full journey)"** persona-flow — a first-run owner going from an empty account to a filled dossier that's ready to share.*

> This flow is the concrete, end-to-end onboarding path built in the [wireframes](../wireframes/) (`?flow=setup`). It expands the Main-job "Set up a pet" branch into every section, and introduces four wireframe-realized screens: **Add photo** (`Upload-photo.html`), the **brand-new-pet dossier empty state** with its **"Add info" section-picker** (`home-new.html`), **Edit an existing record** (`Edit-health-record.html` / `Edit-care-note.html`), and **Document view** (`Document-view.html`). No dead ends — every add opens a pre-filled form, every form returns to the dossier.

```mermaid
flowchart TD
  Start("Open app - first run") --> PetsLoad("Loading: fetching pets")
  PetsLoad --> EmptyPets("Empty: no pets yet")
  EmptyPets -->|+ Add your first pet| Setup["Set up a pet"]
  Setup --> Qphoto{"Add a photo?"}
  Qphoto -->|yes| Photo["Add photo"]
  Photo -->|take / choose| Setup
  Qphoto -->|skip| SaveLoad("Loading: saving pet")
  Setup --> SaveLoad
  SaveLoad --> Q1{"Saved?"}
  Q1 -->|no| SaveErr("Error: could not save")
  SaveErr -->|retry| Setup
  Q1 -->|yes| NewDoss["Pet dossier - brand new, empty"]
  NewDoss --> AddInfo{"+ Add info: what to add?"}
  AddInfo -->|Health & jabs| HealthEmpty["Health & jabs - empty, brand-new pet"]
  HealthEmpty -->|+ Add first vaccine| AddHealth["Add a vaccine / health record"]
  AddHealth --> HealthSave("Loading: saving")
  HealthSave --> Qh{"Saved?"}
  Qh -->|no| RecErr("Error: save failed")
  Qh -->|yes| HealthOne["Health & jabs - just the one vaccine (first-run)"]
  HealthOne --> Filled
  AddInfo -->|Personality & care| PersEmpty["Personality & care - empty"]
  PersEmpty -->|+ Add first note| AddCare["Add care note - behaviour"]
  AddCare --> RecLoad("Loading: saving")
  RecLoad --> Q2{"Saved?"}
  Q2 -->|no| RecErr
  Q2 -->|yes| PersOne["Personality & care - just the one note (first-run)"]
  PersOne --> Filled
  RecErr -->|retry| AddInfo
  AddInfo -->|Documents & passport| DocOne["Documents - one document (first-run)"]
  AddInfo -->|Insurance| InsOne["Insurance - one policy"]
  AddInfo -->|Vet & appointments| VetOne["Vet - vet clinic + one appointment (first-run)"]
  AddInfo -->|Emergency info & authorisation| EmergOne["Emergency - vet + contact; meds/conditions pending (first-run)"]
  DocOne --> Filled
  InsOne --> Filled
  VetOne --> Filled
  EmergOne --> Filled
  Filled["Pet dossier - sections filling up"]
  Filled --> Q3{"Reviewing existing entries?"}
  Q3 -->|edit a record| EditRec["Edit an existing record - pre-filled"]
  EditRec --> Filled
  Q3 -->|open a document| DocView["Document view"]
  DocView --> Filled
  Filled --> Q4{"Enough captured to hand off?"}
  Q4 -->|no, add more| AddInfo
  Q4 -->|yes| Share["Share a pet"]
  Share --> Q5{"Scope, role and link set?"}
  Q5 -->|no| Share
  Q5 -->|yes| LinkLoad("Loading: creating link")
  LinkLoad --> Q6{"Link created?"}
  Q6 -->|no| LinkErr("Error: could not create link")
  LinkErr -->|retry| LinkLoad
  Q6 -->|yes| Sitter["Shared pet view - what the sitter sees"]
  Sitter --> Done(["Success: new pet set up, dossier filled and shared"])

  classDef screen fill:#e7f5ff,stroke:#1971c2,color:#0b3d66;
  classDef state fill:#fff3bf,stroke:#f08c00,color:#663c00;
  classDef error fill:#ffe3e3,stroke:#e03131,color:#7a1212;
  classDef success fill:#d3f9d8,stroke:#2f9e44,color:#14532d;
  classDef start fill:#f1f3f5,stroke:#868e96,color:#343a40;
  class Start start;
  class Setup,Photo,NewDoss,HealthEmpty,AddHealth,HealthOne,PersEmpty,AddCare,PersOne,DocOne,InsOne,VetOne,EmergOne,Filled,EditRec,DocView,Share,Sitter screen;
  class PetsLoad,EmptyPets,SaveLoad,HealthSave,RecLoad,LinkLoad state;
  class SaveErr,RecErr,LinkErr error;
  class Done success;
```

**What this flow added to the product picture**
- **Add photo** is its own step (take photo / choose from library), reachable from both *Set up a pet* and *Edit pet identity* — no longer an inert avatar.
- The **brand-new dossier** has a dedicated empty state (encouraging copy + a single **"+ Add info"** call-to-action) instead of dropping the owner into a dossier that looks "broken but empty."
- **State-truthful sections (all of them).** A section a brand-new pet hasn't filled shows its **empty** state, and immediately after adding the first entry it shows **only that entry** — never the fully-populated demo. Realized for every dossier section with its own `-firstrun` screen:
  - **Health & jabs** — `-empty` → add vaccine → `Health-and-jabs-firstrun.html` (one vaccine, no conditions card, empty health-records list).
  - **Documents & passport** — `Documents-and-passport-firstrun.html` (just the EU pet passport).
  - **Insurance** — `Insurance.html` already shows exactly one policy, so it *is* the first-run state.
  - **Personality & care** — `-empty` → add note → `Personality-and-care-firstrun.html` (one note).
  - **Vet & appointments** — `Vet-and-appointments-firstrun.html` (vet clinic + one upcoming appointment, no past history).
  - **Emergency info** — `Emergency-info-firstrun.html` (vet + one emergency contact; meds & conditions show "None recorded yet — fills in from Health & jabs").
- **"What do you want to add?"** is a section-picker modal — each of the six cards opens the matching form with the **section pre-selected** (e.g. Personality → *Behaviour* pre-chosen), so the owner never re-picks what they just chose.
- Every list item (document, jab, health record, appointment, care note, access grant) opens its **own pre-filled Edit/View screen** — "Edit" means edit *that* entry, not a blank Add form.

---

## R2 — make a stranger understand my pet fast
*Owner prepares and shares (Organised Owner) → carer reads it (Receiving Caregiver).*

```mermaid
flowchart TD
  Dossier["Pet dossier"] --> Care["Personality & care"]
  Care --> Q1{"Care info complete? food, behaviour, not-friendly-with, vet"}
  Q1 -->|no| AddRec["Add / update a record"]
  AddRec --> Care
  Q1 -->|yes| Share["Share a pet"]
  Share --> Q2{"Carer scope and link set?"}
  Q2 -->|no| Share
  Q2 -->|yes| ShareLoad("Loading: creating link")
  ShareLoad --> Q2b{"Link created?"}
  Q2b -->|no| ShareErr("Error: could not create link")
  ShareErr -->|retry| ShareLoad
  Q2b -->|yes| Sent(["Success - owner: link sent"])
  Sent --> Open("Recipient opens link")
  Open --> Load("Loading: opening shared view")
  Load --> Q3{"Link valid and active?"}
  Q3 -->|no| LinkErr("Error: link expired or revoked")
  LinkErr --> Reissue("Owner re-shares a fresh link")
  Reissue --> Open
  Q3 -->|yes| Q3b{"View loaded ok?"}
  Q3b -->|no| ViewErr("Error: could not load shared view")
  ViewErr -->|retry| Load
  Q3b -->|yes| SharedView["Shared pet view"]
  SharedView --> Q4{"Contains what the carer needs?"}
  Q4 -->|yes| Understood(["Success: carer understands the pet in seconds"])
  Q4 -->|no| Empty("Empty: owner filled little")
  Empty --> Q5{"Emergency info present?"}
  Q5 -->|yes| Emerg["Emergency & what I'm allowed to do"]
  Emerg --> Understood
  Q5 -->|no| OwnerContact("Shown: owner contact to ask for details")
  OwnerContact --> Soft1(["Partial: carer has owner contact, not flying blind"])

  classDef screen fill:#e7f5ff,stroke:#1971c2,color:#0b3d66;
  classDef state fill:#fff3bf,stroke:#f08c00,color:#663c00;
  classDef error fill:#ffe3e3,stroke:#e03131,color:#7a1212;
  classDef success fill:#d3f9d8,stroke:#2f9e44,color:#14532d;
  classDef soft fill:#ffe8cc,stroke:#e8590c,color:#7a3000;
  classDef start fill:#f1f3f5,stroke:#868e96,color:#343a40;
  class Open start;
  class Dossier,Care,AddRec,Share,SharedView,Emerg screen;
  class ShareLoad,Load,Empty,Reissue,OwnerContact state;
  class ShareErr,LinkErr,ViewErr error;
  class Sent,Understood success;
  class Soft1 soft;
```

---

## R1 — stay ahead of what's due
*Primary persona: Organised Owner.*

```mermaid
flowchart TD
  Whats["What's due"] --> Load("Loading: fetching reminders")
  Load --> Q0{"Loaded ok?"}
  Q0 -->|no| Err("Error: could not load reminders")
  Err -->|retry| Load
  Err -->|offline| Cached("Showing last-saved reminders")
  Cached --> Q1
  Q0 -->|yes| Q1{"Any reminders due?"}
  Q1 -->|no| EmptyDone(["Success: nothing due, nothing slipping"])
  Q1 -->|yes| Q2{"Which type?"}
  Q2 -->|vaccination| Health["Health & jabs"]
  Q2 -->|insurance| Insurance["Insurance"]
  Q2 -->|appointment| Vet["Vet & appointments"]
  Health --> Q3{"Info current? when last updated and source"}
  Insurance --> Q3
  Vet --> Q3
  Q3 -->|yes| Acted(["Success: acted in time, marked done or booked"])
  Q3 -->|no| AddRec["Add / update a record"]
  AddRec --> SaveLoad("Loading: saving")
  SaveLoad --> Q4{"Saved?"}
  Q4 -->|no| SaveErr("Error: save failed")
  SaveErr -->|retry| AddRec
  SaveErr -->|keep in list| Whats
  Q4 -->|yes| Acted

  classDef screen fill:#e7f5ff,stroke:#1971c2,color:#0b3d66;
  classDef state fill:#fff3bf,stroke:#f08c00,color:#663c00;
  classDef error fill:#ffe3e3,stroke:#e03131,color:#7a1212;
  classDef success fill:#d3f9d8,stroke:#2f9e44,color:#14532d;
  classDef soft fill:#ffe8cc,stroke:#e8590c,color:#7a3000;
  class Whats,Health,Insurance,Vet,AddRec screen;
  class Load,SaveLoad,Cached state;
  class Err,SaveErr error;
  class EmptyDone,Acted success;
```

---

## R5 — make a good call in a worrying moment
*Secondary persona: Worried-at-the-Wrong-Moment Owner. PetPal serves the **information**, not the consultation. Uses the 1-tap emergency shortcut from home.*

```mermaid
flowchart TD
  Start("Open app - worried, clinic closed") --> Pets["My Pets"]
  Pets -->|emergency shortcut, 1 tap| Emerg["Emergency info & authorization"]
  Emerg --> Load("Loading: opening critical info")
  Load --> Q1{"Info loaded?"}
  Q1 -->|no| Err("Error: could not load")
  Err -->|retry| Load
  Err -->|offline| Cached("Showing cached critical info")
  Cached --> Q2
  Q1 -->|yes| Q2{"Critical info present? meds, conditions, vet contact"}
  Q2 -->|yes| Q3{"Is it current? last updated and source"}
  Q2 -->|no| Fallback("Shown: vet contact, owner emergency contact, call your vet")
  Fallback --> Soft1(["Partial: has a number to call"])
  Q3 -->|yes| Acted(["Success: has the facts to call the vet and decide"])
  Q3 -->|no| Source("Shown: last updated and source, confirm with owner or vet")
  Source --> Soft2(["Partial: can verify, not stuck"])

  classDef screen fill:#e7f5ff,stroke:#1971c2,color:#0b3d66;
  classDef state fill:#fff3bf,stroke:#f08c00,color:#663c00;
  classDef error fill:#ffe3e3,stroke:#e03131,color:#7a1212;
  classDef success fill:#d3f9d8,stroke:#2f9e44,color:#14532d;
  classDef soft fill:#ffe8cc,stroke:#e8590c,color:#7a3000;
  classDef start fill:#f1f3f5,stroke:#868e96,color:#343a40;
  class Start start;
  class Pets,Emerg screen;
  class Load,Cached,Fallback,Source state;
  class Err error;
  class Acted success;
  class Soft1,Soft2 soft;
```

---

### Screen nodes used (all in sitemap.md)
My Pets · Set up a pet · Pet dossier · Health & jabs · Personality & care · Insurance · Vet & appointments · Emergency info & authorization · What's due · Share a pet · Shared pet view · Emergency & what I'm allowed to do · **Add / update a record**.
*(Recovery nodes — re-share, show owner contact, offline cache, retry — are **states of existing screens**, not new screens.)*

**New screen nodes introduced by the interactive prototype** (all in [wireframes/](../wireframes/), added to [sitemap.md](sitemap.md) §"Screens realized in the interactive wireframes"):
**Add photo** (`Upload-photo.html`) · **Pet dossier — brand-new empty state / "Add info" hub** (`home-new.html`) · **Add health record** (`Add-health-record.html`, a typed variant of *Add / update a record*) · **Section first-run states** — the one-entry view of each section right after a new pet's first addition: `Health-and-jabs-firstrun.html` (one vaccine, no conditions card), `Documents-and-passport-firstrun.html` (one document), `Personality-and-care-firstrun.html` (one note), `Vet-and-appointments-firstrun.html` (vet + one appointment), `Emergency-info-firstrun.html` (vet + contact, meds/conditions pending) · **Edit an existing record** (`Edit-health-record.html`, `Edit-care-note.html`) · **Document view** (`Document-view.html`) · **Pet dossier — single-pet auto-land** (`home-success-single.html`, realizes the single-pet 0-tap rule).
*("Add info" section-picker is a modal on the brand-new dossier, not a separate page.)*
