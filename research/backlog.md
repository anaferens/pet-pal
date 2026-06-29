# PetPal — Backlog / Ideas to revisit

Parked ideas, not yet in the design. Each notes enough reasoning to pick up later.

---

## Calendar export for reminders  `[?]`
*Raised Jun 2026. Touches: Reminder entity · R1 (stay ahead of what's due).*

**Idea:** let owners push reminders (vet visits, jab due dates, insurance renewals) to their existing calendar instead of building a calendar inside the app.

**Leaning:** **subscribe-able ICS feed** (per-account calendar URL that auto-updates), **not** a Google Calendar OAuth integration, **not** an in-app calendar.
- Works across Google / Apple / Outlook (EU isn't Google-only).
- GDPR-light — reads *out* of PetPal, doesn't touch the user's calendar account/data.
- PetPal stays the single source of truth; a subscribed feed updates automatically (a one-shot "Add to calendar" .ics would go stale — same staleness bug we designed around in flows.md).
- Low capture-friction (research F4) — meets people where they already look.

**Watch-outs:**
- **Hypothesis, no user evidence** — we never validated channel preference (it's why the notification-preferences screen was cut). Validate before building.
- **R1 is table-stakes** — keep it cheap; don't let it crowd out the sharing differentiator (R2 / S1 / R3).
- **Handover ≠ R1** — a dog-walker/sitter handover is coordination (S1/S2), served by the shared care card / Access grant, not a personal calendar event. A calendar nudge is fine, but don't make it the handover channel.

**If picked up:** add "calendar (ICS subscribe)" as a delivery channel on the Reminder entity + an "Add to / subscribe in calendar" affordance on the **What's due** screen (no new screen).
