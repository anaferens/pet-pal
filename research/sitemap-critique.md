# PetPal — Sitemap & Flows Critique

A four-class defect review of [sitemap.md](sitemap.md) and [flows.md](flows.md), in **where → what → how to fix** form. Defect classes: **dead ends · missing states · excessive depth · orphans.**

> **Status: all fixes applied.** Flow recoveries + states are in [flows.md](flows.md); orphan, depth and navigation fixes are in [sitemap.md](sitemap.md). The ✅ markers below show what was done.

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

## Honest residue (not silently hidden)
- **R4** and **E3** remain **empty rows on purpose** — parked, not solved. R4 needs the RC/R4 validation round before any "Updates from carer" feature; E3 is genuinely offline and may never be a PetPal screen.
- The **single-pet auto-land** and **1-tap emergency** rules are navigation *rules*, not yet drawn into the screen tree's structure — they must be honoured when wireframing or the depth risk returns.
- Several in-scope screens still have **no flow** exercising them (Who has access, Vet messages, etc.) — a coverage gap to close when those flows are drawn.
