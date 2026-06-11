# Deep Dive: Pet Info Hub, Health Events & Sharing with Vets/Sitters

**Dimension:** Important pet info, health event management, personality/preference notes (food, treats, animal tolerance, special requirements), and easy overview-sharing with vets and pet sitters.

---

## 1. Evaluation Criteria (1–5 scale)

| # | Criterion | What it measures |
|---|---|---|
| 1 | **Profile completeness** | Does it capture both medical data AND personality/preference data (food, behaviour, tolerances, special needs)? |
| 2 | **Health event tracking & reminders** | Vaccinations, meds, checkups, renewals — proactive nudges, not just storage |
| 3 | **Document/record storage** | Can users store photos/PDFs (prescriptions, insurance, legal) alongside structured data? |
| 4 | **Sharing mechanism simplicity** | How easy is it to give a vet or sitter access — link, code, or full account required? |
| 5 | **Role-based access granularity** | Can different people (owner, vet, sitter) see/edit different things? |
| 6 | **At-a-glance overview** | Can a new caregiver scan one screen and understand the pet in seconds? |
| 7 | **Update/maintenance friction** | How much ongoing effort does it take to keep info current? |
| 8 | **Multi-stakeholder ecosystem** | Are owner, vet, AND sitter/business all designed into the same system? |

---

## 2. Products Selected

| Product | Why selected for this dimension | Source |
|---|---|---|
| **BabelBark** | Explicitly built around "connect everybody in a pet's life" — health dashboard + instant sharing is its core pitch | [babelbark.com/petparents](https://babelbark.com/petparents/) ([screenshot](screens/dim_babelbark_petparents.png)) |
| **Rover** | Sitter-facing pet care profile (feeding, meds, behaviour, allergies) is the gold standard for "personality + special requirements" info shared with a third party | [rover.com/dog-walking](https://www.rover.com/dog-walking/) ([screenshot](screens/asp_01_rover.png)) |
| **MyTherapy** | "One-time code" doctor-sharing is the cleanest lightweight sharing mechanism researched, directly transferable | [mytherapyapp.com](https://www.mytherapyapp.com) ([screenshot](screens/soft_01_mytherapy.png)) |
| **Lassie** | Best-in-class reminder system tied to vet billing/insurance, EU benchmark | [lassie.co/en](https://www.lassie.co/en) ([screenshot](screens/hard_01_lassie.png)) |
| **PetDesk** | Clinic-owner connected record/messaging system — closest to a "vet has access" model | [petdesk.com](https://petdesk.com) ([screenshot](screens/hard_04_petdesk.png)) |

---

## 3. Evaluation Table

| Criterion | BabelBark | Rover | MyTherapy | Lassie | PetDesk |
|---|:---:|:---:|:---:|:---:|:---:|
| 1. Profile completeness | 5 | 4 | 3 | 3 | 3 |
| 2. Health event tracking & reminders | 5 | 2 | 5 | 5 | 4 |
| 3. Document/record storage | 4 | 2 | 3 | 3 | 3 |
| 4. Sharing mechanism simplicity | 5 | 5 | 5 | 3 | 4 |
| 5. Role-based access granularity | 5 | 3 | 2 | 2 | 4 |
| 6. At-a-glance overview | 4 | 4 | 5 | 4 | 3 |
| 7. Update/maintenance friction (5 = low effort) | 3 | 4 | 5 | 3 | 4 |
| 8. Multi-stakeholder ecosystem | 5 | 2 | 2 | 3 | 4 |
| **Total (/40)** | **36** | **26** | **30** | **26** | **29** |

---

## Top 3 Mechanisms to Transfer into PetPal MVP

1. **BabelBark's "Instant Sharing" health dashboard** — "never request a vaccination report again." A single shareable view that pulls from the structured pet profile (vaccines, meds, documents) means PetPal doesn't need separate exports for vet vs. sitter — one source of truth, different views per role.

2. **MyTherapy's one-time share code** — frictionless, time-boxed access without forcing the recipient (vet or sitter) to create a full account. This solves PetPal's "view-only vs. edit access" requirement at MVP without building a full invite/permissions system on day one.

3. **Rover's sitter-facing care card** (feeding, meds, behaviour, allergies, "not friendly with") — this is structurally identical to PetPal's planned "Pet Personality Profile." Rover proves this content works as a quick-reference card optimized for someone who has *never met the pet before* — the right design target for PetPal's walker/sitter view.

---

## 1 Mechanism That Will NOT Work for MVP

**BabelBark's diet/nutrition database (~5,000 pet food brands with caloric/ingredient data).**

**Why it won't work:** This requires an ongoing content-ops investment (maintaining a third-party food database) that's disproportionate to MVP value. PetPal's brief calls for *owner notes* on food preferences ("favourite treats," "solid no's") — a lightweight, manual, personality-card approach (à la Rover) achieves the actual JTBD without the data-maintenance burden. Building a structured food database before validating the core sharing/reminder loop would be premature scope expansion — and risks becoming stale/inaccurate, which undermines trust in the rest of the profile.
