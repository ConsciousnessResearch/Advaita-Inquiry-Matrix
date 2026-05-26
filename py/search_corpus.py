import os
import sys

root = "./corpus"

query = sys.argv[1].lower()

print(f"\nSearching for: {query}\n")

for subdir, dirs, files in os.walk(root):
    for file in files:
        if file.endswith(".md"):
            path = os.path.join(subdir, file)

            with open(path, "r", encoding="utf-8") as f:
                paragraphs = f.read().split("\n\n")

                for para in paragraphs:
                    if query in para.lower():
                        print(path)
                        print(para.strip())
                        print()