#!/usr/bin/env bash
# Build PDFs + PPTX for the 45 Darśana workshop files.
#
# For each curriculum/{band}/{mod}/darshana.md:
#   1. pandoc → DOCX (with reference style)
#   2. soffice → PDF
#   3. soffice → PPTX (auto layout)
#
# Output: exports/pdf/darshana/<band>-<mod>.pdf
#         exports/pptx/darshana/<band>-<mod>.pptx

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

OUT_PDF="$ROOT/exports/pdf/darshana"
OUT_PPTX="$ROOT/exports/pptx/darshana"
TMP="$ROOT/.build-tmp/darshana"
mkdir -p "$OUT_PDF" "$OUT_PPTX" "$TMP"

REF_DOCX="$ROOT/.build-tmp/reference.docx"
if [ ! -f "$REF_DOCX" ]; then
  pandoc --print-default-data-file reference.docx > "$REF_DOCX"
fi

build_one() {
  local band="$1"
  local mod="$2"
  local src="$ROOT/curriculum/$band/$mod/darshana.md"
  [ -f "$src" ] || { echo "  - $band/$mod (no darshana.md)"; return; }

  local stem="${band}-${mod}"
  local out_md="$TMP/${stem}.md"
  local out_docx="$TMP/${stem}.docx"
  local out_pdf="$OUT_PDF/${stem}.pdf"

  {
    echo "% ${mod} - Darshana (60-min workshop)"
    echo "% IKS Curriculum - ${band} band"
    echo ""
    cat "$src"
  } > "$out_md"

  pandoc "$out_md" \
    --reference-doc="$REF_DOCX" \
    -f markdown \
    -t docx \
    -o "$out_docx" 2>/dev/null

  soffice --headless --convert-to pdf --outdir "$OUT_PDF" "$out_docx" > /dev/null 2>&1 || true

  pandoc "$out_md" \
    -f markdown \
    -t pptx \
    -o "$OUT_PPTX/${stem}.pptx" 2>/dev/null || true

  if [ -f "$out_pdf" ] && [ -f "$OUT_PPTX/${stem}.pptx" ]; then
    echo "  ok ${stem}"
  else
    echo "  partial ${stem}"
  fi
}

echo "Building Darshana exports..."
for band in primary middle senior; do
  for mod in module-01-what-is-iks module-02-panchabhuta module-03-ayurveda-good-health \
             module-04-doshas module-05-dot-addition module-06-moon-phases-tithi \
             module-07-eleven-multiplication module-08-yoga module-09-subtraction-nikhilam \
             module-10-herbs-aushadhi module-11-multiplication-near-base \
             module-12-movement-of-sun module-13-indic-ecology module-14-magic-squares \
             module-15-project-implementation; do
    build_one "$band" "$mod"
  done
done

echo ""
echo "Done."
echo "PDFs:  $(find "$OUT_PDF" -name '*.pdf' | wc -l | xargs) files"
echo "PPTX:  $(find "$OUT_PPTX" -name '*.pptx' | wc -l | xargs) files"
