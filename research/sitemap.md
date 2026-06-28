# PetPal — Sitemap (draft)

> Pre-wireframe working doc. **No screens or navigation yet** — this is only the object model behind the jobs.

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
- **Edit pet identity** (microchip, passport details) — infrequent.
- **Archive / delete a pet** — rare and destructive (e.g. a pet that has passed).
- **Account & notification preferences** — deferred, no standalone job yet.
