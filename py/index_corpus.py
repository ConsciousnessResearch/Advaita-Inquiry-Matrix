import os

root = "."

print("\nAIM Corpus Index\n")

for subdir, dirs, files in os.walk(root):
    for file in files:
        if file.endswith(".md"):
            path = os.path.join(subdir, file)
            print(path)