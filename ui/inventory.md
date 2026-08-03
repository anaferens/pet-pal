# PetPal — Component Inventory

Every component that appears in the wireframes, whether or not it has been restyled yet. Built by parsing all **123** files in [`../wireframes/`](../wireframes/), scoped to the product canvas (`.content-mobile → .phone`) so prototype chrome — the sidebar, persona-flow breadcrumb and state tabs — is excluded. Cross-checked against [`../research/sitemap.md`](../research/sitemap.md) and the language board at [`../concept/concept.html`](../concept/concept.html).

**Scope note.** **21** of the 123 screens carried The Signal when this was written; the owner flow's remaining **32** were painted onto the kit in the migration below, so **53** now do. The rest are still grey. This inventory covers both — a grey component is still a component, and most of the kit lives there. Nothing here is inferred from [`../DESIGN.md`](../DESIGN.md) or [`../concept/concept.md`](../concept/concept.md); every row is something that exists in markup.

**Reading the columns.** *Screens* gives the count and the families it appears in (a family = a screen plus its state pages). *States* lists only variants that exist in the CSS or markup — modifier classes and pseudo-states — not states we might want. *Photo* means the component has a slot for a photograph of a pet or a person; icon tiles and illustration tiles are **not** photos.

---

**Marks sit inline, on the title.** A verification tick or not-filled mark goes *inside* the title element, immediately after the text — never as a sibling of the flexible body, where its position becomes whatever space is left over and four sections put it in four different places. The title must be block-flow, not flex: as a flex row the mark centres beside a wrapped title instead of following the last word. Status chips (`.pp-chip`) follow the same rule. This only misbehaves on titles long enough to wrap, so it hides on short ones.

## Navigation

| Component | Screens where it appears | Available states | Requires a photo |
|---|---|---|---|
| **Tab bar** (`.phone-nav`) | **92** across 24 families incl. `home`, `Personality-and-care`, `Emergency-info`, `Whats-due`, `My-Pets`, `Health-and-jabs`. Absent on **31** focused-task screens: the recipient views (`Shared-pet-view`, `Emergency-allowed`), auth (`Login`, `Sign-up`, `Forgot-password`, `Logged-out`), and the full-screen add/edit/upload flows (`Add-*`, `Set-up-a-pet`, `Upload-photo`, `Edit-health-record`, `Section-saving`) | Default · **Active** (`a.active` — filled icon; on styled pages also a 24×3px amber marker). Four destinations: Pets · Reminders · Share · Owner | No |
| **App bar** (`.m-header` → `.pp-appbar`) | **115** across 40 families. The **8** without it are the `*-loading` screens where a skeleton stands in for the header, plus `Section-saving` and `Shared-pet-view` | Title only · With back · With trailing action · **`--sm`** compact (48px, `Me`) · **`--bare`** recipient brand bar · **`--onarch`** amber. **Background is transparent by default**; the amber is `--onarch` only, worn by the 4 screens whose arch continues the band down the page (`home-success`, `-single`, `-cheetah`, `Me`) — elsewhere it would be a stripe with nothing beneath it. Back control is a **bare `←`** on every screen, destination in `aria-label` | No |
| **Back control** (`.back`) | **98** across 31 families | Default | No |
| **Add button / FAB** (`.fab`) | **21** across 9 families — `Personality-and-care` (8), `Documents-and-passport` (2), `Health-and-jabs` (2), `Insurance` (2), `Vet-and-appointments` (2) | Default · **Menu open** (`.fab-menu`, 3 screens, with hover) | No |
| **Pet toggle — 2-up switcher** (`.pet-switcher`, `.pet-pill`, `.pet-seg`) | **5** — `home-empty`, `home-new`, `home-success`, `home-success-cheetah`, `Share-a-pet`. Only where the owner has more than one pet | **Inactive · Active** (`.pet-pill.active`) · Hover. The active segment squares its **inner** corners, so it reads as a tab pulled forward | **Yes** — `.pill-avatar`, 22px circle per pet |
| **Pet toggle — 3-up filter** (`.pet-filter-tabs`) | **2** — `Whats-due`, `Whats-due-offline`. Adds an *All pets* option the 2-up has no room for | **All pets · Miso · Cheetah**, one active. Radius is **positional, not stateful**: the first child keeps the left pill end and the last the right, so a middle selection reads as a square block cut into the bar | **No** — labels only, 31px tall |
| **Search & filter** (`.m-search-filter`, `.search-bar`) | **9** — `home` (7), `home-success` (2) | Default · **Focus** (`.search-bar:focus`) | No |
| **Desktop top nav** (`.top-nav`) | **4** — `Emergency-info` (3), `Vet-and-appointments-clinic` | Default | No |

