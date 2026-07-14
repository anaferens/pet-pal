# PetPal — Sitemap & Flows Critique

A four-class defect review of [sitemap.md](sitemap.md) and [flows.md](flows.md), in **where → what → how to fix** form. Defect classes: **dead ends · missing states · excessive depth · orphans.**

> **Status: all fixes applied.** Flow recoveries + states are in [flows.md](flows.md); orphan, depth and navigation fixes are in [sitemap.md](sitemap.md). The ✅ markers below show what was done.
>
> **v2 update (interactive prototype).** The sitemap and flows are now realized as a clickable prototype in [wireframes/](../wireframes/). Building it surfaced a **second, prototype-level defect layer** — clickable elements that were wired wrong or not at all — that the paper critique above could not see. That review, its four audit classes, and the "all pass at zero" result are in [§5 below](#5-v2--interactive-prototype-audit). The v1 residue items (single-pet auto-land, 1-tap emergency, unbuilt screens) are re-checked there.

---

## 1. Dead ends
*A person stuck with no way out — a "no" branch or error/empty state leading nowhere.*

| Where | What | How to fix | Status |
|---|---|---|---|
| Main · `LinkErr → DeadShare` | Link-creation error terminal; "pass on" half blocked, no exit | Retry → Share + "save & try later" → dossier (record safe) | ✅ |
| R2 · `LinkErr → DeadLink` | Expired/revoked link dead-ends the carer | "Owner re-shares a fresh link" → re-open | ✅ |
| R2 · `Q5 no → DeadGap` | Empty profile + no emergency info → no info, no action | Show owner contact → partial ending (not stuck) | ✅ |
| R1 · `Err → DeadLoad` | Reminder-load failure terminal; may miss a deadline | Retry + offline "last-saved reminders" | ✅ |
| R1 · `SaveErr → DeadSave` | Save failure terminal; due item unresolved | Retry + "keep in list" (stays in What's due) | ✅ |
| R5 · `Err → DeadErr` | Critical-info load fails *in a panic* — worst case | Retry + offline "cached critical info" | ✅ |
| R5 · `Empty → DeadEmpty` | Never-filled fields → no facts | Fallback: show vet + owner contact + "call your vet" | ✅ |
| R5 · `Stale → DeadStale` | Unsure about stale info → stuck | Show last-updated + source + "confirm with owner/vet" | ✅ |

*Result: 0 terminal dead ends remain; former dead ends are now recovery branches or orange "partial" endings.*

## 2. Missing states
*Happy path exists, but no empty / error / loading state.*

| Where | What | How to fix | Status |
|---|---|---|---|
| My Pets (Main, R5 entry) | Only "empty: no pets"; no loading/error on fetch | Add `Loading` + `Error`/retry | ✅ |
| Pet dossier (all flows) | Opened with no loading/error | Add dossier `Loading` + `Error`/retry | ✅ |
| Dossier sections (Health & jabs, etc.) | No **empty** for a brand-new pet | Add per-section `Empty` ("add the first record") | ✅ (Health shown; pattern applies to all) |
| R2 · Share step | No link-create loading/error (Main had them) | Add `Loading: creating link` + `Error` | ✅ |
| Shared pet view (R2) | No generic load error (only expired-link) | Add `Error`/retry distinct from expired-link | ✅ |
| What's due → section (R1) | Deep-link open had no loading/error | Covered by the per-section load/error pattern | ✅ |

## 3. Excessive depth
*Main or frequent related job hidden deeper than 3 taps for the primary persona.*

| Where | What | How to fix | Status |
|---|---|---|---|
| Main job | 1 tap — but only via an unbuilt single-pet auto-land assumption | Make **single-pet auto-land** an explicit rule | ✅ (Navigation rule 4) |
| R2 — Personality & care | Multi-pet: 3 taps to the care section | Single-pet auto-land + surface care/share on dossier home | ✅ |
| R5 — Emergency info (high-stakes) | 3 taps in a panic, no shortcut | Add **1-tap Emergency shortcut** from home | ✅ (Navigation rule 4 + R5 flow) |

## 4. Orphans
*Screens with no job; jobs with no screen (vs. the coverage matrix).*

| Where | What | How to fix | Status |
|---|---|---|---|
| Sc20 Archive / delete a pet | Empty column — screen, no job | Merge under *Edit pet identity & lifecycle* | ✅ merged |
| Sc21 Account & notification preferences | Empty column — no job | Remove; reminder-channel → What's due (R1); prefs → backlog | ✅ removed |
| R4 Proof my pet's okay while away | Empty row — job, no screen | Backlog (no carer→owner channel; known gap) | ⏸ parked |
| E3 Spare my pet stress | Empty row — job, no screen | Out-of-scope (offline outcome; no fabricated screen) | ⏸ parked |
| *(minor)* Who has access, Vet messages, Emergency-auth setup, Edit/revoke, Edit identity | Have a job but appear in no flow | Not orphans — flow coverage gap; add flows later | open |

---

## 5. v2 — Interactive-prototype audit
*Once the sitemap became a clickable prototype ([wireframes/](../wireframes/)), a new defect layer appeared that the paper critique (§1–4) could not: a control that looks tappable but does nothing, or navigates to the **wrong** screen. This is the runtime equivalent of a dead end — the person clicks and is either stuck or misled.*

Four repeatable audits now run over **all 82 wireframe files, both mobile and desktop views** (scripts kept with the build). Each defect class, what it found, and how it was closed:

### 5a. Structural dead ends *(the runtime version of §1)*
*A button/anchor with no action, or a link to a file that doesn't exist.*

| Where | What | How to fix | Status |
|---|---|---|---|
| ~38 screens (both views) | **104** buttons/links with no destination — header actions, record "Edit →", "Call vet", filter chips, "View document", loading-screen "Cancel", empty-state CTAs, home actions | Wire each to its real target (or `tel:` for call actions); disable true "Saving…" buttons | ✅ 0 remain |
| Whole set | Links to non-existent files | Cross-check every `href` against the file list | ✅ 0 broken |

### 5b. Wrong / shared destinations *(new class — invisible on paper)*
*Distinct list items all pointing at one hardcoded detail/edit page — click "Annual checkup", land on "Dental cleaning".*

| Where | What | How to fix | Status |
|---|---|---|---|
| Documents & passport, Insurance, Shared pet view | 4 documents + policy all opened the same hardcoded **Document view** | Parameterize `Document-view.html` by `?doc=`; link each card to its own id | ✅ |
| Health & jabs, Vet & appointments | 2 records + 3 vaccinations + 3 appointments all opened one hardcoded **Edit record** | Parameterize `Edit-health-record.html` by `?rec=`; wire each row | ✅ |
| Personality & care | 6 care notes all opened "Favourite food & treats" | Parameterize `Edit-care-note.html` by `?note=` | ✅ |
| Who has access, Emergency auth setup | 3 grants + 2 contacts all opened one hardcoded **Edit grant** | Parameterize `Edit-access-grant.html` by `?person=` | ✅ |

### 5c. Entity mismatch *(new class)*
*A link whose label names one entity but navigates to another.*

| Where | What | How to fix | Status |
|---|---|---|---|
| My Pets pet cards | Tapping **Miso** opened the dossier *loading* state (never resolved); desktop opened **Cheetah**; Cheetah's card wasn't clickable | Point each pet card at *that pet's* dossier (`home-success.html` / `home-success-cheetah.html`), both views | ✅ |
| Add/Edit forms reached from a section card | Form opened with the wrong (or no) record-type pre-selected | Carry the section as a param (`?type=` / `?cat=`) so the launcher's choice is honoured | ✅ |

### 5d. Inert interactive controls *(new class)*
*Interactive-looking elements that aren't buttons or links, so §5a missed them.*

| Where | What | How to fix | Status |
|---|---|---|---|
| Share a pet, Edit access grant (+ states) | **Scope picker** radio cards (Full dossier / Care / Health / Emergency) didn't respond to clicks | `onclick` to move the `.selected` state | ✅ |
| Add / Edit care note (+ states) | "Mark as warning" **toggle** didn't switch | `onclick` to toggle `.on` | ✅ |

### Screens created to close §5 defects
Some fixes needed a screen that didn't exist yet — logged in [sitemap.md §"Screens realized in the interactive wireframes"](sitemap.md) (Sc22–Sc26):
- **Add photo** — the pet avatar was an inert placeholder (a §5a dead end); now a real capture screen.
- **Edit an existing record** (health / care note) — "Edit" used to open a blank *Add* form (a §5b/§5c defect); now opens the entry pre-filled.
- **Document view** — documents were write-only; the read/download/re-share side existed nowhere.
- **Brand-new-pet dossier + "Add info" hub** — a just-created dossier previously looked like a broken empty page; now an onboarding empty state with a working section-picker.

**Result: all four audits pass at zero findings.** Re-running them catches regressions in every class — including the wrong-destination one that paper review can't detect.

---

## Honest residue (not silently hidden)
- **R4** and **E3** remain **empty rows on purpose** — parked, not solved. R4 needs the RC/R4 validation round before any "Updates from carer" feature; E3 is genuinely offline and may never be a PetPal screen.
- **Single-pet auto-land — now realized.** ✅ It was a navigation *rule* only; the prototype builds it as `home-success-single.html` (no pet-switcher, opens straight onto the one pet). The multi-pet path (`home-success.html`) keeps the switcher.
- **1-tap emergency — realized in-flow.** ✅ The emergency shortcut and the sitter's *Emergency & allowed* screen are wired; still worth a dedicated home-surface entry when the home screen is designed.
- **Flow coverage — improved, not complete.** The new **new-pet setup (full journey)** flow ([flows.md](flows.md)) now exercises previously flow-less screens (every dossier section, Add/Edit, Document view, Share). **Vet messages** and a standalone **Who has access** flow are still undrawn — the remaining coverage gap.
