import csv
from collections import defaultdict

INPUT_FILE = "UNKNOWN_TAG_RESOLUTION.csv"

clusters = defaultdict(list)

with open(INPUT_FILE, encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        tag = row["Tag"]

        # use prefix before first underscore
        prefix = tag.split("_")[0]

        clusters[prefix].append(tag)

print("\nTag Clusters\n")

for prefix in sorted(clusters):

    print(f"\n=== {prefix} ({len(clusters[prefix])}) ===")

    for tag in sorted(clusters[prefix]):
        print(tag)