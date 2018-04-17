import json
import os
loaded_templates = []
localpath = os.getcwd() + "/custom/"
for filename in os.listdir(localpath):
    print("* found {}".format(filename))
    custom_file = open(localpath + filename)
    s = json.load(custom_file)
    loaded_templates.append(s)
    custom_file.close()
print("Generating merged JSON Portainer template")
for t in loaded_templates:
    for j in range(len(t)):
        print("* adding {}".format(t[j]["name"]))
merged = open("merged_portainer_templates.yml", "w")
merged.write(json.dumps(loaded_templates, indent=2))
print("✔️ done")

