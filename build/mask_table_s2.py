"""Mask low-count cohort allele frequencies in Supplementary Table S2.

A variant whose minor allele is observed on 5 or fewer of the 822 T21
chromosome copies (274 participants x 3 copies) could help identify the
participants who carry it. For those variants, the cohort frequency columns
are replaced with the label "5 or lower". The GTEx and gnomAD columns are
public and are left as they are. Running the script on an already masked
table leaves it unchanged.

Usage: python build/mask_table_s2.py IN.csv OUT.csv
"""

import csv
import sys

COPIES = 822
MAX_MASKED_COUNT = 5
LABEL = "5 or lower"
COHORT_FREQUENCY_COLUMNS = ["htp_alt_af", "htp_maf"]


def is_low_count(row):
    if row["htp_maf"] == LABEL:
        return True
    return round(float(row["htp_maf"]) * COPIES) <= MAX_MASKED_COUNT


def main():
    source, target = sys.argv[1], sys.argv[2]
    with open(source, newline="") as handle:
        reader = csv.DictReader(handle)
        fields = reader.fieldnames
        rows = list(reader)
    masked = [row for row in rows if is_low_count(row)]
    for row in masked:
        row.update({column: LABEL for column in COHORT_FREQUENCY_COLUMNS})
    with open(target, "w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(f"masked {len(masked)} of {len(rows)} variants")


if __name__ == "__main__":
    main()
