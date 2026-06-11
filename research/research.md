# PetPal — Competitor Benchmark

Sources: live product/website review (Playwright screenshots in [`screens/`](screens/)) + public web research (app stores, product sites, press).
Screens marked `[?]` are behind login / could not be accessed and are based on web research only.

---

## 🔴 HARD — Same product, same audience, EU market

| | Name | Type | Audience | Product foundation | Key mechanism | Trust | Monetization |
|---|---|---|---|---|---|---|---|
| 1 | **Lassie** 🇸🇪 [screenshot](screens/hard_01_lassie.png) | Pet insurance + health app | SE pet owners (dogs/cats), digitally native | Insurance core with app-based health layer | Gamified "health program" — earn discounts via courses/quizzes; direct vet billing | Direct vet settlement (no out-of-pocket), Tractive partnership, transparent pricing tiers | Monthly/annual insurance premiums, tiered (Bronze/Silver/Gold), upsells via multi-pet discount |
| 2 | **Felmo** 🇩🇪 [screenshot](screens/hard_02_felmo.png) | Home vet visit service + app | DE pet owners, busy professionals, anxious-pet households | Vet-as-a-service; app is a companion to real-world visits | Book a vet to come home; digital health record created per visit | 143+ named vets w/ credentials, testimonials, official GOT fee schedule (regulated pricing) | Per-visit vet fees (regulated tariff) + product shop |
| 3 | **FirstVet** 🇸🇪/EU [screenshot](screens/hard_03_firstvet.png) | Video vet consultation + pet shop | EU pet owners (SE, UK, DE, DK, NO expanding), all species incl. exotics | Telehealth-first, e-commerce attached | Video call with vet 6am–2am, digital prescription, then product recommendation | "98% satisfied", 4.9 app rating, bundled into 11+ insurance policies | Consultation fees (often insurance-covered) + retail markup on supplies |
| 4 | **PetDesk** 🇺🇸 (used in EU clinics) [screenshot](screens/hard_04_petdesk.png) | Vet clinic communication platform | Vet clinics (B2B) with owner-facing app | Clinic-side software with client app layer | Direct booking, two-way messaging, "Scribe" voice-to-schedule for staff | 12,000+ practices, role-specific tooling (DVM/CSR/tech) | B2B SaaS to clinics — owners use free; this is the white-label model PetPal could become |
| 5 | **Tractive** 🇦🇹 [screenshot](screens/hard_05_tractive.png) | GPS + health tracker (hardware + app) | EU-wide pet owners, active/outdoor pets | Hardware tracker + subscription app | Live location, virtual fences, health/sleep/activity insights, bark & scratch monitoring | Trustpilot 4.7/5, 50k+ reviews, 175-country coverage | Hardware sale (€49–79) + mandatory subscription |

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
| 1 | **MyTherapy** [screenshot](screens/soft_01_mytherapy.png) | Medication reminder + health diary (human health) | People managing chronic conditions / medication schedules | Reminder + logging engine, single dashboard | Passive intake logging, one-time codes to share health report with doctor | "Strictest data privacy", featured in Wired/ABC/Healthline, no 3rd-party data sharing | Free — funded via pharma/health-institute partnerships |
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
| 2 | **Airvet** 🇺🇸 [screenshot](screens/asp_02_airvet.png) | Telehealth via employee benefits | Employers (B2B2C) → employee pet owners | 24/7 virtual vet care bundled as a workplace perk | On-demand video vet, online pharmacy, family-sharing of benefit | SOC 2 Type II, 90+ NPS, Fortune 500 clients (Adobe, Workday) | B2B benefits contracts — "pays for itself in year 1" framing |
| 3 | **BabelBark** 🇺🇸 [screenshot](screens/asp_03_babelbark.png) | Multi-stakeholder pet health platform | Owners + vets + pet businesses + shelters | "Links everybody in a pet's life" — role-based connected network | Syncs health data across all parties; real-time updates between vet visits | Industry-leader endorsements, shelter partnerships | Register/sign-in funnels per stakeholder type — likely B2B2C across clinics/businesses |
| 4 | **PetDesk (owner side)** — see Hard #4 | Vet communication platform | Same as Hard #4 | Owner app layer of clinic software | 24/7 self-service booking + messaging | 12,000+ practices | Free to owners, B2B SaaS to clinics |
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
