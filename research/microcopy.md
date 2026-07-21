# PetPal — Microcopy Inventory

> **Status: inventory only.** This is a complete pass over every product-facing string in [`wireframes/*.html`](../wireframes/) (123 files, 622 unique strings). **Nothing here is rewritten** — this document only *records* and *flags*. By end of lesson it becomes the single source of truth that the rewrites are made against.

**Scope.** Extracted from the on-device content (mobile view; desktop is an identical copy). **Excluded as prototype chrome, not product text:** the left sidebar catalog, the Success/Empty/Loading/Error state-bar, the flow-step breadcrumb, and the persona-flow tooltips. **Method:** [`scratchpad/extract_copy.py`](../../..) — regex over each screen's content region, deduplicated to one row per unique string with a "seen on" count.

Because a handful of strings (e.g. `← Dossier` ×46) repeat across dozens of screens, the inventory lists **one row per unique string** with the screens it appears on — rather than repeating identical rows 40+ times. The requested columns (screen · area · row · type) are all present; area/type also drive the section grouping.

---

## Flag legend

| Flag | Meaning |
|---|---|
| 🔴 **TERM** | Same concept named differently across screens |
| 🟠 **LABEL** | Same action, different button/link text |
| 🟡 **TONE** | AI cliché, over-cheerful, needless `!` or emoji |
| 🟣 **STRAY** | Leftover placeholder / dev / meta text that reached the UI |
| ⚪ **ANNOTATION** | Prototype scaffolding label (zone-label) — not real product copy |
| 📝 **USER** | User-authored sample/demo content — **we do not control or rewrite this** |

---

## 1 · Global navigation

| Screen(s) | Area | Text | Type | Flag |
|---|---|---|---|---|
| all | bottom nav | Pets | nav item | |
| all | bottom nav | What's due | nav item | |
| all | bottom nav | Share | nav item | |
| all | bottom nav | Owner | nav item | |
| dossier, sections | header (back) | ← Dossier | button | 🟠 back-label — pattern is `← [destination]` (see §9) |
| My-Pets children | header (back) | ← My Pets | button | 🟠 |
| add/edit forms | header (back) | ← Cancel | button | 🟠 **breaks the pattern** — an action, not a destination |
| Share children | header (back) | ← Share | button | 🟠 |
| Who-has-access child | header (back) | ← Who has access | button | 🟠 |
| Whats-due child | header (back) | ← What's due | button | 🟠 |
| Document-view | header (back) | ← Documents | button | 🟠 |
| Emergency child | header (back) | ← Emergency info | button | 🟠 |
| Shared-pet-view child | header (back) | ← Miso's profile | link | 🟠 + 🔴 (see §11-A) |
| various | header | Edit | button | 🟠 vs `Edit →`, `Edit pet details` |
| Whats-due | header | Settings | button | |

---

## 2 · Buttons & actions

### Add / create

| Screen(s) | Text | Type | Flag |
|---|---|---|---|
| My-Pets (desktop) | Add a pet | button | 🟠 vs `Add your first pet`, `+ Add your first pet` |
| My-Pets-empty | Add your first pet | button | 🟠 |
| My-Pets-empty (alt) | + Add your first pet | button | 🟠 **`+` prefix inconsistent** |
| home-new | + Add info | button | 🟠 |
| Health-and-jabs | + Add vaccine | link | 🟠 + 🔴 vaccine/jab (§11-A) |
| Health-and-jabs-empty | Add first health record | button | 🟠 |
| Personality | + Add another note | button | 🟠 |
| Vet (empty/firstrun) | + Add vet clinic | button | 🟠 |
| Vet | Add vet clinic | button | 🟠 **same action, `+` sometimes** |
| Vet | + Add appointment | button | 🟠 |
| Insurance-empty | Add insurance | button | 🟠 |
| Documents-empty | Upload first document | button | 🟠 + 🔴 "Upload" vs "Add" |
| Documents (header) | Upload | button | 🟠 |
| Emergency | + Add emergency contact | button | 🟠 |
| Emergency | + Add important / allowed meds list | button | 🟠 |
| Whats-due | Add reminder | button | 🟠 |
| generic | Add | button | 🟠 **bare "Add" (×6)** |

