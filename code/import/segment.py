import json
with open("../../data/prompts.json", "r") as f:
    prompts = json.load(f)

with open("../../data/prompts_segmented.json", "w") as outfile:
    json.dump(prompts[:250], outfile, indent=4)