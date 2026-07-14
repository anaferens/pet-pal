# PetPal — Personas

Built from [`research.md`](research.md) and the user-voice quotes in [`research.html`](research.html) (Trustpilot "Voices" section).

**Honesty rules used here**
- 🟢 = backed by a real user voice (verbatim Trustpilot review) or a sourced research line.
- 🔵 = drawn from the project brief ([`CLAUDE.md`](../CLAUDE.md)) — *stated intent, never tested on a user*.
- `[?]` = **no data**. Written as a hypothesis to validate, never as fact.

> ⚠️ Caveat carried over from the people analysis: the research is a **competitor benchmark**. There are **no interviews, surveys, or analytics** with PetPal's own target people. Every real quote below is about a *competitor* product (GPS tracker, vet video call, insurance app), not about PetPal's core job. So the personas are **evidence-shaped hypotheses**, not validated segments. Mood quotes are used only where a competitor's user expressed a feeling that plausibly transfers.

---

## How the interactive prototype embodies these personas

The [wireframes](../wireframes/) ship **three named persona walkthroughs** (sidebar → "Persona flows", or `?flow=…` in the URL). Each maps to a persona below and to a flow in [flows.md](flows.md):

| Prototype walkthrough | Persona | Job(s) exercised | Flow |
|---|---|---|---|
| **Pet owner (Ana)** — *My Pets → dossier → sections → Share → What's due* | ⭐ Organised Owner | Main (consult + pass on), R1 | [Main job](flows.md), [R1](flows.md) |
| **New pet setup (full journey)** — *empty account → set up pet → add photo → fill every section → share with a sitter* | ⭐ Organised Owner (first run) | Main (capture), leads into R2 | [New-pet setup](flows.md) |
| **Pet sitter (recipient)** — *shared link → Shared pet view → Emergency & allowed* | ◦ Receiving Caregiver | R2, R5/F6 | [R2](flows.md) |

> **Naming note.** The Organised Owner is written up below as *Eva*; the prototype's owner walkthrough labels her **Ana** (and the sample sitter view still shows "Shared by Eva"). Same persona — the concrete name is cosmetic and unvalidated (`[?]`). The **Worried-at-the-Wrong-Moment Owner** (R5) is not a standalone walkthrough: her one-tap emergency path is reachable from inside the owner flows (the emergency shortcut and the sitter's *Emergency & allowed* screen), matching the sitemap decision to keep R5 pet-contextual rather than global.

---

## ⭐ PRIMARY — "The Organised Owner"

*Eva ("Ana" in the prototype), 34, lives in an EU city, one dog. Comfortable with apps. `[?]` (age/location are brief scope [CLAUDE.md:14-17](../CLAUDE.md), not observed — the specific person is a hypothesis.)*

**Context**
She treats her dog's admin like her own: she wants to *check when the dog was last vaccinated to plan the next one*, and when she travels she needs to *hand a sitter everything important about the dog*. Two situations, one underlying need: a single trustworthy record she can both **consult** and **pass on**.
- Source: this is PetPal's core job as stated in the brief 🔵 [CLAUDE.md:6-10, 58-71](../CLAUDE.md). The closest real-world signals are MyTherapy users exporting a health summary for a professional ([research.md:33](research.md), [screenshot](screens/soft_01_mytherapy.png)) and Rover owners receiving sitter updates ([research.md:51](research.md), [screenshot](screens/asp_01_rover.png)).

**Jobs**
- Look up vaccination / health history and get reminded before the next one is due. 🔵 [CLAUDE.md:43-56](../CLAUDE.md)
- Produce a "here's my dog" pack (feeding, meds, behaviour, vet contact) for a sitter without rewriting it each time. 🟢 the *receiving* side of this is a proven, loved behaviour on Rover ([research.md:51, 58](research.md)).
- Share with a vet/sitter without making them create an account. 🟢 proven pattern — MyTherapy one-time code, Rover profile share ([research.md:68](research.md)).

