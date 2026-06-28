# PetPal — User Flows

Mermaid `flowchart TD`. Every `["screen"]` node exists in [sitemap.md](sitemap.md). One new node — **Add / update a record** — was introduced by these flows and has been added to the sitemap with its job.

**Shape legend**
- `["Screen"]` — a screen (named from sitemap.md)
- `{"Question?"}` — decision point
- `("Loading / Empty / Error …")` — a **state**, not a screen
- `(["Success / Dead end …"])` — an ending (success or stuck)

**Colour legend**
- 🟦 **blue** — screen · ⬜ decision (default diamond)
- 🟨 **amber** — loading / empty state
- 🟥 **red** — error state
- 🟩 **green** — success ending (happy path)
- 🟫 **dark red** — dead end (person gets stuck)

---

## Main job — keep everything in one trusted place: consult & pass on
*Primary persona: Organised Owner.*

```mermaid
flowchart TD
  Start("Open app") --> Pets["My Pets"]
  Pets --> Q1{"Any pets yet?"}
  Q1 -->|no| EmptyPets("Empty: no pets yet")
  EmptyPets --> Setup["Set up a pet"]
  Q1 -->|yes| Dossier["Pet dossier"]
  Setup --> SaveLoad("Loading: saving pet")
  SaveLoad --> Q2{"Saved?"}
  Q2 -->|no| SaveErr("Error: could not save")
  SaveErr --> Setup
  Q2 -->|yes| Dossier
  Dossier --> Q3{"Is everything captured and current?"}
  Q3 -->|no| Health["Health & jabs"]
  Health --> AddRec["Add / update a record"]
  AddRec --> RecLoad("Loading: saving record")
  RecLoad --> Q4{"Saved?"}
  Q4 -->|no| RecErr("Error: save failed")
  RecErr --> AddRec
  Q4 -->|yes| Dossier
  Q3 -->|yes| Q5{"Pass it on now?"}
  Q5 -->|no| DoneConsult(["Success: trusted record consulted and up to date"])
  Q5 -->|yes| Share["Share a pet"]
  Share --> Q6{"Recipient and scope set?"}
  Q6 -->|no| Share
  Q6 -->|yes| LinkLoad("Loading: creating link")
  LinkLoad --> Q7{"Link created?"}
  Q7 -->|no| LinkErr("Error: could not create link")
  LinkErr --> DeadShare(["Dead end: cannot pass on, falls back to chat and photos"])
  Q7 -->|yes| DoneShare(["Success: handoff sent, consult and pass on complete"])

  classDef screen fill:#e7f5ff,stroke:#1971c2,color:#0b3d66;
  classDef state fill:#fff3bf,stroke:#f08c00,color:#663c00;
  classDef error fill:#ffe3e3,stroke:#e03131,color:#7a1212;
  classDef success fill:#d3f9d8,stroke:#2f9e44,color:#14532d;
  classDef deadend fill:#ffc9c9,stroke:#c92a2a,color:#6a1212;
  classDef start fill:#f1f3f5,stroke:#868e96,color:#343a40;
  class Start start;
  class Pets,Setup,Dossier,Health,AddRec,Share screen;
  class EmptyPets,SaveLoad,RecLoad,LinkLoad state;
  class SaveErr,RecErr,LinkErr error;
  class DoneConsult,DoneShare success;
  class DeadShare deadend;
```

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
  Q2 -->|yes| Sent(["Success - owner: link sent"])
  Sent --> Open("Recipient opens link")
  Open --> Load("Loading: opening shared view")
  Load --> Q3{"Link valid and active?"}
  Q3 -->|no| LinkErr("Error: link expired or revoked")
  LinkErr --> DeadLink(["Dead end: carer back to texting the owner"])
  Q3 -->|yes| SharedView["Shared pet view"]
  SharedView --> Q4{"Does it contain what the carer needs?"}
  Q4 -->|yes| Understood(["Success: carer understands the pet in seconds"])
  Q4 -->|no| Empty("Empty: owner filled little, flying blind")
  Empty --> Q5{"Emergency info present?"}
  Q5 -->|no| DeadGap(["Dead end: carer cannot act confidently"])
  Q5 -->|yes| Emerg["Emergency & what I'm allowed to do"]
  Emerg --> Understood

  classDef screen fill:#e7f5ff,stroke:#1971c2,color:#0b3d66;
  classDef state fill:#fff3bf,stroke:#f08c00,color:#663c00;
  classDef error fill:#ffe3e3,stroke:#e03131,color:#7a1212;
  classDef success fill:#d3f9d8,stroke:#2f9e44,color:#14532d;
  classDef deadend fill:#ffc9c9,stroke:#c92a2a,color:#6a1212;
  classDef start fill:#f1f3f5,stroke:#868e96,color:#343a40;
  class Open start;
  class Dossier,Care,AddRec,Share,SharedView,Emerg screen;
  class Load,Empty state;
  class LinkErr error;
  class Sent,Understood success;
  class DeadLink,DeadGap deadend;