## Profiles

| Component | Screens where it appears | Available states | Requires a photo |
|---|---|---|---|
| **Avatar** (`.pet-photo`, `.me-avatar`, `.recipient-avatar`, `.contact-avatar`, `.pill-avatar`) | **68** across 21 families — the most reused atom after the app bar | **With photo · Awaiting photo** (grey ground). Six sizes in use: 22 · 32 · 40 (`-s`) · 64 (`-m`) · 96 · 104px | **Yes** — this *is* the photo slot |
| **Pet identity strip** (`.m-pet-identity`) | **53** across 16 families — `Personality-and-care` (11), `Emergency-info` (6), `Documents-and-passport` (5), `Health-and-jabs` (5), `Insurance` (5) | Default. Composes a 40px avatar + name + breed/age meta | **Yes** — via `.pet-photo-s` |
| **Arch hero** (`.dv3-hero` + `.dv3-arch`, `.sv-hero`, `.share-hero`) | **12** — `home` (7), `home-success` (2), `Me`, `Share-a-pet`, `Shared-pet-view` | Band height varies by screen — 160 / 188 / 224px — while the **arch rise stays 94px** | **Yes** — 88px circle sitting 50/50 on the arch line |
| **Recipient info block** (`.recipient-info`) | **3** — `Edit-access-grant` (all states) | Default | **Yes** — `.recipient-avatar`, 40px |
| **Role badge strip** (`.role-badge-strip`) | **3** — `Emergency-allowed` (2), `Shared-pet-view` | Default. States *what the holder of the link may do* | No |

## Forms

| Component | Screens where it appears | Available states | Requires a photo |
|---|---|---|---|
| **Action button** (`.btn-primary`, `.btn-secondary`) | **91** across 39 families — the most widespread interactive component | **Primary · Secondary · Hover · Disabled.** Size/width variants: `.btn-sm`, `.btn-full`, `.btn-share`, `.btn-danger` | No |
| **Form field** (`.form-group`) | **30** across 21 families — `Edit-access-grant` (3), `Add-care-note` (2), `Add-record` (2), `Edit-care-note` (2), `Edit-pet` (2), `Emergency-auth-setup` (2) | **Default · Focus · Disabled** · Required (`.req`) · With helper (`.helper`). Covers input, select and textarea | No |
| **Form actions row** (`.form-actions`) | **25** across 17 families | Default. Pairs a primary with a cancel/secondary | No |
| **Helper text** (`.helper`) | **18** across 13 families | Default · Paired with an error banner | No |
| **Text link button** (`.text-link`, `.secondary-link`, `.edit-link`, `.save-link`) | **9** across 7 families | Default | No |
| **Toggle** (`.toggle-switch` + `.toggle-row`) | **8** — `Add-care-note` (2), `Edit-care-note` (2), `Emergency-auth-setup` (2), `Me`, `Reminder-settings` | **Off · On** (`.on`, and `input:checked + .toggle-track`). The styled version adds a knob checkmark that fades in | No |
| **Danger zone** (`.danger-zone`) | **6** — `Edit-access-grant` (3), `Edit-pet` (3) | Default. Destructive action isolated below the form | No |
| **Choice / scope radio** (`.scope-option`, `.scope-radio`) | **4** — `Edit-access-grant` (3), `Share-a-pet` | **Unselected · Selected** (`.selected`) | No |
| **Photo upload area** (`.upload-box`, `.photo-placeholder`, `.photo-section`) | **4** — `Edit-pet` (2), `Add-care-note`, `Edit-care-note` | **Empty** (80px circle awaiting an image) · Upload box | **Yes** — it is the photo intake |

## Reminders

