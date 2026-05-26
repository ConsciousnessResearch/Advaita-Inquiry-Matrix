import os
from collections import defaultdict

root = "./corpus"

prakriya_map = defaultdict(list)

for subdir, dirs, files in os.walk(root):
    for file in files:
        if file.endswith(".md"):
            path = os.path.join(subdir, file)

            with open(path, "r", encoding="utf-8") as f:
                for line in f:
                    if "prakriyā:" in line:
                        prakriya = line.split("prakriyā:")[1].strip()
                        prakriya_map[prakriya].append(path)

print("\nPrakriyā Index\n")

for prakriya in sorted(prakriya_map):
    print(prakriya)

    for location in prakriya_map[prakriya]:
        print("   ", location)

    print()