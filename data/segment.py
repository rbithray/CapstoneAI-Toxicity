import json

prompts = json.load(open("prompts.json"))

segment = [int(input("start: ")), int(input("end: "))]

with open("segment.json", "w") as outfile:
    json.dump(prompts[segment[0]:segment[1]], outfile, indent=4)