| Component | Screens where it appears | Available states | Requires a photo |
|---|---|---|---|
| **Status chip** (`.status`, `.record-status`, `.vax-status`, `.appt-status`, `.doc-status`, `.auth-status`) | **14** across 4 families — `home` (9), `Health-and-jabs` (2), `home-success` (2), `Shared-pet-view` | One per status value; six named variants across record, vaccination, appointment, document and authorisation contexts | No |
| **Fill counter** (`.m-fill-counter`, `.count`) | **11** — `home` (9), `home-success` (2) | Default. Tracks how much of a section is complete | No |
| **Verification tick** (`.check`) | **10** — the six `home-progress-1…6` steps, `home-success` + its `-single` and `-cheetah` variants, and `Shared-pet-view` | Present / absent per section | No |
| **Not-filled mark** (`.pp-pending`) | **1** — `home-success-cheetah`, on the Insurance section | Single state. The counterpart to the tick: same 18px box, baseline and inline placement, in `--pp-warning` bronze, so a row reads identically whichever mark it carries. Added 2026-08-04 | No |
| **Reminder card** (`.reminder-card`) | **2** — `Whats-due`, `Whats-due-offline` | Default · Hover | No |
| **Reminder badge** (`.reminder-badge`) | **2** — `Whats-due`, `Whats-due-offline` | **Overdue · Due this month · Coming up** — driven by the parent `section[aria-label]`, not a modifier class | No |
| **Urgency heading** (`.urgency-heading`) | **2** — `Whats-due`, `Whats-due-offline` | Default. Groups reminders by urgency band | No |

## Cards

| Component | Screens where it appears | Available states | Requires a photo |
|---|---|---|---|
| **Empty state** (`.empty-state` + `.empty-illustration`) | **25** across 21 families — `Set-up-a-pet` (2), `Share-a-pet` (2), `Share` (2), `home` (2), plus 17 more | Illustration tile + headline + body + optional CTA (`.empty-cta`) | **No** — a 120px illustration tile, which is precisely the *replacement* for a photo |
| **Error state** (`.error-state`, `.error-block`) | **13** across 13 families — one per section family | Default, with `.error-cta` recovery | No |
| **Loading skeleton** (`.skeleton*`) | **12** across 12 families | Default. Block, line, circle, card and list variants | No |
| **Section / listing card** (`.m-section-card`, `.card-body`, `.card-icon`, `.card-arrow`) | **12** — `home` (7), `Whats-due` (2), `home-success` (2), `My-Pets` | Default · Hover · **Collapsed / Open** on `Shared-pet-view` | No — leads with a 36px icon tile, not a photo |
| **Shared footer** (`.shared-footer`) | **8** — `Emergency-allowed` (4), `Shared-pet-view` (4) | Default. The recipient's persistent footer, replacing the tab bar | No |
| **Error banner** (`.error-banner`) | **7** across 7 families — `Add-care-note`, `Add-record`, `Edit-access-grant`, `Edit-care-note`, `Edit-pet`, `Emergency-auth-setup`, `Set-up-a-pet` | Default · With detail (`.error-detail`). Always inside a form | No |
| **Auth block** (`.auth-wrap`, `.auth-card`) | **6** — `Login` (2), `Sign-up`, `Forgot-password`, `Emergency-info`, `Emergency-allowed` | Default · **Error** (`.auth-error`) | No |
| **Vet card** (`.vet-card`) | **5** across 4 families — `Vet-and-appointments` (2), `Emergency-info`, `Shared-pet-view`, `Vet-and-appointments-clinic` | Default | No |
| **Detail row** (`.detail-label` / `.detail-value`) | **4** — `Document-view`, `Emergency-allowed`, `Shared-pet-view`, `Whats-due` | Default. The label/value pair inside a record | No |
| **Contact row** (`.contact-row`, `.contact-info`) | **3** — `Emergency-auth-setup` (2), `Emergency-info` | Default | **Yes** — `.contact-avatar`, 32px |
| **Document card** (`.doc-card` + `.doc-thumb`) | **3** — `Documents-and-passport` (2), `Insurance` | Default | **Yes** — `.doc-thumb`, a 48px thumbnail of the scan or PDF |
| **Record entry** (`.record-entry`) | **3** — `Health-and-jabs` (2), `Health-and-jabs-record1` | Default, with `.record-action` | No |
| **Appointment entry** (`.appt-entry`) | **2** — `Vet-and-appointments`, `Vet-and-appointments-firstrun` | Default, with `.appt-status` | No |
| **Policy card** (`.policy-card`) | **2** — `Insurance`, `Insurance-firstrun` | Default | No |
| **Pinned card** (`.pinned-card`) | **2** — `Emergency-info`, `Health-and-jabs` | Default | No |