### Save

| Screen(s) | Text | Type | Flag |
|---|---|---|---|
| Add-record | Save record | button | 🟠 |
| Add-care-note | Save note | button | 🟠 |
| Set-up-a-pet | Save pet | button | 🟠 |
| Emergency-auth-setup | Save authorization | button | 🟠 + 🔴 authoriz**ation**/authoris­ation (§11-A) |
| Reminder-settings | Save settings | button | 🟠 |
| Add-vet-clinic, Add-insurance… | Save | button | 🟠 **bare "Save" (×5)** |
| Owner (Me), Edit forms | Save changes | button | 🟠 |

### Retry / recovery

| Screen(s) | Text | Type | Flag |
|---|---|---|---|
| error screens | Try again | button | 🟠 **(×17)** |
| one error screen | Retry | button | 🟠 |
| save-error screens | Retry save | button | 🟠 **three retry labels for one action** |

### Share / sitter

| Screen(s) | Text | Type | Flag |
|---|---|---|---|
| dossier | Share Miso's info | button | (pet-specific — OK) |
| cheetah dossier | Share Cheetah's info | button | (pet-specific — OK) |
| Share-a-pet | Create share link | button | |
| Share-a-pet | Show QR code | button | |
| QR modal | Save QR image / Print QR | button | |
| Share-success | See what your sitter sees | button | 🟠 vs `Preview as sitter` |
| Personality | Preview as sitter | button | 🟠 **same action, two labels** |
| Share-success | Share with a pet sitter | button | 🟠 vs `Share with someone new` |
| Who-has-access | Share with someone new | button | 🟠 |
| grant | Re-share | button | |

### Call / contact

| Screen(s) | Text | Type | Flag |
|---|---|---|---|
| Emergency-info | Call vet | button | 🟠 |
| Emergency-allowed | Call vet now | button | 🟠 **"now" only sometimes** |
| Emergency, Shared | Call Eva | button | 🟠 vs `Contact Eva` / `Contact owner` |
| Shared-pet-view | Contact Eva | button | 🔴 Call vs Contact (§11-A) |
| Shared-pet-view | Contact owner | nav-action | 🔴 |

### Edit / delete / lifecycle

| Screen(s) | Text | Type | Flag |
|---|---|---|---|
| section rows | Edit → | button | 🟠 vs bare `Edit` |
| dossier | Edit pet details | button | |
| Edit-care-note | Delete this note | button | 🟠 |
| Edit-health-record | Delete this record | button | 🟠 |
| Edit-pet | Archive Miso | button | |
| Edit-pet | Permanently delete Miso | button | 🟠 vs `Delete` / `Delete profile` |
| Owner (Me) | Delete profile | button | 🟠 |
| delete modals | Delete | button | 🟠 **five delete labels** |
| Who-has-access, grant | Revoke / Revoke access | button | 🟠 |

### Auth

| Screen(s) | Text | Type | Flag |
|---|---|---|---|
| Login | Log in | button | |
| Owner, Logout-modal | Log out | button | |
| Logged-out | Log back in | button | |
| Login, Sign-up | Continue with Google / Continue with Apple | button | |
| Sign-up | Create account | button | 🔴 screen/concept is "Sign up" (§11-A) |
| Forgot-password | Send reset link | button | |

### Misc actions

| Screen(s) | Text | Type | Flag |
|---|---|---|---|
| Reminder-detail | Mark done / Snooze / **Action** | button | 🟣 "Action" is a **placeholder label** (§11-D) |
| Reminder-done | Back to What's due / Undo | button | |
| Upload-photo | Take photo / Choose from library / Use photo | button | |
| Document-view | Download PDF / Share | button | |
| home-error | Go to My Pets | button | |
| home-empty | Clear search | button | |
| celebration modal | Got it / Maybe later — keep it stored here | button | |

---

## 3 · Screen titles & section headings

