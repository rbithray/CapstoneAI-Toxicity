# CapstoneAI-Toxicity

> [!Warning]
> Due to the nature of this project, this repo contains toxic and potentially offensive language that may be harmful or distressing.  

This is a project, that functions as Capstone for the "Engineering with AI" minor programme at the TUDelft. The aim of this project is to systematically characterise toxicity in Language Models (LLMs), with a focus
on understanding when and why toxic outputs are generated. By combining benchmarking techniques
with explainability methods, this work seeks to provide a clearer picture of the conditions under which
LLMs fail and the underlying mechanisms driving these failures.

## Table of Contents

- [Background](#background)
- [Project Plan](docs/CapstoneAI_Project_Plan.pdf)
- [Research Question 1](#research-question-1)
- [Research Question 2](#research-question-2)

- [Tools](#tools)
  * [Required Libraries](#required-libraries)
  * [APIs and Tokens](#apis-and-tokens)
  * [Dataset](#dataset)
- [References](#references)
- [Contributions](#contributions)
- [File structure](#file-structure)

## Background

Large Language Models (LLMs) are becoming increasingly sophisticated, producing outputs that are not only coherent but also impactful in shaping digital interactions. As these models grow in size and capability, their influence expands [[1]].

Generative AI, while impressive, operates by predicting the next word in a sequence based on patterns learned from vast datasets. This results in no true understanding of meaning or context behind its outputs. Consequently, this lack of comprehension and judgment becomes problematic when LLMs generate toxic content, as they often fail to recognize appropriate or inappropriate responses on their own. This issue becomes even more concerning in scenarios where developers, users, or stakeholders disregard the ethical implications of these outputs or fail to take responsibility for mitigating harm.

Language, being highly context-dependent, makes the identification and mitigation of toxic outputs a particularly challenging task. When characterizing these model failures, we encounter two main challenges: benchmarking toxicity and explaining why the model generates a toxic output.

Although defining toxic output through benchmarking is crucial for identifying failures, it is not sufficient for understanding the underlying causes of toxicity. Benchmarks provide representative examples of toxic content, but do not inherently explain the mechanisms behind the generation of such outputs. To address this gap, we must go beyond the benchmarks and dive into explainability techniques.

Explainable AI (XAI) has long been a vital area of research, undergoing a renaissance with works like LIME and SHAP, which provide algorithmic explanations. Despite advances in generative AI, XAI remains essential for understanding and mitigating the toxic output produced by LLM. This is particularly important because LLM outputs can often be inconsistent, overly confident, or prone to hallucinations. Given the societal impact of language toxicity, ensuring transparency in model decision making is crucial.



## Research Questions

This projects aims to answer the following research questions:

1. How prone are Mistral, llama3, Gemma, and BLOOM to generate toxic outputs when prompted?
2. What are lexical features of prompts that lead Mistral, llama3, Gemma, and BLOOM to generate toxic outputs?
3. Which syntactic structures of prompts lead the three selected LLMs to generate toxic outputs?



***
## Tools


### Required Libraries


### APIs and Tokens


### Dataset
[Decoding Trust][2] is a project aimed at providing a thorough assessment of trustworthiness in Generative Pretrained Transformer (GPT) models. The project provides datasets to test models on a variety of aspects of trustworthiness, including toxicity. The prompts concerning toxicity are a subset of [RealToxicityPrompts][3]. The dataset consists of prompts, along with their toxicity score, calculated using [PerspectiveAPI][4], a widely used toxicity-scoring tool developed by Google Jigsaw. This data will be used in this project to analyse models, as well as to analyse the features in prompts that solicit toxic responses.

## Usage

After installation, you can start training the model or use a pre-trained model to make predictions.



## Dataset




## References

```
[1]: https://arxiv.org/abs/2206.06336 "Language Models are General-Purpose Interfaces"
[2]: https://arxiv.org/abs/2306.11698 "DecodingTrust: A Comprehensive Assessment of Trustworthiness in GPT Models"
[3]: https://arxiv.org/abs/2009.11462 "RealToxicityPrompts: Evaluating Neural Toxic Degeneration in Language Models"
[4]: https://arxiv.org/abs/2202.11176 "A New Generation of Perspective API: Efficient Multilingual Character-level Transformers"
[5]: https://arxiv.org/abs/2401.04088 "Mixtral of Experts"
[6]: https://arxiv.org/abs/2407.21783 "The Llama 3 Herd of Models"
[7]: https://arxiv.org/abs/2403.08295 "Gemma: Open Models Based on Gemini Research and Technology"
[8]: https://arxiv.org/abs/2211.05100 "BLOOM: A 176B-Parameter Open-Access Multilingual Language Model"
[9]: https://arxiv.org/abs/2310.06825 "Mistral 7B"
[10]: https://arxiv.org/abs/2009.07896 "Captum: A unified and generic model interpretability library for PyTorch"
```
## Contributions

Contributing members

| Name            | Student Number |
| --------------- | -------------- |
| Wies Meijers    | 5449197        |
| Job Sanders     | 5162246        |
| Thijn Hillen    | 5639328        |
| Michiel Jurgens | 5404029        |
| Robbert Bithray | 5279119        |



***
## File Structure

```aiignore
CapstoneAI-Toxicity
├── code
│   ├── import
│   ├── llms
│   ├── postprocess
│   └── scoring
├── data
│   ├── random
│   └── toxic
├── docs
└── figures
    ├── distributions
    ├── random
    └── toxic
```


