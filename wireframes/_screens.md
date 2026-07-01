# PetPal — Wireframe screen list (main flow)

Screens for the **main job** only: *"keep everything I know about my pet somewhere I trust and can pass on."*
Primary persona: **Organised Owner (Eva).**
Flow source: `flows.md → Main job — consult & pass on`.

Other flows (R1, R2, R5, recipient) are **step 08** — not here.

---

## State matrix

| # | Screen | Job(s) | Empty | Loading | Error | Success |
|---|---|---|---|---|---|---|
| 1 | My Pets | Main | ✓ | ✓ | ✓ | ✓ |
| 2 | Set up a pet | Main | — | ✓ | ✓ | ✓ |
| 3 | Pet dossier | Main | ✓ | ✓ | ✓ | ✓ |
| 4 | Health & jabs | R1, R3 | ✓ | ✓ | ✓ | ✓ |
| 5 | Documents & passport | Main, R3 | ✓ | ✓ | ✓ | ✓ |
| 6 | Insurance | R1 | ✓ | ✓ | ✓ | ✓ |
| 7 | Personality & care | R2 | ✓ | ✓ | ✓ | ✓ |
| 8 | Vet & appointments | R1, R5 | ✓ | ✓ | ✓ | ✓ |
| 9 | Add / update a record | Main | — | ✓ | ✓ | ✓ |
| 10 | Share a pet | S2 | — | ✓ | ✓ | ✓ |

---

## Screen details

### 1. My Pets

**Job:** Main — "keep everything in one trusted place."
**Flow position:** Entry point. First screen after sign-in. Fetches the owner's pet list.

**Key decisions:**
- **Single-pet auto-land.** If owner has exactly 1 pet → skip this screen entirely, land on Pet dossier (0 taps to main job). My Pets only renders for 2+ pets or 0 pets.
- **Pet card, not a list row.** Each pet is a card with photo, name, species, and a fill-status hint (e.g. "3 of 5 sections filled") so Eva sees at a glance which pet needs attention.
- **"Add a pet" is always visible** — not hidden in a menu. Prominent button or card.
- **MVP species:** dogs and cats only. Species picker on the card is limited to these two (resolved Q7).
- **Multi-pet switching (Q8):** the active pet must always be signalled clearly. If Eva has a dog and a cat, she must never accidentally edit the wrong one. Consider: pet photo + name in the nav bar once inside a dossier.

**States:**
| State | What happens | Recovery |
|---|---|---|
| Empty | No pets yet. Big illustration + "Add your first pet" CTA. | → Set up a pet |
| Loading | Fetching pets from server. Skeleton cards. | — |
| Error | Could not load pets (network / server). | Retry button |
| Success | Pet cards displayed. Tap a card → Pet dossier. | — |

---

### 2. Set up a pet

**Job:** Main — creating the pet record that everything else hangs off.
**Flow position:** Reached from empty My Pets or "add another pet." After save → Pet dossier.

**Key decisions:**
- **Minimum viable pet:** only name + species are required to save. Everything else (breed, photo, date of birth) is optional — reduce capture friction (research F4: the real make-or-break).
- **Species = dog or cat** (MVP). No rabbit/guinea pig/bird until post-MVP (resolved Q7).
- **Photo upload is optional** but encouraged — a pet photo makes the dossier and shared view feel personal. Support camera capture and library pick.
- **No multi-step wizard.** Single scrollable form. The owner can fill in as little as name + species and come back later. Don't gate progress on completeness.
- **After save → land on Pet dossier** with all sections empty. The dossier's empty state guides next steps.

**States:**
| State | What happens | Recovery |
|---|---|---|
| Empty | — (form starts blank by design, not an empty state) | — |
| Loading | Saving the new pet. Inline spinner on the save button. | — |
| Error | Could not save (network / validation). | Retry; form data preserved, nothing lost |
| Success | Pet created. Navigate to Pet dossier (fresh, empty). | — |

---

### 3. Pet dossier

**Job:** Main — "one trusted place." The hub screen for a single pet.
**Flow position:** Central node. Every dossier section returns here. The "consult" verb lives here; the "pass on" verb exits to Share a pet.

**Key decisions:**
- **Section cards, not a flat menu.** Each dossier section (Health, Docs, Insurance, Personality, Vet) is a card showing: section name, fill status (empty / X items / last updated), and a visual cue (icon or illustration). This answers "what have I filled, what's missing?" at a glance.
- **Fill-status indicator.** Eva's main anxiety is "did I capture everything?" (E2). A completeness signal per section (not a percentage — just filled/empty/partial) helps without feeling like a chore.
- **Pet identity at the top.** Photo, name, species, breed — always visible. This is the "single trusted record" header. For multi-pet owners, this header is the anchor that says "you're looking at Luna, not Max."
- **Quick actions.** "Share this pet" and "Edit pet details" should be reachable from here — not buried.
- **Emergency info shortcut.** Although emergency is step 08, the dossier should reserve a prominent slot for it (1-tap access, per navigation model).
- **Depth = 1 tap** from My Pets. With single-pet auto-land = 0 taps. Nothing in the dossier should be deeper than 1 more tap (dossier → section).