| Screen(s) | Text | Type | Flag |
|---|---|---|---|
| dossier | My pet | title | 🔴 vs `Pet dossier`, `Miso` as title (§11-A) |
| section pages | Health & jabs · Documents & passport · Insurance · Personality & care · Vet & appointments | title | (canonical section names) |
| Emergency | Emergency info & authorisation | title | 🔴 **-isation** vs `authorization` elsewhere (§11-A) |
| Add-record | Add vaccination | title | 🔴 vaccination/vaccine/jab (§11-A) |
| Add-care-note | Add note | title | |
| Health-and-jabs | Vaccinations / Health records | heading | 🔴 "Vaccinations" but section is "…jabs" |
| Owner (Me) | Owner | title | |
| Shared-pet-view | Personality & Care · Health Summary · Vet Contact · Documents | card heading | 🔴 Title Case here, sentence case in owner app (§11-A) |

---

## 4 · Empty states

| Screen(s) | Text | Type | Flag |
|---|---|---|---|
| My-Pets-empty | No pets yet | heading | |
| My-Pets-empty | Add your first pet to keep their health, documents, and care info in one place. | body | 🟠 near-duplicate of next |
| Set-up-a-pet-empty | Add your first pet to start building their health records, documents, and care notes — all in one place. | body | 🟠 **two wordings for the same empty state** |
| Health-and-jabs-empty | No health records yet | heading | |
| Health-and-jabs-empty | Add Miso's first vaccination or health record. Track jabs, checkups, conditions, and medications — all in one place. | body | 🔴 jab + vaccination + record in one line |
| Documents-empty | No documents yet | heading | |
| Documents-empty | Upload Miso's first document — pet passport, microchip registration, insurance policy, or vaccination certificate. | body | |
| Insurance-empty | No insurance added | heading | 🟠 "added" vs "saved"/"yet" pattern |
| Vet-empty | No vet clinic saved | heading | 🟠 "saved" vs "yet"/"added" |
| Vet-empty | Add Miso's vet clinic so you can call them in one tap when it matters. You can also track upcoming and past appointments here. | body | |
| Personality-empty | What should a sitter know about Miso? | heading | |

---

## 5 · Status & badges

| Screen(s) | Text | Type | Flag |
|---|---|---|---|
| Health, Whats-due | Up to date · Due soon · Overdue | status | (consistent set — OK) |
| Vet, Whats-due | Confirmed · Upcoming | status | |
| grant | Active · Expired / revoked | status | |
| dossier cards | k of 6 sections filled | status | |
| dossier cards | Profile filled · Updated 5 days ago | status | 🔴 "Profile filled" for the Personality section (§11-A) |

---

## 6 · Loading & error messages

| Screen(s) | Text | Type | Flag |
|---|---|---|---|
| all `-error` screens | **Something went wrong** | heading | 🟡 **AI cliché — appears as the heading on 10 error screens** |
| Add-*-error | Something went wrong on our end. Your text is still here — try saving again. | body | 🟡 opens with the cliché |
| Share-a-pet-error | Something went wrong while generating Miso's share link. Check your connection and try again… | body | 🟡 |
| most `-error` | Couldn't load Miso's [health records / insurance / vet information / dossier / …]. Check your connection and try again. | body | ✅ specific & good — keep as the model |
| Add-record-error | Couldn't save this record. Check your connection and try again. | body | ✅ |
| Emergency-allowed-error | Check your connection and try again. If urgent, call the vet or owner directly. | body | ✅ good escalation |
| Shared-pet-view-error | This link has expired | heading | |
| Share-a-pet-error | Couldn't create the link | heading | 🟠 vs body "Something went wrong while generating…" — two voices in one screen |
| `-loading` screens | Loading Miso's [care profile / shared profile / …]… | body | 🔴 profile/dossier drift (§11-A) |
| Login-loading | Logging you in… | heading | |
| Section-saving | Saving… | heading | |
| Section-saving | Let us save your updated info so we can store it and keep it accessible for you at any moment. | body | 🟡 slightly overwrought for a spinner |

---

## 7 · Field labels, placeholders & options

### Labels (representative)

