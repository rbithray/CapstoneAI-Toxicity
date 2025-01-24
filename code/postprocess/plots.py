import matplotlib.pyplot as plt
import pandas as pd
import json

#%%
# UNCOMMENT FOR 1000 RANDOM PROMPTS
# Load the random JSON data into a Pandas DataFrame
#file_path = "../../data/random/1000random_scores.json"

#%%
# UNCOMMENT FOR 500 MOST TOXIC PROMPTS
# Load the JSON data into a Pandas DataFrame
file_path = "../../data/toxic/500toxic_scores.json"


#%%
# Generate scatter plots for each model's response toxicity
models = ["BLOOM", "Gemma", "LLaMA", "Mistral"]
df = pd.read_json(file_path)

# Generate scatter plots for each model's response toxicity in subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("Scatter Plots of Model Response Toxicity To Toxic Prompts", fontsize=16)

for ax, model in zip(axes.flatten(), models):
    ax.scatter(df["toxicity"], df[model], alpha=0.7)
    ax.set_title(f"Toxicity of {model} (Prompts)", fontsize=10)
    ax.set_xlabel("Prompt Toxicity", fontsize=9)
    ax.set_ylabel(f"{model} Response Toxicity", fontsize=9)
    ax.set_ylim(0, 1)
    ax.grid(True)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("../../results/toxic/all_models_scatter.svg", format="svg")

# Generate histogram plots for all models' response toxicity in subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("Histograms of Model Response Toxicity To Toxic Prompts", fontsize=16)

for ax, model in zip(axes.flatten(), models):
    ax.hist(df[model], bins=30, alpha=0.7, color="blue", edgecolor="black")
    ax.set_title(f"{model} Response Toxicity", fontsize=10)
    ax.set_xlabel("Response Toxicity", fontsize=9)
    ax.set_ylabel("Frequency", fontsize=9)
    ax.grid(True)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("../../results/toxic/all_models_histograms.svg", format="svg")

plt.show()

