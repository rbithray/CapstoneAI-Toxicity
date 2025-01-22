import pandas as pd

base_path = "../../data/toxic/"

scores = pd.DataFrame(pd.read_json(f"{base_path}500toxic.json").reset_index().toxicity)

bloom = pd.read_json(f"{base_path}BLOOM_results.json")[2]
gemma = pd.read_json(f"{base_path}Gemma_results.json")[2]
llama = pd.read_json(f"{base_path}LLaMA_results.json")[2]
mistral = pd.read_json(f"{base_path}Mistral_results.json")[2]

scores["BLOOM"] = bloom
scores["Gemma"] = gemma
scores["LLaMA"] = llama
scores["Mistral"] = mistral
scores.to_json(f"{base_path}500toxic_scores.json", orient="records", indent=4)