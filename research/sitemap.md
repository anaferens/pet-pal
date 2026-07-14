# PetPal — Sitemap

> Started as a pre-wireframe object model (Entities → Screens → Navigation → Traceability). **Now realized** as a clickable prototype in [wireframes/](../wireframes/); the wireframe-added screens are logged in §"Screens realized in the interactive wireframes (v2)" and folded into the traceability matrix (Sc22–Sc26). The Entities section below remains the object model behind the jobs.

## Entities

The main objects a person touches to complete the [jobs](jtbd.md). Rules:
- Every entity in the main list names the **job that creates the need** (codes from [jtbd.md](jtbd.md): Main, R1–R5, E1–E3, S1–S2).
- An object with **no job behind it → "Questionable"**, not the main list.
- `[?]` = the object is an **assumption** (the job doesn't strictly require it yet, or the supporting job is itself a hypothesis).
- Tags: 🔵 brief ([CLAUDE.md](../CLAUDE.md)) · 🟢 research-backed ([research.md](research.md)).
- **Nothing invented** that the jobs don't require.

---

### Main entities

**1. Owner account**
- *Parts:* person name, contact (email / phone), the set of pets they manage, the access-grants they've issued.
- *Job that needs it:* **Main** (someone has to own the "single trusted record"); **S1** (the owner is who grants others access).
- *Connected to:* **Pet** (1 owner → many pets, 🔵 CLAUDE.md:40); **Access grant** (issues them); receives **Reminders**.

**2. Pet**
- *Parts:* name, species (1 of 5: dog/cat/rabbit/guinea pig/bird), breed, sex `[?]`, date of birth / age, photo, microchip number.
- *Job that needs it:* **Main** — the anchor everything hangs off ("keep everything I know about *it*").
- *Connected to:* **Owner** (belongs to); **Pet dossier** (1 ↔ 1, the pet *is* the spine of its dossier); target of every **Access grant**.

**3. Pet dossier**
- *Parts:* the umbrella record for one pet — aggregates identity (→Pet), health records, documents, personality, reminders, vet contact. The thing that is "in one trusted place."
- *Job that needs it:* **Main** ("keep everything in one place"); **R3** (the accurate picture handed to a vet); **R2** (the source a carer view is drawn from).
- *Connected to:* **Pet** (1 ↔ 1); aggregates **Vaccination records, Health records, Documents, Insurance policies, Personality, Appointments, Vet clinic**; projected through **Access grants**.

**4. Vaccination record (jab)** — *"jabs history / state"*
- *Parts:* vaccine name/type, date given, valid-until / next-due date, administering vet `[?]`, proof file (photo/PDF). *Derived:* status (up-to-date / due / overdue) computed from next-due vs today — not stored separately.
- *Job that needs it:* **R1** (stay ahead of what's due — needs the due date); **R3** (accurate history for a vet); **Main**; plus the **proof-of-vaccination requirement** at boarding/daycare/grooming/travel 🟢 ([research.md → F9](research.md)).
- *Connected to:* **Pet dossier**; its next-due date generates a **Reminder**; its proof file is a **Document**; surfaced in **Access grant** (carer/vet view).

**5. Health / medical record**
- *Parts:* dated entries of type checkup / treatment / prescription; **conditions & allergies**; **current medications** (name, dose, frequency, route 🟢 [F5](research.md)); free-text notes; attached document; vet.
- *Job that needs it:* **Main**; **R3** (real history, not memory); **R5** (fast access to meds/conditions in a worrying moment); **R2** (the meds a carer must give).
- *Connected to:* **Pet dossier**; **medications** feed the **Access grant** (carer) and **Emergency authorization** (R5); prescriptions back onto **Documents**.

**6. Document**
- *Parts:* type, file (PDF/photo), label, issue/expiry date, the record it backs. **Subtypes:** **pet passport** (EU passport no., microchip, rabies linkage — 🔵 CLAUDE.md:51, Reg. 576/2013), insurance policy doc, legal / microchip registration, prescription scan, vaccination proof.
- *Job that needs it:* **Main** (store documents/legal); **R3** (hand over records); **F9** proof requirement 🟢.
- *Connected to:* **Pet dossier**; individual documents back a **Vaccination record**, **Insurance policy**, or stand alone (passport); expiry dates can feed a **Reminder**.

**7. Insurance policy** — *"insurances list" = the collection of these*
- *Parts:* insurer, policy number, coverage type, premium, start / renewal date, policy document.
- *Job that needs it:* **R1** (renewal reminders — "stay ahead of what's due" explicitly includes insurance renewals, 🔵 CLAUDE.md:55); **Main** (store insurance docs).
- *Connected to:* **Pet dossier**; renewal date → **Reminder**; policy file → **Document**.

**8. Appointment**
- *Parts:* date/time, vet clinic, reason, status (upcoming / done).
- *Job that needs it:* **R1** ("upcoming appointment tracking", 🔵 CLAUDE.md:47).
- *Connected to:* **Pet dossier**, **Vet clinic**; generates a **Reminder**.

**9. Reminder** — *incl. "reminders about insurance"*
- *Parts:* type (vaccination due / insurance renewal / checkup / legal-or-passport deadline), the record it points to, due date, channel (push / email), status (upcoming / done / snoozed `[?]`).
- *Job that needs it:* **R1** — this *is* the "stay ahead of what's due" job.
- *Connected to:* **derived from** a **Vaccination record** (next-due), **Insurance policy** (renewal), **Appointment** (date), or **Document** (expiry). Delivered to **Owner**. ("Reminders about insurance" is a Reminder *type*, not its own entity.)

**10. Personality / character profile** — *incl. "friendliness with others"*
- *Parts:* favourite food & treats (free-text owner notes), likes / dislikes, behaviour notes, preferred walks & routines, **"not friendly with"** (breeds / animal types), special requirements.
- *Job that needs it:* **R2** — make a stranger understand my pet fast (this is the core carer-facing content, 🟢 Rover care card [research.md:51,58](research.md)).
- *Connected to:* **Pet dossier**; surfaced through the **Access grant** (carer view).

**11. Vet clinic (preferred vet)**
- *Parts:* clinic name, address, phone, the pet's named vet `[?]`.
- *Job that needs it:* **R5** (fast access to "who its vet is" when worried); **R2** (the carer needs the vet contact, 🟢 [F5](research.md)); **R3** (dealing with a vet).
- *Connected to:* **Pet dossier**; referenced by **Appointments**, **Emergency authorization**, **Access grant**, **Vet message thread**.

**12. Access grant / Share**
- *Parts:* recipient (by link/code or account), role (carer / vet / co-owner), which pet, scope (what's visible), permission (view-only / limited-edit, 🔵 CLAUDE.md:67-70), access window / expiry, link or code.
- *Job that needs it:* **S1** (keep everyone on the same page — role-based access); **S2** (easy handoff, no account, 🟢 [research.md:68](research.md)); **R2** (the carer's scoped view); **R3** (the vet's scoped view).
- *Connected to:* **Owner** (issues it), **Pet / Pet dossier** (projects a subset), **Recipient**.

**13. Emergency authorization** — `[?]` partly new
- *Parts:* permission to seek emergency vet care, pre-approved spend limit, payment arrangement, owner emergency contact, plus pointers to the pet's vet + current meds/conditions.
- *Job that needs it:* **R5** (make a good call in a worrying moment) and **R2 / F6** (the carer's "what am I *allowed* to do in an emergency", 🟢 [research.md → F6](research.md)).
- *Connected to:* **Pet dossier** (pulls vet, meds, conditions), **Access grant** (carer sees the authorization), **Owner** (emergency contact).
- *Note:* the data (spend cap, payment, authorization) is **documented as a real caregiver need but not yet in PetPal's model** — flagged `[?]` until scoped.

**14. Vet message thread / request (chat)**
- *Parts:* participants (owner ↔ clinic), messages, records shared into the thread, related pet.
- *Job that needs it:* **R3** (the matrix feature for R3 is "share records from app + **vet messaging**"); partial **R5**.
- *Connected to:* **Pet dossier**, **Vet clinic**, **Documents/records** (shared in).
- *Note:* whether real-time vet messaging belongs in **MVP** is an **open research question** ([research.md:79](research.md)) — entity is valid, MVP scope `[?]`.

---

### Relationship spine (text)

```
Owner ──< Pet ──1:1── Pet dossier
                          ├── Vaccination record ──> Reminder ; Document(proof)
                          ├── Health record (conditions, meds, prescriptions)
                          ├── Document (passport, insurance doc, legal/microchip)
                          ├── Insurance policy ──> Reminder ; Document
                          ├── Appointment ──> Reminder
                          ├── Personality / character (friendliness, food, behaviour)
                          ├── Vet clinic
                          └── Emergency authorization (vet + meds + spend cap)  [?]
Owner ──< Access grant ──> (projects a scoped view of Pet dossier) ──> Recipient
Owner ── Vet message thread ── Vet clinic   (MVP scope [?])
```

---

### Questionable (no validated job behind them yet)

- **Recipient / carer as a saved contact** `[?]` — jobs **R2/S1/S2** require a *share target*, but **S2** is explicitly "no account, low-friction" ([research.md:68](research.md)), so a persistent stored contact may not be needed — an anonymous link/code can satisfy the job. Promote only if repeat-carer reuse is confirmed.
- **Pet update / status post** `[?]` — would serve **R4** (proof my pet's okay while away), but R4 **has no feature** and is a flagged gap ([jtbd.md R4](jtbd.md)); the sender side has **no caregiver voice**. Build the entity only if R4 is taken on.
- **Review / trust rating** `[?]` — the user's *"review/trust"*. In the research this is how *competitors* build trust (Rover reviews, Trustpilot), but it maps only to the **hypothesis** job "find/choose a carer" — which PetPal does **not** do (no matchmaking, [jtbd.md Hypotheses](jtbd.md)). No validated job ⇒ not in the main list.
- **Handoff-completeness indicator** `[?]` — would serve **E2** (feel sure nothing was forgotten), but E2 is an **inferred/interpretation** job ([jtbd.md E2](jtbd.md)); likely a *computed cue* over the dossier rather than a stored object.
- **Product / treat recommendation** & **breed-aware food database** — **cut**: address **no job** and flagged premature ([jtbd.md Conclusion](jtbd.md), [dimension-info-sharing.md](dimension-info-sharing.md)). Personality keeps only free-text food notes. Not entities.
- **White-label clinic instance** `[?]` — a **business-model** object, not an owner/carer job; deferred ([jtbd.md](jtbd.md)). Out of MVP entity scope.

---

---

## Screens

Draft screen hierarchy derived from the **jobs** and **entities** above — *not* from competitor structures. **Every node carries the job it serves** (codes from [jtbd.md](jtbd.md)); a node with no job is marked `[ORPHAN]` and must not silently enter the tree.

**Legend:** `⭐OO` = needed for the **primary** persona (Organised Owner) · `◦WO` / `◦RC` = needed for a **secondary** persona (Worried Owner / Receiving Caregiver) · `[?]` = depends on an entity/job still flagged.
**States, not screens:** empty / loading / error / "no access yet" are *states* of the screens below, not their own nodes.
Depth is kept deliberately shallow — levels get added in step 3.

```
OWNER app — signed in  (the OO journey)
│
├─ My Pets ................................. [Main]          ⭐OO
│   └─ Set up a pet ........................ [Main]          ⭐OO
│
├─ Pet dossier  (one pet) ................. [Main]          ⭐OO
│   ├─ Health & jabs ...................... [R1, R3]        ⭐OO
│   ├─ Documents & passport ............... [Main, R3]      ⭐OO
│   ├─ Insurance .......................... [R1]            ⭐OO
│   ├─ Personality & care ................. [R2]            ⭐OO
│   ├─ Vet & appointments ................. [R1, R5]        ⭐OO
│   └─ Emergency info & authorization ..... [R5, R2·F6]     ◦WO  ◦RC   [?]
│
├─ What's due  (reminders, all pets) ...... [R1]            ⭐OO
│
├─ Share a pet  (create access grant) ..... [S2]            ⭐OO
│   └─ Who has access  (manage roles) ..... [S1]            ⭐OO
│
└─ Vet messages ........................... [R3]            ⭐OO   [MVP scope ?]


RECIPIENT entry — no account  (the RC journey)
│
└─ Shared pet view ........................ [R2, R3]        ◦RC
    └─ Emergency & what I'm allowed to do .. [R5, R2·F6]     ◦RC   [?]
```

### Why these nodes (object + human logic, not "website sections")

- **My Pets / Set up a pet** — the **Pet** collection; the owner manages more than one (Main).
- **Pet dossier** — the **Pet dossier** object; the single hub a person consults and passes on. Its children are the *parts of the dossier*, each load-bearing for a job, not generic menu sections.
- **What's due** — the **Reminder** object, lifted out of any single pet because the human question "*what do I need to act on?*" spans all pets (R1).
- **Share a pet / Who has access** — the **Access grant** object: *creating* a handoff (S2) is a different act from *managing who can see what* (S1), so they are two nodes.
- **Vet messages** — the **Vet message thread** (R3); kept, but MVP necessity is an open question ([research.md:79](research.md)).
- **Shared pet view** — the carer/vet projection of a dossier via an Access grant; a **separate entry** because the recipient arrives by link with **no account** (S2).

### Persona split (explicit)

- **Primary (⭐OO) — the owner's full loop:** My Pets, Set up a pet, Pet dossier + all six sections, What's due, Share a pet, Who has access, Vet messages.
- **Secondary (◦WO):** **Emergency info & authorization** — the owner pulling critical info fast in a worried moment (R5).
- **Secondary (◦RC):** **Shared pet view** and **Emergency & what I'm allowed to do** — the no-account recipient (R2, R3, R5/F6).

### Deliberately absent (so they don't sneak in as orphans)

- **Updates-from-carer / "proof okay while away"** — would serve **R4**, but R4 has **no feature** (flagged gap, [jtbd.md R4](jtbd.md)). No screen until that's decided.
- **Account settings / notification preferences** — no standalone job today; would be `[ORPHAN]`. Reminder channel choice lives *with* "What's due" (R1) until a real job demands its own screen.
- **Emotional jobs E1 (calm), E2 (nothing forgotten), E3 (spare pet stress)** — served *through* the screens above (reliability, a complete share, low-friction), **not** as their own nodes. E3 currently has no feature at all.
- **Carer discovery / reviews / trust ratings** — the "find a carer" job is a **hypothesis** PetPal doesn't serve ([jtbd.md Hypotheses](jtbd.md)); no node.

---

## Navigation

### 1. Global navigation — 3 items

Each item is the entry to a **main-job cluster** — not "because every app has one." The three map cleanly onto the three verbs of the [main job](jtbd.md): *consult · act in time · pass on.*

| Global item | Job behind it | Why it earns a global slot |
|---|---|---|
| **Pets** | **Main** ("keep everything in one trusted place… *consult*") | The single trusted record — the dossier hub. The most frequent felt need and #1 adoption driver ([research.md F9/F10](research.md)). This is the home. |
| **What's due** | **R1** ("act in time, never reacting last-minute") | The reminder view, lifted above any one pet because "*what must I act on?*" spans all pets. The frequent, recurring reason to open the app. |
| **Share** | **S2** (create a handoff) + **S1** (manage who sees what) | The "**…and can pass on**" half of the main job — and PetPal's documented market whitespace (role-based portable sharing, [research.md:75](research.md)). |

**Why not 4–5:**
- **Vet messages (R3)** → folded in as **contextual** (reachable from a pet / from a share); its MVP necessity is itself an open question ([research.md:79](research.md)) — too uncertain to hold a permanent global slot.
- **Emergency (R5)** → a **secondary-persona** job (Worried Owner) and pet-specific; it lives *inside* a pet, surfaced prominently, not in global nav.
- **Account / settings** → no job → would be an `[ORPHAN]`; excluded.

### 2. Depth to the main job (primary persona — Organised Owner)

First screen for a signed-in owner = **Pets** (My Pets).

```
Pets (first screen)  →  tap a pet  →  Pet dossier  =  the "one trusted place"
       tap 0                tap 1         ← main job (consult) reached in 1 TAP ✅
```

- **Consult the trusted record:** **1 tap** (My Pets → open pet). With a *single* pet (the OO's typical case — "one dog"), the app can land directly on that pet's dossier = **0 taps**.
- **Pass it on (other half of the job):** dossier → **Share** = **2 taps**, or via the global **Share** item = **1 tap**.
- **Full main job (consult *and* initiate a handoff): ≤ 2 taps.**

**Within the 3-tap budget — no restructure needed.** The flat tree (global cluster → object → its parts) keeps the core record one tap from the door, with no compromise to report.

*(Bonus — secondary RC persona: the recipient opens a link straight into the **Shared pet view** = **0 taps** to their job, R2.)*

### 3. Global / Contextual / Deep

**Global — always visible** (the 3 job-cluster entries):
- **Pets** [Main] · **What's due** [R1] · **Share** [S1/S2]

**Contextual — appears inside a flow** (scoped to the object you're in):
- Pet-dossier sections: **Health & jabs** [R1/R3], **Documents & passport** [Main/R3], **Insurance** [R1], **Personality & care** [R2], **Vet & appointments** [R1/R5], **Emergency info** [R5/R2·F6] — appear *inside a pet*.
- **Set up a pet** [Main] — inside My Pets / first run.
- **Vet messages** [R3] — inside a pet or a share.
- **Who has access** [S1] — inside the Share cluster.
- **Add / update a record** (upload a document / add a reminder) — `[Main · R1 · R3]` — inside the relevant dossier section. *(node used across the flows in [flows.md](flows.md))*
- **Emergency & what I'm allowed to do** [R5/R2·F6] — inside the recipient's Shared pet view (RC).

**Deep — rare actions** (intentionally a few taps down):
- **Emergency authorization setup** (spend cap, payment, who-may-authorize) `[?]` — set once, seldom touched ([research.md F6](research.md)).
- **Edit / revoke a specific access grant** — inside *Who has access*.
- **Edit pet identity & lifecycle** (microchip, passport details, **archive / delete a pet**) — infrequent; the destructive archive/delete action lives here, **not** as a standalone screen. `[Main]` *(merged per [critique](sitemap-critique.md) — was orphan Sc20.)*
- ~~Account & notification preferences~~ — **removed** (was orphan Sc21, no job): the only job-bearing setting, **reminder-channel choice**, now lives in **What's due** (R1); true account preferences are **backlog**.

### 4. Navigation rules (from the [critique](sitemap-critique.md))

- **Single-pet auto-land.** When the owner has exactly **one** pet, the first screen is that pet's **Pet dossier** (not My Pets) → main job consulted in **0 taps**. My Pets becomes a switcher that only matters with 2+ pets. *(Closes the depth risk where dossier sections sat at 3 taps in the multi-pet path.)*
- **1-tap Emergency shortcut.** A persistent shortcut on the home surface opens **Emergency info & authorization** in **1 tap** — a worried moment (R5) can't afford the 3-tap dossier path.
- **No dead ends.** Every error/empty state must offer a next step (retry / offline cache / back-to-dossier / re-share / show owner contact). See [flows.md](flows.md).

---

## Screens realized in the interactive wireframes (v2)

> The [wireframes](../wireframes/) now implement the sitemap as a **clickable prototype** (mobile + desktop, three persona walkthroughs). Building it surfaced a handful of screens that the object model implied but the pre-wireframe tree hadn't named as pages. They are **not new entities** — each is a view or sub-action of an existing entity — but they *are* real screens, so they're logged here and folded into the traceability matrix below (Sc22–Sc26).

| New screen | Realizes | Entity / parent | Why it's a screen, not just a state |
|---|---|---|---|
| **Sc22 · Add photo** (`Upload-photo.html`) | Main (identity), the "photo" part of **Pet** | Set up a pet (Sc2) · Edit pet identity (Sc19) | The avatar was an inert placeholder; capturing a photo (camera / library) is a distinct task reachable from two parents. |
| **Sc23 · Pet dossier — brand-new empty state + "Add info" hub** (`home-new.html`) | Main (first-run) | Pet dossier (Sc3) | A just-created dossier needs an onboarding empty state (encouraging copy + one CTA) and a **section-picker** — clearly a different screen from the populated dossier. The picker itself is a modal, not a page. |
| **Sc24 · Edit an existing record** (`Edit-health-record.html`, `Edit-care-note.html`) | Main / R1 / R3 (correct a record) | Add / update a record (Sc14) | "Edit" opens the entry **pre-filled** and supports delete — semantically distinct from the blank *Add*. Every list item now opens *its own* instance (via id param), not one shared page. |
| **Sc25 · Document view** (`Document-view.html`) | Main / R3 (retrieve & hand over a document) | Document entity · Documents & passport (Sc5), Insurance (Sc6) | Viewing / downloading / re-sharing / replacing one stored document — the read side of the Document entity, previously only writable. |
| **Sc26 · Pet dossier — single-pet auto-land** (`home-success-single.html`) | Main (0-tap consult) | Pet dossier (Sc3) | Realizes the **single-pet auto-land** navigation rule: no pet-switcher, the app opens straight onto the one pet. A layout variant of Sc3, tracked so the rule is testable. |
| **Sc27 · Reminder detail** (`Whats-due-detail.html?rem=…`) | R1 (act in time) | Reminder entity · What's due (Sc10) | Where R1's *"marked done or booked"* actually happens — Mark done / Snooze + a contextual action (Book / Renew / Add to calendar / Start renewal) + view the record. Each reminder opens its own instance (fixes the old shared-section jump). |
| **Sc28 · Reminder settings** (`Reminder-settings.html`) | R1 | What's due (Sc10) | Realizes the IA's **Reminder channel setting** node (push/email, lead time, default snooze, quiet hours) — the setting that justified removing the old Account/notification-prefs screen. |
| **Sc29 · What's due — offline** (`Whats-due-offline.html`) | R1 | What's due (Sc10) | The R1 flow's *"showing last-saved reminders"* recovery — a banner + Retry over the cached list, reached from the error state. Closes the last partial dead-end. |

**Typed *Add / update a record* (Sc14).** The generic add-record form now ships as **type-aware variants** — the "Record type" selector arrives **pre-selected** from context: *Add health record* (`Add-health-record.html`), documents, insurance, vet, and *Add care note* (`Add-care-note.html`, category pre-chosen). Same screen and job (Sc14); the pre-selection is state carried in from the launching card, not a new page.

**Interaction patterns introduced (not screens):**
- **Floating "+" action button** on every dossier section — the single, consistent add-entry affordance (expands to *Add vaccine / Add health record* on Health & jabs). Replaces the old header "Add/Upload/Edit" text buttons.
- **"What do you want to add?"** section-picker modal on the brand-new dossier (Sc23).
- **QR share** presented as a centered modal (was a bottom sheet), consistent across mobile and desktop.

---

## Traceability

Coverage matrix: **rows = every job** ([jtbd.md](jtbd.md)) · **columns = every screen** in this sitemap (the 16 tree/contextual screens + the 5 deep-action screens). `✓` = the screen *actually participates* in completing that job. Goal: **no empty row, no empty column.**

**Screen codes**

| | | | |
|---|---|---|---|
| Sc1 My Pets | Sc2 Set up a pet | Sc3 Pet dossier | Sc4 Health & jabs |
| Sc5 Documents & passport | Sc6 Insurance | Sc7 Personality & care | Sc8 Vet & appointments |
| Sc9 Emergency info & authorization | Sc10 What's due | Sc11 Share a pet | Sc12 Who has access |
| Sc13 Vet messages | Sc14 Add / update a record | Sc15 Shared pet view | Sc16 Emergency & what I'm allowed to do |
| Sc17 Emergency authorization setup `[?]` | Sc18 Edit / revoke an access grant | Sc19 Edit pet identity & lifecycle *(incl. archive/delete)* | — |

*Sc20 (Archive/delete) merged into Sc19, and Sc21 (Account prefs) removed — see Orphan-screen decisions below.*

**Matrix A — owner-app screens (Sc1–Sc14)**

| Job | Sc1 | Sc2 | Sc3 | Sc4 | Sc5 | Sc6 | Sc7 | Sc8 | Sc9 | Sc10 | Sc11 | Sc12 | Sc13 | Sc14 |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| **Main** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ |  |  | ✓ |
| **R1** |  |  |  | ✓ | ✓ | ✓ |  | ✓ |  | ✓ |  |  |  | ✓ |
| **R2** |  |  | ✓ |  |  |  | ✓ |  |  |  | ✓ |  |  | ✓ |
| **R3** |  |  | ✓ | ✓ | ✓ |  |  |  |  |  | ✓ |  | ✓ | ✓ |
| **R4** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **R5** | ✓ |  | ✓ | ✓ |  |  |  | ✓ | ✓ |  |  |  |  |  |
| **E1** |  |  |  |  |  |  |  |  | ✓ | ✓ | ✓ |  |  |  |
| **E2** |  |  | ✓ |  |  |  |  |  |  |  | ✓ |  |  |  |
| **E3** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **S1** |  |  | ✓ |  |  |  |  |  |  |  | ✓ | ✓ |  |  |
| **S2** |  |  |  |  |  |  |  |  |  |  | ✓ |  |  |  |

**Matrix B — recipient + deep-action screens (Sc15–Sc19, post-fix)**

| Job | Sc15 | Sc16 | Sc17 | Sc18 | Sc19 |
|---|:--:|:--:|:--:|:--:|:--:|
| **Main** |  |  |  |  | ✓ |
| **R1** |  |  |  |  |  |
| **R2** | ✓ | ✓ |  |  |  |
| **R3** | ✓ |  |  |  |  |
| **R4** ⏸ |  |  |  |  |  |
| **R5** |  | ✓ | ✓ |  |  |
| **E1** | ✓ |  |  |  |  |
| **E2** |  |  |  |  |  |
| **E3** ⏸ |  |  |  |  |  |
| **S1** | ✓ |  |  | ✓ |  |
| **S2** | ✓ | ✓ |  |  |  |

*(⏸ = job parked: **R4** backlog, **E3** out-of-scope — empty rows are intentional, not unresolved defects. Sc20/Sc21 columns removed.)*

**Matrix C — wireframe-realized screens (Sc22–Sc29)** — *added in v2, see "Screens realized in the interactive wireframes" above.*

| Job | Sc22 Add photo | Sc23 New-dossier + Add-info | Sc24 Edit a record | Sc25 Document view | Sc26 Single-pet auto-land | Sc27 Reminder detail | Sc28 Reminder settings | Sc29 What's due offline |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| **Main** | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |  |
| **R1** |  | ✓ | ✓ |  |  | ✓ | ✓ | ✓ |
| **R2** |  | ✓ |  |  |  |  |  |  |
| **R3** |  |  | ✓ | ✓ |  |  |  |  |
| **R5** |  | ✓ |  |  |  |  |  |  |
| **S2** |  |  |  | ✓ |  |  |  |  |

*Every new screen carries ≥1 job (no orphan columns); each is a view/sub-action of an existing entity (Pet, Pet dossier, Document, Health/Personality record, **Reminder**), so no new entity or empty job-row is introduced. Sc27–29 complete R1's "act in time" screens — the flow previously reached only the sections.*

*Note on emotional jobs:* **E1** and **E2** are satisfied **indirectly** — no dedicated screen, the calm/confidence is a by-product of the marked screens doing their job. That is acceptable (the screens do participate). **E3** is a different case — see orphan jobs. *(The brand-new-dossier onboarding empty state, Sc23, also serves **E1/E2** indirectly — encouraging copy that reassures the first-run owner nothing's broken and nothing's been forgotten.)*

---

### ⛔ Orphan screens (empty columns) — ✅ resolved

- **Sc20 — Archive / delete a pet.** A real data-lifecycle need, but **no job** drove a whole screen. → **Done: merged** as a destructive action under **Sc19 Edit pet identity & lifecycle**; removed as a standalone node.
- **Sc21 — Account & notification preferences.** Existed out of habit. → **Done: removed** for MVP; the reminder-channel setting **moved to What's due (Sc10/R1)**; true account prefs → **backlog**.

### ⛔ Orphan jobs (empty rows) — ⏸ parked

- **R4 — get proof my pet's okay while away.** No carer→owner update channel exists (Shared pet view is one-way read; Vet messages is owner↔clinic), matching the jtbd "no feature / no caregiver voice" flag. → **Backlog.** Revisit an "Updates from carer" capability only after the RC/R4 validation round.
- **E3 — spare my pet unnecessary stress.** No screen can serve it — the stress reduction happens **offline** (vet's room / carer's hands). → **Out-of-scope** (accepted gap, no fabricated screen).

### Result after decisions

Decisions **applied**: Sc20 merged, Sc21 removed, R4 → backlog, E3 → out-of-scope. **No empty column remains.** The two empty rows (**R4, E3**) are now **explicitly parked** (⏸ backlog / out-of-scope) rather than silent defects. Every other in-scope job has ≥1 screen, and every remaining screen carries ≥1 job. Dead-end and missing-state defects are fixed in [flows.md](flows.md); depth risks closed by the **single-pet auto-land** and **1-tap emergency** rules in the Navigation section.
