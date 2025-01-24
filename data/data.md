# Data

The data used in this project has been taken from
RealToxicityPrompts [[3]](../README.md#3-realtoxicityprompts-evaluating-neural-toxic-degeneration-in-language-models).
This is a database containing `99441` prompts along with their toxicity as determined by
PerspectiveAPI [[4]](../README.md#4-a-new-generation-of-perspective-api-efficient-multilingual-character-level-transformers).
RealToxicityPrompts is widely used as a toxicity benchmark for developers to test the toxicity of their LLMs, and was
therefore found to be suitable for this project.

To get a better understanding of when LLMs generate toxic content, two subsets were generated from this large dataset.

1. 1000 randomly sampled prompts
2. 500 most toxic prompts, as scored in the dataset.

The code to import and split the data can be
found [here](https://github.com/rbithray/CapstoneAI-Toxicity/blob/a9ca84cfae292e1a89840e47da802e00071e7e34/code/import).
The json files containing the final set of prompts used in this project can be
found [here](https://github.com/rbithray/CapstoneAI-Toxicity/blob/fea604123dc5190ca9245089c50a8ac80fa5162f/data).