# CapstoneAI-Toxicity

This is a project, that functions as Capstone for the "Engineering with AI" minor programme at the TUDelft. This project aims to characterise from a linguistic viewpoint what formulations and structures might cause generative large language models to generate toxic content.

## Table of Contents

- [Background](#background)
- [Project Plan] (docs/CapstoneAI_Porject_Plan.pdf)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Model Training](#model-training)
- [Evaluation](#evaluation)
- [References](#ceferences)
- [Contributions](#contributions)

## Background

Large Language Models (LLMs) are becoming increasingly sophisticated, producing outputs that are not only coherent but also impactful in shaping digital interactions. As these models grow in size and capability, their influence expands [1] [.

Generative AI, while impressive, operates by predicting the next word in a sequence based on patterns learned from vast datasets. This results in no true understanding of meaning or context behind its outputs. Consequently, this lack of comprehension and judgment becomes problematic when LLMs generate toxic content, as they often fail to recognize appropriate or inappropriate responses on their own. This issue becomes even more concerning in scenarios where developers, users, or stakeholders disregard the ethical implications of these outputs or fail to take responsibility for mitigating harm.

Language, being highly context-dependent, makes the identification and mitigation of toxic outputs a particularly challenging task. When characterizing these model failures, we encounter two main challenges: benchmarking toxicity and explaining why the model generates a toxic output.

Although defining toxic output through benchmarking is crucial for identifying failures, it is not sufficient for understanding the underlying causes of toxicity. Benchmarks provide representative examples of toxic content, but do not inherently explain the mechanisms behind the generation of such outputs. To address this gap, we must go beyond the benchmarks and dive into explainability techniques.

Explainable AI (XAI) has long been a vital area of research, undergoing a renaissance with works like LIME and SHAP, which provide algorithmic explanations. Despite advances in generative AI, XAI remains essential for understanding and mitigating the toxic output produced by LLM. This is particularly important because LLM outputs can often be inconsistent, overly confident, or prone to hallucinations. Given the societal impact of language toxicity, ensuring transparency in model decision making is crucial.

## Features

- **Data Preprocessing**: Tools for cleaning and preparing text data for model training.
- **Model Training**: Scripts to train machine learning models on labeled datasets.
- **Evaluation Metrics**: Functions to assess model performance using metrics like accuracy, precision, recall, and F1-score.
- **Prediction Interface**: A simple interface to input new comments and receive toxicity predictions.

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/rbithray/CapstoneAI-Toxicity.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd CapstoneAI-Toxicity
   ```

3. **Install the required packages**:

   Ensure you have [Python 3.8](https://www.python.org/downloads/release/python-380/) installed. Then, install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

After installation, you can start training the model or use a pre-trained model to make predictions.

### Training the Model

To train the model, run:

```bash
python train.py --data_path data/train.csv --model_output models/toxicity_model.pkl
```

### Making Predictions

To predict the toxicity of new comments:

```bash
python predict.py --model_path models/toxicity_model.pkl --input_text "Your comment here."
```

## Dataset

The project utilizes the [Jigsaw Toxic Comment Classification Challenge](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge) dataset, which includes thousands of comments labeled for different types of toxicity.

## Model Training

The training process involves:

1. **Data Loading**: Importing the dataset.
2. **Data Cleaning**: Removing unnecessary characters, handling missing values, and normalizing text.
3. **Feature Extraction**: Converting text into numerical features using techniques like TF-IDF.
4. **Model Selection**: Choosing appropriate machine learning algorithms (e.g., Logistic Regression, Random Forest).
5. **Training**: Fitting the model to the training data.
6. **Saving the Model**: Storing the trained model for future use.

## Evaluation

The model is evaluated using a separate validation set. Key metrics include:

- **Accuracy**: Proportion of correct predictions.
- **Precision**: Proportion of true positive predictions among all positive predictions.
- **Recall**: Proportion of true positive predictions among all actual positives.
- **F1-Score**: Harmonic mean of precision and recall.

## References

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

## Contributions

Contributing members

| Name            | Student Number |
| --------------- | -------------- |
| Wies Meijers    | 5449197        |
| Job Sanders     | 5162246        |
| Thijn Hillen    | 5639328        |
| Michiel Jurgens | 5404029        |
| Robbert Bithray | 5279119        |




