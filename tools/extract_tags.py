import os
import re
import yaml
from collections import defaultdict

corpus_root = "corpus"
tags = defaultdict(set)

for root, dirs, files in os.walk(corpus_root):
    for file in files:
        if file.endswith(".md"):

            path = os.path.join(root, file)

            with open(path, encoding="utf8") as f:
                text = f.read()

            blocks = re.findall(r"```yaml(.*?)```", text, re.S)

            for block in blocks:
                try:
                    data = yaml.safe_load(block)

                    for key, value in data.items():
                        if isinstance(value, str):
                            tags[key].add(value)

                except:
                    pass

for k,v in tags.items():
    print("\n",k)
    for i in sorted(v):
        print("   ",i)