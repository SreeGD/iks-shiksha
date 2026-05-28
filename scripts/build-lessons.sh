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
  # Skip with IKS_PPTX_ONLY=1 (e.g. when only the deck pipeline changed).
  if [ -z "${IKS_PPTX_ONLY:-}" ]; then
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
  fi

  # ----- PPTX (pre-process via md-to-deck.py) -----
  # md-to-deck.py does all deck preprocessing: tables→bullet-lists, flatten
  # nested lists, normalise blockquote bullets, split at H2/H3, overflow-aware
  # packing onto "(cont.)" slides, and a leading `---`. This eliminates the
  # blank-table gaps and most IKS_LENIENT overflow/bullet-symbol skips.
  local deck_md="$TMP/$pack_id-$day_stem-deck.md"
  python3 "$ROOT/scripts/md-to-deck.py" "$md" > "$deck_md"

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

# Loop over target modules. Pass module slugs as args to override default.
DEFAULT_MODULES=(
  module-01-what-is-iks
  module-02-panchabhuta
  module-03-ayurveda-good-health
  module-04-doshas
  module-05-dot-addition
  module-06-moon-phases-tithi
  module-07-eleven-multiplication
  module-08-yoga
  module-09-subtraction-nikhilam
  module-10-herbs-aushadhi
  module-11-multiplication-near-base
  module-12-movement-of-sun
  module-13-indic-ecology
  module-14-magic-squares
  module-15-project-implementation
)
if [ "$#" -gt 0 ]; then
  MODULES=("$@")
else
  MODULES=("${DEFAULT_MODULES[@]}")
fi

for band in primary middle senior; do
  for mod in "${MODULES[@]}"; do
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