| Screen(s) | Text | Type | Flag |
|---|---|---|---|
| Add-record | Vaccine name * | field label | 🔴 vaccine (§11-A) |
| Add-record | Date given * · Next due date · Administering vet · Notes · Proof / attachment | field label | |
| Set-up-a-pet | Pet name * · Species * · Breed · Sex · Microchip · Photo | field label | |
| Owner (Me) | Full name · Email · Phone · Language | field label | |

### Placeholders

| Screen(s) | Text | Type | Flag |
|---|---|---|---|
| all sections | Search sections, records, documents… | placeholder | (consistent ×9 — OK) |
| Set-up-a-pet | **e.g. Miso, Miso, Buddy** | placeholder | 🟣 **BUG — "Miso" listed twice** |
| Add-record | e.g. Rabies, DHPP, Leptospirosis | placeholder | ✅ |
| various | e.g. Dr. Müller, Tierklinik am Stadtpark · e.g. Border Terrier, Tabby stray · e.g. Lassie, Petplan, Agila | placeholder | ✅ good `e.g.` pattern |
| Add-record | Context-aware form — fields adapt to record type. Shown: vaccination. | body | 🟣 **dev/meta note leaked into UI** |
| Login | you@example.com · •••••••• · 8+ characters | placeholder | |

### Dropdown options (all controlled — listed for the source of truth)

Record type: `Vaccination · Health & jabs · Documents & passport · Insurance · Vet & appointments · Personality & care · Other` — 🔴 "Vaccination" as a type but section is "Health & jabs".
Care category: `Favourite food & treats · Likes & temperament · Not friendly with (warning) · Behaviour notes · Walking & routines · Grooming & hygiene · Special requirements · Other`.
Role: `Carer (read-only) · Vet (can add records) · Co-owner (full edit)`. Sex: `— · Male · Female · Unknown`. Species: `Dog · Cat`. Expiry: `1 week · 1 month · Permanent · Custom date`. Reminder lead: `1 week before · 2 weeks before · 1 month before`. Language: `English · Deutsch`. Payment: `Carer pays, owner reimburses · Owner's card on file at vet`.

---

## 8 · Confirmations & destructive actions

| Screen(s) | Text | Type | Flag |
|---|---|---|---|
| Reminder-done | Nice — marked done | heading | 🟡 "Nice —" (see §11-C) |
| home-new done modal | Nice — Miso's dossier is ready! | heading | 🟡 `!` |
| home-progress-6 modal | **Awesome — all set up! 🎉** | heading | 🟡 emoji + `!` + "Awesome" |
| Share-success | Miso's share link is ready | heading | |
| Share-sent | **Your pet's info was shared! 🎉** | heading | 🟡 emoji + `!` |
| Share-sent | Shared! | heading | 🟡 `!` |
| Shared-pet-view (last) | Done! This is what your sitter sees | heading | 🟡 `!` |
| Delete-profile modal | Delete profile? | heading | |
| Delete-profile modal | This permanently removes your account, Miso's and Cheetah's dossiers, and every share link. This cannot be undone. | body | ✅ clear & appropriately serious |
| Log-out modal | Log out? | heading | |

---

## 9 · Consistency of the back-button pattern

Header back-buttons mostly follow **`← [destination]`**: `← Dossier`, `← My Pets`, `← Share`, `← Who has access`, `← What's due`, `← Documents`, `← Emergency info`, `← Miso's profile`. **Exception:** `← Cancel` (add/edit forms) uses an *action* word in the destination slot. 🟠

`section` / `block`: **checked — consistent.** Product copy only ever says "section" (`View in section`, `Search sections`, `k of 6 sections filled`). "block" appears **only** inside user-authored walking-routine sample text ("around the block"), never as UI. ✅

---

## 10 · Sample / user-authored content — 📝 **we do not control or rewrite this**

These are demo values standing in for what a real owner would type. They must **not** be treated as product copy; when real content design starts, they stay as illustrative examples only.

