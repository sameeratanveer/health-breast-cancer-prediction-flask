# 🧬 Breast Cancer Prediction Web App

This Flask-based web application predicts whether a tumor is **cancerous** or **not cancerous** using a pre-trained logistic regression model based on user input features.

---


---

## Overview

Breast cancer is one of the most common forms of cancer in women worldwide. Early detection significantly improves the chances of recovery. This app provides a simple interface where users can input tumor features and get an instant prediction on whether the tumor is likely **cancerous (malignant)** or **not cancerous (benign)**.

---

##  Tech Stack

| Technology     | Description                     |
|----------------|---------------------------------|
| Python         | Core programming language       |
| Flask          | Web framework for backend       |
| HTML/CSS       | Frontend design                 |
| scikit-learn   | Model training and serialization|
| NumPy, Pandas  | Data manipulation               |
| Joblib         | For model loading               |

---

## Model Details

- **Algorithm Used**: Logistic Regression
- **Dataset**: Breast Cancer Wisconsin (Diagnostic) Dataset from [UCI ML Repository](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic))
- **Features Used**:
  - radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, etc.
- **Target**:
  - 1: Cancerous (Malignant)
  - 0: Not Cancerous (Benign)

---

## Input Format

The application accepts comma-separated feature values in the following order:

| Feature Index | Feature Name       | Description                          |
|---------------|--------------------|--------------------------------------|
| 1             | radius_mean        | Mean of distances from center to points on the perimeter |
| 2             | texture_mean       | Standard deviation of gray-scale values |
| 3             | perimeter_mean     | Mean size of the core tumor          |
| ...           | ...                | ...                                  |
| N             | feature_n          | Additional features as used in model |

📝 **Note**: You must enter **all required features** in the same order, separated by commas.

