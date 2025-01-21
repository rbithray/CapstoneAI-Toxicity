import json
with open("prompts.json", "r") as f:
    prompts = json.load(f)

with open("prompts_segmented.json", "w") as outfile:
    json.dump(prompts[:250], outfile, indent=4)