| Kind | Sample values in the prototype |
|---|---|
| Pet identity | Miso (Dog · Border Terrier · Female · DOB 2022-03-15 · Microchip 276 098 106 412 345); Cheetah (Cat · Tabby stray · Female) |
| Owner identity | Eva Schmidt · eva.schmidt@example.com · +49 171 9876543 · Berlin |
| Vaccine / record names | Rabies · DHPP · Leptospirosis · Dental cleaning · Annual checkup · General check-up · Vaccination (Rabies + DHPP) · Dermatitis follow-up |
| Care-note bodies | "Royal Canin Maxi Adult, 350 g twice daily…", "Calm and affectionate. Loves belly rubs…", "Small rodents (strong prey drive)…", "Morning walk 30 min (around the block)…", etc. |
| Vet / clinic | Tierklinik am Stadtpark · Dr. Müller · Parkstraße 12, 10115 Berlin · +49 30 1234567 |
| Insurance | Lassie Haustierversicherung · OP-Schutz Plus · LSS-2024-0847291 · €29.90/month |
| Documents | EU Pet Passport DE-0812345 · Microchip registration · Rabies certificate · Pedigree papers |
| Emergency | Carer authorization up to €500 · allowed meds notes |
| Dates / numbers | 15 Mar 2027, 1 Oct 2026, 12 Nov 2026, etc. |