---

## Added to the kit during migration

Components promoted out of the one-off list because a migrated screen depends on them.
Each is measured from the screen that needed it, not designed fresh.

| Component | Screens where it appears | Available states | Requires a photo |
|---|---|---|---|
| **Confirm sheet** (`.pp-modal` + `.pp-sheet`) | **1 wired** — `Me` (log out, delete account); `home-new` and `home-progress-6` are the same block, not yet migrated. **Not** `Share-a-pet`: its QR modal is a different animal (scrim `.4` not `.5`, `z-index:100`, no scrim padding, and a header row with a close button) and stays the one-off it is listed as below | **Closed · Open** (`.is-open`). Scrim `rgba(0,0,0,.5)`, 340px max, 16px radius, `--sh-pop` | No |
| **Destructive text button** (`.pp-btn--dangerlink`) | **3** — `Me`, `Edit-pet`, `Edit-access-grant` | Default · Hover. Underlined, 13px, danger red, 44px hit area on a `normal` line-height | No |
| **Compact app bar** (`.pp-appbar--sm`) | **1+** — `Me`. A 48px bar with a centred title and no back/action | Default | No |
| **Inset form field** (`.pp-field--inset`) | **30** — every `.form-group` screen | Inherits the field's states; carries its own 16px inset when the form sits on the canvas | No |
| **Ruled switch row** (`.pp-switchrow--ruled`) | **8** — `Me`, `Add-care-note`, `Edit-care-note`, `Emergency-auth-setup`, `Reminder-settings` | **Off · On.** Banded top and bottom, full-bleed to the inset | No |
| **Collapsible section** (`.pp-collapse` + `__head` / `__body` / `__chev`) | **1** — `Shared-pet-view`. The listing card doubling as its own disclosure trigger | **Closed · Open** (`.is-open`). Card values match `.m-section-card`; the chevron rotates 180° over `--pp-t-state`. The head reuses `.pp-row__tile` / `.pp-row__body` / `.pp-row__meta` and `.pp-check` | No |
| **Bare brand bar** (`.pp-appbar--bare` + `.pp-appbar__brand` + `.pp-appbar__link`) | **1** — `Shared-pet-view`. The recipient has no app chrome, so the brand rides inside the hero band | Default. Transparent, no inset, 44px tall off the link's own tap target; brand at body-face 16/700 | No |
| **Arch chip line** (`.pp-arch__chip`) | **1** — `Shared-pet-view`. The third arch line under name and meta — microchip / registry id | Default. 12px muted, 2px off the meta, which drops its own bottom margin under `.pp-arch--recipient` | No |
| **Caution line** (`.pp-caution`) | **1** — `Shared-pet-view` (*"approach with caution around these animals"*) | Default. 12/600 in `--pp-danger`, sitting directly under the value it qualifies. Replaces `.warning-text` | No |
| **Subject avatar** (`.pp-avatar--miso`, from `--pp-img-miso`) | **1** — `Shared-pet-view` | Default. Carries the demo portrait so no screen needs an inline `background-image`. One modifier per subject the wireframes show | **Yes** — it *is* the photo |

### Added by the owner-flow migration

The owner flow — `My-Pets`, `home-success`, `Health-and-jabs`, `Documents-and-passport`,
`Personality-and-care`, `Share-a-pet`, `Who-has-access` and their state pages, 37 files —
brought these in. Everything measured from `home-success` or `Share-a-pet` where one of
them had the component; the rest measured from the grey screen it replaced.

