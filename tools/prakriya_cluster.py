import json
from collections import Counter
from difflib import SequenceMatcher

# -------------------------------------
# Load corpus database
# -------------------------------------

with open("corpus_database.json", encoding="utf-8") as f:
    records = json.load(f)

# -------------------------------------
# Collect prakriyā labels
# -------------------------------------

prakriyas = []

for r in records:

    if "prakriyā" in r:

        v = r["prakriyā"]

        if isinstance(v, list):
            prakriyas.extend(v)
        else:
            prakriyas.append(v)

counts = Counter(prakriyas)

labels = list(counts.keys())

# -------------------------------------
# Similarity clustering
# -------------------------------------

clusters = []

visited = set()

for label in labels:

    if label in visited:
        continue

    cluster = [label]
    visited.add(label)

    for other in labels:

        if other in visited:
            continue

        sim = SequenceMatcher(None, label, other).ratio()

        if sim > 0.65:
            cluster.append(other)
            visited.add(other)

    clusters.append(cluster)

# -------------------------------------
# Sort clusters by size
# -------------------------------------

clusters.sort(key=len, reverse=True)

print("\nPrakriyā clusters\n")

for c in clusters[:30]:

    total = sum(counts[x] for x in c)

    print(f"\nCluster size {len(c)}  (occurrences {total})")

    for x in c:
        print(" ", x, ":", counts[x])