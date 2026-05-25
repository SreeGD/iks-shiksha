#!/usr/bin/env bash
# Build per-pack audience-specific PDFs (teacher / parent / student / activity).
#
# Pipeline per guide:
#   1. Concatenate the relevant markdown source files into one combined .md
#      (with page-break markers and section dividers)
#   2. pandoc combined.md -o combined.docx  (apply reference style)
#   3. soffice --convert-to pdf combined.docx
#
# Output: exports/pdf/<band>-<module>-<audience>.pdf

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

OUT="$ROOT/exports/pdf"
TMP="$ROOT/.build-tmp"
mkdir -p "$OUT" "$TMP"

# Cache the reference DOCX so all generated PDFs share consistent styling.
REF_DOCX="$TMP/reference.docx"
if [ ! -f "$REF_DOCX" ]; then
  pandoc --print-default-data-file reference.docx > "$REF_DOCX"
fi

# Helper: combine a list of .md files into one big .md with a top header.
# Usage: combine_md output_md title file1 file2 ...
combine_md() {
  local outmd="$1"; shift
  local title="$1"; shift
  {
    echo "% $title"
    echo "% IKS Curriculum"
    echo ""
    for f in "$@"; do
      if [ -f "$f" ]; then
        echo ""
        # Section heading from filename (no extension)
        local base
        base=$(basename "$f" .md)
        # Skip a redundant repeating intro for the per-day files
        case "$base" in
          README) echo "# Overview" ;;
          lesson-plan) echo "\\newpage" ; echo "# 10-Day Lesson Plan" ;;
          teacher-notes) echo "\\newpage" ; echo "# Teacher Notes" ;;
          sources) echo "\\newpage" ; echo "# Sources" ;;
          writing-prompts) echo "\\newpage" ; echo "# Writing Prompts" ;;
          homework) echo "\\newpage" ; echo "# Homework" ;;
          student-workbook) echo "\\newpage" ; echo "# Student Workbook" ;;
          parent-guide) echo "\\newpage" ;;
          rubric) echo "\\newpage" ; echo "# Rubric" ;;
          project-brief) echo "\\newpage" ; echo "# Project Brief" ;;
          *) echo "\\newpage" ;;
        esac
        echo ""
        cat "$f"
        echo ""
      fi
    done
  } > "$outmd"
}

# Convert a combined .md to PDF via DOCX
md_to_pdf() {
  local md="$1"
  local out_pdf="$2"
  local stem
  stem=$(basename "$out_pdf" .pdf)
  local docx="$TMP/$stem.docx"

  pandoc "$md" \
    --reference-doc="$REF_DOCX" \
    --from=markdown+raw_tex+raw_html \
    --to=docx \
    --toc --toc-depth=2 \
    -o "$docx" 2>/dev/null

  # Convert DOCX to PDF via soffice (suppress noisy output)
  soffice --headless --convert-to pdf --outdir "$(dirname "$out_pdf")" "$docx" \
    >/dev/null 2>&1

  echo "  ✓ $(basename "$out_pdf")"
}

# Build all guide types for one pack
build_pack() {
  local band="$1"
  local mod="$2"
  local pack_dir="$ROOT/curriculum/$band/$mod"
  local stem="$band-$mod"

  if [ ! -d "$pack_dir" ]; then
    echo "Skip: $pack_dir not found"; return
  fi

  echo "Pack: $band / $mod"

  # ----- Teacher guide: full pack -----
  local tmd="$TMP/$stem-teacher.md"
  combine_md "$tmd" "Teacher Guide — $band / $mod" \
    "$pack_dir/README.md" \
    "$pack_dir/lesson-plan.md" \
    "$pack_dir/teacher-notes.md" \
    "$pack_dir/sources.md" \
    "$pack_dir/days"/day-*.md \
    "$pack_dir/quizzes"/*.md \
    "$pack_dir/homework.md" \
    "$pack_dir/writing-prompts.md" \
    "$pack_dir/activities"/*.md \
    "$pack_dir/assessments"/*.md
  md_to_pdf "$tmd" "$OUT/$stem-teacher.pdf"

  # ----- Parent guide: just the parent guide + lesson plan overview -----
  local pmd="$TMP/$stem-parent.md"
  combine_md "$pmd" "Parent Guide — $band / $mod" \
    "$pack_dir/parent-guide.md" \
    "$pack_dir/lesson-plan.md" \
    "$pack_dir/homework.md"
  md_to_pdf "$pmd" "$OUT/$stem-parent.pdf"

  # ----- Student guide: workbook + day content + prompts -----
  local smd="$TMP/$stem-student.md"
  combine_md "$smd" "Student Guide — $band / $mod" \
    "$pack_dir/student-workbook.md" \
    "$pack_dir/days"/day-*.md \
    "$pack_dir/writing-prompts.md" \
    "$pack_dir/homework.md"
  md_to_pdf "$smd" "$OUT/$stem-student.pdf"

  # ----- Activity guide: printable activities + project brief -----
  local amd="$TMP/$stem-activities.md"
  combine_md "$amd" "Activity Guide — $band / $mod" \
    "$pack_dir/activities"/*.md \
    "$pack_dir/assessments/project-brief.md"
  md_to_pdf "$amd" "$OUT/$stem-activities.pdf"
}

# Iterate over all packs (syllabus order)
for band in primary middle senior; do
  for mod in module-01-what-is-iks module-02-panchabhuta module-03-ayurveda-good-health module-05-dot-addition module-08-yoga; do
    build_pack "$band" "$mod"
  done
done

echo ""
echo "Done. Output in $OUT/"
ls -la "$OUT" | head -45
