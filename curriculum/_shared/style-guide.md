# Style Guide

Every module pack must follow this guide. When in doubt, choose clarity over reverence and accuracy over fluency.

## Voice

**Lead with the observable phenomenon or the underlying mechanism. Situate the tradition as historical context.**

✅ "Matter exists in five observable states — solid (earth-like), liquid (water-like), gas (air-like), plasma/heat (fire-like), and empty space. Around 1500 BCE, thinkers in the Indian subcontinent organised this same observation into a framework they called *pañcabhūta* — 'the five great elements'."

❌ "The ancient ṛṣis in their divine wisdom revealed the eternal truth of the pañcabhūtas which Western science later rediscovered."

This rule holds for all three age bands. Primary just uses simpler words.

### Tone by age band

| Band    | Sentence length | Voice | Vocabulary |
|---------|----------------|-------|------------|
| Primary | 8–12 words avg | Friendly, curious, story-led | Common words; one new Sanskrit term per lesson, repeated |
| Middle  | 15–20 words avg | Inquiry-driven, balanced | Technical terms allowed if defined inline |
| Senior  | 20–30 words avg | Analytical, comparative | Primary-source language; assumes prior context |

## Sanskrit terms

Every Sanskrit term on first appearance in a file uses this triple format:

> *pañcabhūta* (IAST: pañca-bhūta; lit. "five great elements")

After first appearance, italicised Sanskrit alone is fine: *pañcabhūta*.

- IAST diacritics required (ā, ī, ū, ṛ, ṭ, ḍ, ṇ, ś, ṣ, ṁ, ḥ). No ad-hoc romanisations.
- Always italicise Sanskrit; never bold for emphasis.
- In quizzes and worksheets aimed at students, give the meaning on first use within the worksheet itself, even if it appeared in the lesson.
- Glossary entry required in `_shared/glossary.md` for every term used.

## Citations (hard rules)

1. **Scripture citations** come from the **vidya-karana-kg RAG**. Preserve the `source` field verbatim (e.g. "SB 3.26.36" or "BG 6.13"). If the RAG did not return it, do not cite it.
2. **Vedic-math sūtra references** come from **SutraGanita**'s `sources` array (e.g. "Vedic Mathematics.pdf"). Cite the sūtra by name (Śuddha, Ekādhikena, Nikhilam, Ūrdhva-tiryagbhyāṁ) and the source file.
3. **No invented citations.** A drafting pass that produces an unverifiable citation must be rewritten, not patched.
4. **By age band:**
   - **Senior** — at least one direct quoted verse with citation per module
   - **Middle** — at least one paraphrase with citation per module; direct quotes optional
   - **Primary** — concepts used without student-facing citation; citations belong in teacher notes only

## NEP 2020 alignment

Each module's `README.md` lists which NEP 2020 principles the module advances. Common ones:
- §4.6 — Integration of Indian Knowledge Systems
- §4.23 — Experiential learning (hands-on activities, project-based assessment)
- §11.8 — Holistic, multidisciplinary education (cross-disciplinary connections day 6)
- §4.27 — Local context and language

State the alignment in one sentence per principle. Do not pad.

## Lesson structure (45-min class)

Every `day-NN-*.md` lesson follows this skeleton (times approximate, adjust as needed):

- **Warm-up (5 min)** — hook, recall, or sensory grounding
- **Core (20 min)** — new concept introduced and demonstrated
- **Activity (15 min)** — hands-on, paired, or written practice
- **Wrap-up (5 min)** — exit ticket, reflection question, or preview of next day

The lesson file lists: learning objective, materials, teacher script bullets, student-facing content, homework (if any), differentiation note.

## Differentiation

Every day-lesson includes a **Differentiation** block with one suggestion **one tier up** (for fast finishers) and one suggestion **one tier down** (for students who need scaffolding). Two sentences total is enough.

## Assessment

- **Formative** — woven into days 2, 4, and 6. 3–5 quick checks each, no grade weight.
- **Summative** — single end-of-module quiz (day 5 or 10) — mix of MCQ, short answer, diagram label / draw, and one open question.
- **Project** — days 8–9 work session, day 10 presentation; assessed against the rubric in `assessments/rubric.md`.

### Rubric scale (consistent across all packs)

| Score | Label | Meaning |
|-------|-------|---------|
| 4 | Exceeds | Goes beyond what was taught; makes connections; teaches a peer |
| 3 | Meets | Demonstrates the objective accurately and independently |
| 2 | Approaches | Demonstrates with prompting; minor errors |
| 1 | Beginning | Attempts; major errors or significant scaffolding needed |

## Safety notes (especially for Yoga and physical activities)

- **Primary band yoga:** no inversions (śīrṣāsana, halāsana), no advanced backbends (cakrāsana, dhanurāsana). Stick to seated, standing, and balance poses.
- **Middle band:** Sūrya Namaskāra acceptable; supervise alignment.
- **Senior band:** Inversions allowed only with experienced teacher supervision; contraindication note required (BP, neck/back injury, pregnancy, menstruation per traditional guidance).
- **All bands:** Prāṇāyāma (breath retention practices) limited to natural-breath observation only, unless a certified yoga teacher is present.

## File naming

- Day files: `day-NN-short-slug.md` (e.g. `day-01-hook.md`, `day-04-element-sort.md`). Zero-padded.
- Activities: `activity-NN-short-slug.md`.
- Slides: a single `slides/deck.md` per module, ~25 slides, markdown converted via the `pptx` skill.
- All file content in English; Sanskrit terms inline in IAST with translation.

## Writing prompts

Each module ships **6–10 prompts** covering:
- 2 reflection (personal connection)
- 2 explanatory (in your own words)
- 1 argumentative (defend or critique a position)
- 1 creative (story, dialogue, or imagined scenario)
- Optional: 1 cross-disciplinary (link to a non-IKS subject)

Each prompt names the band it suits — primary prompts can be illustrated, middle written, senior essay-length.

## Things to avoid

- Civilisational chest-thumping ("ancient Indians knew this before everyone").
- Implying that modern science "rediscovered" or "validates" tradition. Frame them as parallel observations from different methods.
- Treating mythology as history. Stories from the Purāṇas are taught as stories with embedded ideas, not as factual events.
- Religious framing of yoga or breath practice in school context. Stick to physiological and observational language.
- Sanskrit terms without meaning, on the assumption "students will pick it up."
