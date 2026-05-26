import os

root = "./corpus/upanishads"

index = []

for subdir, dirs, files in os.walk(root):
    for file in files:
        if file.endswith(".md"):
            path = os.path.relpath(os.path.join(subdir, file), root)
            index.append(path)

index.sort()

with open("upanishad_index.txt", "w") as f:
    for item in index:
        f.write(item + "\n")

print("Index written to upanishad_index.txt")