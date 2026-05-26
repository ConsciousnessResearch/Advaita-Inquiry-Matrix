import os

root = "./corpus"

counts = {}

for subdir, dirs, files in os.walk(root):
    for file in files:
        if file.endswith(".md"):
            parts = subdir.split("/")
            
            if len(parts) > 2:
                category = parts[2]
            else:
                category = "unknown"

            counts[category] = counts.get(category, 0) + 1

print("\nAIM Corpus Summary\n")

for category in counts:
    print(f"{category}: {counts[category]} files")