**Pains in today's ways**
- Info is **scattered** across notes apps and paper. **Correction (follow-up research):** the earlier framing that the "good enough" status quo *stops* people switching is too strong — a real user described keeping pet info in the Notes app until it got "tedious having to scroll through the long notes," then switching to a structured app. People **do** migrate, but only past a tipping point (volume/tedium) **and only if the new tool is low-friction**. 🟢 [research.md → Follow-up research, F2 & F4](research.md), [Keep login screenshot](screens/soft_02_googlekeep_LOGIN.png)
- For sitters, the status quo is **Google Sheets templates, printable PDFs, texted/emailed photos, and WhatsApp** — info gets buried, no single "current state." Confirmed as a real, structured behaviour (template market + AAHA sitter guidance), not just an assumption. 🟢 [research.md → Follow-up research, F3](research.md); also [research.md:68](research.md).
- **Facebook groups / asking acquaintances** for sitter recommendations and advice. `[?]` — *hypothesis, still open*: searched in follow-up research and **not confirmed** (found docs/sheets/text channels, but no evidence for Facebook-group recommendations). Keep as a gap to validate.
- **The handoff itself is emotionally loaded** (now evidenced): leaving the pet is a high-anxiety moment — **56% of owners feel "overwhelming guilt and anxiety" leaving their pet**, 61% worry about its welfare on vacation, 52% have been "too guilty to go." 🟢 [research.md → Follow-up research, F11](research.md). *Note:* this is intense but **episodic** (sitter use is occasional, not routine — F9/F11), vs. the planning/records job which is the more frequent driver.

