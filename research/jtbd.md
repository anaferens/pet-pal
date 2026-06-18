# PetPal — Jobs To Be Done

Derived from [`personas.md`](personas.md) and [`research.md`](research.md). Format: **"When [situation], I want [motivation], so that [outcome]."**

**Rules applied**
- Wording describes the **person's progress**, not the product — no feature names.
- Each job names its **persona** and its **evidence**.
- Tags: 🟢 real user voice / sourced research line · 🔵 brief intent ([CLAUDE.md](../CLAUDE.md)), stated but untested · jobs with **no support → moved to Hypotheses**, not listed as real.
- Personas: **OO** = Organised Owner (primary) · **WO** = Worried-at-the-Wrong-Moment Owner · **RC** = Receiving Caregiver.

> Carried-over caveat: all real quotes are from *competitor* products. These jobs are evidence-shaped, not validated with PetPal's own users.

---

## 🎯 Main product job

> **When I'm responsible for a pet's health and care over its whole life, I want to keep everything I know about it somewhere I trust and can pass on, so that I can act in time and never scramble to find or explain what matters.**

- **Persona:** OO (primary)
- **Evidence:** 🔵 the product's stated reason to exist ([CLAUDE.md:6-10](../CLAUDE.md)). Closest real signals: people exporting a health summary to give a professional 🟢 ([research.md:33](research.md), [MyTherapy screenshot](screens/soft_01_mytherapy.png)) and owners handing pet info to a third-party carer 🟢 ([research.md:51, 58](research.md), [Rover screenshot](screens/asp_01_rover.png)).

---

## 🪜 Related jobs on the way to it

**1. Stay ahead of what's due**
> When a routine or preventive treatment is coming up, I want to know before it lapses, so that my pet stays protected and I'm not reacting at the last minute.
- **Persona:** OO · **Evidence:** 🔵 [CLAUDE.md:43-56](../CLAUDE.md); 🟢 proactive nudging is a proven, valued pattern in reminder/health products ([research.md:33](research.md) MyTherapy; [research.md:14](research.md) Lassie health program).

**2. Make a stranger understand my pet fast**
> When I'm leaving my pet with someone who has never cared for it, I want them to grasp what it needs in seconds, so that it's looked after the way it would be with me.
- **Persona:** OO → RC · **Evidence:** 🟢 the most complete real example of this content is Rover's carer-facing care card ([research.md:51, 58](research.md), [screenshot](screens/asp_01_rover.png)).

