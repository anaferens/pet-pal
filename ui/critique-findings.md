# PetPal — combined critique findings

Four `/impeccable critique` passes, one per screen group, run in parallel over all 123
wireframes. Report only — nothing was fixed. Counts marked **(verified)** were re-measured
independently across all 123 screens, and in two cases the agent's own figure was wrong.

Severity: **P1** breaks the system or the user's task · **P2** visible inconsistency · **P3** polish.

---

## P1 — systemic, affects many screens

| # | File(s) | Element | What's wrong | How to fix |
|---|---|---|---|---|
| 1 | **81 of 123 screens** *(verified — agents said 13 and 16)* | Tab bar, 2nd destination | Reads **"What's due"**; only **11** read **"Reminders"**, which is what DESIGN.md specifies. The majority is the drift, so fixing the minority would make it worse. `Me` contradicts itself on one screen. | Markup change → all 123 screens. Set tab 2 to "Reminders" everywhere; align `<title>`, back-control `aria-label`s and the `Me` switch caption. |
| 2 | **23 files, 91 controls** *(verified — agent said 15 files / 69)* | every `<input>`/`<select>`/`<textarea>` | No programmatic label: `<label class="pp-field__label">` has no `for`, doesn't wrap the control, and the control has no `id`/`aria-label`. `Edit-pet` and `Edit-access-grant` already use the correct pattern. | Markup change → 23 screens. Add `id` + `for`, following the pattern those two already ship. |
| 3 | **all 123** | focus indicator | `kit.css` scopes its only focus rule to `.pp :focus-visible`, but no wireframe carries a `.pp` host — it was removed during migration because it forced a base font. The rule is dead in the product and alive in the showcase. Input focus ring is `#ffbf00` at 1.63:1 on white, under the 3:1 non-text minimum. | **Kit value + selector.** Unscope the focus rule from `.pp`; darken the ring to `--pp-signal-ink` or add a second offset ring. |
| 4 | `Shared-pet-view-empty`, `-error`, `-loading` | whole screen | Never migrated: legacy `header.m-header`, no `pp-` components, no arch, no amber, uppercase headings, an 88px grey circle reading "photo". Three of the four highest-stakes recipient screens are a different product from their success sibling. | Migrate to the kit like the success screen. |
| 5 | `Shared-pet-view` | `.pp-collapse__body` ×4 | All four sections collapsed on load — a stranger holding the pet sees only headers; medications, allergies and the vet's number are each behind a tap. The `-empty` sibling shows everything expanded. | Open by default on the recipient screen, or hoist emergency-critical content above the folds. |
| 6 | `Shared-pet-view` | call affordances | The owner is not callable: "Questions? Call Eva directly." is plain text, not a `tel:` link. The one `tel:` on the page is inside a collapsed section. | Markup → make the footer a `tel:` link; surface a Call action outside the folds. |
| 7 | `Shared-pet-view` | `a.emergency-link` | The emergency path is the least prominent block on screen — full-bleed grey, no radius, no icon, no shadow — between two white shadowed cards. Reads as a divider. | Promote to a card with an icon tile and the danger pair. |
| 8 | `Share-a-pet`, `Reminder-settings`, `Emergency-auth-setup`(+`-error`), `Edit-access-grant`(×3), `Add-care-note`(×2), `Edit-care-note`(×2) | `[role=radio]` / `[role=switch]` | `onclick` only, no `keydown` — Space/Enter do nothing. All options carry `tabindex="0"` instead of roving tabindex. The share-scope decision — what a stranger may see — cannot be made from a keyboard. | Markup + kit. Add key handling and roving tabindex to the choice and switch components. |
| 9 | `Login`, `Login-error`, `Sign-up`, `Forgot-password` | auth inputs | 6 unlabelled fields (subset of #2, called out because auth is the entry point). | As #2. |
| 10 | `home-progress-1…6` (21 rows) | `.pp-check` | Carries a literal `✓` character. `font-size:0` hides the glyph but it still generates a line box, so the tick drops **19px below** the title and every ticked row is 15px too tall. | Markup → remove the character; the mark is a background image. |
| 11 | `Set-up-a-pet-error`, `Add-record-error`, `Add-care-note-error`, `Edit-care-note-error` | form body | The banner promises the work is intact while the form is truncated — `Set-up-a-pet-error` shows 3 of 7 fields under "nothing was lost". | Restore the full field set in the error state. |
| 12 | 8 screens | `.pp-drop` upload zone | A bare `<div>` — no `tabindex`, no `role`, no `<input type=file>`. Unreachable by keyboard, invisible to assistive tech. The `<label>` above it labels nothing. | Kit + markup: make it a real control. |
| 13 | `Edit-care-note`, `Edit-health-record`, `Edit-pet` | Delete / Remove | Destructive actions with no consequence statement, no "It can't be undone.", no confirmation — while sibling controls `Delete Miso` and `Stop sharing` do it correctly. | Follow voice.md §Destructive, as the siblings already do. |
| 14 | `home-success-single` | `.zone-label` ×2 | Wireframe annotation boxes render **inside the phone** — dashed "COUNTER" and "SEARCH & FILTER" boxes in `-apple-system`. | Move to the hidden desktop block, as every other screen does. |
| 15 | `My-Pets-loading`, `Share-a-pet-loading` | loading copy | Prototype navigation leaks into product text: "Loading your pets… **→ when loaded**" and an underlined link inside the `<h2>`. | Remove the scaffolding. |
| 16 | `home-error`, `home-loading` | `.pp-appbar__title` | The pet's name is flush right (+152px off centre) because these states omit the trailing action. The name jumps to the edge when the card errors. `.pp-appbar--center` exists for this and isn't applied. | Markup → apply `--center`. |

## P2 — visible inconsistency

| # | File(s) | Element | What's wrong | How to fix |
|---|---|---|---|---|
| 17 | 9 screens | primary CTA | "Share Miso's **info**" vs `home-success`'s "Share Miso's **card**". voice.md's glossary is one-concept-one-term and the word is **pet card**. `home-empty` contradicts itself in adjacent lines. | Copy → "card" everywhere. |
| 18 | 13 screens | local `:root` | Still pre-migration: `--wf-text:#1a1a1a` vs the token `#141414`, plus 4 more. Body ink — including the 36px pet name — computes `rgb(26,26,26)` on 13 screens and `rgb(20,20,20)` on the rest. | Retokenise to the kit values. |
| 19 | 17 of 29 form screens | `.pp-actions` | Button order flips: primary-first on 5, primary-last on 12. Same component, same task, opposite reading order. | Pick one; DESIGN.md should state it. |
| 20 | 10 screens | primary button | Generic "Save" where voice.md requires verb + object. The screen titled "Add a policy" offers a button reading "Save". | Copy. |
| 21 | 17 of 29 form screens | `.pp-tabbar` | Present on 12, missing on 17, with no rule distinguishing them — `Edit-care-note` has it, `Edit-health-record` doesn't. DESIGN.md says every owner-facing screen. | Decide the rule, apply it. |
| 22 | 6 loading screens | loading state | Two incompatible patterns: `Edit-access-grant-loading` keeps the form and dims it; six others replace the screen with an hourglass and drop the app bar, leaving **zero interactive elements** — no exit while saving. | Standardise on the dimmed-form pattern. |
| 23 | `Share-sent` vs `Share-success` | whole screens | Two near-identical terminal screens that contradict each other ("It lasts a month" vs "It expires in 1 month"); `Share-sent` claims a handoff with no link, no copy action, no recipient. Neither names who it was shared with. | Merge or differentiate; follow voice.md's success rule. |
| 24 | `Who-has-access` | row buttons | "Edit" is an ink pill on all three rows; "Stop sharing" — the safety action — is muted secondary. Four ink pills on one screen. Hierarchy inverted. | Re-weight. |
| 25 | `Who-has-access` | status | Zero status chips on the screen whose job is legibility of who-can-see-what. State is plain text "Status: Active". | Use the status pairs. |
| 26 | `Whats-due`, `Whats-due-offline` | `.pp-chip` | Status chips sit below the meta, outside the title — `Whats-due-detail` puts the same chip inside its title. The intended pattern exists and the list screen doesn't follow it. | Markup → inside the title, per the standing rule. |
| 27 | `home-success-cheetah` | Emergency row / Personality row | Same not-filled state as Insurance above it but **no mark**; and Personality carries the green verified tick while its meta says "Partially filled". | Apply `.pp-pending` / correct the tick. |
| 28 | `Whats-due` (reference) | pet filter | Uses a bespoke `.pet-filter-tabs`; its own offline sibling uses the kit's `.pp-seg__item`. The reference is the un-migrated one. | Migrate the reference. |
| 29 | 3 screens | `.pp-appbar` | Titled bars at 50px vs 68px elsewhere, and `--plain` renders 69px on Share and 51px on auth. Three heights for one bar. | Kit value. |
| 30 | `Who-has-access` | "Re-share" | Unstyled anchor — browser-default blue `rgb(0,0,238)`, the only off-palette colour in the project. | Apply a kit class. |
| 31 | `Reminder-settings` | email meta | Shows a real personal address instead of the `eva@example.com` placeholder used everywhere else. | Copy. |
| 32 | `Reminder-settings` | 2 labels | Render in `-apple-system` instead of Hanken Grotesk. | Kit/markup. |
| 33 | `home-new` vs `home-progress-1` | screen header | One section apart, two entirely different headers — compact identity strip vs full amber band + arch. Of the pet card's four declared states, only Success carries the band. | Decide when the arch appears. |
| 34 | `home-progress-6` vs `home-success` | whole screen | Both "6 of 6 filled" on Miso's card, differing in five ways (CTA shape, arch third line, switcher, edit pencil, share button). | Reconcile. |
| 35 | `My-Pets` vs the cards | row meta | Counts contradict at identical timestamps: My-Pets says Miso 5 of 6, the card says 6 of 6. | Copy. |
| 36 | `Add-insurance`, `Add-document`, `Add-vet-record` | labels/placeholders | Vaccination copy leaked into unrelated forms — an insurance policy has an "Administering vet" field and a batch-number placeholder. | Copy. |
| 37 | `Add-document`, `Add-health-record`, `Edit-health-record` | `.pp-note` | Design-spec commentary rendered as product copy ("Context-aware form — fields adapt to record type"). | Remove. |
| 38 | `Add-record-empty` | whole screen | The only content is an un-migrated prototype annotation in `-apple-system`. | Migrate or remove the state. |
| 39 | 12 screens | `.pp-photoslot` / `.pp-drop` | Grey `#f4f4f4` placeholder fills where an image belongs, against DESIGN.md's explicit ban, with literal strings "Upload", "photo", "no photo yet". `Edit-pet` shows a grey circle for Miso while `Add-care-note` shows her photograph. | Use the tint illustration tile; wire the photo. |
| 40 | `Add-care-note`, `Edit-care-note` | `.pp-textarea` | Content clipped at rest — `scrollHeight` 114 vs `clientHeight` 94, cutting the user's saved note mid-sentence. | Kit value. |
| 41 | `Edit-pet` | `.pp-danger` | "Are you sure?" printed as permanent static text under both Archive and Delete, with nothing to answer. | Remove or make it a real confirmation. |
| 42 | `Add-vet-clinic`, `Add-emergency-contact` | fields | "Add" screens open fully pre-filled, reading as edit screens under an add title. | Blank them. |
| 43 | 4 error screens | `.pp-banner` | No `role="alert"`/`aria-live` — the failure is never announced. `Edit-pet-error` and `Edit-access-grant-error` set it on the identical component. | Kit + markup. |
| 44 | 15 files | required marking | Visual `*` only — no `required`/`aria-required` except on `Edit-pet`. Most screens carry no legend explaining the asterisk. | Markup. |
| 45 | `Login-error` | email field | Value cleared after a failed attempt; no `aria-invalid`/`aria-describedby`. | Preserve the value. |
| 46 | `Emergency-auth-setup` ×3 | `<title>` | "author**iz**ation" — US spelling against the one explicit spelling ruling. The H1 is correct. | Copy. |
| 47 | 8 screens | `.pp-btn--sm`, `.pp-iconbtn` | 36px, 30px and 26px tall — under the 44×44 rule, and two sizes for adjacent round buttons on one screen. The kit itself defines `--sm` at 36px, so the defect is in the token. | **Kit value.** |
| 48 | `Who-has-access`(×4), `Whats-due`(×2) | `.pp-seg__item` | 31px against the kit's canonical 36px. | Kit value. |
| 49 | `Emergency-allowed` | backup contact | The only contact with no Call button — the person you call when the owner doesn't answer. | Markup. |
| 50 | `Emergency-auth-setup` | `.pp-contact` avatars | Empty grey circles; `Who-has-access` fills the same circles with initials. "Edit" is a text link here and an ink pill there. | Markup. |

## P3 — polish

| # | File(s) | Element | What's wrong | How to fix |
|---|---|---|---|---|
| 51 | 13 screens | `.pp-illus` | A leftover text node "illustration" inside the tile — invisible, but in the accessible name, so a screen reader announces "illustration". | Markup. |
| 52 | `My-Pets` | `.pp-is-name` | Pet names in EB Garamond at 16px — DESIGN.md's own X-Height Rule describes this failure and prescribes 1.25×. `.pp-is-name` sets no size, so the slot's 16px wins. | Kit value. |
| 53 | `home-empty`, `home-new`, `My-Pets-empty` | `.pp-illus--pets` | One paw tile for three unrelated moments; DESIGN.md asks for a content-matched glyph and the kit ships 11 variants. | Markup. |
| 54 | `home-error`, `My-Pets-error` | error block | No illustration tile, where all three empty states lead with one. | Markup. |
| 55 | `Share-sent`, `Logged-out` | `<title>` | "Shared**!**" — the exclamation is the literal example in voice.md's Forbidden table. | Copy. |
| 56 | `Emergency-allowed` | body copy | Literal double hyphens `--` rendered as text where em dashes are used everywhere else. | Copy. |
| 57 | `Emergency-allowed`, `Who-has-access` | vet name/address | "Dr. Muller", "Parkstrasse" — missing umlaut/ß in a German-market product that spells "Tierklinik am Stadtpark" correctly. | Copy. |
| 58 | 5 auth screens | wordmark | "PetPal" appears twice, ~70px apart. | Markup. |
| 59 | 6 auth/secondary screens | links | 17px-tall targets — the only route between the two auth screens. | Kit value. |
| 60 | `Share-a-pet-loading` | body copy | "**full access** for a sitter" contradicts the Role field's "Sitter (read-only)". | Copy. |
| 61 | `Share-a-pet`, `Whats-due` | arch | Both hand-roll the signature geometry in page-local CSS and switch the kit's off. Measures correct, but two reference screens own a private copy. | Move to the kit. |
| 62 | `Edit-access-grant` ×3 | `<legend>` | Invalid nesting — `<legend>` isn't the fieldset's first child; duplicates the label in the accessibility tree. | Markup. |
| 63 | 6 loading screens | headings | No `<h1>` — the app bar that supplies it is removed and "Saving…" is an `<h2>`. | Markup. |

---

## Checked and clean (all four groups agreed)

- **Contrast** — zero failures at 4.5:1 / 3:1 across all 123 screens, measured with rgba composited onto its real backdrop. Uncomposited alpha gives false failures; both passes avoided that.
- **Fonts** — no Georgia/Times/system-ui substitution in visible text except the two `Reminder-settings` labels. `-apple-system` hits are `font-size:0` icon labels.
- **Back control** — bare `←` at 44×44 on every screen that has one, destination in `aria-label`. Zero labelled back controls.
- **`Edit →`** — no occurrences anywhere.
- **Amber discipline** — one amber element per screen; no amber-filled buttons; amber bar only where an arch exists, transparent everywhere else. No violations either direction.
- **Voice** — no "Something went wrong", "Oops", "Welcome", "successfully", "dossier", "profile", "carer", emoji, or exclamation marks in rendered product copy (the two `<title>` hits are listed above).
- **Layout** — no horizontal overflow, no zero-height or overlapping visible elements on any screen.
- **Card geometry** — 340px, 14px padding, 16px radius, hairline + two-part shadow; 36px icon tiles; 13px/400 meta; 61px tab bar. Identical everywhere.
- **`Emergency-allowed`** — called out as genuinely well built: numbered steps, viewing-as banner, ink Call vet first, medications and allergies surfaced without a tap.

---

## Group 2 — Sections (40 screens), merged

| Sev | File(s) | Element | What's wrong | How to fix |
|---|---|---|---|---|
| P1 | `Emergency-info-fill1`, `-fill2`, `-firstrun`, `Vet-and-appointments-clinic` | `nav.pp-tabbar` | Tab bar nested **inside** `.m-main` instead of being its sibling — renders mid-screen with 300–500px of white beneath it. On `-clinic` the FAB then floats below the tab bar. | Markup → move it out, matching the other 36. |
| P1 | `Documents-and-passport`(×4), `-firstrun`, `Insurance`, `Vet-and-appointments`(×3) | `.pp-row__chev` link | `<a><button class="pp-row__chev" aria-hidden="true">→</button></a>` — the hidden button is the anchor's only content, so the link has **no accessible name**. Target is **14×24** and the title/meta/thumb are inert, so the arrow glyph is the only way in. | Markup → make the whole row the link; name it. |
| P1 | `Vet-and-appointments`, `-clinic`, `-firstrun` | `.pp-detail__row--action` | The eyebrow says "Vet clinic (**1-tap call**)" and Phone/Address are underlined, but both are plain `<strong>` — no `tel:`, no link. Link-looking dead text on the screen whose promise is calling in a hurry. | Markup → real `tel:` links. |
| P1 | `Health-and-jabs-firstrun` | `.pp-chip--success` | Chip is a child of `.pp-headrow` *after* the Edit link, not inside `.pp-row__title` — renders far right and shoves Edit ~175px left, so the two Edit links no longer align. `Health-and-jabs` does it correctly. | Markup → inside the title (rule 5). |
| P1 | **15 screens** across all six families | app-bar trailing action | **Inverted**: the action appears only on empty/error/loading and vanishes on success. Insurance and Personality show "Edit" on `-empty` (nothing to edit) and `-error` (nothing loaded). | Markup → action on success, not on broken states. |
| P1 | `Emergency-info`, `-fill1`, `-fill2`, `-firstrun` | contact `tel:` links | Eva's and Thomas's numbers are bare inline anchors at **101×17px** — the only way to reach a human — while the vet gets a 310×44 Call button. | Markup + kit. |
| P2 | whole group | record row | **Three components for one job**: Health/Personality use `.pp-headrow` + 37×44 "Edit" text link; Vet uses `.pp-headrow` + 14×24 "→"; Documents/Insurance use `.pp-doc` + grey thumb + "→". Proof it's one job: the same record opens `Edit-health-record.html?rec=dental` from two of them. | Consolidate to one row component. |
| P2 | `Documents*`, `Insurance*`, `Emergency-info*` | record title | Hanken 14px/600 here vs Bricolage 16px/700 on Health/Vet/Personality, while all six share the same 13px meta — so the heading barely outranks its own metadata. | Kit/markup. |
| P2 | `Personality-and-care` + `-fill1…6`, `-firstrun` | FAB + full-width button | Same label, same destination ("Add a note" → `Add-care-note.html`), visible together ~60px apart. | Drop one. |
| P2 | `Emergency-info`, `Health-and-jabs`, `Personality-and-care` | `.pp-fab` overlap | `.m-main` reserves 20px for a 52px FAB. The FAB covers "Info last verified …" at any height, and at ~950px overlaps the last row's Edit link and the "Preview as sitter" button. | Kit value → bottom padding ≥ FAB height + gap. |
| P2 | `Emergency-info` | contact avatars | Empty `#eaeaea` discs — no photo, initials or glyph — the grey placeholder DESIGN.md rejects by name; and their hidden text is the literal word "icon" while the pet avatar beside them is properly labelled. | Markup. |
| P2 | `Vet-and-appointments*` vs `Emergency-info*` | clinic data | One clinic, two phone numbers and two doctors ("+49 30 1234 5678"/"Dr. Sarah Müller" vs "+49 30 1234567"/"Dr. Müller"). | Copy. |
| P2 | `Vet*`, `Emergency-info*` | block heading | One block, three names: "Vet clinic (1-tap call)" (a spec phrase), "Vet contact", "Vet clinic". Also "Emergency contacts" vs "Emergency contact". | Copy. |
| P2 | `Documents*`, `Insurance*`, `Vet*`, `Emergency-info` | FAB `aria-label` | Four values for one control — "Add record", "Add a note", bare "Add". `Emergency-info`'s is labelled "Add" but navigates to authorisation setup. | Markup. |
| P2 | `Emergency-info-empty`(×3), `-fill1`(×2), `-fill2`(×2) | stacked primaries | Three full-width ink primaries with no hierarchy; the "+" prefix on a button label appears nowhere else. | Re-weight. |
| P2 | `Vet-and-appointments`, `-clinic`, `-firstrun` | `.pp-chip` "Confirmed" | Bare chip renders surface grey — a status chip carrying no status colour, beside Health's correctly paired green/amber. Same grey chip also carries non-status roles ("Owner", "Backup"). | Kit + markup. |
| P2 | 5 of 6 `-loading` | `.pp-loading-label` | Prototype navigation rendered as product copy — `→ when loaded` inline with an inline-style override. | Remove. |
| P2 | all six `-loading` | skeleton | Five use four undifferentiated grey blocks resembling nothing on the loaded screen; `Emergency-info-loading` alone shape-matches — and is the only one to drop the pet's name. | Standardise on the shape-matched one. |
| P2 | `Health-and-jabs-record1`, `Vet-and-appointments-clinic`, `Personality-and-care-empty`, `Emergency-info-empty` | inline empty state | Three patterns, one of which instructs on a gesture ("tap **+** and choose…"). | Standardise. |
| P2 | all 40 | nested interactives | `<a><button class="pp-appbar__back">←</button></a>`. Health mixes both forms within one screen. | Markup. |
| P2 | `Health-and-jabs*`, `Personality-and-care*` | `.pp-btn--link` | **37×44** — under 44 on width, and the only tap target on the row. | Kit value. |
| P3 | `Emergency-info` | headings | "Emergency authorisation" printed twice in a row. |
| P3 | `Health*` vs `Vet*`, `Emergency-info*` | `.pp-heading` | `<div>` on one, `<h2>` on others; three families have no group heading at all. |
| P3 | `Personality-and-care-fill1…5` | row rhythm | Filled blocks are full-bleed ruled rows, unfilled are inset dashed cards — the rhythm breaks at every boundary. |
| P3 | `Health-and-jabs-error`, `-loading` | app-bar action | Offers "Add a jab" on a screen that just failed to load the jabs. |
| P3 | `Personality-and-care` vs `-empty` | `.pp-note` | Same band, drifting copy. |
| P3 | `Emergency-info` | `.pp-caution` | Severity carried by red text alone — no chip, no icon; the only red on any of the 40. |

**Group 2 checked and clean:** all 40 app bars transparent at 68px with no arch anywhere (so the amber rule can't be violated); back control bare `←` at 44×44 on all 40; no `Edit →`; **zero form controls** in this group; contrast passes throughout once composited — three suspicions specifically re-tested and dropped; identity strip byte-identical on 39 of 40; the four `-empty` illustration tiles are the group's strongest sibling moment.