**Trust triggers**
- Convinces: a record that updates itself and is shareable instantly ("never request a vaccination report again"). 🟢 [research.md:52](research.md). Direct, low-friction sharing. 🟢 [research.md:68](research.md)
- Puts off: being forced to re-enter everything (manual-entry friction is PetPal's known weak spot). 🟢 [research.md:73](research.md). `[?]` *hypothesis*: a clinical/cold tone would put her off — the brief wants "companion, not medical record system" 🔵 [CLAUDE.md:90-91](../CLAUDE.md), but no user has said this.

**Mood quote** 🟢
> "It is possible to automatically… create health reports in PDF format. Once you have created a report, you can send it by email… it can also help family members keep track of their health."
> — Tom (HK), MyTherapy review ([research.html Voices](research.html); [original](https://www.trustpilot.com/reviews/661a938c2b072470fafaee1b))

**Why primary:** *(rationale upgraded by follow-up research — see [research.md → Follow-up research, Round 3](research.md))* her core job — keeping and proving pet records — is the **most frequent felt need and the documented #1 reason people adopt pet apps** (F9, F10), not merely "the persona that exercises the full loop" (the earlier, weaker rationale flagged in the critique). The record/proof need recurs at every boarding, daycare, grooming and travel touchpoint, where verbal "he's up-to-date" isn't accepted. She also has the most (even if indirect) real-user support, via MyTherapy's report-sharing and Rover's care profile. The other two personas are real but each touches only *part* of the product — and one (the worried moment) is **rare per person** (F11).

---

## SECONDARY — "The Worried-at-the-Wrong-Moment Owner"

*A pet owner facing a "something's not right" moment, often out of hours.*

**Context**
The pet seems unwell, it's late, the clinic is closed, and they need information or reassurance *now*. They reach for whatever is fastest.
- Source: 🟢 strongly evidenced in FirstVet reviews — out-of-hours, "wasn't right" moments ([research.md:16](research.md), [screenshot](screens/hard_03_firstvet.png)).

**Jobs**
- Get fast access to the pet's info and to help when anxious. 🟢 [research.md:16](research.md)
- `[?]` *hypothesis*: in that moment, pull up the pet's meds/conditions/vet contact in one tap — PetPal could serve this, but no user has asked PetPal for it.

**Pains in today's ways**
- Out-of-hours emergency vets are expensive and stressful for the animal. 🟢 (FirstVet reviewers contrast the service with "going to the vets in the middle of the night who charged the absolute earth," [FirstVet Trustpilot](https://www.trustpilot.com/review/firstvet.com)).
- Scrolling chats/groups for "has anyone had this?" `[?]` *hypothesis* — plausible, not in research.

**Trust triggers**
- Convinces: speed ("video call within half an hour," "in the middle of the night"), and a real named professional. 🟢 [research.md:16](research.md)
- Puts off: **expectation mismatch** — discovering the tool can't actually do what they urgently needed (e.g. FirstVet "cannot issue prescriptions") reads as a "con." 🟢 ([FirstVet Trustpilot](https://www.trustpilot.com/review/firstvet.com), Lysia 1★).

**Mood quote** 🟢
> "We had a video call with Dr Cato as our cat 'wasn't right'… I got a video call within half an hour of requesting one… Turns out our cat has pancreatitis."
> — jess (GB), FirstVet review ([research.html Voices](research.html); [original](https://www.trustpilot.com/reviews/69e345e50787d3986e4fa9a7))

**Why secondary:** *(confirmed by follow-up research, [Round 3 / F11](research.md))* the emotion is the most intense of the three jobs, but the moment is **rare per person** ("few owners are prepared for emergencies") and PetPal is **not** a telehealth or GPS product — it can serve only the *information* slice, not the consultation. Low frequency + partial serviceability = secondary. Important for tone and a "one-tap critical info" view, not a core loop driver.

---

## SECONDARY — "The Receiving Caregiver" (sitter / walker / new vet)

*The person on the other end of the share — a sitter watching the dog while the owner is away, or a new vet meeting the pet for the first time.*

**Context**
They've never met this animal and need to understand it fast: what it eats, what it's scared of, what it can't be near, who its vet is.
- Source: 🔵 this is PetPal's "Pet Personality Profile" recipient ([CLAUDE.md:58-71](../CLAUDE.md)). 🟢 The *content* model is proven by Rover's sitter-facing care card ([research.md:51, 58](research.md), [screenshot](screens/asp_01_rover.png)). **Confirmed (follow-up research):** a consistent caregiver info-checklist is documented across sitter-industry sources ([research.md → Follow-up research, F5](research.md)).

**Jobs**
- Scan one screen and "get" the pet in seconds; not dig through a chat history. 🟢 (Rover care card; [dimension deep-dive](dimension-info-sharing.md) criteria 6).
- **Know what to do — and what they're allowed to do — in an emergency.** 🟢 **New, from follow-up research:** sitter release forms centre on emergency vet authorization, a pre-approved spend limit, and how to pay — a need **not yet in PetPal's model** ([research.md → Follow-up research, F6](research.md)).
- `[?]` *hypothesis*: send the owner reassuring photo/status updates back. (Owners value receiving these on Rover 🟢, but we still have **no voice from a sitter** about wanting to send them.)

**Pains in today's ways**
- **Corrected (follow-up research):** this is no longer "all hypothesis." The caregiver's *needs* are documented — missing emergency contacts, no vet/authorization details, info scattered across a long message — and Rover confirms a sitter "only sees the care instructions the client entered," so a half-filled handoff leaves them flying blind. 🟢 [research.md → Follow-up research, F5/F8](research.md). What's still missing is the caregiver's own *lived voice* `[?]`.

**Trust triggers**
- Convinced by being able to help **without creating an account** — now supported by analogy: account/auth friction is a documented abandonment driver (92% abandon rather than reset a password; gated forms convert ~2–3%). 🟡 [research.md → Follow-up research, F7](research.md). Put off by being told to install/sign up for a one-week job. **Caveat:** evidence is general UX research, **not tested with actual caregivers** — whether they'll use a link vs. fall back to "just text me" is still `[?]`.

**Mood quote** — *owner-side proxy only (no caregiver quote exists in the research):* 🟢
> "It is wonderful to know that you can be provided with pictures and updates from time to time."
> — Andre Keaton, Rover review ([research.html Voices](research.html); [original](https://www.trustpilot.com/reviews/6a2a93f9c4694b7541c32a65))

**Why secondary:** designing for the recipient is essential to PetPal's sharing promise. Follow-up research has **firmed up *what* this persona needs** (info checklist + emergency authorization) and the *no-signup* design default, but it still has **no first-person sitter/walker/vet voice** — needs are documented by the industry, not spoken by caregivers. It remains the **highest-risk persona** and the clearest candidate for the next round of primary research (talk to actual sitters).

---

## Biggest validation gaps before these become real `[?]`

1. **No PetPal-target user has been interviewed** — all evidence is competitor-product reviews, app-store themes and surveys. The **choice** of the Organised Owner as primary is now frequency-/adoption-backed (Round 3, F9/F10), but her individual *emotional* pains remain inferred and all stats are **US-skewed** — EU applicability unproven `[?]`.
2. **The Receiving Caregiver has no *lived* voice** — *partly closed*: their needs (info checklist, emergency authorization, no-signup expectation) are now documented via sitter-industry sources and UX research ([research.md → Follow-up research, F5-F8](research.md)), but every source is *for* owners or *by* the industry — **no first-person sitter/walker/vet testimony yet `[?]`**. The **vet recipient** specifically is still unaddressed.
3. **The status quo channels** — *partly closed* (follow-up research, [research.md F2/F3](research.md)): Notes apps, Google Sheets templates, printable PDFs, texted photos and WhatsApp are now confirmed. **Facebook-group recommendations and "ask an acquaintance" remain unconfirmed `[?]`.**
4. **No non-dog/cat owners** — *barely cracked*: one follow-up review came from a *gecko* owner ([research.md F2](research.md)), but rabbit/guinea-pig/bird owners (3 of 5 target species, [research.md:74](research.md)) are still absent. Personas remain implicitly dog-owner-shaped.
5. **No EU-mainland voices** — *still fully open `[?]`*: every source remains GB/AU/CA/US/HK and English-language app stores ([research.html Voices](research.html); follow-up research found no EU-mainland reviews).
6. **The core bet is now capture-friction, not pain** — follow-up research ([research.md F4](research.md)) indicates the pain is real but adoption hinges on low-effort data entry. The *size* of switching inertia is still unmeasured.