**3. Give a professional an accurate picture quickly**
> When I'm dealing with a vet, I want to hand over my pet's real history without relying on my memory, so that they can help based on facts, not guesswork.
- **Persona:** OO · **Evidence:** 🟢 directly mirrors MyTherapy users creating a report to share with their doctor ([research.html Voices](research.html), Tom; [original](https://www.trustpilot.com/reviews/661a938c2b072470fafaee1b); [research.md:33, 40](research.md)).

**4. Get proof my pet is okay while I'm away**
> When I'm apart from my pet, I want reassurance that it's fine, so that the time away isn't spent worrying.
- **Persona:** OO (owner side), RC (sender side) · **Evidence:** 🟢 owners explicitly value receiving updates while away ([research.html Voices](research.html), Andre/Rover; [original](https://www.trustpilot.com/reviews/6a2a93f9c4694b7541c32a65); [research.md:51](research.md)).

**5. Make a good call in a worrying moment**
> When something seems wrong and the clinic is closed, I want fast access to what I already know and to help, so that I can decide well under stress instead of panicking.
- **Persona:** WO · **Evidence:** 🟢 out-of-hours "wasn't right" moments are heavily evidenced ([research.html Voices](research.html), jess & Luke/FirstVet; [research.md:16](research.md), [screenshot](screens/hard_03_firstvet.png)). *Note:* PetPal can serve the **information** part of this, not the consultation.

---

## ❤️ Emotional jobs

**E1. Trade worry for calm**
> When I can't be with my pet, I want to feel calm instead of anxious, so that I'm not carrying low-level dread all day.
- **Persona:** OO, WO · **Evidence:** 🟢 "peace of mind" is the single most repeated feeling in real reviews ([research.html Voices](research.html), Heather L/Tractive; [original](https://www.trustpilot.com/reviews/6a2ae53abd66814a09215adb)).

**E2. Feel sure nothing was forgotten**
> When I hand my pet to someone else, I want confidence that everything important has been passed on, so that I'm not second-guessing myself the whole time.
- **Persona:** OO · **Evidence:** 🟢 partial — inferred from owners' relief at being kept in the loop ([Andre/Rover](https://www.trustpilot.com/reviews/6a2a93f9c4694b7541c32a65)); the "confidence I didn't forget" framing is an interpretation, not a direct quote `[?]`.

**E3. Spare my pet unnecessary stress**
> When my pet needs care, I want the experience to be as calm for it as possible, so that I'm not putting it through avoidable distress.
- **Persona:** OO · **Evidence:** 🟢 owners value low-stress care for the animal ([research.html Voices](research.html), Anja/Felmo "so much less stressful for the cats"; [original](https://www.trustpilot.com/reviews/69cd09e89deb646c05d3bf2e); [research.md:15](research.md)).

---

## 👥 Social jobs

**S1. Keep everyone caring for my pet on the same page**
> When more than one person looks after my pet, I want us all working from the same picture, so that nothing falls through the gaps between us.
- **Persona:** OO · **Evidence:** 🟢 MyTherapy users note the value of helping "family members keep track" ([research.html Voices](research.html), Tom; [original](https://www.trustpilot.com/reviews/661a938c2b072470fafaee1b)).

**S2. Be an easy, trustworthy handoff**
> When I ask someone to care for my pet, I want them to feel I've made it easy and complete, so that they take the responsibility seriously and want to help again.
- **Persona:** OO → RC · **Evidence:** `[?]` partial — the *low-friction* expectation is supported owner-side ([research.md:68](research.md)), but **how an owner wants to be perceived by a carer is not in the research**. Treat the "be seen as trustworthy" framing as hypothesis.

---

## 🧪 Hypotheses (not supported by current data — validate before treating as real)

These are plausible jobs the research **does not** back. Phrased as questions to test.

- **Finding/choosing a carer in the first place.** *Hypothesis:* "When I need someone to mind my pet, I want to find someone I can trust, so that I can leave without worry." → No data; PetPal does no matchmaking, and no source covers the discovery step. `[?]`
- **The carer's own job.** *Hypothesis:* "When I'm minding a pet I've just met, I want to do it right and reassure the owner, so that I'm rebooked." → **Zero caregiver/sitter voice exists in the research.** `[?]` (highest-risk gap, per [personas.md](personas.md))
- **Escaping the messy status quo.** *Hypothesis:* "When my pet's info is scattered across chats and notes, I want one tidy place, so that I stop losing track." → Partly supported (Notion/Keep as "good enough" status quo, [research.md:34-35, 41](research.md); WhatsApp as informal default in [research.html](research.html)) but the **pain intensity is unmeasured** — people may be content with "good enough." `[?]`
- **Jobs of non-dog/cat owners** (rabbit, guinea pig, bird). → No voices at all for 3 of 5 target species ([research.md:74](research.md)). `[?]`
- **How people decide to adopt a tool like this.** *Hypothesis:* "When I'm weighing a new pet tool, I want proof it works, so that I don't waste effort." → The "read reviews, compare prices" behaviour is real but observed for a *hardware purchase* (Dave/Tractive), not for an app like PetPal. `[?]`

---

## 📊 JTBD × Persona matrix

**Importance scale:** 1 = nice-to-have · 2 = matters · 3 = central to the persona. `[?]` = no data (no averaged guesses).
**Personas:** OO = Organised Owner (primary) · WO = Worried-at-the-Wrong-Moment Owner · RC = Receiving Caregiver.
Job codes refer to the jobs listed above.

| Job | OO (primary) | WO | RC | FEATURE (what addresses it) | COMPETITORS (per research.md) |
|---|---|---|---|---|---|
| **Main** — keep everything in one trusted place, act in time + pass on | **3** — product's core, 🔵 [CLAUDE.md:6-10](../CLAUDE.md); 🟢 [research.md:33,51](research.md) | `[?]` — no data WO values long-term record-keeping | `1` — carer receives, doesn't maintain (role-inferred, no data) | Unified per-pet record + document storage | Partial: only **BabelBark** attempts the full picture 🟢 [research.md:53,75](research.md) |
| **R1** — stay ahead of what's due | **3** — 🔵 [CLAUDE.md:43-56](../CLAUDE.md); 🟢 reminders valued [research.md:14,33](research.md) | `[?]` — WO is reactive, not preventive (no data) | `[?]` | Vaccination/renewal reminders + appointment tracking | **Well covered**: Lassie, MyTherapy, PetDesk 🟢 [research.md:14,33,17](research.md) |
| **R2** — make a stranger understand my pet fast | **3** — 🟢 strongest match to Rover care card [research.md:51,58](research.md) | `1` — tangential | **3** — 🟢 this is literally the carer's task; Rover proves the content for "never met the pet" [research.md:58](research.md) | Personality profile + shareable carer view | **Only Rover** — and locked inside its booking marketplace 🟢 [research.md:51](research.md) |
| **R3** — give a professional an accurate picture quickly | **3** — 🟢 mirrors MyTherapy doctor-report [research.html Voices](research.html), [research.md:33,40](research.md) | **2** — 🟢 relevant in the worry moment [research.md:16](research.md) | `[?]` | Share records from app + vet messaging | Covered but **account-bound**: MyTherapy code, PetDesk, BabelBark 🟢 [research.md:33,17,53](research.md) |
| **R4** — get proof my pet's okay while away | **2** — 🟢 owners value updates [research.html Voices](research.html), Andre/Rover | `[?]` | `[?]` — sender side, no caregiver voice | **Gap** — PetPal has no carer-update flow `[?]` | **Only Rover** (sitter photos/updates) 🟢 [research.md:51](research.md) |
| **R5** — make a good call in a worrying moment | **2** — 🟢 [research.md:16](research.md) | **3** — 🟢 defining job; FirstVet out-of-hours [research.html Voices](research.html) | `[?]` | Fast access to stored info (no consultation) | FirstVet, Airvet — but **different category** (telehealth) 🟢 [research.md:16,52](research.md) |
| **E1** — trade worry for calm | **3** — 🟢 "peace of mind" most-repeated feeling [research.html Voices](research.html), Heather/Tractive | **3** — 🟢 same | `[?]` | Served indirectly via reliability + access | Tractive leans on this emotionally 🟢 [research.md:18](research.md) |
| **E2** — feel sure nothing was forgotten | **2** — 🟢 partial/inferred from Andre/Rover; framing is interpretation `[?]` | `[?]` | `[?]` | Completeness of profile before handoff | `[?]` — none address this directly |
| **E3** — spare my pet stress | **2** — 🟢 Anja/Felmo "less stressful for the cats" [research.md:15](research.md) | `1` | `[?]` | **Gap** — PetPal doesn't reduce the pet's stress directly `[?]` | Felmo (home visits) 🟢 [research.md:15](research.md) |
| **S1** — keep everyone on the same page | **3** — 🟢 Tom/MyTherapy "help family members keep track" [research.html Voices](research.html) | `[?]` | **2** — RC is one of the "everyone" (role-inferred) | Shared access + roles (multi-user) | **Only BabelBark** attempts true multi-party 🟢 [research.md:53,75](research.md) |
| **S2** — be an easy, trustworthy handoff | **2** — 🟢 low-friction supported [research.md:68](research.md); "be seen as trustworthy" is `[?]` | `[?]` | **2** — RC benefits from no-signup access (role-inferred) | Share via link/code, no account needed | MyTherapy one-time code, Rover 🟢 [research.md:68](research.md) |

---

## 🧭 Conclusion

### 3 jobs for the MVP core
*Criteria: importance **3** for the primary persona (OO) **and** thinly covered by the market.* The research names role-based, portable, multi-party sharing as the genuine whitespace ([research.md:75](research.md)) — all three cluster there.

1. **R2 — make a stranger understand my pet fast.** OO = 3. Market: **only Rover**, and it's trapped inside a booking marketplace, not a portable record an owner controls ([research.md:51](research.md)). Clear whitespace.
2. **S1 — keep everyone caring for my pet on the same page.** OO = 3. Market: **only BabelBark** attempts true multi-stakeholder access; "everyone else is single-owner or B2B-only" ([research.md:75](research.md)). The strongest documented gap.
3. **R3 — give a professional an accurate picture quickly.** OO = 3. Market: solved only as *account-bound* systems (MyTherapy code, PetDesk, BabelBark) — none is an owner-held record portable to *any* vet ([research.md:33,17,53](research.md)).

*Deliberately excluded:* **R1 (stay ahead of what's due)** is a 3 for OO but is **table-stakes** — already well covered by Lassie/MyTherapy/PetDesk ([research.md:14,33,17](research.md)). Build it competently, but it won't differentiate.

### Feature candidates to remove (address no job)
- **Contextual product/treat recommendations** ([CLAUDE.md:84](../CLAUDE.md)) — a monetization mechanism, maps to **no user job** in this matrix. Cut from MVP.
- **Breed-aware food/treat *suggestions*** inside the personality profile ([CLAUDE.md:59](../CLAUDE.md)) — addresses no job, and the deep-dive already flagged a food database as premature, maintenance-heavy MVP scope ([dimension-info-sharing.md](dimension-info-sharing.md)). Cut; keep only free-text owner notes.
- **White-label / clinic-app foundation** ([CLAUDE.md:75](../CLAUDE.md)) — a *business-model* ambition, not an owner/carer job. **Defer** (not "remove" — it's a future B2B path, [research.md:61](research.md)), but it should not consume MVP design effort.

*Note:* **R4 (proof okay while away)** and **E3 (spare my pet stress)** currently have **no feature** behind them — these are gaps to decide on consciously, not features to cut.