| Component | Screens where it appears | Available states | Requires a photo |
|---|---|---|---|
| **Hero frame** (`.pp-hero__frame`) | **1** — `home-success`. Photo-width, centred, one layer above the photo so `.pp-hero__edit` can hang off its edge | Default | No — it holds the photo |
| **Plain arch** (`.pp-arch--plain`) | **1** — `Share-a-pet`. Name + meta with no shape: the hero above already drew the arch | Default. Its meta drops the 8px it reserves elsewhere | No |
| **Switcher band** (`.pp-switcher` + `__label`, `--tight`, `--split`) | **4** — `home-success`, `home-success-cheetah`, `Share-a-pet`, `Who-has-access` | `--split` = no separate track, so segments close the gap, each paints its own and only the pair's outer corners round. `--tight` = the shallower band a filter rides | No |
| **Segment avatar** (`.pp-seg__avatar`) | **3** — `home-success`, `home-success-cheetah`, `Share-a-pet` | **Inactive** (`--pp-tint-ink` on ink) · **Active** (`--pp-tint-paper` on paper). 22px, 8/700 initial | No — it is the initial that stands in for one |
| **Icon-only box** (`.pp-iconbox`) | **10** — every screen whose tile / tick / FAB still carries the text the icon replaced ("icon", "✓", "photo") | Default. Centres the box and renders the label invisibly | No |
| **Listing card** (`.pp-card--row` + `--inset`, `--dashed`, `__title`, `__body`) | **4** — `home-success`, `home-success-single`, `home-success-cheetah`, `My-Pets`, plus the pinned card on `Health-and-jabs` | `--dashed` = the section has nothing in it yet; `--inset` = the card stands alone and carries its own 16px | No |
| **Ruled band** (`.pp-ruled` + `--warn`) | **14** — the record list (`Health-and-jabs`), the document list (`Documents-and-passport`), the care notes (`Personality-and-care`) | Default · `--warn` (warm ground, title leads with ⚠). Last child drops its rule | No |
| **Head row** (`.pp-headrow`) | **14** — every ruled band and record entry with a trailing Edit | Default | No |
| **Unfilled slot** (`.pp-slot`) | **8** — `Personality-and-care` `-empty` / `-fill1…6` / `-firstrun` | Default. Dashed card holding the prompt for its first entry | No |
| **Quiet note** (`.pp-note`) | **9** — `Personality-and-care` family | Default. Full-bleed, surface ground, hairline foot | No |
| **Share CTA** (`.pp-btn--share`) + **CTA block** (`.pp-cta`) | **3** — `home-success`, `My-Pets`, `Who-has-access` | Default · Hover. The one button that leads with an icon | No |
| **Choice list** (`.pp-choices`) | **1** — `Share-a-pet`. The block a set of `.pp-choice` cards sits in | Default | No |
| **Drawn select** (`.pp-select--chev`) | **1** — `Share-a-pet` | Inherits the field's states. `appearance:none` + a Solar chevron on a 42px right gutter, so the glyph clears the border | No |
| **Plain app bar** (`.pp-appbar--plain`) | **3** — `Share-a-pet` `-empty` / `-error` / `-loading`. No fill of its own, hairline foot — the bar these states still render | Default | No |
| **Pet identity strip** (`.pp-identity` + `__body`, `__name`, `__meta`) | **22** — `Health-and-jabs`, `Documents-and-passport`, `Personality-and-care` families | Default. 40px avatar + serif-italic name + 12px meta, closed with a hairline | **Yes** — `.pp-avatar--md` |
| **Group heading** (`.pp-heading`) | **10** — `Health-and-jabs` (Jabs / Health records), `Who-has-access` (Expired / revoked) | Default. 13/700 uppercase on `--pp-ls-caps` | No |
| **FAB menu** (`.pp-menu`) | **3** — `Health-and-jabs`, `-firstrun`, `-record1` | **Closed · Open** (`.is-open`). Sits `--pp-tabbar-h + 84px` off the foot, `--sh-pop` | No |
| **Skeleton stack** (`.pp-skels` + `.pp-skel--card`) | **6** — every `-loading` state in the flow | Default. 72px cards on a 10px rhythm inside the canvas inset | No |
| **Grant detail block** (`.pp-detail` + `strong`) | **3** — `Who-has-access` | Default. The terms of one access grant set as a single 13/1.6 paragraph | No |
| **Flush actions** (`.pp-actions--flush`) | **3** — `Who-has-access`. The actions row inside a card, where the inset is already spent | Default | No |
| **Subject avatar** (`.pp-avatar--cheetah`, from `--pp-img-cheetah`) | **2** — `My-Pets`, `home-success-cheetah` | Default. Points at `visuals/pet-cat-cheetah.jpg`, the repo's own asset. `--pp-img-miso` stays on its Unsplash URL because the frozen reference screens render it | **Yes** — it *is* the photo |
| **Utilities** (`.pp-inset`, `.pp-sr`, `.pp-is-name`) | **12** | The kit's only three utilities. `.pp-inset` = the canvas inset alone; `.pp-sr` = present to a screen reader, absent to the eye; `.pp-is-name` = the serif italic a name takes in whatever slot it lands in | No |

