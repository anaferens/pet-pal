# PetPal — Backlog / Ideas to revisit

Parked ideas, not yet in the design. Each notes enough reasoning to pick up later.

---

## Calendar — in-app + export  `✅ decided`
*Raised Jun 2026, resolved Jun 2026. Touches: Reminder entity · R1 (stay ahead of what's due).*

**Decision:** Build an **in-app calendar view** inside PetPal, plus an **export option** to Google Calendar, Apple Calendar, and Outlook so owners can see pet events alongside their personal schedule.

**Watch-outs (still apply):**
- **R1 is table-stakes** — keep it cheap; don't let it crowd out the sharing differentiator (R2 / S1 / R3).
- **Handover ≠ R1** — a dog-walker/sitter handover is coordination (S1/S2), served by the shared care card / Access grant, not a personal calendar event.
- GDPR: export reads *out* of PetPal only — doesn't touch the user's calendar account/data.

**Implementation:** add a calendar view to the **What's due** screen + export affordance (Google / Apple / Outlook).
