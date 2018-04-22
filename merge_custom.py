#!/usr/bin/env python

import json
import os


loaded_templates = []
localpath = os.getcwd() + "/custom/"
for filename in os.listdir(localpath):
    print("* found {}".format(filename))
    custom_file = open(localpath + filename)
    s = json.load(custom_file)
    loaded_templates.extend(s)
    custom_file.close()

# print(loaded_templates)
print("+ Generating merged JSON Portainer template")

merged = open("merged_portainer_templates.yml", "w")

for t in loaded_templates:
    print("* {} added".format(t["name"]))
merged.write(json.dumps(loaded_templates, indent=2))
print("\n✔️ done")

