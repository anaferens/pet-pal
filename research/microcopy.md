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

### Batch 2 · Emoji & celebration sweep

Triggered by a 🎉 spotted on the share-success screen. Scanned all 123 files for emoji in product copy: **only two decorative pictographic emoji existed** (both 🎉, both already on the Forbidden list), plus two bare celebratory `✓`. All removed, and the celebratory copy around them rewritten per the Success rule (state the fact, don't celebrate).

| Screen | Element | Before | After | Rule applied |
|---|---|---|---|---|
| Share-sent | Screen heading | Shared**!** | **Shared** | Forbidden — drop the "!". |
| Share-sent | Success headline | Your pet's info was shared! **🎉** | **Miso's card is shared** | Forbidden (emoji + "!"); Glossary (**card**); Microcopy · Success — no celebrating. |
| Share-sent | Success body | Now more people know about your Miso — and can care for her exactly the way she needs. | **Your sitter can open Miso's card from the link — no app or account needed. It lasts a month, and you can stop it any time.** | Principle 4 (sharing is safe: no account + revocable) + Principle 2 (precise); glossary (**card, sitter**). Facts aligned with `Share-success.html`. |
| home-progress-6 | Completion heading | Awesome — all set up! **🎉** | **Miso's card is ready** | Forbidden (emoji + "!" + "Awesome"); Glossary (**card**). |
| home-progress-6 | Completion body | Miso's **dossier** is **complete**. Everything is stored safely here — and you can share it with your trusted person or pet sitter any moment. | **It's all saved and stored safely. You can share Miso's card with your sitter whenever you like.** | Principle 1 (drop the completeness claim "complete"); Glossary (**dossier → card**); Principle 4. |
| Forgot-password | Success heading | Check your inbox **✓** | **Check your inbox** | Forbidden — decorative ✓. |
| Emergency-info-firstrun | Status label | Set up **✓** | **Set up** | Forbidden — decorative ✓. |

**Kept — functional glyphs, not emoji:** the `<span class="check">✓</span>` section-complete marks (9 screens), the `✕` close buttons (4 screens), and the `★`/`→` breadcrumb flow-markers (prototype chrome). These carry UI meaning, so they stay. If you want the section-complete ✓ gone too, say so and I'll swap it for a text state.

---

## 13 · Rewrite log — Batch 3 · all remaining screens

The remaining screen set (110 files, 15 clusters) rewritten to [voice.md](voice.md) by parallel sub-agents — one per screen-cluster — then reconciled for cross-screen consistency (§14 below). Rows are grouped by cluster, Before → After. User-authored content (§10) and prototype chrome (§E) were left untouched throughout; this pass covers headings, buttons, field labels/hints, and empty/error/loading/success/destructive messages.

### Account & auth

| Screen | Area | Element | Before | After |
|---|---|---|---|---|
| Login | main | hint (tagline) | One trusted place for everything about your pet. | Everything about your pet, in one trusted place. |
| Login | main | heading | Welcome back | Log in |
| Login | main | field label (link) | Forgot password? | Forgot your password? |
| Login-error | main | hint (tagline) | One trusted place for everything about your pet. | Everything about your pet, in one trusted place. |
| Login-error | main | heading | Welcome back | Log in |
| Login-error | main | field label (link) | Forgot password? | Forgot your password? |
| Sign-up | main | hint (tagline) | Create a profile — then set up your first pet. | Create your account — then set up your first pet. |
| Logged-out | main | heading | You're signed out | You're logged out |
| Logged-out | main | status (deleted state, via script) | Profile deleted | Account deleted |
| Logged-out | main | success (deleted state, via script) | Your account and all pet data have been removed. Thanks for trying PetPal — you can create a new profile any time. | Your account and all pet data have been removed. Thanks for trying PetPal — you can create a new account any time. |
| Me | main | destructive button | Delete profile | Delete account |
| Me | modal | destructive heading | Delete profile? | Delete account? |
| Me | modal | destructive body | This permanently removes your account, Miso's and Cheetah's dossiers, and every share link. This cannot be undone. | This permanently removes your account, Miso's and Cheetah's cards, and every share link. It can't be undone. |
| Me | modal | destructive (confirm button) | Delete | Delete account |

### Home / dashboard

| Screen | Area | Element | Before | After |
|---|---|---|---|---|
| Home · search empty (home-empty.html) | main | empty | Nothing in Miso's dossier matches "rabies cert." Try a broader term or clear the search to see all sections. | Nothing in Miso's card matches "rabies cert." Try a broader term or clear the search to see all sections. |
| Home · error (home-error.html) | main | error | Something went wrong | Couldn't load Miso's card |
| Home · error (home-error.html) | main | error | Couldn't load Miso's dossier. Check your connection and try again. | Check your connection and try again. |
| Home · loading (home-loading.html) | main | loading | Loading… | Loading Miso's card… |
| Home · new pet (home-new.html) | main | empty | Nice — Miso's dossier is ready! | Miso's card is set up |
| Home · new pet (home-new.html) | main | empty | Let's add some notes: jabs, health records, personality & care, emergency info, vet & appointment notes, pet passport, insurance — keep everything in one place and share it when needed. | Add jabs, documents, and care notes whenever it suits you — ready for the vet or a sitter when it matters. |
| Home · new pet (home-new.html) | main | button | + Add info | + Add a section |
| Home · new pet (home-new.html) | modal | hint | Add important health related info about your pet | Jabs, check-ups, and health records |
| Home · new pet (home-new.html) | modal | hint | Add official documents like passport, so you always have them nearby | EU pet passport, microchip cert, pedigree papers |
| Home · new pet (home-new.html) | modal | hint | Add your pet's insurance | Policy, coverage and renewal reminders |
| Home · new pet (home-new.html) | modal | hint | Anything about your pet's personality, preferences, behaviour etc | Food, temperament, warnings, routines — what a sitter needs |
| Home · new pet (home-new.html) | modal | hint | Have an appointment soon? Keep it here so we can remind you on time | Your vet clinic and upcoming appointments |
| Home · setup 1/6–6/6, success (Miso), success (single pet) | header | heading | My pet | Miso |
| Home · success (Cheetah) | header | heading | My pet | Cheetah |
| Home · success (Miso), success (single pet) | main | status | Profile filled · Updated 5 days ago | Filled · Updated 5 days ago |
| Home · success (Miso), success (single pet) | main | status | Set up · Vet, meds, contacts, authorization | Set up · Vet, meds, contacts, authorisation |

### Set up a pet & identity

| Screen | Area | Element | Before | After |
|---|---|---|---|---|
| Set-up-a-pet, Set-up-a-pet-empty, Set-up-a-pet-error | header | button | ← My Pets | ← Your pets |
| Set-up-a-pet | main | hint | e.g. Miso, Miso, Buddy | e.g. Miso, Buddy |
| Set-up-a-pet | main | hint | MVP: dogs and cats only. | Dogs and cats only, for now. |
| Set-up-a-pet | main | button | Save pet | Save |
| Set-up-a-pet-empty | main | empty | Add your first pet to start building their health records, documents, and care notes — all in one place. | Add your first pet to start their card — jabs, documents, and care, ready for the vet or a sitter. |
| Set-up-a-pet-empty | main | button | + Add your first pet | Add your first pet |
| Set-up-a-pet-loading | main | loading | Saving… | Saving your pet… |
| Set-up-a-pet-loading, Edit-pet-loading | main | loading | Let us save your updated info so we can store it and keep it accessible for you at any moment. | *(removed — heading already names what's saving)* |
| Upload-photo | main | status | photo selected ✓ | photo selected |
| Edit-pet, Edit-pet-error | header | button | ← Dossier | ← Miso's card |
| Edit-pet, Edit-pet-error, Edit-pet-loading | header | button | ← Back to Dossier | ← Back to Miso's card |
| Edit-pet, Edit-pet-error | main | field label | EU Passport number | EU Pet Passport number |
| Edit-pet, Edit-pet-error | main | status | Photo removed ✓ | Photo removed |
| Edit-pet | main | button | Save changes | Save |
| Edit-pet, Edit-pet-error | main | destructive | Are you sure? This action cannot be undone. | Are you sure? |
| Edit-pet, Edit-pet-error, Edit-pet-loading | main | destructive | This removes all of Miso's data -- dossier, records, documents, shares -- and cannot be undone. | This removes all of Miso's jabs, documents, notes, and share links. It can't be undone. |
| Edit-pet-error | main | error | Couldn't save changes to Miso's profile. | Couldn't save Miso's details. |
| Edit-pet-loading | main | loading | Saving… | Saving Miso's details… |

### Health & jabs

| Screen | Area | Element | Before | After |
|---|---|---|---|---|
| Health & jabs | header | button | ← Dossier | ← Miso's card |
| Health & jabs | main | Section heading | Vaccinations | Jabs |
| Health & jabs | main | button | + Add (inline, next to "Jabs", desktop) | + Add a jab |
| Health & jabs | main | button | + Add (inline, next to "Health records", desktop) | + Add a health record |
| Health & jabs | main | button | + Add vaccine (FAB menu) | + Add a jab |
| Health & jabs | main | button | + Add health record (FAB menu) | + Add a health record |
| Health & jabs · empty | header | button | ← Dossier | ← Miso's card |
| Health & jabs · empty | header | button | Add | Add a jab |
| Health & jabs · empty | main | Empty headline | No health records yet | No jabs yet |
| Health & jabs · empty | main | Empty body | Add Miso's first vaccination or health record. Track jabs, checkups, conditions, and medications — all in one place. | Add Miso's first jab — kennels and groomers will ask for it. |
| Health & jabs · empty | main | Empty CTA | Add first health record | Add a jab |
| Health & jabs · error | header | button | ← Dossier | ← Miso's card |
| Health & jabs · error | header | button | Add | Add a jab |
| Health & jabs · error | main | Error headline | Something went wrong | Couldn't load Miso's health records |
| Health & jabs · error | main | Error body | Couldn't load Miso's health records. Check your connection and try again. | Check your connection and try again. |
| Health & jabs · loading | header | button | ← Dossier | ← Miso's card |
| Health & jabs · loading | header | button | Add | Add a jab |
| Health & jabs · first record | header | button | ← Dossier | ← Miso's card |
| Health & jabs · first record | main | Section heading | Vaccinations | Jabs |
| Health & jabs · first record | main | button | + Add (inline, next to "Jabs", desktop) | + Add a jab |
| Health & jabs · first record | main | button | + Add (inline, next to "Health records", desktop) | + Add a health record |
| Health & jabs · first record | main | button | + Add vaccine (FAB menu) | + Add a jab |
| Health & jabs · first record | main | button | + Add health record (FAB menu) | + Add a health record |
| Health & jabs · 1 record | header | button | ← Dossier | ← Miso's card |
| Health & jabs · 1 record | main | Section heading | Vaccinations | Jabs |
| Health & jabs · 1 record | main | Empty (inline) | No vaccines yet — tap + and choose "Add vaccine". | No jabs yet — tap + and choose "Add a jab". |
| Health & jabs · 1 record | main | button | + Add (inline, next to "Jabs", desktop) | + Add a jab |
| Health & jabs · 1 record | main | button | + Add (inline, next to "Health records", desktop) | + Add a health record |
| Health & jabs · 1 record | main | button | + Add vaccine (FAB menu) | + Add a jab |
| Health & jabs · 1 record | main | button | + Add health record (FAB menu) | + Add a health record |
| Add health record | main | hint | Context-aware form — fields adapt to record type. Shown: health record. | Record type is pre-selected — change it if this belongs somewhere else. |
| Add health record | main | field option | Vaccination (Record type dropdown option) | Jab |
| Add health record | main | button | Save record | Save |
| Edit health record | main | field option | Vaccination (Record type dropdown option) | Jab |
| Edit health record | main | button | Save changes | Save |

### Documents & passport

| Screen | Area | Element | Before | After |
|---|---|---|---|---|
| Documents & passport | header | button (back) | ← Dossier | ← Miso's card |
| Documents & passport · empty | header | button (back) | ← Dossier | ← Miso's card |
| Documents & passport · empty | header | button | Upload | Add a document |
| Documents & passport · empty | main | empty | Upload Miso's first document — pet passport, microchip registration, insurance policy, or vaccination certificate. | Add Miso's first document — the EU Pet Passport, microchip registration, insurance policy, or vaccination certificate — ready for the vet or a sitter. |
| Documents & passport · empty | main | button | Upload first document | Add a document |
| Documents & passport · error | header | button (back) | ← Dossier | ← Miso's card |
| Documents & passport · error | header | button | Upload | Add a document |
| Documents & passport · error | main | error | Something went wrong | Couldn't load Miso's documents |
| Documents & passport · error | main | error | Couldn't load Miso's documents. Check your connection and try again. | Check your connection and try again. |
| Documents & passport · firstrun | header | button (back) | ← Dossier | ← Miso's card |
| Documents & passport · loading | header | button (back) | ← Dossier | ← Miso's card |
| Documents & passport · loading | header | button | Upload | Add a document |
| Document view | main | field label | Vaccine | Vaccination |
| Document view | main | field label | Chip number | Microchip number |
| Document view | main | button (link) | Replace / update this document → | Update this document → |
| Add document | main | hint | e.g. EU pet passport, insurance policy | e.g. EU Pet Passport, insurance policy |
| Add document | main | hint | The document file — passport, certificate, or policy (PDF or photo). | The document file — EU Pet Passport, certificate, or policy (PDF or photo). |
| Add document | main | hint | e.g. No adverse reaction. Batch #LR-2026-041. | e.g. Where you keep the original, or anything else worth noting. |

### Insurance

| Screen | Area | Element | Before | After |
|---|---|---|---|---|
| Insurance | header | button | ← Dossier | ← Miso's card |
| Insurance (empty) | header | button | ← Dossier | ← Miso's card |
| Insurance (empty) | main | empty | No insurance added | No insurance yet |
| Insurance (empty) | main | empty | Add Miso's insurance policy to track renewal dates, coverage details, and keep the policy document handy for vets and sitters. | Add Miso's insurance policy — renewal date, coverage, and the policy document, ready for the vet or a sitter. |
| Insurance (empty) | main | button | Add insurance | Add a policy |
| Insurance (error) | header | button | ← Dossier | ← Miso's card |
| Insurance (error) | main | error | Something went wrong | Couldn't load Miso's insurance |
| Insurance (error) | main | error | Couldn't load Miso's insurance data. Check your connection and try again. | Check your connection and try again. |
| Insurance (first policy) | header | button | ← Dossier | ← Miso's card |
| Insurance (loading) | header | button | ← Dossier | ← Miso's card |
| Add insurance | header | heading | Add insurance | Add a policy |
| Add insurance | main | hint | Context-aware form — fields adapt to record type. Shown: insurance. | *(removed — left empty, matching the fix already applied in Add-record.html)* |
| Add insurance | main | field label | Vaccination *(record-type dropdown option)* | Jab |
| Add insurance | main | field label | Date | Start date |
| Add insurance | main | field label | Next due date | Renewal date |

### Personality & care

| Screen | Area | Element | Before | After |
|---|---|---|---|---|
| Personality & care (all 11 states: success, empty, error, loading, fill1–6, firstrun) | header | button | ← Dossier | ← Miso's card |
| Personality & care (success, fill1–6, firstrun) | main | status | This is what your sitter will see in the shared view. | This is what your sitter sees on Miso's shared card. |
| Personality & care (success, fill1–6, firstrun) | main | button | + Add another note | Add a note |
| Personality & care (success, fill1–6, firstrun) | main | button (FAB, accessibility label) | Add | Add a note |
| Personality & care (empty, fill1–fill5 — one row per not-yet-filled category card) | main | button | + Add | Add |
| Personality & care · error | main | error | Something went wrong | Couldn't load Miso's care notes |
| Personality & care · error | main | error | Couldn't load Miso's care profile. Check your connection and try again. | Check your connection and try again. |
| Personality & care · loading | main | loading | Loading Miso's care profile… | Loading Miso's care notes… |

### Care notes

| Screen | Area | Element | Before | After |
|---|---|---|---|---|
| Add care note | header | heading | Add note | Add a note |
| Add care note | main | hint | Add a note about Miso's personality, food, routines, or anything a sitter should know. This will appear in the shared profile. | Add a note about Miso's personality, food, routines, or anything a sitter should know. This will appear on Miso's card. |
| Add care note | main | hint | Determines where this note appears in the profile. | Determines where this note appears in Personality & care. |
| Add care note | main | button | Save note | Save |
| Add care note (error) | header | heading | Add note | Add a note |
| Add care note (error) | main | error | Could not save note. | Couldn't save the note. |
| Add care note (error) | main | error | Something went wrong on our end. Your text is still here — try saving again. | Check your connection and try again. Your note is still here. |
| Add care note (error) | main | button | Retry save | Try again |
| Add care note (loading) | main | loading | Saving… | Saving the note… |
| Add care note (loading) | main | loading | Let us save your updated info so we can store it and keep it accessible for you at any moment. | *(removed — heading alone now names what's loading)* |
| Edit care note | main | hint | Edit this note. Changes will be visible to anyone you've shared Miso's profile with. | Edit this note. Changes will be visible to anyone you've shared Miso's card with. |
| Edit care note | main | button | Save changes | Save |
| Edit care note (error) | main | error | Could not save note. | Couldn't save the note. |
| Edit care note (error) | main | error | Something went wrong on our end. Your text is still here — try saving again. | Check your connection and try again. Your note is still here. |
| Edit care note (error) | main | button | Retry save | Try again |
| Edit care note (loading) | main | loading | Saving… | Saving the note… |
| Edit care note (loading) | main | loading | Let us save your updated info so we can store it and keep it accessible for you at any moment. | *(removed — heading alone now names what's loading)* |

### Vet & appointments

| Screen | Area | Element | Before | After |
|---|---|---|---|---|
| Vet & appointments (success) | header | button | ← Dossier | ← Miso's card |
| Vet & appointments · clinic only | header | button | ← Dossier | ← Miso's card |
| Vet & appointments · clinic only | main | button | + Add appointment | Add an appointment |
| Vet & appointments · empty | header | button | ← Dossier | ← Miso's card |
| Vet & appointments · empty | header | button | Add | Add an appointment |
| Vet & appointments · empty | main | empty (heading) | No vet clinic saved | No vet clinic yet |
| Vet & appointments · empty | main | empty (body) | Add Miso's vet clinic so you can call them in one tap when it matters. You can also track upcoming and past appointments here. | Add Miso's vet clinic — call them in one tap when it matters, and track appointments here too. |
| Vet & appointments · empty | main | empty (button) | Add vet clinic | Add a clinic |
| Vet & appointments · error | header | button | ← Dossier | ← Miso's card |
| Vet & appointments · error | header | button | Add | Add an appointment |
| Vet & appointments · error | main | error (heading) | Something went wrong | Couldn't load Miso's vet information |
| Vet & appointments · error | main | error (body) | Couldn't load Miso's vet information. Check your connection and try again. | Check your connection and try again. |
| Vet & appointments · firstrun | header | button | ← Dossier | ← Miso's card |
| Vet & appointments · firstrun | main | button | + Add appointment | Add an appointment |
| Vet & appointments · loading | header | button | ← Dossier | ← Miso's card |
| Vet & appointments · loading | header | button | Add | Add an appointment |
| Vet & appointments · loading | main | loading | Loading Miso's vet info… | Loading Miso's vet information… |
| Add a vet clinic | header | heading | Add vet clinic | Add a clinic |
| Add an appointment | header | heading | Add appointment | Add an appointment |
| Add an appointment | main | hint (stray dev note) | Context-aware form — fields adapt to record type. Shown: vet & appointments. | *(removed — leaked dev/meta note, not product copy; emptied the text node, left the `<p>` tag in place)* |
| Add an appointment | main | field label | Date | Date of the appointment |
| Add an appointment | main | field label (dropdown option) | Vaccination | Jab |

**Unchanged but reviewed (kept — already on-voice or out of scope):**
- Screen heading "Vet & appointments" — canonical section name from the glossary, correct as-is.
- Status badges "Confirmed" / "Up to date" — canonical, already consistent app-wide.
- "No appointments yet." (Vet-and-appointments-clinic.html, inline sub-section message) — already matches the "No … yet" pattern.
- Vet clinic data (clinic name, doctor, phone, address), appointment titles/dates (Annual checkup, Dental cleaning, Vaccination (Rabies + DHPP), Dermatitis follow-up), and all form input values — user/sample data per microcopy.md §10, left untouched.
- Field labels "Clinic / vet", "Next due date", "Administering vet", "Notes", "Proof / attachment", and all `e.g. …` placeholders — already clear, already matched the approved examples in microcopy.md §7.
- "Save" / "Cancel" / "← Cancel" on both Add-* forms — already match voice.md exactly; "← Cancel" is the sanctioned pattern-exception for form-cancel back buttons (confirmed against the already-rewritten Add-record.html, which also left it untouched).
- Zone-label annotations "Vet clinic (1-tap call)" — treated as prototype/wireframe scaffolding (like the breadcrumb and sidebar), not shipped product copy; confirmed by precedent (Health-and-jabs.html's sibling zone-label "Conditions & current meds (pinned)" was also left untouched by that screen's rewrite).

### Emergency

| Screen | Area | Element | Before | After |
|---|---|---|---|---|
| Emergency info (success/empty/error/fill1/fill2/firstrun/loading) | header | button | ← Dossier | ← Miso's card |
| Emergency info (error) | main | error | Back to dossier | Back to Miso's card |
| Emergency info (success) | main | heading | Emergency authorization | Emergency authorisation |
| Emergency info (success/firstrun) | main | button | Edit authorization → | Edit authorisation → |
| Emergency info (empty/fill1/fill2/firstrun) | main | heading | Important — authorization & allowed meds | Important — authorisation & allowed meds |
| Emergency info (empty/fill1/fill2) | main | button | + Add important / allowed meds list | + Set up authorisation & allowed meds |
| Emergency info (error) | main | error | Something went wrong | Couldn't load Miso's emergency info |
| Emergency info (error) | main | error | Couldn't load Miso's emergency info. Check your connection and try again. | Check your connection and try again. |
| Emergency & allowed (success/empty/error/loading) | header | button | ← Miso's profile | ← Miso's card |
| Emergency & allowed (success/empty/error/loading) | header | button | ← Back to Miso's profile | ← Back to Miso's card |
| Emergency & allowed (success/empty/error/loading) | header | button | Contact owner | Call owner |
| Emergency & allowed (success) | main | heading | Contact the owner | Call the owner |
| Emergency & allowed (success) | main | status | Eva has authorized you to seek emergency vet care | Eva has authorised you to seek emergency vet care |
| Emergency & allowed (success) | main | status | Up to EUR 500 | Up to €500 |
| Emergency & allowed (empty) | main | empty | No emergency info available | No emergency info yet |
| Emergency & allowed (empty) | main | empty | Eva hasn't set up emergency instructions for Miso yet. Contact Eva directly if you need guidance. | Eva hasn't set up Miso's emergency info yet. Call Eva directly if you need guidance. |
| Emergency & allowed (loading) | main | loading | Loading emergency info... | Loading emergency info… |
| Emergency auth setup (success/error/loading) | header | heading | Emergency authorization | Emergency authorisation |
| Emergency auth setup (success/error) | main | hint | The maximum your carer may authorize for emergency treatment. | The maximum your carer may authorise for emergency treatment. |
| Emergency auth setup (success) | main | button | Save authorization | Save |
| Emergency auth setup (error) | main | error | Couldn't save your authorization settings. Check your connection and try again. | Couldn't save your authorisation settings. Check your connection and try again. |
| Emergency auth setup (loading) | main | loading | Let us save your updated info so we can store it and keep it accessible for you at any moment. | Miso's authorisation settings are being saved. |

### What's due & reminders

| Screen | Area | Element | Before | After |
|---|---|---|---|---|
| Whats-due.html | main / bottom | button | Add reminder | Add a reminder |
| Whats-due-offline.html | main | button | Add reminder | Add a reminder |
| Whats-due-offline.html | main | button | Retry | Try again |
| Whats-due-offline.html | main | status | Offline — showing last saved. Some items may be out of date. | Offline — showing your last saved reminders. Some may be out of date. |
| Whats-due-empty.html | main | empty | Nothing due right now | No reminders yet |
| Whats-due-empty.html | main | empty | When you add vaccinations, appointments, or insurance, their due dates appear here automatically. | When you add jabs, appointments, or insurance, their due dates appear here automatically. |
| Whats-due-empty.html | main | button | Go to My Pets | Go to your pets |
| Whats-due-error.html | main | error | Something went wrong | Couldn't load your reminders |
| Whats-due-error.html | main | error | Couldn't load your reminders. Check your connection and try again. | Check your connection and try again. |
| Whats-due-error.html | main | link | View last saved (offline) → | View your last saved reminders → |
| Whats-due-detail.html | main | button | Action | Book vet appointment |
| Whats-due-detail.html | main | field value | Vaccination (Type row, rabies \& fvrcp reminders) | Jab |
| Whats-due-detail.html | main | status | Snoozed 1 week ✓ | Snoozed 1 week |
| Reminder-done.html | main | success | Nice — marked done | Marked done |
| Reminder-done.html | main | status | Restored ✓ | Restored |
| Reminder-settings.html | main | hint | Choose how and when PetPal reminds you about what's due — vaccinations, renewals and appointments across all your pets. | Choose how and when PetPal reminds you about what's due — jabs, renewals and appointments across all your pets. |
| Reminder-settings.html | main | field hint | Applies to vaccinations, insurance renewals and passport expiry. | Applies to jabs, insurance renewals and passport expiry. |

Notes:
- Whats-due-loading.html: no changes — "Loading your reminders…" already matches the reference "Loading <thing>…" pattern.
- "What's due" screen name and heading kept verbatim throughout (established name per brief).
- Badges (Overdue / Due soon / Upcoming), urgency-group headings (Overdue / Due this month / Coming up), pet filter tabs (All pets / Miso / Cheetah), and the day-filter fallback ("Nothing due on this day — pick another date, or browse below.") were reviewed and left unchanged — already on-voice, consistent controlled vocabulary.
- Reminder titles, due dates, clinic/policy names, and pet identity (Miso, Cheetah, breed, sex) were left untouched as user data throughout, per instructions.
- The `<footer class="d-footer">` line on every screen (e.g. "What's due · desktop adaptation · reminders hub across all pets") was left untouched — confirmed via cross-file grep to be a site-wide wireframe/dev scaffolding template ("[screen] · [state] · [note]", e.g. "error state · fetch failed", "loading state · skeleton placeholder") used identically across ~35 other screens, not real product copy.

### Share a pet

| Screen | Area | Element | Before | After |
|---|---|---|---|---|
| Share a pet | header | button | ← Dossier | ← Miso's card |
| Share a pet | header | heading | Share Miso | Share Miso's card |
| Share a pet | main | field label | Full dossier | Full card |
| Share a pet | main | hint | Care info only | Personality & care only |
| Share a pet | main | field label | Health info only | Health & jabs only |
| Share a pet | main | hint | Vaccinations, conditions, meds — for a vet visit | Jabs, conditions, meds — for a vet visit |
| Share a pet | main | field label | Emergency only | Emergency info only |
| Share a pet | main | field label | Carer (read-only) | Sitter (read-only) |
| Share a pet | main | hint | Default: carer — read-only, no account needed. | Default: sitter — read-only, no account needed. |
| Share a pet | main | hint | The recipient opens the link in a browser or scans the QR — no sign-up or app install needed. | The recipient opens the link in a browser or scans the QR code — no app or account needed. |
| Share a pet | modal | status | Full dossier · Carer (read-only) | Full card · Sitter (read-only) |
| Share a pet | modal | hint | QR matches your scope and role selection above. | Matches what you picked above. |
| Share a pet | modal | hint | Scan to open Miso's shared profile — no app needed. | Scan to open Miso's shared pet card — no app needed. |
| Share a pet | modal | button | Save QR image | Save QR code |
| Share a pet | modal | button | Print QR | Print QR code |
| Share a pet (empty) | header | button | ← Dossier | ← Miso's card |
| Share a pet (empty) | header | heading | Share Miso | Share Miso's card |
| Share a pet (error) | header | button | ← Dossier | ← Miso's card |
| Share a pet (error) | header | heading | Share Miso | Share Miso's card |
| Share a pet (error) | main | error | Couldn't create the link | Couldn't create the share link |
| Share a pet (error) | main | error | Something went wrong while generating Miso's share link. Check your connection and try again, or go back to the dossier and try later. Back to dossier | Check your connection and try again, or go back to Miso's card and try later. Back to Miso's card |
| Share a pet (loading) | header | button | ← Dossier | ← Miso's card |
| Share a pet (loading) | header | heading | Share Miso | Share Miso's card |
| Share a pet (loading) | main | loading | Setting up Miso's shared view with full dossier access for a carer. | Setting up Miso's shared pet card — full access for a sitter. |

### Access management

| Screen | Area | Element | Before | After |
|---|---|---|---|---|
| Who has access (all states) | header | heading | Who has access | Who can see your pets' cards |
| Who has access | main | heading | Manage who can see your pets' information. Edit roles, scopes, or revoke access at any time. | Change what each person can see, or stop sharing with them any time. |
| Who has access | main | field label | Full dossier | Full card |
| Who has access · empty | main | empty | No one has access yet | No one can see your pets' cards yet |
| Who has access · empty | main | empty | Share your pet's info with a carer, vet, or co-owner. You control exactly what they can see. | Share your pet's card with a carer, vet, or co-owner. You control exactly what they can see. |
| Who has access · error | main | error | Something went wrong | Couldn't load your sharing settings |
| Who has access · error | main | error | Couldn't load your sharing settings. Check your connection and try again. | Check your connection and try again. |
| Who has access · loading | main | loading | Loading access list... | Loading your sharing settings… |
| Edit access grant (all states) | header | heading | Edit access | Marie's access |
| Edit access grant (all states) | main | heading | Modify Marie's access to Miso's information, or revoke it entirely. | Change what Marie can see on Miso's card, or stop sharing it with her. |
| Edit access grant (all states) | main | field label | Full dossier | Full card |
| Edit access grant (all states) | main | field label | Vaccinations, conditions, meds — for a vet visit | Jabs, conditions, meds — for a vet visit |
| Edit access grant | main | button | Save changes | Save |
| Edit access grant (all states) | main | destructive | Revoke access | Stop sharing |
| Edit access grant (all states) | main | destructive | Marie will immediately lose access to Miso's info. You can re-share later. | Marie can no longer open Miso's card — this happens immediately. You can share it with her again later. |
| Edit access grant · loading | main | loading | Saving... | Saving changes… |

### Shared pet view (sitter)

| Screen | Area | Element | Before | After |
|---|---|---|---|---|
| Shared pet view (success) | main | heading | Personality & Care | Personality & care |
| Shared pet view (success) | main | status | Profile filled · Updated 5 days ago | Filled · Updated 5 days ago |
| Shared pet view (success) | main | heading | Health Summary | Health summary |
| Shared pet view (success) | main | heading | Vet Contact | Vet contact |
| Shared pet view (success) | bottom nav | status | Shared via PetPal · This link expires 12 Jul 2026 · Contact owner: Eva · Questions? Ask Eva directly. | Shared via PetPal · This link expires 12 Jul 2026 · Questions? Call Eva directly. |
| Shared pet view (success) | header | button | Contact owner | Call owner |
| Shared pet view (empty) | main | empty | Eva hasn't added care info yet. Contact her to ask. | Eva hasn't added care info yet. Call her to ask. |
| Shared pet view (empty) | main | empty | No vet details added yet. Contact Eva directly in an emergency. | No vet details added yet. Call Eva directly in an emergency. |
| Shared pet view (empty) | main | empty | For care details, health info, or emergencies — contact Eva directly. | For care details, health info, or emergencies — call Eva directly. |
| Shared pet view (empty) | main | button | Contact Eva | Call Eva |
| Shared pet view (empty) | bottom nav | status | Shared via PetPal · This link expires 12 Jul 2026 · Contact owner: Eva · Questions? Ask Eva directly. | Shared via PetPal · This link expires 12 Jul 2026 · Questions? Call Eva directly. |
| Shared pet view (empty) | header | button | Contact owner | Call owner |
| Shared pet view (empty) | main | empty | Eva shared Miso's profile, but hasn't filled in the details yet. | Eva shared Miso's card, but hasn't filled in the details yet. |
| Shared pet view (empty) | main | empty | Contact Eva directly if you need care instructions, health info, or emergency details. | Call Eva directly if you need care instructions, health info, or emergency details. |
| Shared pet view (error) | main | error | This link has expired | This link is no longer available |
| Shared pet view (error) | main | error | Eva's shared link for Miso is no longer active. Ask Eva to send a new one. | It may have expired, or Eva may have stopped sharing it. Ask her to send a new one. |
| Shared pet view (loading) | main | loading | Loading Miso's shared profile... | Loading Miso's card… |
| Shared pet view (loading) | header | button | Contact owner | Call owner |

### Add / update a record

| Screen | Area | Element | Before | After |
|---|---|---|---|---|
| Add a record (success / empty / error) | header | heading | Add vaccination | Add a record |
| Add a record | main | field label | Vaccine name | Jab name |
| Add a record | main | field label | Date given | Date of the jab |
| Add a record | main | field label | Vaccination | Jab |
| Add a record | main | button | Save record | Add a record |
| Add a record | main | hint | Context-aware form — fields adapt to record type. Shown: vaccination. | *(removed — leaked dev/meta note, not real product copy)* |
| Add a record · error | main | field label | Vaccine name | Jab name |
| Add a record · error | main | field label | Date given | Date of the jab |
| Add a record · loading | main | loading | Saving… | Saving the record… |
| Add a record · loading | main | loading | Let us save your updated info so we can store it and keep it accessible for you at any moment. | *(removed — filler, violates Loading rule)* |
| Section-saving | main | loading | Saving… | Saving the section… |
| Section-saving | main | loading | Let us save your updated info so we can store it and keep it accessible for you at any moment. | *(removed — filler, violates Loading rule)* |


---

## 14 · Cross-screen consistency audit

After all 15 clusters landed, every final wireframe was grepped for competing labels of the same action/term. **Forbidden clichés confirmed gone site-wide** (`Something went wrong` / `successfully` / `Welcome back` / `Oops` / `Awesome` / `Congratulations` = 0). `Dossier` / `profile` / `authorization` survive **only in prototype chrome** (sidebar nav, breadcrumb, JS flow-tooltips) and a few `aria-label`s — not in visible product copy.

### Reconciled — fixed in this pass

| Action / thing | Was (drift) | Now (canonical) | Scope |
|---|---|---|---|
| Back to the pet list | `← My Pets` | `← Your pets` | 13 home screens (the My-Pets heading was renamed to "Your pets"; back-buttons hadn't followed) |
| Add-form heading | `Add document` · `Add health record` · `Add emergency contact` | `Add a document` · `Add a health record` · `Add an emergency contact` | 3 forms (5 sibling add-forms already used the article) |
| Save (owner profile) | `Save changes` | `Save` | Me.html (26 other Save buttons are bare "Save") |

### Consistent by design — no change needed

- **Error-headline possessive** tracks whose data it is: pet-section screens say *"Couldn't load **Miso's** X"*; cross-pet / account / settings screens say *"Couldn't load **your** X"*; the sitter view says neither. Intentional, not drift.
- **`Add a …`** button pattern, **`Try again`** (retry ×42 — zero `Retry` left), **`No … yet`** empty pattern, **`Call`** for phone actions, **`It can't be undone.`** destructive tail — all uniform across clusters.

### Needs a decision — NOT auto-changed

| # | Item | Variants (where) | Recommendation |
|---|---|---|---|
| 1 | **Carer vs Sitter** — the trusted person | `Sitter (read-only)` (Share) vs `Carer` / `carer` (Emergency, Access, Shared-view — ~13 files) | Standardise to **Sitter** (glossary term). Touches the role dropdown (Carer / Vet / Co-owner), so confirm before changing ~13 files. |
| 2 | **`Save settings`** (Reminder settings) | vs canonical `Save` | Keep `Save settings` (clearer here) *or* unify to `Save` |
| 3 | **Bare `Add` / `Edit`** inline per-category (Personality, 6 files) | vs `Add a note` | Keep the compact inline pair *or* promote to `Add a note` |
| 4 | **`Add photo` vs `Add a photo`** (Upload-photo) | H1 vs button, same screen | Align H1 → `Add a photo` |
| 5 | **`Danger zone`** label (Edit-pet, Edit-access-grant) | used consistently, but alarmed vs the "calm confidence" voice | Optional: drop / soften |

### Cosmetic / non-visible — noted

- Stale **`aria-label`s** (`Back to Miso's profile`, `Back to Dossier`, `Delete profile?`) — visible text is correct; the attributes lag because the pass was text-nodes-only. Worth a separate accessibility sync.
- `No appointments yet.` carries a trailing period the other empty headlines drop; `Loading emergency info&hellip;` uses the HTML entity where siblings use the `…` character.
