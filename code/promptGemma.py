"""
	Get generated content and toxicity scores for Gemma
"""

from llms.gemma import init_gemma
from perspective import get_score
import json

gemma = init_gemma()

prompts = json.load()# TODO open file with comments and correct structure

results = {}

for i, prompt in enumerate(prompts):
	print(f"Prompt {i+1} of {len(prompts)}\n")
	print(f"> {prompt}\n")
	generated = gemma.generate(prompt, max_length=50)
	print(f"{generated}\n")
	score = get_score(generated)

	results[prompt] = [generated, score]

with open("../generated/result_Gemma.json", "w") as outfile:
    json.dump(results, outfile, indent=4)

