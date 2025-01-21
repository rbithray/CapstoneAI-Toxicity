"""
	Get generated content and toxicity scores for Gemma
"""
import os

from llms.gemma import init_gemma
from get_scores_keras import get_responses_scores
import json

gemma = init_gemma()

prompts = json.load()# TODO open file with comments and correct structure

token_file = os.path.join("..", "secrets")

results = get_responses_scores(prompts, token_file)

with open("../generated/result_Gemma.json", "w") as outfile:
    json.dump(results, outfile, indent=4)

