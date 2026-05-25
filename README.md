# Indian Knowledge Systems (IKS) Curriculum

A three-age-band school curriculum covering 15 modules on Indian Knowledge Systems — adapted across primary, middle, and senior school years. See [ATTRIBUTION.md](ATTRIBUTION.md) for the sources and original program that inspired this work.

## Audience

| Band    | Grades | Ages  | Notes |
|---------|--------|-------|-------|
| Primary | 3–5    | 8–10  | Story-led, sensory, lots of visuals |
| Middle  | 6–8    | 11–13 | Original audience; balanced text + activity |
| Senior  | 9–12   | 14–17 | Primary-source reading, independent inquiry, essays |

## What this curriculum is (and isn't)

**Is:** A secular, NEP-2020-aligned curriculum that teaches Indian intellectual traditions (cosmology, mathematics, wellness, ecology) by leading with the underlying science or observable phenomenon, then situating it in its historical Indian context. Sanskrit terms appear with transliteration and meaning; verses are cited only from verified primary sources (see `_shared/style-guide.md`).

**Isn't:** A devotional program, a replacement for a science textbook, or a substitute for trained teacher judgement. The teacher notes assume a thoughtful adult adapts pacing to the class in front of them.

## Layout

```
curriculum/
├── _shared/            Style guide, templates, glossary, RAG config
├── primary/            Grades 3–5 module packs
├── middle/             Grades 6–8 module packs
└── senior/             Grades 9–12 module packs
exports/                Generated PPTX/PDF/DOCX (do not edit by hand)
```

Each `module-XX-name/` pack contains a 10-day lesson plan, formative + summative quizzes, writing prompts, hands-on activities, homework, teacher notes, a student workbook, assessments, and a slide deck source.

## Pilot scope (current)

Three modules × three age bands = **9 module packs**, complete:
- ✅ Module 2 — Panchabhuta (Five Elements)
- ✅ Module 5 — Dot Addition / Bindu Paddhati (mental-math long addition)
- ✅ Module 8 — Yoga and the Body

The remaining 12 modules are listed in [`BACKLOG.md`](BACKLOG.md) with a checklist for extending the same template.

## Exports

Generated outputs (PPTX decks, PDF handouts, DOCX workbooks) live in [`exports/`](exports/README.md). The markdown source is the source of truth; regenerate exports whenever source changes.

## Source-of-truth retrieval

Curriculum content draws scriptural and mathematical references from two upstream systems (see `_shared/rag-config.md`):

- **vidya-karana-kg** — Bhāgavatam, Bhagavad-gītā, Caitanya Caritāmṛta, Prabhupāda books (89k chunks). Used for cosmology / philosophy / wellness modules.
- **SutraGanita** — Bharati Krishna Tirthaji corpus + general Vedic-math literature. Used for math modules.

No verse, sūtra, or source is cited unless it appears in one of these systems' returned `sources` or in a module's `sources.md`. This is enforced by the citation audit in the verification checklist.

## How to use

1. Read `_shared/style-guide.md` first — it codifies voice, citation rules, and age-band adaptation.
2. For each module pack, start with `README.md` (objectives + materials) and `lesson-plan.md` (10-day overview).
3. Teach from `days/day-NN-*.md`; students use `student-workbook.md`; printable handouts are in `exports/pdf/`.

## Extending to new modules

See the checklist at the bottom of `BACKLOG.md` (generated in Phase D).
