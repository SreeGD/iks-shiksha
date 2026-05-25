#!/usr/bin/env bash
# Build one combined DOCX workbook per age band (compiling all 3 pilot modules).
#
# Output: exports/docx/iks-curriculum-<band>.docx

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

OUT="$ROOT/exports/docx"
TMP="$ROOT/.build-tmp"
mkdir -p "$OUT" "$TMP"

REF_DOCX="$TMP/reference.docx"
if [ ! -f "$REF_DOCX" ]; then
  pandoc --print-default-data-file reference.docx > "$REF_DOCX"
fi

build_band_workbook() {
  local band="$1"
  local band_title
  case "$band" in
    primary) band_title="Primary (Grades 3–5)" ;;
    middle)  band_title="Middle (Grades 6–8)" ;;
    senior)  band_title="Senior (Grades 9–12)" ;;
    *) echo "bad band"; return 1 ;;
  esac

  local combined="$TMP/workbook-$band.md"
  local out_docx="$OUT/iks-curriculum-$band.docx"

  {
    echo "% IKS Curriculum — $band_title"
    echo "% Compiled pilot workbook"
    echo ""
    echo "# IKS Curriculum — $band_title"
    echo ""
    echo "This combined workbook compiles the five pilot modules for the **$band_title** band:"
    echo "  - Module 1 — What is IKS?"
    echo "  - Module 2 — Panchabhuta (Five Elements)"
    echo "  - Module 3 — Ayurveda and Good Health"
    echo "  - Module 4 — Doshas (Vāta, Pitta, Kapha)"
    echo "  - Module 5 — Bindu Paddhati (Dot Method of Addition)"
    echo "  - Module 6 — Moon Phases and Tithi"
    echo "  - Module 7 — ×11 Multiplication (Ekādhikena Pūrveṇa)"
    echo "  - Module 8 — Yoga and the Body"
    echo "  - Module 9 — Subtraction Nikhilam (All from 9, last from 10)"
    echo "  - Module 10 — Herbs (Auṣadhi)"
    echo "  - Module 11 — Multiplication Near a Power of 10"
    echo "  - Module 12 — Movement of the Sun"
    echo "  - Module 13 — Indic Ecology (Vasudhaiva Kuṭumbakam)"
    echo "  - Module 14 — Magic Squares (Bhadragaṇita)"
    echo "  - Module 15 — Project Implementation (Capstone)"
    echo ""
    echo "Each module contains: overview, 10-day lesson plan, teacher notes, sources, all day files, quizzes, writing prompts, homework, activities, project brief, and rubric."
    echo ""
    echo "\\newpage"
    for mod in module-01-what-is-iks module-02-panchabhuta module-03-ayurveda-good-health module-04-doshas module-05-dot-addition module-06-moon-phases-tithi module-07-eleven-multiplication module-08-yoga module-09-subtraction-nikhilam module-10-herbs-aushadhi module-11-multiplication-near-base module-12-movement-of-sun module-13-indic-ecology module-14-magic-squares module-15-project-implementation; do
      local pack_dir="$ROOT/curriculum/$band/$mod"
      if [ ! -d "$pack_dir" ]; then continue; fi

      echo ""
      echo "# ──── $mod ────"
      echo ""

      # Order to compile within each module
      for f in \
        "$pack_dir/README.md" \
        "$pack_dir/lesson-plan.md" \
        "$pack_dir/teacher-notes.md" \
        "$pack_dir/sources.md" \
        "$pack_dir/parent-guide.md" \
        "$pack_dir/days"/day-*.md \
        "$pack_dir/quizzes"/*.md \
        "$pack_dir/writing-prompts.md" \
        "$pack_dir/homework.md" \
        "$pack_dir/activities"/*.md \
        "$pack_dir/assessments"/*.md \
        "$pack_dir/student-workbook.md" ; do
        if [ -f "$f" ]; then
          echo ""
          echo "\\newpage"
          echo ""
          cat "$f"
          echo ""
        fi
      done
      echo ""
      echo "\\newpage"
    done
  } > "$combined"

  pandoc "$combined" \
    --reference-doc="$REF_DOCX" \
    --from=markdown+raw_tex+raw_html \
    --to=docx \
    --toc --toc-depth=3 \
    -o "$out_docx"

  echo "  ✓ $(basename "$out_docx") ($(du -h "$out_docx" | cut -f1))"
}

for band in primary middle senior; do
  build_band_workbook "$band"
done

echo ""
echo "Done."
ls -la "$OUT"
