# PetPal — Design Repository

Mobile-first lifestyle app for pet owners. One place for health records, reminders, documents, vet communication, and pet personality info.

**Brief:** See [CLAUDE.md](CLAUDE.md) for full product brief.
**Research:** See [research/research.md](research/research.md) for competitor benchmark.

---

## Repository Structure

| Folder | Contents |
|---|---|
| [`research/`](research/) | Competitor benchmark, market notes, screen references |
| [`wireframes/`](wireframes/) | Low and mid-fidelity wireframes |
| [`concept/`](concept/) | Visual concepts and mood exploration |
| [`tokens/`](tokens/) | Design tokens: color, typography, spacing, radius |
| [`components/`](components/) | Individual UI components |
| [`design-system/`](design-system/) | Full design system documentation |
| [`handoff/`](handoff/) | Developer handoff specs and notes |

---

## Structure

The information architecture lives in [`research/`](research/):

| File | What's inside |
|---|---|
| [`sitemap.md`](research/sitemap.md) | **Entities** (the objects a person touches), the **Screens** tree (every screen tagged with the job it serves), the **Navigation** model (3 global items, depth-to-main-job, global/contextual/deep), and the **Traceability** matrix (jobs × screens, with orphan decisions). |
| [`flows.md`](research/flows.md) | All **user flows** as colour-coded Mermaid diagrams — main job + R1/R2/R5 — with screen nodes, decision points, loading/empty/error states, and success/partial endings (no dead ends). |
| [`ia.md`](research/ia.md) · [`ia.html`](research/ia.html) | The **unified IA tree** combining every page from sitemap + flows; `ia.html` also renders the live flows and the traceability matrix. |
| [`personas.md`](research/personas.md) · [`jtbd.md`](research/jtbd.md) | Personas and jobs-to-be-done the IA is built from. |
| [`sitemap-critique.md`](research/sitemap-critique.md) · [`.html`](research/sitemap-critique.html) | Defect review (dead ends, missing states, depth, orphans) and the applied fixes. |

Every screen traces to a job; every job (in scope) traces to a screen.

---

## Status

| Phase | Status |
|---|---|
| Brief | ✅ Done |
| Competitor research | ✅ Done |
| Wireframes | 🔜 Up next |
| Concept | — |
| Design system | — |
| Handoff | — |

---

## Platform
Mobile web first → desktop adaptation later. EU market launch.
