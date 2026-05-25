# Exports — Generated Outputs

This directory holds files generated from the markdown source in `curriculum/`. **Do not edit these files by hand** — re-generate them from the source.

## Subdirectories

- `pptx/` — Slide decks (one per module × age band = 9 in the pilot)
- `pdf/` — Printable handouts and worksheets (per day, per activity)
- `docx/` — Combined workbooks (one per age band)

## How to generate

These exports require invoking the relevant skills. The slide-deck source files all live at `curriculum/<band>/module-XX-name/slides/deck.md`.

### PPTX decks (9 total)

For each of the 9 module packs, run the `pptx` skill with the deck markdown:

```
For middle/module-02-panchabhuta:
  Skill: pptx
  Args: source = curriculum/middle/module-02-panchabhuta/slides/deck.md
        output = exports/pptx/middle-module-02-panchabhuta.pptx
```

Repeat for all 9 (3 bands × 3 modules).

### PDF handouts and worksheets

For each module pack, generate:
- Per-day handouts (one PDF per day from `days/day-NN-*.md`)
- Activity worksheets (one PDF per activity)
- Quiz sheets (formative + summative)
- Project brief
- Rubric

```
Skill: pdf
Source: curriculum/<band>/module-XX-name/days/day-01-*.md
Output: exports/pdf/<band>-module-XX-name/day-01.pdf
```

This generates ~150 PDFs per band × 3 bands = ~450 PDFs for the full pilot.

### DOCX combined workbooks (3 total)

For each age band, compile all 3 pilot modules into a single workbook:

```
Skill: docx
Source: curriculum/primary/module-02-panchabhuta/, curriculum/primary/module-05-dot-addition/, curriculum/primary/module-08-yoga/
Output: exports/docx/iks-curriculum-primary.docx
```

Repeat for middle and senior bands.

## Suggested generation order

1. Slide decks first (visible immediately).
2. DOCX workbooks (one per band — most useful for teacher review).
3. Per-day PDFs as needed for printing.

## Verification

After generation, spot-check:
- 1 PPTX file opens correctly in PowerPoint / Keynote.
- 1 PDF prints cleanly.
- 1 DOCX renders all 3 modules with consistent formatting.
- Pages match expected count.

## Regenerate when source changes

If you edit any source markdown, regenerate the affected exports. Do not edit PPTX/PDF/DOCX files directly.
