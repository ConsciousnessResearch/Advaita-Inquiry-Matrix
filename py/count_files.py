import os

root = "."

print("\nAIM Corpus Index\n")

count = 0

for subdir, dirs, files in os.walk(root):
    for file in files:
        if file.endswith(".md"):
            count += 1
            path = os.path.join(subdir, file)
            print(path)

print("\nTotal text files:", count)