**States:**
| State | What happens | Recovery |
|---|---|---|
| Empty | Freshly created pet — all sections show "no data yet" with individual CTAs ("Add your first vaccination," "Upload a document," etc.). A "get started" banner suggests which section to fill first (Health & jabs, since it's the most frequent need — F9/F10). | Tap any section CTA |
| Loading | Opening the dossier. Skeleton layout for section cards. | — |
| Error | Could not load dossier (network / server). | Retry button |
| Success | Section cards loaded with fill status. Tap a card → section detail. | — |

---

### 4. Health & jabs

**Job:** R1 (stay ahead of what's due), R3 (give a professional an accurate picture).
**Flow position:** Dossier section. The flow's representative "add records" path. Return to dossier after adding/updating.

**Key decisions:**
- **Two content types, one screen.** Vaccinations (with due dates and proof) and general health records (checkups, treatments, conditions, meds) live together. Tabs or segmented control to switch — not two separate screens.
- **Status badges.** Each vaccination shows: up-to-date (green), due soon (amber), overdue (red). Eva scans this to know if she needs to act — the "stay ahead" job.
- **Conditions & current meds** are pinned at the top (or a prominent section) — this is what a vet or carer needs instantly (R3, R5). Not buried under a history list.
- **Proof attachment.** Each vaccination/treatment can have a photo or PDF attached (the proof-of-vaccination requirement at boarding/daycare/travel — research F9).
- **Chronological history.** Past records in reverse-chronological order. Each entry: date, type, brief description, attached proof if any.
- **"Add" button is always visible** — floating action or sticky footer. The most common action on this screen.

**States:**
| State | What happens | Recovery |
|---|---|---|
| Empty | No health records yet. Illustration + "Add your first vaccination or health record." Explain what goes here (jabs, checkups, conditions, meds). | → Add / update a record |
| Loading | Fetching health data. Skeleton list. | — |
| Error | Could not load health data. | Retry button |
| Success | Records listed with status badges. Conditions/meds pinned. | — |

---

### 5. Documents & passport

**Job:** Main (store documents), R3 (hand over records to a vet).
**Flow position:** Dossier section. Stores all uploaded files: pet passport, microchip registration, insurance docs, legal papers, prescription scans.

**Key decisions:**
- **Document types with smart defaults.** When uploading, offer type presets: Pet passport, Microchip registration, Insurance document, Prescription, Other. This structures the list without forcing the user to categorize.
- **Pet passport is special.** EU pet passport (Regulation 576/2013) has specific fields: passport number, microchip number, rabies vaccination linkage. Show these as structured fields, not just a PDF upload. This is a legal document Eva needs at every border crossing.
- **Expiry tracking.** Documents with expiry dates (passport, insurance, registrations) show status: valid / expiring soon / expired. Feeds into the reminder system (step 08).
- **Upload = camera or file.** Support photo capture (snap a document) and file picker (PDF from email). Keep it to one tap to start an upload.
- **Preview without leaving.** Tapping a document opens a preview (image viewer or PDF reader) — don't force the user to download.

**States:**
| State | What happens | Recovery |
|---|---|---|
| Empty | No documents yet. Illustration + "Upload your first document" with type suggestions (passport, microchip, insurance). | → Add / update a record (upload mode) |
| Loading | Fetching documents. Skeleton cards. | — |
| Error | Could not load documents. | Retry button |
| Success | Document cards with type, name, expiry status, thumbnail preview. | — |

---

### 6. Insurance

**Job:** R1 (stay ahead of renewal dates).
**Flow position:** Dossier section. Insurance policy details and renewal tracking.

**Key decisions:**
- **One policy view, not a list (for now).** Most pets have one active insurance policy. Show it as a detail card, not a list. If multi-policy is needed later, the card pattern scales to a list.
- **Key fields:** insurer name, policy number, coverage type (what's covered), premium amount, start date, renewal date, policy document (attached PDF).
- **Renewal status badge.** Active (green) / renewing soon (amber) / expired (red). The renewal date feeds the reminder system (step 08).
- **Policy document attachment.** The actual PDF/photo of the policy — so Eva can find it instantly instead of digging through email.
- **Coverage summary.** Free-text or structured: what the policy covers and what it doesn't. Eva's vet or sitter can see this through the shared view.

**States:**
| State | What happens | Recovery |
|---|---|---|
| Empty | No insurance added. Illustration + "Add your pet's insurance" with a note on why (renewal reminders, shareable with vet). | → Add / update a record (insurance mode) |
| Loading | Fetching insurance data. | — |
| Error | Could not load insurance data. | Retry button |
| Success | Policy card with insurer, coverage, renewal status, attached document. | — |

---

### 7. Personality & care

**Job:** R2 (make a stranger understand my pet fast).
**Flow position:** Dossier section. The core content a carer sees through the shared view. This is PetPal's differentiator — Rover's care card, but portable and owner-controlled.

**Key decisions:**
- **Structured sections, free-text within each.** Sections: favourite food & treats, likes & dislikes, behaviour notes, preferred walks & routines, "not friendly with" (breeds/animal types), special requirements. Each is a free-text field — no rigid forms. The owner knows their pet best.
- **"Not friendly with" is safety-critical.** Give it visual prominence (warning-style card or icon). A sitter who misses this risks an incident. Consider: amber/red styling to draw the eye.
- **This IS the shared care card.** What Eva fills here is exactly what the carer sees in the Shared pet view (step 08). Make this connection visible: "This is what your sitter will see."
- **Quick-fill, not essay.** Short prompts, placeholder examples ("e.g. loves belly rubs, hates loud noises"). The capture friction is the biggest risk — if this feels like homework, Eva won't fill it.
- **Photo spots.** Optional photos within personality (e.g. "favourite sleeping spot," "walking route") make the profile feel alive and help the carer connect with the pet.

**States:**
| State | What happens | Recovery |
|---|---|---|
| Empty | No care info yet. Friendly illustration + section prompts: "What does [pet name] love? What should a sitter know?" Show section headers with placeholder text to lower the barrier. | Tap any section to start typing |
| Loading | Fetching care data. | — |
| Error | Could not load care data. | Retry button |
| Success | Personality profile filled. Sections with content, edit buttons. A "preview as sitter" link shows what the carer will see. | — |

---

### 8. Vet & appointments

**Job:** R1 (stay ahead of what's due — appointments), R5 (fast access to vet contact in a worrying moment).
**Flow position:** Dossier section. Vet clinic info + appointment history/upcoming.

**Key decisions:**
- **Vet clinic is a saved contact, not just text.** Structured fields: clinic name, address (with map link), phone (tappable to call), named vet/doctor. In a worrying moment (R5), Eva needs to call her vet in one tap — not scroll through notes.
- **Address links to maps.** Tapping the address opens the native maps app. Small detail, big value in a stressed moment.
- **Appointments: upcoming first, then past.** Upcoming appointments at the top with date, time, reason, status (confirmed / pending). Past appointments below in reverse-chronological order.
- **One vet clinic for MVP.** Most pets have one regular vet. Support one saved clinic; multi-clinic is post-MVP.
- **Appointment → reminder.** Creating an appointment auto-generates a reminder (feeds What's due, step 08). The user shouldn't have to create both manually.

**States:**
| State | What happens | Recovery |
|---|---|---|
| Empty | No vet clinic or appointments. Illustration + "Add your vet clinic" as the primary CTA — the vet contact is the most critical piece (R5). | → Add / update a record (vet mode) |
| Loading | Fetching vet data. | — |
| Error | Could not load vet data. | Retry button |
| Success | Vet clinic card (name, address, phone, doctor) + appointment list (upcoming highlighted). | — |

---

### 9. Add / update a record

**Job:** Main — the editing action within any dossier section.
**Flow position:** Reached from any dossier section's "add" or "edit" action. After save → returns to the section (and the dossier).

**Key decisions:**
- **Context-aware form.** The form adapts to what's being added: a vaccination has different fields than an insurance policy or a personality note. The entry point (which section the user came from) determines the form type.
- **Minimal required fields.** For every record type, only 1–2 fields are required (e.g. vaccine name + date). Everything else is optional. Capture friction (F4) is the adoption gate — never block a save on optional fields.
- **File attachment on every record type.** Photo or PDF upload is available everywhere: vaccination proof, prescription scan, insurance document, passport photo. One consistent "attach file" pattern.
- **Inline validation, not modal errors.** Show field errors inline as the user types, not after they tap save. Red border + message under the field.
- **Edit = same form, pre-filled.** Tapping "edit" on an existing record opens the same form with data pre-populated. No separate "edit mode."
- **Destructive actions (delete) require confirmation.** Swipe-to-delete or a delete button with a confirmation dialog. No accidental data loss.
- **Save preserves input on error.** If the save fails (network), the form data stays — the user just taps retry, not re-enters everything.

**States:**
| State | What happens | Recovery |
|---|---|---|
| Empty | — (form starts blank for "add", pre-filled for "edit") | — |
| Loading | Saving the record. Spinner on the save button; form is disabled. | — |
| Error | Save failed (network / server / validation). | Retry; all form data preserved. Inline validation for field errors. |
| Success | Record saved. Brief confirmation (toast or checkmark animation) → navigate back to section/dossier. | — |

---

### 10. Share a pet

**Job:** S2 — "pass it on." The other half of the main job.
**Flow position:** End of the main flow. Reached from Pet dossier ("share this pet") or from the global Share nav item. After success → link sent, flow complete.

**Key decisions:**
- **Recipient doesn't need an account.** The share generates a link or code. The carer opens it in a browser, sees a read-only pet view. No sign-up, no app install (research F7: 92% abandon on forced account creation).
- **Scope picker.** Owner chooses what's visible to the recipient: full dossier, care info only, health info only, emergency only. Default = full dossier (most common for a trusted sitter). Advanced users can customise.
- **Role selection.** Carer (read-only) / Vet (can add medical records) / Co-owner (full edit). MVP default = carer.
- **Link has an expiry.** Owner can set how long the link is active: 1 week, 1 month, permanent. Default = 1 month. Expired links show a friendly "ask the owner for a new link" page.
- **Share via any channel.** Once the link is generated, the owner shares it however they want: copy link, WhatsApp, SMS, email. PetPal doesn't own the delivery channel — WhatsApp is the additional channel, not replaced (resolved Q3).
- **Confirmation before creating.** Show a summary of what will be shared, with whom, for how long. One tap to confirm. The link is the handoff — it should feel intentional, not accidental.
- **Re-share / revoke from Who has access** (step 08). This screen creates; managing existing shares is a different screen.

**States:**
| State | What happens | Recovery |
|---|---|---|
| Empty | — (the sharing form is always present, pre-populated with the current pet) | — |
| Loading | Creating the share link. Spinner. | — |
| Error | Could not create link (network / server). | Retry, or "save and try later" → return to dossier |
| Success | Link created. Show the link with copy/share actions. Confirmation: "Your pet's info is now shared." | — |

---

## Excluded from this step (and why)

| Screen | Why excluded |
|---|---|
| Emergency info & authorization | R5 flow (worried moment), not main flow. Spend cap / payment cut from MVP. |
| What's due (reminders) | R1 flow — separate "stay ahead" path, step 08. |
| Who has access | S1 flow — managing existing shares, not creating them. Step 08. |
| Vet messages | Deferred from MVP entirely (Q4 resolved: one-way record-sharing is enough). |
| Shared pet view | Recipient journey (R2 flow), no account. Step 08. |
| Emergency & what I'm allowed to do | Recipient journey (R5/R2 flow). Step 08. |

---

## State definitions

| State | Meaning | Design implication |
|---|---|---|
| **Empty** | The screen's primary content doesn't exist yet. | Clear CTA — not a blank page. Guide to the first step. Use illustration + action verb. |
| **Loading** | Data is being fetched or saved. | Skeleton shimmer for fetches, inline spinner for saves. Brief — never let the user wonder if the app is stuck. |
| **Error** | A fetch or save failed. | Always offer recovery: retry, offline fallback, or save-and-try-later. **No dead ends.** |
| **Success** | Content loaded and usable, or action completed. | The primary state — wireframe this first, then derive the others. |

---

## Global wireframe rules

- **Single-pet auto-land:** 1 pet → skip My Pets, open Pet dossier directly (0 taps to main job).
- **Multi-pet clarity (Q8):** always signal which pet is active — pet photo + name in the nav bar inside a dossier. Quick-switch button on home screen.
- **No dead ends:** every error state has a recovery action. Established in the critique and flows.
- **MVP species:** dogs and cats only (Q7).
- **Vet messaging:** not in MVP. R3 served by one-way record sharing via Share a pet (Q4).
- **Emergency authorization:** info-only for MVP (vet contact, meds, conditions). No spend cap / payment (Q5).
- **Calendar:** in-app calendar + export to Google/Apple/Outlook. Lives on What's due — step 08 (Q6).
- **Capture friction is the #1 adoption risk (F4).** Every form should have minimal required fields. Never block progress on optional data. Make it easy to come back and fill in more later.
- **3-tap budget.** Nothing core exceeds 3 taps from home. Main job is 1 tap (0 with single pet). Emergency is 1 tap from home.
- **Mobile-first.** All wireframes target mobile viewport. Desktop adaptation is later phase.
