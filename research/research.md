# PetPal — Competitor Benchmark

Sources: live product/website review (Playwright screenshots in [`screens/`](screens/)) + public web research (app stores, product sites, press).
Screens marked `[?]` are behind login / could not be accessed and are based on web research only.

**Note on "Trust" column:** every quantitative claim (rating, review count, certification, client list) carries an inline source + access date. Where a number could not be independently verified, it is labelled `(unverified, company claim)` rather than stated as fact. Vague descriptors like "good UX" or "clean interface" are avoided in favour of naming the specific screen/flow they refer to.

---

## 🔴 HARD — Same product, same audience, EU market

| | Name | Type | Audience | Product foundation | Key mechanism | Trust | Monetization |
|---|---|---|---|---|---|---|---|
| 1 | **Lassie** 🇸🇪 [screenshot](screens/hard_01_lassie.png) | Pet insurance + health app | SE pet owners (dogs/cats), digitally native | Insurance core with app-based health layer | Gamified "health program" — earn discounts via courses/quizzes; direct vet billing | Direct vet settlement (no out-of-pocket), Tractive partnership, transparent pricing tiers | Monthly/annual insurance premiums, tiered (Bronze/Silver/Gold), upsells via multi-pet discount |
| 2 | **Felmo** 🇩🇪 [screenshot](screens/hard_02_felmo.png) | Home vet visit service + app | DE pet owners, busy professionals, anxious-pet households | Vet-as-a-service; app is a companion to real-world visits | Book a vet to come home; digital health record created per visit | Vets shown by name with photo + credentials on the [booking screen](screens/hard_02_felmo.png); fees follow the official German GOT tariff (regulated pricing, per [felmo.de](https://felmo.de)). Total active vet count not publicly disclosed `(unverified, company claim)` | Per-visit vet fees (regulated tariff) + product shop |
| 3 | **FirstVet** 🇸🇪/EU [screenshot](screens/hard_03_firstvet.png) | Video vet consultation + pet shop | EU pet owners (SE, UK, DE, DK, NO expanding), all species incl. exotics | Telehealth-first, e-commerce attached | Video call with vet 6am–2am, digital prescription, then product recommendation | App Store rating **4.7/5 from 444 ratings** ([apps.apple.com/us/app/firstvet/id1349241101](https://apps.apple.com/us/app/firstvet/id1349241101), accessed Jun 2026). "100% satisfaction from 600k+ users" is FirstVet's own marketing claim `(unverified, company claim)`. Insurance-bundling: multiple insurer partnerships are listed on [firstvet.com](https://www.firstvet.com), exact count "11+" not confirmed | Consultation fees (often insurance-covered) + retail markup on supplies |
| 4 | **PetDesk** 🇺🇸 (used in EU clinics) [screenshot](screens/hard_04_petdesk.png) | Vet clinic communication platform | Vet clinics (B2B) with owner-facing app | Clinic-side software with client app layer | Direct booking, two-way messaging, "Scribe" voice-to-schedule for staff | "12,000+ clinics trust PetDesk" — stated on [petdesk.com](https://petdesk.com) homepage, accessed Jun 2026 `(company claim, not third-party verified)`. A 2025 PetDesk blog post cited 8,200+ clinics, suggesting the 12,000 figure may include a broader partner definition | B2B SaaS to clinics — owners use free; this is the white-label model PetPal could become |
| 5 | **Tractive** 🇦🇹 [screenshot](screens/hard_05_tractive.png) | GPS + health tracker (hardware + app) | EU-wide pet owners, active/outdoor pets | Hardware tracker + subscription app | Live location, virtual fences, health/sleep/activity insights, bark & scratch monitoring | Trustpilot **TrustScore 4.6/5 from ~37,000 reviews** ([trustpilot.com/review/tractive.com](https://www.trustpilot.com/review/tractive.com), accessed Jun 2026; 77% are 5-star). "175-country coverage" is stated on [tractive.com](https://tractive.com) `(unverified, company claim)` | Hardware sale (€49–79) + mandatory subscription |

### What to study
- **Lassie**: gamification of preventive care — could inspire reminder "streaks" or rewards in PetPal
- **Felmo**: how a real-world service visit becomes a clean digital record — model for vet-uploaded records
- **FirstVet**: insurance-bundling as distribution — relevant to PetPal's insurance referral monetization
- **PetDesk**: the clinic-to-owner two-way messaging UX — directly maps to PetPal's vet communication feature and white-label ambition
- **Tractive**: health data visualization (activity/sleep) — reference for PetPal's health dashboard

---

## 🟡 SOFT — Different product, same JTBD (keep info, documents, reminders)

| | Name | Type | Audience | Product foundation | Key mechanism | Trust | Monetization |
|---|---|---|---|---|---|---|---|
| 1 | **MyTherapy** [screenshot](screens/soft_01_mytherapy.png) | Medication reminder + health diary (human health) | People managing chronic conditions / medication schedules | Reminder + logging engine, single dashboard | Passive intake logging, one-time codes to share health report with doctor | **100,000+ 5-star ratings** on Google Play ([play.google.com/store/apps/details?id=eu.smartpatient.mytherapy](https://play.google.com/store/apps/details?id=eu.smartpatient.mytherapy), accessed Jun 2026). Privacy-first positioning is stated on [mytherapyapp.com](https://www.mytherapyapp.com). Previously listed "featured in Wired/ABC/Healthline" — **removed**, could not find a source for this claim | Free — funded via pharma/health-institute partnerships |
| 2 | **Google Keep** `[?]` [screenshot](screens/soft_02_googlekeep_LOGIN.png) | General notes app | Anyone — default tool for ad-hoc pet info today | Free-form notes/lists, no structure | Quick capture, photo attach, simple reminders | Google account trust | Free, ad-supported ecosystem |
| 3 | **Notion** [screenshot](screens/soft_03_notion.png) | Personal workspace / templates | Power users who build custom "pet trackers" themselves | Database + page building blocks, huge template library | Templates for "personal" life management (incl. pet trackers made by community) | Large template marketplace, community-vetted | Freemium — free for personal use, paid for teams/AI |
| 4 | **Apple Wallet** [screenshot](screens/soft_04_applewallet.png) | Document/card storage | iPhone users storing IDs, cards, passes | Native OS-level secure storage | Add pass/card via scan or app integration, lives on lock screen | Apple ecosystem security (Face ID-gated) | Free — platform feature, not a product |
| 5 | **Tractive (health module)** — see Hard #5 | GPS + health tracker | Same as above, but JTBD overlap is the health/activity log, not location | Sensor-driven logging vs. manual entry | Automatic vs. PetPal's manual/photo entry | Same as above | Same as above |

### What to study
- **MyTherapy**: this is the closest *non-pet* analog to PetPal's reminder + doctor-sharing flow — the "one-time code to share with doctor" pattern is directly transferable to PetPal's vet-sharing feature
- **Google Keep / Notion**: these represent the "good enough" status quo — understand why people *don't* switch, and what minimum structure would justify migrating
- **Apple Wallet**: the bar for frictionless document storage — PetPal's insurance/legal doc storage should feel this lightweight
- **Tractive**: passive data logging vs. PetPal's manual entry — a gap PetPal could close with optional device integrations later

---

## 🟣 ASPIRATIONAL — International benchmarks, pet companion category

| | Name | Type | Audience | Product foundation | Key mechanism | Trust | Monetization |
|---|---|---|---|---|---|---|---|
| 1 | **Rover** 🇺🇸 [screenshot](screens/asp_01_rover.png) | Pet sitting / dog walking marketplace | Pet owners + sitters/walkers (two-sided) | Marketplace with detailed pet + sitter profiles | Pet profile shared with sitter incl. care instructions, feeding, meds, behaviour notes | Sitter reviews, background checks, booking guarantee | Marketplace commission on bookings |
| 2 | **Airvet** 🇺🇸 [screenshot](screens/asp_02_airvet.png) | Telehealth via employee benefits | Employers (B2B2C) → employee pet owners | 24/7 virtual vet care bundled as a workplace perk | On-demand video vet, online pharmacy, family-sharing of benefit | **SOC 2 Type II** achieved 2024 and **90+ NPS for 2 consecutive years** (up from 80→93 in 2024, 71% client response rate) — both per [airvet.com/blog/airvet-nps-90-2025](https://www.airvet.com/blog/airvet-nps-90-2025), accessed Jun 2026. **Adobe is a named employer client** (same source). "Workday" is a **strategic Workday Wellness integration partner**, not a confirmed client — corrected from the earlier "Fortune 500 clients (Adobe, Workday)" framing | B2B benefits contracts — "pays for itself in year 1" framing |
| 3 | **BabelBark** 🇺🇸 [screenshot](screens/asp_03_babelbark.png) | Multi-stakeholder pet health platform | Owners + vets + pet businesses + shelters | "Links everybody in a pet's life" — role-based connected network | Syncs health data across all parties; real-time updates between vet visits | Industry-leader endorsements, shelter partnerships | Register/sign-in funnels per stakeholder type — likely B2B2C across clinics/businesses |
| 4 | **PetDesk (owner side)** — see Hard #4 | Vet communication platform | Same as Hard #4 | Owner app layer of clinic software | 24/7 self-service booking + messaging | Same as Hard #4: "12,000+ clinics" is a company claim (petdesk.com), a 2025 PetDesk blog post cited 8,200+ `(unverified, company claim)` | Free to owners, B2B SaaS to clinics |
| 5 | **MyTherapy (cross-category)** — see Soft #1 | Health reminder/diary | Same as Soft #1 | Reminder engine | Doctor-sharing via one-time code | Privacy-first positioning | Free, sponsor-funded |

### What to study
- **Rover**: the **pet care profile shared with a third-party caregiver** is *exactly* PetPal's "Pet Personality Profile" use case at scale — study the structure of what info sitters see and how it's presented
- **Airvet**: B2B2C distribution model (employer-sponsored) — a future monetization channel beyond vet/insurance partnerships
- **BabelBark**: closest existing attempt at PetPal's full vision (owner + vet + business + shelter network with role-based access) — worth a deeper teardown of their registration flows for each role type
- **PetDesk**: white-label potential — if PetPal succeeds, this is the adjacent business model (B2B SaaS to clinics)

---

## ✅ 3 Shared Patterns Across All Groups

1. **Insurance and monetization are deeply entangled with health records.** Lassie, FirstVet, and Airvet all bundle financial products (insurance, employer benefits) directly with health data — the data itself is the retention/monetization hook, not a side feature.
2. **"Share with a third party via a simple code/link" is a recurring trust mechanism.** MyTherapy's one-time doctor code, Rover's pet profile shared with sitters, and BabelBark's multi-party sync all solve PetPal's "transferable between vets/walkers" requirement the same way: lightweight, time-boxed sharing rather than full account access.
3. **Mobile-first, app-centric experience is the default expectation**, even for products with a B2B core (PetDesk, Airvet) — the owner-facing layer is always a clean, simple app regardless of how complex the backend is.

## ⚡ 3 Key Differences

1. **Manual vs. passive data entry.** Tractive logs health data automatically via hardware; Lassie, Felmo, MyTherapy, and PetPal rely on manual or photo-based entry. PetPal sits in the "manual" camp — UX must minimize friction here since there's no sensor doing it for the user.
2. **Single-species vs. multi-species support.** Most direct competitors (Lassie, Felmo, Tractive) focus on dogs/cats only. FirstVet and PetPal's planned scope (5 species incl. rabbits, guinea pigs, birds) are broader — fewer reference patterns exist for non-dog/cat profile structures.
3. **Role-based multi-user access is rare and underbuilt.** Only BabelBark attempts true multi-stakeholder access (owner/vet/business/shelter); everyone else is single-owner or B2B-only. This is a genuine whitespace for PetPal but also means there's little proven UX to copy — most of this will need original design work.

## ❓ 3 Questions for the PM

1. **How "real-time" does vet communication need to be at MVP?** PetDesk and BabelBark both invest heavily in real-time sync between owner and vet — is that core to PetPal's MVP, or can v1 ship with async messaging + manual record sharing (like MyTherapy's doctor code)?
2. **Should PetPal pursue passive data sources (wearables/trackers) at all, even as a "connect your Tractive" integration?** Tractive already partners with Lassie — is there an opportunity (or risk of redundancy) in supporting third-party device data instead of building our own?
3. **Which monetization comes first — insurance referral or vet/clinic partnerships?** FirstVet's insurance-bundling and PetDesk's clinic-SaaS model represent two very different go-to-market paths, and they likely imply different MVP feature priorities (insurance docs/reminders vs. vet messaging/booking). Which should the design prioritize for v1?

---

## 🔎 Follow-up research after personas

**Question tested:** *Is the core pain (scattered records / forgotten vaccinations / sitter info gaps) real and strong enough to make people switch from WhatsApp/Notes?* This was the #1 gap flagged in the persona/JTBD critique. Sources below are public app-store reviews, sitter-guidance articles, and the template market — **not** PetPal-target interviews, so this raises confidence but is not validation.

**F1 — The pain sustains a whole product category (pain is real). 🟢**
There is an active category of apps built *explicitly* to fix this: 11pets ([apps.apple.com/us/app/11pets-pet-care/id1232470530](https://apps.apple.com/us/app/11pets-pet-care/id1232470530)), VetKit, and **PetVax — "designed to replace the crumbling paper card with a clean Health Passport that vets and boarding facilities prefer"** ([apps.apple.com/us/app/-/id6758548102](https://apps.apple.com/us/app/-/id6758548102), accessed Jun 2026). Marketing framing `(company claim)`, but the *existence* of many such apps with positive reviews is real demand signal.

**F2 — The Notes/paper → structured-app switch is documented by a real user. 🟢 (directly answers the question)**
A reviewer reported tracking their pets in the phone **Notes app** "but it was getting tedious having to scroll through the long notes," which led them to switch to a structured pet-record app (PetNote+, [apps.apple.com/us/app/petnoteplus-dog-and-cat-care/id1553584485](https://apps.apple.com/us/app/petnoteplus-dog-and-cat-care/id1553584485), via review search accessed Jun 2026). This is direct evidence of (a) Notes as the real status quo, (b) the **tipping point = volume/tedium of scrolling**, and (c) people *do* switch. Notably this reviewer kept *geckos* — a first signal from outside the dog/cat majority.

**F3 — Sitter handoff is a real, structured behaviour today. 🟢**
Owners already assemble sitter info — but in **Google Sheets templates, printable PDFs, and texted/emailed photos**, not only WhatsApp. A template market exists ([youarelovedtemplates.com pet-sitter sheet](https://youarelovedtemplates.com/products/pet-sitter-instructions-pet-sitter-information-pet-sitter-pet-sitter-notes-google-sheets-pdf-cat-sitter-dog-sitter)), and veterinary guidance (AAHA, "Preparing for the Unexpected: Essential Pet Sitter Instructions") spells out the same fields PetPal plans (profile, routine, feeding, meds, emergency contacts). The demand is real; the status-quo tools are docs/sheets/printables/text.

**F4 — The make-or-break is *capture friction*, not whether the pain exists. 🟢**
Reviews of pet-record apps repeatedly flag data entry as "tedious" or needing "some learning… to input data" (Pet Health app reviews, [apps.apple.com/us/app/pet-health/id6447807502](https://apps.apple.com/us/app/pet-health/id6447807502?see-all=reviews), accessed Jun 2026). This sharpens the existing manual-entry concern (see [§Key Differences](#-3-key-differences), point 1): the bet isn't "does the pain exist" (it does) — it's **whether PetPal makes capturing/maintaining the record low-effort enough to beat 'good enough' inertia.**

**What this changes**
- The "good enough status quo stops people switching" framing is **too strong** — people *do* migrate, but only past a tipping point (volume/tedium) and only if the new tool is low-friction. Corrected in [personas.md](personas.md).

**Still open (not closed by this round) `[?]`**
- **No EU-mainland voices** — every source is US/English-language app stores. The launch-market user remains unverified.
- **No evidence for the "Facebook groups / acquaintances" sitter-recommendation channel** — searched, not found. Kept as `[?]` in [personas.md](personas.md).
- **No strong "I refuse to switch" inertia voice** either — so the *size* of the switching barrier is still unmeasured; F4 is a risk, not a proven blocker.
- **The receiving caregiver's own view** is still absent — sitter-guidance articles are written *for owners*, not *by* sitters.

### Round 2 — Receiving caregiver needs & no-signup access

**Question tested:** *What does the receiving caregiver (sitter / walker / new vet) actually need, and will they accept no-signup access?* This was flagged as the **highest-risk gap** (zero caregiver voice). Sources are sitter-industry guidance, release-form templates, Rover's own docs, and general sign-up/auth UX research — **still owner-/industry-facing, not lived sitter testimony.**

**F5 — The caregiver's essential info needs are well-documented (confirmed). 🟢**
A consistent checklist appears across independent sitter-guidance sources: **owner + emergency contacts** (incl. travel companions), **vet office details**, a **vaccination + medication list** (name, dose, frequency, route), age/weight/sex, medical history, microchip number, plus daily routine, feeding specifics and dos/don'ts. Sources: Pet Sitters International veterinary release form ([petsit.com/veterinary-release-form](https://www.petsit.com/veterinary-release-form)), Preventive Vet ([preventivevet.com/pets/pet-sitter-treatment-authorization](https://www.preventivevet.com/pets/pet-sitter-treatment-authorization)), AAHA (Round 1). This maps closely to PetPal's planned profile — **the content model is validated**.

**F6 — A need PetPal's brief does NOT cover: emergency vet *treatment authorization* + spend cap. 🟢 (new)**
Every sitter release-form source centres on something absent from PetPal's model: **explicit permission to seek emergency vet care, a pre-approved cost limit, and a payment arrangement** ("authorize treatment up to a certain amount"). Sources: [Pet Sitters International](https://www.petsit.com/veterinary-release-form), [Preventive Vet](https://www.preventivevet.com/pets/pet-sitter-treatment-authorization). **Design implication:** the shared caregiver view likely needs an "in an emergency: your vet is X · you're authorized up to €Y · pay via Z" block. Currently nowhere in [CLAUDE.md](../CLAUDE.md).

**F7 — No-signup access is the right default — supported by analogy, not by sitter voice. 🟡**
Account-creation/auth friction is a heavily documented abandonment driver: 15–25% drop-off at password steps, **92% of users abandon rather than reset a forgotten password**, gated forms convert at just 2–3%, and friction "impacts 100% of visitors" ([securityboulevard.com/2026/03/how-authentication-friction-affects-conversion-rates](https://securityboulevard.com/2026/03/how-authentication-friction-affects-conversion-rates-the-data-behind-frictionless-login/)). Recipients also actively resent a supposedly-open link that still gates them (Google Docs "view-only shared link still requires sign-in" support thread). **Caveat:** this is SaaS/e-commerce UX research, **not pet-sitting** — strong analogy that forcing a one-week sitter to sign up would cause drop-off, but not direct caregiver testimony.

**F8 — The recipient sees exactly what the owner entered — completeness is the owner's job. 🟢**
Rover confirms "sitters only see the care instructions that clients have entered" ([rover.com sitter resources](https://www.rover.com/blog/sitter-resources/communication-on-rover-a-step-by-step-guide/)). This reinforces the capture-friction risk (F4): a half-filled profile leaves the sitter flying blind. A documented real failure mode — a dog got loose and the owner wasn't told for an hour ([news report](https://www.yahoo.com/news/dog-owner-beloved-pet-dies-184344896.html)) — underlines that a *working owner-contact / update-back path* is part of the caregiver's real need, not a nice-to-have.

**What this changes**
- The Receiving Caregiver's needs are **no longer all `[?]`** — the info checklist and the no-signup expectation now have evidence. The persona's "everything is hypothesis" framing is corrected in [personas.md](personas.md), and the **emergency-authorization gap (F6)** is added as a new need.

**Still open `[?]`**
- **No lived sitter/walker/vet voice** — every source is written *for* owners or *by* the industry. The persona still lacks a first-person caregiver quote.
- **The no-signup conclusion is by analogy** (F7) — untested with actual sitters; whether they'll use a link vs. fall back to "just text me" is unknown.
- **The vet recipient** specifically is still unaddressed — all Round-2 evidence is about sitters/walkers, not vets meeting the pet for the first time.

### Round 3 — Which job is most frequent and most painful?

**Question tested:** *Of the three jobs — planning-ahead (records/reminders), sitter-handoff, and the worried moment (emergency) — which is most frequent and most painful?* This decides the true primary persona and should replace the **assumed** importance scores in the JTBD matrix. Sources are usage statistics, app-review themes, and owner surveys — **US-skewed, general pet-owner data, not PetPal users.**

**F9 — Planning/records is the most *frequent* felt need. 🟢**
Vet *events* are only ~1–2×/year (dogs ≈1.5, cats ≈0.7 visits/yr; ~half of owners go once a year — [AVMA / PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7143178/)). But the **record/proof** need recurs far more often: boarding, daycare, grooming and travel all **require written proof of vaccination**, and "simply stating your dog is up-to-date is usually not enough" ([PetSmart day-camp requirements](https://services.petsmart.com/content/daycamp-requirements); [Hemopet](https://hemopet.org/boarding-kennels-and-grooming-vaccination-laws-and-issues/), which notes the rules are "vague… cause outright confusion and frustration"). So retrieving/proving records is a **recurring, multi-touchpoint friction**, not a once-a-year one.

**F10 — Records/reminders is the #1 *adoption driver* for pet apps. 🟢**
Across pet-record app review round-ups, **vaccination reminders + record/proof storage** are consistently the most-praised and most-requested features — owners explicitly ask to "upload hard copy vaccination documents" because "it's difficult to keep track of all paperwork" ([PetNoter](https://petnoter.com/best-pet-care-apps/), [JGDHealth](https://pets.jgdhealth.com/blogs/top-7-best-pet-vaccine-tracking-apps-you-should-know/), accessed Jun 2026). This is the job that actually pulls people into the category.

**F11 — But pain *intensity* ranks in the opposite order. 🟢**
Sitter-handoff carries a heavy emotional load: **56% of owners feel "overwhelming guilt and anxiety" leaving pets**, 61% worry about their pet's welfare on vacation, and 52% have been "too guilty to go" ([Trusted Housesitters survey](https://stevedalepetworld.com/blog/separation-anxiety-from-pets/); PetMeds 2,000-owner survey). The worried/emergency moment is the highest acute stress but **rare** ("few pet owners are prepared for emergencies"). Planning is the lowest-intensity (administrative). → **Frequency order (planning > sitter > emergency) is the reverse of pain-per-event order (emergency > sitter > planning).**

**F12 — Counter-nuance on the reminder job. 🟡 `[?]`**
Vaccine hesitancy is non-trivial — **22% of dog owners / 26% of cat owners are vaccine-hesitant**, ~40% believe canine vaccines are unsafe ([Boston University / AVMA](https://www.bu.edu/articles/2023/nearly-half-of-dog-owners-are-hesitant-to-vaccinate-their-pets/)). This may shrink the audience for the *"remind me to vaccinate"* job specifically — but the **records/proof** need persists regardless (boarding still demands proof), so the *records* job is more robust than the reminder job alone. EU size of this effect unknown `[?]`.

**Conclusion (resolves the question)**
- **Most frequent + main adoption driver:** planning/records → the **Organised Owner's** core job.
- **Most painful per event:** the worried moment (rare, and PetPal can serve only the info slice), then sitter-handoff (very high, well-evidenced guilt/anxiety), then planning.
- **Best frequency × pain × serviceability for the *core*:** planning/records (frequent + serviceable). **Sitter-handoff is the high-emotion episodic spike** PetPal can genuinely ease — less frequent, but intensely felt and the documented market whitespace.

**What this changes**
- The **Organised Owner stays primary, but on firmer grounds**: not "she exercises the full loop" (the earlier, weak rationale flagged in the critique) but "she owns the **most frequent felt need and the #1 reason people adopt these apps**." Corrected in [personas.md](personas.md).
- The **Worried Owner is confirmed secondary** by frequency (rare per person) and serviceability (info-only).
- **Action for the JTBD matrix** (not edited here): the assumed OO importance "3"s on the planning/records jobs are now **frequency-backed**, and the sitter-handoff job should be read as **lower-frequency / higher-intensity** rather than uniformly "important."

**Still open `[?]`**
- All stats are **US surveys / English app stores** — no EU-market frequency or pain data.
- "Most painful" is inferred by comparing **separate** surveys, not a single head-to-head ranking study.
- These measure **general** pet owners, not people who have chosen a tool like PetPal.

### IA cross-check — gaps the architecture made concrete

Building the [sitemap / flows / IA](sitemap.md) surfaced three structural points where the **design now depends on data we don't have** (none invented here — flagging for the next research round):
- **Carer→owner updates (R4)** — the IA has *no page* for "proof my pet's okay while away" because there's no validated need or caregiver voice (parked, [jtbd.md R4](jtbd.md)). If owners actually want this, the tree is missing a branch — **needs RC-side validation**.
- **In-app vet *messaging* vs. record-*sharing* (R3)** — the tree carries a *Vet messages* page, but whether real-time messaging (not just sharing a record) is wanted at MVP is **still the open PM question** above — unvalidated demand for a whole page.
- **Emergency authorization data (F6)** — *Emergency info & authorization* is now a real screen, but the **spend-cap / payment / who-may-authorize** data behind it is a documented caregiver need (F6) with **no owner-side evidence** that owners will fill it in. Capture-friction risk (F4) applies doubly here.

---

## Competitor Language

Verbatim UI/marketing copy pulled from live product pages and app stores (accessed **Jul 2026**) — collected to see where the whole category *sounds the same*, so PetPal's voice can stand apart. Quotes are word-for-word; each carries its source.

| # | Competitor | Verbatim line | What it names | Pattern |
|---|---|---|---|---|
| 1 | 11pets | "The most complete pet care app" | tagline | completeness claim |
| 2 | 11pets | "From nose to tail and everything in between" | scope | completeness claim |
| 3 | 11pets | "Track your pet's weight, vital signs, and activities all in one place" | features | "all in one place" + list |
| 4 | 11pets | "medical records, veterinary visits, unlimited pet seats" | features | clinical feature inventory |
| 5 | 11pets | "Track flea & tick medication, medical/vet incidents, vaccinations" | health section | clinical labels |
| 6 | 11pets | "you are the owner of your data at all times" | trust | data-ownership cue |
| 7 | Pet Health | "A Professional Health Application for Your Pets." | positioning | clinical |
| 8 | Pet Health | "Your pet's digital booklet. Keep it next to yours." | tagline | warm + clever *(exception)* |
| 9 | Pet Health | "Never forget a treatment, the app will remind you." | reminders | functional |
| 10 | MyTherapy | "your personal, digital health companion" | positioning | warm *(the bar)* |
| 11 | MyTherapy | "a safe and uncomplicated one-time code … share … at the push of a button" | sharing | trust + effortless |
| 12 | Lassie | "Care more. Get more." | tagline | warm, punchy |
| 13 | Lassie | "Most pet insurers only know your pet when it's sick. Lassie is there every day." | positioning | warm, relationship |
| 14 | Lassie | "Cover vet costs, support healthier years, feel calmer doing it." | benefit | ends on a feeling |
| 15 | Lassie | "Kind help from real pet lovers" | support | warm, human |
| 16 | Rover | "care instructions" — fields *feeding, medication, bathroom routine* | the sitter-facing profile | warm section name (not "records") |
| 17 | Rover | "You haven't added care instructions for Buster and Kelce yet" | empty state | plain, uses pet names |
| 18 | PetVax *(F1)* | "replace the crumbling paper card with a clean Health Passport that vets and boarding facilities prefer" | positioning | proof/trust for third parties |
| 19 | owners, PetNoter *(F10)* | "it's difficult to keep track of all paperwork" | the felt pain | the need in the owner's own words |

Sources: [11pets App Store](https://apps.apple.com/us/app/11pets-pet-care/id1232470530) · [11pets.com](https://11pets.com/en/) · [Pet Health App Store](https://apps.apple.com/us/app/pet-health/id6447807502) · [mytherapyapp.com](https://www.mytherapyapp.com/) · [lassie.co](https://lassie.co/en) · [Rover community — "care instructions" empty state](https://www.rover.com/community/question/48885/why-do-i-keep-seeing-you-havent-added-care-instructions-for-buster-and-kelce-yet/) · PetVax/PetNoter as cited in §F1/§F10 above. All accessed Jul 2026.

**Three things the whole category does — so PetPal shouldn't:**
1. **Claims completeness.** "Most complete" · "everything in between" · "all in one place" (#1–3). The category competes on *how much* it holds — table stakes, and nobody owns *trust*.
2. **Names things clinically.** "medical records" · "medical/vet incidents" · "A Professional Health Application" (#4,5,7). Admin, cold, hospital-flavoured. **Rover is the lone warm exception** — "care instructions", pet names in the empty state (#16,17).
3. **Lists features.** "Track X, Y, Z" (#3,5) — an inventory of what the database stores, not what the owner is trying to *do*.

**Where the good ones point (our bar):** MyTherapy's "personal, digital health companion" and "safe and uncomplicated one-time code"; Lassie's "there every day" / "feel calmer doing it"; Pet Health's "Keep it next to yours." Warmth, relationship, and **a feeling at the end of the line** — never a spec sheet.

**The gap PetPal takes:** everyone says *complete* → we say **trusted**. Everyone lists *records* → we speak to the **moment**: *"for every walk, vet visit, and weekend away."*
