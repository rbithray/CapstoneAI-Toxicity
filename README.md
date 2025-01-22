# CapstoneAI-Toxicity

CapstoneAI-Toxicity is a machine learning project aimed at detecting toxic comments in online discussions. This repository contains the code and resources necessary to train and evaluate models for identifying various types of toxicity, including threats, obscenity, insults, and identity-based hate.

## Table of Contents

- [Background](#background)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Model Training](#model-training)
- [Evaluation](#evaluation)
- [Contributing](#contributing)
- [License](#license)

## Background

Online platforms often struggle with managing toxic comments that can harm user experience and community health. This project leverages machine learning techniques to automatically detect and classify such comments, facilitating better content moderation.

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

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure that your code adheres to the project's coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

*Note: This README is generated based on the typical structure of a machine learning project for toxicity detection. Please customize it to align with the specific details and structure of your project.* 