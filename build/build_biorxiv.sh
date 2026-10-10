#!/usr/bin/env bash

## build_biorxiv.sh: build the main manuscript and the supplement as two
## separate PDFs, each with its own reference list, for submission.
##
## Run from the repository root with the manubot conda environment active:
##   conda activate manubot
##   bash build/build_biorxiv.sh
##
## Outputs:
##   output/biorxiv/manuscript.pdf
##   output/biorxiv/supplement.pdf
## Cross-references between the two documents are written as literal labels
## (e.g. "Figure S1" in the main text); see build/split_content.py.

set -o errexit \
    -o nounset \
    -o pipefail

export TZ=Etc/UTC
export LC_ALL=en_US.UTF-8

PANDOC_DATA_DIR="${PANDOC_DATA_DIR:-build/pandoc}"
OUT=output/biorxiv

python build/split_content.py content "$OUT"

# Image paths in the manuscript are relative to the repository root.
if [ -L images ]; then rm images; fi
ln -s content/images

for part in main supplement; do
  echo >&2 "Processing the ${part} document"
  manubot process \
    --content-directory="$OUT/$part/content" \
    --output-directory="$OUT/$part" \
    --cache-directory=ci/cache \
    --skip-citations \
    --log-level=INFO

  name="$part"
  if [ "$part" = "main" ]; then name="manuscript"; fi
  # pandoc adds up input files across defaults files, so each part gets its
  # own copy of common.yaml with the input path replaced.
  sed "s#^input-file: .*#input-file: $OUT/$part/manuscript.md#" \
    "$PANDOC_DATA_DIR/defaults/common.yaml" > "$OUT/$part/common.yaml"
  echo "output-file: $OUT/$name.pdf" > "$OUT/$part/output.yaml"

  echo >&2 "Exporting $OUT/$name.pdf using WeasyPrint"
  pandoc \
    --data-dir="$PANDOC_DATA_DIR" \
    --defaults="$OUT/$part/common.yaml" \
    --defaults=html.yaml \
    --defaults=pdf-weasyprint.yaml \
    --defaults="$OUT/$part/output.yaml"
done

rm images
echo >&2 "Built $OUT/manuscript.pdf and $OUT/supplement.pdf"
