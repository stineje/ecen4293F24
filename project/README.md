# Project Title: Basic Machine Learning Project on FASHION-mnist Dataset

## Overview
In this project, you will [brief description of project goals, e.g., "build a machine learning model to classify images from the MNIST dataset"]. The project will help you understand [key concepts, e.g., "data preprocessing, model training, and evaluation metrics"].

## Objectives
- Understand and preprocess the dataset.
- Develop a neural network model for classification.
- Train and evaluate the model.
- Analyze and interpret the results.

## Requirements
- Python 3.10 or higher
- Jupyter Notebook or VS Code
- Libraries:
  - NumPy
  - Pandas
  - Matplotlib
  - PyTorch 
  - Scikit-learn
  - jupyterlab

## Setup Instructions
1. Clone the project repository:
   ```bash
   git clone https://github.com/stineje/ecen4293F24
   ```
2. Install the necessary libraries:
   ```bash
   cd ./ecen4293F24/project
   pip install -r requirements.txt
   ```
3. Open the Jupyter Notebook:
   ```bash
   jupyter notebook project-name.ipynb
   ```
   or use VS-code built in jupyter editor

## Project Tasks
### 1. Data Loading and Preprocessing
- Load the [fashion-mnist](https://openml.org/search?type=data&status=active&id=40996) dataset and inspect the data.
- Perform any necessary preprocessing steps, such as normalization or encoding.

### 2. Model Building
- Use Sklearn premade models for classification tasks
- Define a neural network model with at least two hidden layers.
- Choose an appropriate activation function and output layer.

### 3. Model Training
- Set up a training loop to optimize your model.
- Track and display training loss for each epoch.

### 4. Model Evaluation
- Evaluate your model on the test set using appropriate metrics (e.g., accuracy, precision, recall).
- Generate a confusion matrix and discuss the results.

### 5. Analysis and Discussion
- Analyze the performance of your model.
- Identify any potential improvements or limitations.

## Important Links
- [NumPy Documentation](https://numpy.org/doc/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [PyTorch Documentation](https://pytorch.org/)
- [Scikit Learn](https://scikit-learn.org/stable/api/index.html)

## Submission Guidelines
1. Complete all tasks in the provided Jupyter Notebook.
2. Save and export your notebook as a PDF:
   - In Jupyter Notebook, go to **File > Download as > PDF via LaTeX** (if available).
3. Submit the PDF and notebook file (.ipynb) through [submission portal, e.g., Canvas].

## Grading Criteria
- **Data Preprocessing**: 20%
- **Model Building**: 30%
- **Model Training**: 20%
- **Model Evaluation and Analysis**: 20%
- **Code Quality and Documentation**: 10%

## Checklist

- [ ] Step 0: Install all necessary libraries
- [ ] Step 1: Import Libraries and Load Dataset
- [ ] Step 2: Explore the dataset
- [ ] Step 3: Preprocess and normalize the data
- [ ] Step 4: Split the data into test and training
- [ ] Step 5: Baseline model with scikit-learn
- [ ] Step 6: Evaluate the baseline model
- [ ] Step 7: Convert the data to PyTorch tensors
- [ ] Step 8: Create DataLoaders
- [ ] Step 9: Define the custom NN with PyTorch
- [ ] Step 10: Train your NN
- [ ] Step 11: Visualize the training loss
- [ ] Step 12: Evaluate the NN model
- [ ] Step 13: Create a confusion matrix
- [ ] Step 14: Visualize classification vectors of custom NN
- [ ] Step 15: Repeat steps 7-14 for CNN
- [ ] Step 16: Convert data to tensors
- [ ] Step 17: Create DataLoaders
- [ ] Step 18: Define simple CNN model
- [ ] Step 19: Train CNN
- [ ] Step 20: Visualize the training loss
- [ ] Step 21: Evaluate the CNN model
- [ ] Step 22: Create a confusion matrix
- [ ] Step 23: Visualize the classification vectors
- [ ] Step 24: Display the feature maps for CNN
- [ ] Step 25: Compare and contrast prebuilt models vs your custom models


Good luck, and feel free to ask questions if you need help!
