# PetPal — Personas

Built from [`research.md`](research.md) and the user-voice quotes in [`research.html`](research.html) (Trustpilot "Voices" section).

**Honesty rules used here**
- 🟢 = backed by a real user voice (verbatim Trustpilot review) or a sourced research line.
- 🔵 = drawn from the project brief ([`CLAUDE.md`](../CLAUDE.md)) — *stated intent, never tested on a user*.
- `[?]` = **no data**. Written as a hypothesis to validate, never as fact.

> ⚠️ Caveat carried over from the people analysis: the research is a **competitor benchmark**. There are **no interviews, surveys, or analytics** with PetPal's own target people. Every real quote below is about a *competitor* product (GPS tracker, vet video call, insurance app), not about PetPal's core job. So the personas are **evidence-shaped hypotheses**, not validated segments. Mood quotes are used only where a competitor's user expressed a feeling that plausibly transfers.

---

## ⭐ PRIMARY — "The Organised Owner"

*Eva, 34, lives in an EU city, one dog. Comfortable with apps. `[?]` (age/location are brief scope [CLAUDE.md:14-17](../CLAUDE.md), not observed — the specific person is a hypothesis.)*

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

**Trust triggers**
- Convinces: a record that updates itself and is shareable instantly ("never request a vaccination report again"). 🟢 [research.md:52](research.md). Direct, low-friction sharing. 🟢 [research.md:68](research.md)
- Puts off: being forced to re-enter everything (manual-entry friction is PetPal's known weak spot). 🟢 [research.md:73](research.md). `[?]` *hypothesis*: a clinical/cold tone would put her off — the brief wants "companion, not medical record system" 🔵 [CLAUDE.md:90-91](../CLAUDE.md), but no user has said this.

**Mood quote** 🟢
> "It is possible to automatically… create health reports in PDF format. Once you have created a report, you can send it by email… it can also help family members keep track of their health."
> — Tom (HK), MyTherapy review ([research.html Voices](research.html); [original](https://www.trustpilot.com/reviews/661a938c2b072470fafaee1b))

**Why primary:** she is the **only persona that exercises PetPal's full core loop** — records + reminders + role-based sharing — which is the product's reason to exist ([CLAUDE.md:9-10](../CLAUDE.md)). She is also the persona with the most (even if indirect) real-user support, via MyTherapy's report-sharing and Rover's care profile. The other two personas are real but each touches only *part* of the product.

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

**Why secondary:** the emotion is real and well-evidenced, but PetPal is **not** a telehealth or GPS product — it can only serve the *information* slice of this moment, not the consultation. Important for tone and the "one-tap critical info" view, not a core loop driver.

---

## SECONDARY — "The Receiving Caregiver" (sitter / walker / new vet)

*The person on the other end of the share — a sitter watching the dog while the owner is away, or a new vet meeting the pet for the first time.*

**Context**
They've never met this animal and need to understand it fast: what it eats, what it's scared of, what it can't be near, who its vet is.
- Source: 🔵 this is PetPal's "Pet Personality Profile" recipient ([CLAUDE.md:58-71](../CLAUDE.md)). 🟢 The *content* model is proven by Rover's sitter-facing care card ([research.md:51, 58](research.md), [screenshot](screens/asp_01_rover.png)).

**Jobs**
- Scan one screen and "get" the pet in seconds; not dig through a chat history. 🟢 (Rover care card; [dimension deep-dive](dimension-info-sharing.md) criteria 6).
- `[?]` *hypothesis*: send the owner reassuring photo/status updates back. (Owners value receiving these on Rover 🟢, but we have **no voice from a sitter** about wanting to send them.)

**Pains in today's ways**
- `[?]` **Everything here is hypothesis — there is zero caregiver/vet user voice in the research.** Likely pains (info arrives as a long WhatsApp message, half-remembered verbal instructions, no single reference) are plausible but **unvalidated**.

**Trust triggers**
- `[?]` *hypothesis*: convinced by being able to help without creating an account (low-friction, time-boxed access — proven owner-side, [research.md:68](research.md)); put off by being asked to install/sign up for a one-week job. **Not tested with actual caregivers.**

**Mood quote** — *owner-side proxy only (no caregiver quote exists in the research):* 🟢
> "It is wonderful to know that you can be provided with pictures and updates from time to time."
> — Andre Keaton, Rover review ([research.html Voices](research.html); [original](https://www.trustpilot.com/reviews/6a2a93f9c4694b7541c32a65))

**Why secondary:** designing for the recipient is essential to PetPal's sharing promise, but this persona is **almost entirely `[?]`** — the research has no data from sitters, walkers, or vets as people. It's the **highest-risk persona** and the clearest candidate for the next round of primary research.

---

## Biggest validation gaps before these become real `[?]`

1. **No PetPal-target user has been interviewed** — all evidence is competitor-product reviews. The Organised Owner's emotional pains are inferred.
2. **The Receiving Caregiver has no voice at all** — sitters/walkers/vets are represented only by B2B product positioning ([research.md:53-54](research.md)).
3. **The status quo channels** — *partly closed* (follow-up research, [research.md F2/F3](research.md)): Notes apps, Google Sheets templates, printable PDFs, texted photos and WhatsApp are now confirmed. **Facebook-group recommendations and "ask an acquaintance" remain unconfirmed `[?]`.**
4. **No non-dog/cat owners** — *barely cracked*: one follow-up review came from a *gecko* owner ([research.md F2](research.md)), but rabbit/guinea-pig/bird owners (3 of 5 target species, [research.md:74](research.md)) are still absent. Personas remain implicitly dog-owner-shaped.
5. **No EU-mainland voices** — *still fully open `[?]`*: every source remains GB/AU/CA/US/HK and English-language app stores ([research.html Voices](research.html); follow-up research found no EU-mainland reviews).
6. **The core bet is now capture-friction, not pain** — follow-up research ([research.md F4](research.md)) indicates the pain is real but adoption hinges on low-effort data entry. The *size* of switching inertia is still unmeasured.