New tiles and tints back these: `.pp-row__tile--insurance` / `--emergency`, and
`.pp-illus--warn` / `--wait` / `--pets` / `--share` / `--insurance` / `--emergency`
(each the same Solar glyph re-filled to `--pp-signal-ink`).

New tokens: `--pp-fs-fine: 12.5px` (the fine print — helper text, choice description),
`--pp-sh-float` (a control lifted off a photo), `--pp-sh-select` (a chosen card),
`--pp-tint-ink` / `--pp-tint-paper` (the two washes a control paints on itself),
`--pp-i-chev`, `--pp-img-cheetah`. `--pp-appbar-h` moved 68 → **48px** (the bar's floor;
44px tap targets take it to 68 on their own) and `--pp-tabbar-h` 0 → **60px** (measured;
the bar stays content-driven, the token is now only the clearance a FAB must keep).

The kit also carries its own `@import` for Bricolage Grotesque, Hanken Grotesk and
EB Garamond. It names three typefaces, so it must not depend on the host page linking
them — the grey screens loaded no webfont at all.

### Kit values corrected against the reference screens

The migrated screen is the measurement; the kit conformed to it. All measured on
`Shared-pet-view` (in the extraction set, and the only screen that uses these):

| Selector | Was | Now |
|---|---|---|
| `.pp-sharedfoot` | `padding:14px 16px`, `font-size:13px` | `padding:12px 16px`, `font-size:11px`, explicit `line-height:1.5` |
| `.pp-detail__label` | `12px`, `margin-top:12px` | `11px`, uppercase + `.04em`, `line-height:1.6`, `margin:10px 0 2px` |
| `.pp-detail__value` | `14px`, `line-height:1.5` | `13px`, `line-height:1.6`, `color:--pp-ink`, `margin-bottom:4px` |
| `.pp-collapse__head` | (no tracking rule) | `letter-spacing:normal` + `text-transform:none` — the page's `h1–h4` rule would otherwise pull `-0.01em` through |
| `.pp-collapse__chev` | inherits 16px, no motion | `font-size:17px`, `transition:transform`, and a `.is-open` 180° rule |
| `.pp-hero--recipient` | (no clip) | `overflow:hidden` — the inset band must not bleed |
| `.pp-avatar` | `background-repeat` unset | `no-repeat` |

Two new tokens back these: `--pp-fs-micro: 11px` (detail label, shared-link
footnote) and `--pp-lh-detail: 1.6` (reading copy inside an opened section),
plus `--pp-ls-caps: .04em` for uppercase labels.

`:where(.pp-collapse__body) p` carries the section's base reading copy (13 / 1.6
/ 4px) at element specificity, so a nested card's own paragraph rules still win —
the exact relationship `.shared-section p` had with `.vet-card p`.

#### Corrected by the owner-flow migration

Measured on `home-success` and `Share-a-pet` (plus its three states), each driven to a
zero computed-style diff against the pre-migration file:

