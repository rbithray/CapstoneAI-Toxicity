import pandas as pd

prompts = pd.read_json("../../data/random/1000random.json", lines=True)

bloom = pd.read_json("../../data/random/BLOOM_results.json", lines=True)
gemma = pd.read_json("../../data/random/Gemma_results.json", lines=True)
llama = pd.read_json("../../data/random/LLaMA_results.json", lines=True)
mistral = pd.read_json("../../data/random/Mistral_results.json", lines=True)

scores = prompts.toxicity
bloom_scores = bloom[2]
gemma_scores = gemma[2]
llama_scores = llama[2]
mistral_scores = mistral[2]

scores["BLOOM"] = bloom_scores
scores["Gemma"] = gemma_scores
scores["LLaMA"] = llama_scores
scores["Mistral"] = mistral_scores
scores.to_json("../../data/random/1000random_scores.json", orient="records", indent=4)