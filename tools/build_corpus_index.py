import os
import re
import yaml

corpus_root = "corpus"
rows = []

for root, dirs, files in os.walk(corpus_root):
    for f in files:
        if f.endswith(".md"):
            path = os.path.join(root, f)

            with open(path, "r", encoding="utf8") as file:
                text = file.read()

            yaml_blocks = re.findall(r"```yaml(.*?)```", text, re.S)

            for block in yaml_blocks:
                try:
                    data = yaml.safe_load(block)

                    rows.append({
                        "file": path,
                        "cluster": data.get("cluster"),
                        "prakriya": data.get("prakriyā"),
                        "role": data.get("pedagogical_role"),
                        "adhikara": data.get("adhikāra_level")
                    })

                except:
                    pass


with open("AIM_CORPUS_INDEX.md","w",encoding="utf8") as out:

    out.write("# AIM Corpus Index\n\n")
    out.write("| File | Cluster | Prakriyā | Role | Adhikāra |\n")
    out.write("|------|---------|----------|------|----------|\n")

    for r in rows:
        out.write(f"| {r['file']} | {r['cluster']} | {r['prakriya']} | {r['role']} | {r['adhikara']} |\n")