| Selector | Was | Now | Proved by |
|---|---|---|---|
| `.pp-appbar` | `min-height:68px`, `padding:0 16px`, `gap:12px` | `min-height:48px`, `padding:12px 16px`, no gap — the box is 48px and grows to 68 on its own when the row carries 44px tap targets | `home-success`, `Share-a-pet` |
| `.pp-appbar__back` | `justify-content:flex-start`, `font-weight:600` | `center`, `400` | `home-success` |
| `.pp-appbar__action` | `margin-right:-10px`, `font-weight:600` | no negative margin (it sits flush to the inset), `400` | `home-success` |
| `.pp-appbar__title.pp-is-name` | `font-size:21.25px` (17 × `--pp-serif-scale`), `line-height:1` | `17px`, `line-height:1.5` — the app-bar name is set at the bar's own size | `home-success` |
| `.pp-iconbtn` | `display:inline-flex` + centring | `display:block` — the icon is the background, the box needs no inner layout | `home-success` |
| `.pp-hero__edit` | `box-shadow:--pp-sh-card` | `--pp-sh-float`, on a **doubled class** (`.pp-iconbtn` is declared later and won the shadow) | `home-success` |
| `.pp-stack` | (no list rule) | `list-style:none` — a stack is often a `<ul>` and must drop the marker without a `.pp` host | `home-success` |
| `.pp-arch__meta` | always `margin-bottom:8px` | `:has(+ .pp-tag)` zeroes it — the tag brings its own 10px lead. `Me` keeps the 8px, `home-success` needs 0 | `home-success` vs `Me` |
| `.pp-tag` | (no lead) | `margin-top:10px` | `home-success` |
| `.pp-seg` | `overflow:hidden`, no gap | `gap:0`, no clip — the track never clipped its segments | `home-success` |
| `.pp-seg__item` | `inline-flex`, `14px/600`, no padding, no radius; active corners keyed off `+` sibling | `flex`, `13px/500`, `padding:7px 14px`, `border-radius:pill` on the base; only the **active** segment squares a corner, and only on `:first-child` / `:last-child`; active also carries `border-color:ink` | `home-success` |
| `.pp-seg__item` hit area | `position:relative` + a `::before` inset on **every** segmented control | scoped to `--filter` only. The two-pet switcher's reference renders a static, unpadded pill, and the kit may not quietly re-position an element the reference leaves in flow | `home-success` |
| `.pp-counter` | `align-items:center`, `padding:0 16px 12px`, `gap:12px`, `13px`, `color:meta` | `align-items:baseline`, `padding:14px 16px 6px`, and the type moves to the parts: `__count` 14/600 ink (no `nowrap`), new `__meta` 12px meta | `home-success` |
| `.pp-choice` | `align-items:flex-start`, `gap:12px`, `padding:14px`, `text-align:left` | `center`, `10px`, `12px 14px`, `text-align:start`, `margin-bottom:8px`, and a selected state: ink edge + `--pp-sh-select` | `Share-a-pet` |
| `.pp-choice__radio` | `margin-top:2px`, `position:relative`, transparent, selected = ink `border-color` + an inset `::after` dot | no offset, no positioning, `background:paper`, selected = `border:6px solid ink` — the dot **is** the paper showing through | `Share-a-pet` |
| `.pp-choice__desc` | `13px`, `margin-top:2px` | `--pp-fs-fine` (12.5px), no offset | `Share-a-pet` |
| `.pp-help` | `13px`, `margin-top:6px` | `--pp-fs-fine`, `margin-top:4px` | `Share-a-pet` |
| `.pp-actions` | `padding:0 16px`, `margin-top:24px` | `padding:16px`, no top margin | `Share-a-pet` |
| `.pp-illus` | `background-size:52px`, `margin-bottom:16px` | `56px`, `20px`, plus `font-size:0; color:transparent` — the tile renders nothing but its glyph. 56px is what all **12** styled screens carry | `Share-a-pet-error`, `-loading` |
| `.pp-error` / `.pp-empty` | `padding:24px 16px`; title `700/1.3`; body `margin-top:6px` | `padding:60px 32px`; title `600/1.5` + `margin-bottom:8px`; body `line-height:1.5` + `margin-bottom:20px` | `Share-a-pet-error` |
| `.pp-tabbar` | `min-height:var(--pp-tabbar-h)` | no `min-height` — the bar is content-driven, and the token now means the FAB's clearance | `home-success`, `Me` |

Four more were corrected against the grey screens, where the kit class was simply wrong
for the element it had to carry: `.pp-btn--link` became `inline-flex` and centred (as an
`inline-block` its label hung off the top of the 44px tap target); `.pp-row__chev` picked
up the resets a `<button>` needs (`background`, `border`, `padding`, `font`); `.pp-fab`
became flex-centred with `text-decoration:none` so it works as a link as well as a button;
and `.pp-doc__thumb` centres its format label at 10/700 caps.

---

## One-offs — single-screen blocks, not going into the UI kit

These appear on exactly one screen each. Listed so nothing is lost, but they are deliberately **out of scope** for the kit.