```

---

## R1 — stay ahead of what's due
*Primary persona: Organised Owner.*

```mermaid
flowchart TD
  Whats["What's due"] --> Load("Loading: fetching reminders")
  Load --> Q0{"Loaded ok?"}
  Q0 -->|no| Err("Error: could not load reminders")
  Err --> DeadLoad(["Dead end: cannot see what's due, may miss a deadline"])
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
  SaveErr --> DeadSave(["Dead end: due item stays unresolved"])
  Q4 -->|yes| Acted

  classDef screen fill:#e7f5ff,stroke:#1971c2,color:#0b3d66;
  classDef state fill:#fff3bf,stroke:#f08c00,color:#663c00;
  classDef error fill:#ffe3e3,stroke:#e03131,color:#7a1212;
  classDef success fill:#d3f9d8,stroke:#2f9e44,color:#14532d;
  classDef deadend fill:#ffc9c9,stroke:#c92a2a,color:#6a1212;
  class Whats,Health,Insurance,Vet,AddRec screen;
  class Load,SaveLoad state;
  class Err,SaveErr error;
  class EmptyDone,Acted success;
  class DeadLoad,DeadSave deadend;
```

---

## R5 — make a good call in a worrying moment
*Secondary persona: Worried-at-the-Wrong-Moment Owner. PetPal serves the **information**, not the consultation.*

```mermaid
flowchart TD
  Start("Open app - worried, clinic closed") --> Pets["My Pets"]
  Pets --> Dossier["Pet dossier"]
  Dossier --> Emerg["Emergency info & authorization"]
  Emerg --> Load("Loading: opening critical info")
  Load --> Q1{"Info loaded?"}
  Q1 -->|no| Err("Error: could not load")
  Err --> DeadErr(["Dead end: the scramble PetPal was meant to prevent"])
  Q1 -->|yes| Q2{"Critical info present? meds, conditions, vet contact"}
  Q2 -->|no| Empty("Empty: fields never filled in")
  Empty --> DeadEmpty(["Dead end: no facts to decide on"])
  Q2 -->|yes| Q3{"Is it current? last updated and source"}
  Q3 -->|yes| Acted(["Success: has the facts to call the vet and decide"])
  Q3 -->|no| Stale("Empty: shown info looks stale")
  Stale --> Q4{"Act on it anyway?"}
  Q4 -->|no| DeadStale(["Dead end: unsure, stuck"])
  Q4 -->|yes| Acted

  classDef screen fill:#e7f5ff,stroke:#1971c2,color:#0b3d66;
  classDef state fill:#fff3bf,stroke:#f08c00,color:#663c00;
  classDef error fill:#ffe3e3,stroke:#e03131,color:#7a1212;
  classDef success fill:#d3f9d8,stroke:#2f9e44,color:#14532d;
  classDef deadend fill:#ffc9c9,stroke:#c92a2a,color:#6a1212;
  classDef start fill:#f1f3f5,stroke:#868e96,color:#343a40;
  class Start start;
  class Pets,Dossier,Emerg screen;
  class Load,Empty,Stale state;
  class Err error;
  class Acted success;
  class DeadErr,DeadEmpty,DeadStale deadend;
```

---

### Screen nodes used (all in sitemap.md)
My Pets · Set up a pet · Pet dossier · Health & jabs · Personality & care · Insurance · Vet & appointments · Emergency info & authorization · What's due · Share a pet · Shared pet view · Emergency & what I'm allowed to do · **Add / update a record** *(added to sitemap by these flows)*.
