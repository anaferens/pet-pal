# PetPal — Project Brief

## Concept
PetPal is a mobile-first lifestyle app that keeps everything related to your pet in one place — health records, reminders, documents, care preferences, and vet communication — all easily transferable and accessible.

## Problem
Pet owners miss important checks, vaccinations, insurance renewals, and legal deadlines. Records are scattered across clinics, paper, and email. Dog walkers and sitters lack access to essential pet care info. Vets have no shared record baseline with owners.

## Goal
One source of truth for a pet's entire life: medical, legal, behavioral, and social.

---

## Target Audience
- Age 16–70, EU market (launch market)
- Pet owners who want to stay on top of health, legal, and care responsibilities
- Secondary users: vet doctors, dog walkers, pet sitters (shared access roles)

---

## Platform
- Mobile web (mobile-first)
- Desktop adaptation (later phase)

---

## Supported Pet Types
Top 5 most common pets in the EU:
1. Dogs
2. Cats
3. Rabbits
4. Guinea pigs
5. Birds

---

## Core Features

### Pet Profile
- Multiple pets per account
- Per-pet profile with: name, breed, age, photo, species

### Health & Medical
- Vaccination records and reminders
- Vet prescriptions (upload PDF/photo or manual entry)
- Health check history
- Upcoming appointment tracking

### Documents & Legal
- Insurance documents + renewal reminders
- Legal documents (EU pet passport, microchip registration, etc.)
- Upload PDF/photo or manual data entry

### Reminders
- Push notifications + email
- Vaccination due dates, insurance renewals, vet checkups, legal compliance deadlines

### Pet Personality Profile
- Favourite food and treats (breed-aware suggestions)
- Preferred walk activities and routines
- Likes and dislikes
- Behaviour notes
- Breeds or animal types this pet is not friendly with
- Intended for: dog walkers, sitters, new vets — anyone needing fast context on the pet

### Shared Access & Roles
- Owner (full access, can edit)
- Vet / Clinic (can view and add medical records)
- Dog walker / Sitter (view-only or limited edit)
- Shareable pet profile link or invite

### Vet Communication
- Two-way messaging with vet clinic
- Share records directly from the app
- Foundation for white-labelling as a vet clinic's own app

---

## Information Architecture
*Full detail in [research/sitemap.md](research/sitemap.md), [research/flows.md](research/flows.md), [research/ia.md](research/ia.md). Visual: [ia.html](research/ia.html).*

### Top-level sitemap
```
Owner app (signed in)
├─ My Pets → Pet dossier → {Health & jabs · Documents & passport · Insurance ·
│                           Personality & care · Vet & appointments · Emergency info}
├─ What's due   (reminders, all pets)
├─ Share a pet → Who has access
└─ Vet messages
Recipient (no account, via link)
└─ Shared pet view → Emergency & what I'm allowed to do
```

### Main flow (primary persona)
Keep everything in one trusted place and pass it on:
**My Pets → Pet dossier → (add/update records) → Share a pet → handoff sent.** Every error/empty state has a recovery — no dead ends.

### Navigation
3 global items, one per verb of the main job: **Pets** (consult) · **What's due** (act in time) · **Share** (pass on). Vet messages is contextual; Emergency is a 1-tap shortcut.

### Depth
Main job is **1 tap** from the first screen (**0 taps** with single-pet auto-land). Emergency info is **1 tap** from home. Nothing core exceeds 3 taps.

---

## Business Model
- Freemium base (free core features)
- Monetisation:
  - Vet clinic partnerships (white-label or referral)
  - Insurance referrals
  - Contextual product recommendations (treats, food) based on breed and owner notes — subtle, lifestyle-aligned, not intrusive

---

## Design Direction

### Tone
Warm, friendly, lifestyle app — not clinical. Think companion app, not medical record system.

### Reference Apps
**Direct competitors to study:** Lassie (and similar to be researched)
**Indirect / design inspiration:** Airbnb, Sellpy, Headspace, Revolut, Uber, Karma, Too Good To Go

### Key Design Values
- Clean and approachable
- Easy for 16-year-olds and 70-year-olds alike
- Delight in the details (pet photos, personality cards)
- Trust and reliability (for the medical/legal side)

---

## Voice

Full spec: [`research/voice.md`](research/voice.md) — **Principles → Glossary → Forbidden → Microcopy rules**. Every product string is written to it; the inventory, rewrite logs, consistency audit, and defect-fix pass live in [`research/microcopy.md`](research/microcopy.md). All 123 wireframe screens have been rewritten and audited against it.

**Master line:** *Everything about your pet, in one trusted place.* · *For every walk, vet visit, and weekend away.*
**Stance:** calm confidence — warm by default, precise when it matters (health, money, legal, emergencies).

**Principles**
1. Own "trusted," not "complete."
2. Warm by default, precise under pressure.
3. Speak to the moment, not the feature.
4. Make sharing feel safe and effortless.

**Glossary — one term per concept:** pet card (never dossier/profile) · section · **jab** (everyday) / vaccination (formal proof only) · **sitter** (never carer) · owner (never user/account holder) · **Call** (never Contact) · **Create account** + **Log in** (never a "Sign up" button) · **authorisation** and British spelling throughout · **"No … yet"** empty pattern. Address the reader as informal singular **you**. Loanwords allowed: App, Link, PDF, Chip, QR code, Sitter, Update, Vet. Refused: Dashboard, Onboarding, Manage, CTA.

**Never:** "Something went wrong," "Oops," "Welcome," "successfully," "Awesome/Congratulations," exclamation marks or emoji in system copy, motivational filler ("Start your pet journey"). Functional glyphs (`✓` complete, `✕` close) are fine.

**Microcopy by element:** button = verb + object (`Add a jab`, not `OK`) · heading = names the place in glossary words · error = what failed + what to do, no apology or joke · empty = `No … yet` + the next step · loading = silent, or `Loading …` · success = the fact + next step, no celebration · destructive = what's removed + "It can't be undone."

---

## Compliance Notes
- EU market: GDPR applies to all user and pet data
- Pet passport format follows EU regulation (Regulation (EU) No 576/2013)
- Microchip registration varies by country — support manual entry initially
