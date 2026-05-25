#!/usr/bin/env bash
# Build per-day PDFs + PPTX for selected modules.
#
# For each day-NN-*.md file in the named modules:
#   1. Convert markdown -> DOCX (pandoc) -> PDF (soffice) directly.
#   2. Pre-process: insert --- before each H2 to make a multi-slide deck,
#      then run through generate-pptx.js to produce a per-day PPTX.
#
# Outputs:
#   exports/pdf/lessons/<band>-<module>/day-NN.pdf
#   exports/pptx/lessons/<band>-<module>/day-NN.pptx

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
export NODE_PATH="$ROOT/node_modules"

OUT_PDF="$ROOT/exports/pdf/lessons"
OUT_PPTX="$ROOT/exports/pptx/lessons"
TMP="$ROOT/.build-tmp/lessons"
mkdir -p "$OUT_PDF" "$OUT_PPTX" "$TMP"

REF_DOCX="$ROOT/.build-tmp/reference.docx"
if [ ! -f "$REF_DOCX" ]; then
  pandoc --print-default-data-file reference.docx > "$REF_DOCX"
fi

# Convert one day .md to PDF (via DOCX) and PPTX (via deck split).
one_day() {
  local band="$1"
  local mod="$2"
  local md="$3"
  local day_stem
  day_stem=$(basename "$md" .md)   # e.g. day-04-element-sort

  local pack_id="$band-$mod"
  mkdir -p "$OUT_PDF/$pack_id" "$OUT_PPTX/$pack_id"

  local pdf_out="$OUT_PDF/$pack_id/$day_stem.pdf"
  local pptx_out="$OUT_PPTX/$pack_id/$day_stem.pptx"

  # ----- PDF (direct from markdown) -----
  local docx_tmp="$TMP/$pack_id-$day_stem.docx"
  pandoc "$md" \
    --reference-doc="$REF_DOCX" \
    --from=markdown+raw_tex+raw_html \
    --to=docx \
    -o "$docx_tmp" 2>/dev/null
  soffice --headless --convert-to pdf --outdir "$OUT_PDF/$pack_id" "$docx_tmp" \
    >/dev/null 2>&1
  # soffice names output by docx stem; rename if needed
  local soffice_pdf="$OUT_PDF/$pack_id/$(basename "$docx_tmp" .docx).pdf"
  if [ -f "$soffice_pdf" ] && [ "$soffice_pdf" != "$pdf_out" ]; then
    mv "$soffice_pdf" "$pdf_out"
  fi

  # ----- PPTX (pre-process: split aggressively + escape leading dashes) -----
  local deck_md="$TMP/$pack_id-$day_stem-deck.md"
  # Split BEFORE every H2 (##) AND H3 (###); demote H3 to bold H2 for cleaner slides;
  # replace leading "- " (in non-list contexts) with "– " to avoid bullet-validator.
  awk '
    BEGIN { first = 1 }
    /^## / || /^### / {
      if (!first) print "---"
      first = 0
      # Demote ### to ## for visual consistency
      sub(/^### /, "## ", $0)
    }
    # Replace leading "- " or "-x" in code/script lines so html2pptx validator
    # does not flag them as bullets.
    /^[[:space:]]*- [A-Z0-9]/ { sub(/- /, "– ") }
    { print }
  ' "$md" > "$deck_md"
  # Ensure leading --- exists (the deck splitter expects --- as separator)
  if ! head -1 "$deck_md" | grep -q '^---$'; then
    { echo '---'; cat "$deck_md"; } > "$deck_md.tmp" && mv "$deck_md.tmp" "$deck_md"
  fi

  node "$ROOT/scripts/generate-pptx.js" \
    --in "$deck_md" \
    --out "$pptx_out" \
    --band "$band" 2>&1 | grep -v "Parsed " | grep -v "^Wrote" || true

  if [ -f "$pdf_out" ]; then
    echo "  ✓ $pack_id/$day_stem.pdf + .pptx"
  else
    echo "  ✗ $pack_id/$day_stem.pdf MISSING"
  fi
}

# Loop over target modules
for band in primary middle senior; do
  for mod in module-01-what-is-iks module-02-panchabhuta module-03-ayurveda-good-health; do
    pack_dir="$ROOT/curriculum/$band/$mod"
    [ -d "$pack_dir/days" ] || continue
    echo "Pack: $band/$mod"
    for md in "$pack_dir/days"/day-*.md; do
      [ -f "$md" ] || continue
      one_day "$band" "$mod" "$md"
    done
  done
done

echo ""
echo "Done."
echo "PDFs: $(find "$OUT_PDF" -name '*.pdf' | wc -l | xargs) files"
echo "PPTX: $(find "$OUT_PPTX" -name '*.pptx' | wc -l | xargs) files"
