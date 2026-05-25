# BACKLOG — Remaining 12 IKS Modules

The pilot delivered 9 module packs (3 modules × 3 age bands):
- ✅ Module 2 — Panchabhūta (Primary / Middle / Senior)
- ✅ Module 5 — Bindu Paddhati / Dot Addition (Primary / Middle / Senior)
- ✅ Module 8 — Yoga and the Body (Primary / Middle / Senior)

This file lists the **12 remaining modules** from the original IKS syllabus on which this curriculum is based (see [ATTRIBUTION.md](ATTRIBUTION.md)), with notes on how to apply the same template.

## Status legend

- 🟢 Strong RAG/source coverage available
- 🟡 Partial coverage; some primary-source work needed
- 🔴 Minimal source coverage; significant outside research required

## Remaining modules

| # | Module | RAG/SutraGanita support | Notes |
|---|--------|---------------------------|-------|
| 1 | What is IKS? | 🟡 | Introductory module; use Plofker (2009) and the original source materials (see ATTRIBUTION). |
| 3 | Ayurveda and Good Health | 🟢 | Vidya-karana RAG has `radha_ayurveda` subset. Plus standard Ayurveda primers. |
| 4 | Doshas (Vāta, Pitta, Kapha) | 🟢 | Same as #3 plus Caraka Saṁhitā / Suśruta Saṁhitā extracts. |
| 6 | Astronomy — Moon Phases & Tithi | 🔴 | Need Sūrya-siddhānta + modern astronomy textbook references. |
| 7 | 11 Multiplication (Vedic Math) | 🟢 | SutraGanita corpus + Tirthaji (1965). Same approach as Module 5. |
| 9 | Subtraction — Complements Method | 🟢 | Tirthaji's *Nikhilam* sūtra (#2). SutraGanita PDFs. |
| 10 | Herbs (Aushadhi) | 🟡 | Tulsi, Neem, Turmeric, Ginger, Ajwain, Mint. Use Ayurveda subset + modern phytochemistry. |
| 11 | Multiplication Close to 10 & 100 | 🟢 | Tirthaji's *Nikhilam* sūtra. Same approach as Module 5. |
| 12 | Movement of the Sun (Solar Year, Uttarāyaṇa, Dakshiṇāyana, Rāshis) | 🔴 | Sūrya-siddhānta + modern astronomy. |
| 13 | Indic Ecology (Vasudhaiva Kuṭumbakam) | 🟡 | Vidya-karana RAG has some references; modern sustainability texts needed. |
| 14 | Magic Squares (Bhadragaṇita) | 🔴 | Need Nārāyaṇa Paṇḍita's *Gaṇita-kaumudī*. Some references in SutraGanita PDFs. |
| 15 | Project Implementation (Panchagavya etc.) | 🟡 | Original program project; needs hands-on safety vetting. |

## How to extend — checklist per module

For each new module, replicate the structure used in the pilot:

### Step 1 — Foundation
- [ ] Run RAG queries (if RAG-eligible) for cosmology / philosophy queries.
- [ ] For SutraGanita-eligible modules, identify the relevant PDFs in `/Users/sree/Projects/SutraGanita/content/`.
- [ ] For neither-supported modules, locate primary sources (textbooks, scholarly works).

### Step 2 — Create module directories
```bash
for band in primary middle senior; do
  mkdir -p curriculum/$band/module-XX-name/{days,quizzes,activities,assessments,slides,.rag-cache,.sutraganita-cache}
done
```

### Step 3 — Write per-band content (follow the 9 pilot packs as templates)
- README.md — objectives, NEP alignment, prerequisites, materials, day-by-day overview
- lesson-plan.md — 10-day overview
- sources.md — primary + secondary sources used
- teacher-notes.md — common misconceptions, safety, differentiation
- days/day-NN-*.md (10 files) — full lesson plans
- quizzes/formative.md + summative.md
- writing-prompts.md (Middle/Senior; oral-recall for Primary)
- homework.md
- activities/activity-NN-*.md (1–3 files)
- assessments/rubric.md + project-brief.md
- student-workbook.md
- slides/deck.md

### Step 4 — Adapt to the three age bands

Use the rules in `curriculum/_shared/style-guide.md`:
- **Primary (3–5):** story-led, drawing-heavy, ~30-min sessions, sticker-based assessment, oral recall.
- **Middle (6–8):** balanced text + activity, ~45-min sessions, mixed quiz formats, project + presentation.
- **Senior (9–12):** primary-source reading, research-paper projects, ~45-min sessions, argumentative writing.

### Step 5 — Generate exports
Once a pack is approved, run:
- `pptx` skill on `slides/deck.md` → PPTX in `exports/pptx/`
- `pdf` skill on day handouts → PDFs in `exports/pdf/`
- `docx` skill compiling band's modules → DOCX in `exports/docx/`

## Module sequencing recommendation

If teaching the full 15-module curriculum, sequence:

1. **What is IKS?** (Module 1) — intro
2. **Panchabhūta** (Module 2) — ✅ pilot
3. **Indic Ecology** (Module 13) — extends Module 2's imbalance theme
4. **Ayurveda + Doshas + Herbs** (Modules 3, 4, 10) — wellness cluster
5. **Yoga and the Body** (Module 8) — ✅ pilot
6. **Dot Addition** (Module 5) — ✅ pilot
7. **11 Multiplication, Subtraction, Mult. Near 10/100** (Modules 7, 9, 11) — math cluster
8. **Magic Squares** (Module 14) — math culmination
9. **Astronomy — Moon Phases / Tithi + Sun's Movement** (Modules 6, 12) — astronomy cluster
10. **Project** (Module 15) — synthesis

(15 modules × 10 days = 150 instructional days = ~7.5 months at one module per 3 weeks. Adjust pacing as needed.)

## Open questions for the user

1. **Which 3 modules should be the second-pilot batch?** Suggestion: Modules 3, 4, 10 (Ayurveda + Doshas + Herbs) — strong RAG coverage, complements pilot.
2. **Should the BACKLOG be filled to the same depth as the pilot?** The pilot averages ~22 files per pack. 12 modules × 3 bands × 22 = ~800 files. Significant scope.
3. **Should additional age bands be added?** (e.g. "Foundational" for K–2, "College preparatory" for 11–12 honors track).

## Sanity-check note

The pilot can be taught immediately. The 12 remaining modules are *planning artefacts* until they are filled out following this checklist.
