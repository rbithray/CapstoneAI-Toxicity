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
- [Research Questions](#research-questions)
  - [Research Question 1](docs/RQ1.md)
  - [Research Question 2](docs/RQ2.md)
- [Dataset](#dataset)
- [Tools](#tools)
- [Ethics](docs/Ethical_Reflection_Capstone.pdf)
- [Conclusion](docs/conclusion.md)
- [Discussion](docs/discussion)
- [References](#references)
- [File structure](#file-structure)

## Background

Large Language Models (LLMs) are becoming increasingly sophisticated, producing outputs that are not only coherent but also impactful in shaping digital interactions. As these models grow in size and capability, their influence expands [[1]](#1-language-models-are-general-purpose-interfaces).

Generative AI, while impressive, operates by predicting the next word in a sequence based on patterns learned from vast datasets. This results in no true understanding of meaning or context behind its outputs. Consequently, this lack of comprehension and judgment becomes problematic when LLMs generate toxic content, as they often fail to recognize appropriate or inappropriate responses on their own. This issue becomes even more concerning in scenarios where developers, users, or stakeholders disregard the ethical implications of these outputs or fail to take responsibility for mitigating harm.

Language, being highly context-dependent, makes the identification and mitigation of toxic outputs a particularly challenging task. When characterizing these model failures, we encounter two main challenges: benchmarking toxicity and explaining why the model generates a toxic output.

Although defining toxic output through benchmarking is crucial for identifying failures, it is not sufficient for understanding the underlying causes of toxicity. Benchmarks provide representative examples of toxic content, but do not inherently explain the mechanisms behind the generation of such outputs. To address this gap, we must go beyond the benchmarks and dive into explainability techniques.

Explainable AI (XAI) has long been a vital area of research, undergoing a renaissance with works like LIME and SHAP,
which provide algorithmic explanations. Despite advances in generative AI, XAI remains essential for understanding and
mitigating the toxic output produced by LLM. This is particularly important because LLM outputs can often be
inconsistent, overly confident, or prone to hallucinations. Given the societal impact of language toxicity, ensuring
transparency in model decision-making is crucial.



## Research Questions

This projects aims to answer the following research questions:

1. How prone are Mistral, llama3, Gemma, and BLOOM to generate toxic outputs when prompted?
2. What are lexical features of prompts that lead Mistral, llama3, Gemma, and BLOOM to generate toxic outputs?
3. Which syntactic structures of prompts lead the three selected LLMs to generate toxic outputs?

The approach and results for the research question can be found here: [RQ1](docs/RQ1.md), [RQ2](docs/RQ2.md). For RQ3,
more information can be found in [Discussion](docs/discussion)

## Dataset

This project relies on data from
RealToxicityPrompts [[3]](#3-realtoxicityprompts-evaluating-neural-toxic-degeneration-in-language-models). More
information on what and how this data was used can be found in [data](data/data.md).

***
## Tools

This project uses `python 3.12` for [RQ1](docs/RQ1.md), and `python 3.10` for [RQ2](docs/RQ2.md). More information on
the specific libraries used are listed in [code](code/code.md).

## Ethical Reflection

As the project concerns toxicity in the in- and outputs of LLMs ethical consideration is a necessity. We reflected on
ethical implications of our product and potential implications if research on this topic is expanded. We believe that
the most important ethics of our product is discussed, however, we encourage a constant ethical reflection during future
research. The ethical reflection of the project and its process can be found here [add link](
docs/Ethical_Reflection_Capstone_.

## Conclusion

The conclusion for this project can be found [here](docs/conclusion.md)

## Discussion

The discussion can be found [here](docs/discussion).

---
## References

### 1. Language Models are General-Purpose Interfaces
- **Authors**: Yaru Hao, Haoyu Song, Li Dong, Shaohan Huang, Zewen Chi, Wenhui Wang, Shuming Ma, Furu Wei  
- **Year**: 2022  
- **arXiv ID**: [2206.06336](https://arxiv.org/abs/2206.06336)  
- **Primary Class**: cs.CL  

---

### 2. DecodingTrust: A Comprehensive Assessment of Trustworthiness in GPT Models
- **Authors**: Boxin Wang, Weixin Chen, Hengzhi Pei, Chulin Xie, Mintong Kang, Chenhui Zhang, Chejian Xu, Zidi Xiong, Ritik Dutta, Rylan Schaeffer, et al.  
- **Year**: 2024  
- **arXiv ID**: [2306.11698](https://arxiv.org/abs/2306.11698)  
- **Primary Class**: cs.CL  

---

### 3. RealToxicityPrompts: Evaluating Neural Toxic Degeneration in Language Models
- **Authors**: Samuel Gehman, Suchin Gururangan, Maarten Sap, Yejin Choi, Noah A. Smith  
- **Year**: 2020  
- **arXiv ID**: [2009.11462](https://arxiv.org/abs/2009.11462)  
- **Primary Class**: cs.CL  

---

### 4. A New Generation of Perspective API: Efficient Multilingual Character-level Transformers
- **Authors**: Alyssa Lees, Vinh Q. Tran, Yi Tay, Jeffrey Sorensen, Jai Gupta, Donald Metzler, Lucy Vasserman  
- **Year**: 2022  
- **arXiv ID**: [2202.11176](https://arxiv.org/abs/2202.11176)  
- **Primary Class**: cs.CL  

---

### 5. Mixtral of Experts
- **Authors**: Albert Q. Jiang, Alexandre Sablayrolles, Antoine Roux, Arthur Mensch, Blanche Savary, Chris Bamford, et al.  
- **Year**: 2024  
- **arXiv ID**: [2401.04088](https://arxiv.org/abs/2401.04088)  
- **Primary Class**: cs.LG  

---

### 6. The Llama 3 Herd of Models
- **Authors**: Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, et al.  
- **Year**: 2024  
- **arXiv ID**: [2407.21783](https://arxiv.org/abs/2407.21783)  
- **Primary Class**: cs.AI  

---

### 7. Gemma: Open Models Based on Gemini Research and Technology
- **Authors**: Gemma Team, Thomas Mesnard, Cassidy Hardin, Robert Dadashi, Surya Bhupatiraju, Shreya Pathak, et al.  
- **Year**: 2024  
- **arXiv ID**: [2403.08295](https://arxiv.org/abs/2403.08295)  
- **Primary Class**: cs.CL  

---

### 8. BLOOM: A 176B-Parameter Open-Access Multilingual Language Model
- **Authors**: BigScience Workshop, Teven Le Scao, Angela Fan, Christopher Akiki, Ellie Pavlick, Suzana Ilić, et al.  
- **Year**: 2023  
- **arXiv ID**: [2211.05100](https://arxiv.org/abs/2211.05100)  
- **Primary Class**: cs.CL  

---

### 9. Captum: A Unified and Generic Model Interpretability Library for PyTorch
- **Authors**: Narine Kokhlikyan, Vivek Miglani, Miguel Martin, Edward Wang, Bilal Alsallakh, Jonathan Reynolds, Alexander Melnikov, Natalia Kliushkina, Carlos Araya, Siqi Yan, et al.  
- **Year**: 2020  
- **arXiv ID**: [2009.07896](https://arxiv.org/abs/2009.07896)

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