*(The `e.g. …` placeholders in §7 are product copy — they're the app suggesting what to type — even though they contain sample-flavoured words. Only actual field **values** and body content above are user territory.)*

---

## 11 · Consistency findings (the flag summary)

### A. 🔴 Same thing, different names — **decide one term each**

| Concept | Terms found in the wild | Where |
|---|---|---|
| The owner's whole pet record | **dossier** ("Pet dossier", "← Dossier", "Miso's dossier") **vs** **profile** ("Miso's profile", "care profile", "Loading Miso's shared profile") **vs** title **"My pet"** vs pet name as title ("Miso") | dossier, all `-loading`/`-error`, Shared-pet-view |
| The Personality & care section | called a **section** in the dossier, but its status reads **"Profile filled"** and its copy says the note "will appear in **the profile**" | dossier card, Personality, Add-care-note |
| The sitter's read-only view | **"Shared pet view"** (name) vs **"Miso's profile"** (back link) vs **"shared profile"** (loading) vs **"shared view"** (body) vs the mockup's **"Shared card"** | Shared-pet-view + states |
| A shot | **jab** ("Health & jabs") vs **vaccine** ("+ Add vaccine") vs **vaccination** ("Add vaccination", "Vaccinations", option "Vaccination") | Health-and-jabs, Add-record |
| Emergency permissions | **authorisation** ("Emergency info & authorisation") vs **authorization** ("Save authorization", "authorization settings", "Emergency authorization setup") | Emergency screens — also a **British/American spelling** split (favourite/behaviour are British → pick `-isation`) |
| Creating an account | screen/nav **"Sign up"** vs button **"Create account"** | Sign-up |
| Contacting a person | **Call** ("Call vet", "Call Eva") vs **Contact** ("Contact Eva", "Contact owner") | Emergency, Shared-pet-view |

### B. 🟠 Same action, different button labels — **pick one pattern**

- **Add:** `Add` / `+ Add` / `Add a pet` / `Add your first pet` / `+ Add your first pet` / `+ Add info` / `Upload` — the **`+` prefix is applied inconsistently**, and "Upload" competes with "Add" for documents.
- **Save:** `Save` / `Save record` / `Save note` / `Save pet` / `Save authorization` / `Save settings` / `Save changes` — bare "Save" vs "Save [noun]" vs "Save changes".
- **Retry:** `Try again` (×17) / `Retry` / `Retry save`.
- **Delete:** `Delete` / `Delete this note` / `Delete this record` / `Delete profile` / `Permanently delete Miso`.
- **Preview sharing:** `Preview as sitter` vs `See what your sitter sees`.
- **Share again:** `Share with someone new` vs `Share with a pet sitter` vs `Re-share`.
- **Back:** `← [destination]` everywhere **except** `← Cancel`.
- **Edit:** `Edit` vs `Edit →` vs `Edit pet details`.

### C. 🟡 AI clichés & over-cheerful tone

- **"Something went wrong"** — the classic filler, used as the **heading on 10 error screens**. (The *bodies* underneath are specific and good — the generic heading is the weak link.)
- **Emojis in headings:** `Awesome — all set up! 🎉`, `Your pet's info was shared! 🎉`.
- **Exclusive exclamation cluster:** `Shared!`, `Done! This is what your sitter sees`, `Nice — Miso's dossier is ready!`, `Nice — marked done`, `Awesome — all set up!` — repeated "Nice —" / "Awesome" openers.
- **Overwrought for context:** the saving spinner's "Let us save your updated info so we can store it and keep it accessible for you at any moment."

### D. 🟣 Stray / placeholder / meta text still in the UI

- **`e.g. Miso, Miso, Buddy`** — pet-name placeholder lists "Miso" twice (bug).
- **`Context-aware form — fields adapt to record type. Shown: vaccination.`** — a developer/meta note showing in the Add-record form.
- **`Action`** — the primary button on the Reminder-detail screen is literally labelled "Action" (placeholder that shipped).

### E. ⚪ Prototype annotations (not product copy — strip before shipping)

Wireframe **zone-labels** are visible on screen but are scaffolding, not UI text: `Pet identity`, `Counter`, `Search & filter`, `Card entry point → …`, `Main job · step n of 4`, `R1, R3`, etc. Listed here only so they aren't mistaken for microcopy to rewrite — they should be **removed** in the visual-design build.

---

*Next step (not this pass): turn §11 into decisions — one canonical term per concept, one label per action, an error/empty/success voice spec — and apply them back across the 123 screens.*

---

## 12 · Rewrite log — Batch 1 · My Pets + states

First screens rewritten against [`voice.md`](voice.md). Product copy only — headings, buttons, state messages. **Prototype chrome** (left sidebar nav, breadcrumb flow-steps, page `<title>`, CSS comments) still say "My Pets" by their screen name; that is scaffolding (§10/§E), out of scope, left untouched. **User content** (pet names, notes) untouched (§10, 📝).

Files: `My-Pets.html`, `My-Pets-empty.html`, `My-Pets-error.html`, `My-Pets-loading.html`.

| Screen | Element | Before | After | Rule applied |
|---|---|---|---|---|
| My Pets (all states) | Screen heading `<h1>` | My Pets | **Your pets** | Glossary — address the reader as **you**, not first-person "My"; sentence case (owner app). |
| My Pets (list) | Button | Add a pet | Add a pet | *Unchanged* — action verb + object (Microcopy · Button). |
| My Pets (list) | Card status | 5 of 6 sections filled · Updated 2 days ago | 5 of 6 sections filled · Updated 2 days ago | *Unchanged* — glossary term **section**; on-voice. |
| My Pets (list) | Card titles / notes | Miso · Cheetah · … | *(untouched)* | 📝 user content (§10) — never rewritten. |
| My Pets · empty | Empty headline | No pets yet | No pets yet | *Unchanged* — glossary **"No … yet"** pattern. |
| My Pets · empty | Empty body | Add your first pet to keep their health, documents, and care info in one place. | **Add your first pet to start their card — jabs, documents, and care, ready for the vet or a sitter.** | Principle 1 (drop the completeness cliché "in one place") + Principle 3 (end on the moment) + Glossary (**card, jabs**); Microcopy · Empty state leads to the action. |
| My Pets · empty | Empty CTA | Add your first pet | Add your first pet | *Unchanged* — action verb + object (Microcopy · Button). |
| My Pets · error | Error headline | ~~Something went wrong~~ | **Couldn't load your pets** | **Forbidden** list — replace the cliché; Microcopy · Error names what failed. |
| My Pets · error | Error body | Couldn't load your pets. Check your connection and try again. | **Check your connection and try again.** | Microcopy · Error — "what happened" moves to the heading, body carries "what to do" (no duplication, no apology). |
| My Pets · error | Error button | Try again | Try again | *Unchanged* — action verb; canonical retry label (§11-B winner). |
| My Pets · loading | Loading text | Loading your pets… | Loading your pets… | *Unchanged* — names exactly what is loading (Microcopy · Loading). |

**Four strings changed** (heading ×1, empty body, error headline, error body); the rest were already on-voice and are logged as unchanged for a complete before/after. No markup or structure changed — text nodes only.
