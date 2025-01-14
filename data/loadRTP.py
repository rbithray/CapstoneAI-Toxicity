import pandas as pd
import json

df = pd.read_json("hf://datasets/allenai/real-toxicity-prompts/prompts.jsonl", lines=True)
prompts = pd.DataFrame(list(df.prompts))
prompt_text = list(prompts.text)
with open("prompts.json", "w") as outfile:
    json.dump(prompt_text, outfile, indent=4)