| Screen | One-off block |
|---|---|
| `Share-a-pet` | QR code modal (`.modal-overlay`, `.modal-header`, `.modal-body`, `.modal-close`); bone + bowl hero illustration (`.sh-bone`, `.sh-bowl`) |
| `Whats-due` | Date strip / day sections (`.date-strip`, `.day-section`, `.day-list`, `.day-label`, `.day-empty`, `.wd-month`, `.wd-pet`) |
| `home-success` | Share CTA bar (`.m-share-cta`, `.btn-share`); pet segmented switcher (`.pet-seg`); round photo-edit button (`.photo-edit`); up-to-date tag (`.uptodate`) |
| `Shared-pet-view` | Document item (`.doc-item`, `.doc-name`); emergency link; vaccination list (`.vax-list`); vet card's 13px call button — a sub-44px legacy control the kit's `.pp-btn` deliberately does not reproduce |
| `Emergency-allowed` | Contact card (`.contact-card`, `.contact-name`, `.contact-phone`); emergency step list; important notes; medication list; auth highlight |

> **`Emergency-allowed` (all 4 states) is not on the kit.** That family never had
> The Signal applied: it still runs the pre-Signal token set (`#1a1a1a` ink,
> `#757575` muted, `#333333` button, `#f5f5f5` surface, `#e0e0e0` line,
> `#d0d0d0` placeholder) and loads no webfont, so every kit class differs from
> what is on screen in colour, face and metrics. It needs the Signal restyle
> first; migrating it onto the kit is the step after that, not instead of it.
| `Who-has-access` | Expired grant card (`.expired-card`, `.expired-section`, `.expired-heading`, `.expired-meta`); grant actions |
| `home-new` | Add-a-pet sheet (`.add-sheet`, `.add-modal`, `.add-option`, `.opt-body`, `.opt-arrow`) |
| `Me` | Confirm sheet (`.me-sheet`, `.me-modal`); danger link; toggle label + description |
| `Emergency-info` | Authorisation detail / link / status; contact entry; info footer |
| `My-Pets` | Pet card (`.pet-card`, `.pet-card-info`); fill hint |
| `Whats-due-detail` | Reminder detail block (`.rd-title`, `.rd-due`, `.rd-badge`, `.rd-primary`, `.rd-view`) |
| `Edit-health-record` | Record fields (`.ehr-title`, `.ehr-date`, `.ehr-vet`, `.ehr-notes`, `.ehr-followup`) |
| `Document-view` | Document viewer (`.dv-thumb`, `.dv-title`) |
| `home-progress-6` | Done sheet + done illustration (`.done-sheet`, `.done-modal`, `.done-illustration`, `.done-later`) |
| `Forgot-password` | Request form / sent confirmation (`.fp-form`, `.fp-sent`) |
| `Shared-pet-view-empty` | Empty notice (`.empty-notice`) |
| `Emergency-allowed-error` | Fallback contacts (`.fallback-contacts`) |

---

## Notes

**Chat bubble — does not exist.** It was on the list to include, but no messaging screen was ever wireframed. `sitemap.md` carries **"14. Vet message thread / request (chat)"** as an entity and lists *Vet messages* in the tree, but flags it **`[MVP scope ?]`** — an open question ([sitemap.md:150, 197](../research/sitemap.md)). Searching all 123 files returns zero classes containing *chat*, *message*, *bubble*, *thread* or *reply*. The eight `Vet-*` screens are appointments and clinic details, not conversations. Rather than invent a row, it is recorded here as a **gap**: if Vet messages enters MVP, the chat bubble is a component that must be designed from scratch.

**Board components with no wireframe yet.** The language board demos several patterns that exist on the board only and appear in **no** wireframe: illustration tile (`.illus`), generic segmented control (`.seg`), section row (`.srow`), choice card (`.choice`), confirm sheet (`.sheet`), round icon button (`.iconbtn`), calendar tiles (`.daystrip` / `.daycell`), pet pair (`.petpair`) and link button (`.linkbtn`). Most are *renames* of things that do exist — `.srow` is the section card, `.choice` is the scope radio, `.illus` is `.empty-illustration`, `.iconbtn` is `.photo-edit`. The calendar tiles and pet pair have no wireframe counterpart at all.

**Photo dependency, in total.** Seven components need a photograph: Avatar, Pet identity strip, Arch hero, Recipient info block, Pet toggle, Photo upload area, Contact row — plus Document card, which needs a document thumbnail rather than a pet photo. Across all 123 screens only **11** real image references are wired (10 Unsplash, 1 `assets/cat.png`); every other photo slot renders as its grey ground awaiting an image.

**Components carrying no state variants.** App bar, back control, helper text, danger zone, and most card types have a single rendering. That is a finding, not an omission — several of them, particularly the cards, will need at least a loading and an error treatment once the grey screens are restyled.
