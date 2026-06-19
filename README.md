# ✈️ Airline Passenger Satisfaction Prediction System

## 📌 Business Domain
Aviation & Customer Experience Analytics

## ❓ Problem Statement
Airlines receive thousands of customer feedback records but struggle to identify passengers likely to be dissatisfied. This limits proactive service improvements and customer retention.

## 🎯 Objective
Build a Machine Learning model that predicts passenger satisfaction based on travel details, service ratings, and flight experience attributes.

## 📊 Data Overview

![Airline Passenger Satisfaction](https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction)

- 📁 Dataset Size: 103,904 records
- 🔢 Features: 26 input variables
- 🎯 Target Variable: `satisfaction`
- 🧩 Key Features:
  - Passenger demographics
  - Flight distance & travel class
  - Wi-Fi, seat comfort, cleanliness
  - Online booking & boarding experience
  - Delay-related metrics
- ⚙️ Engineered Features:
  - Total Delay
  - Delayed Flight
  - Average Service Rating
  - Long Haul Indicator

## 🛠️ Tech Stack
- 🐍 Python
- 📊 Pandas, NumPy
- 📈 Matplotlib, Seaborn
- 🤖 Scikit-Learn
- 🚀 Streamlit
- 💾 Pickle

## 📂 Folder Structure
```text
📦 Airline-Passenger-Satisfaction-Prediction-System
│
├── 📁 data
│   ├── train.csv
│   ├── test.csv
│   └── processed_data.csv
│
├── 📁 notebooks
│   ├── Data Analysis.ipynb
│   └── Model Training & Evaluation.ipynb
│
├── 📁 models
│   └── passenger_satisfaction_model.pkl
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 🔄 End-to-End Workflow & Approach
1. 📥 Data Collection & Understanding
2. 🧹 Data Cleaning & Preprocessing
3. 🔍 Exploratory Data Analysis (EDA)
4. 🏗️ Feature Engineering
5. ✂️ Train-Test Split
6. 🤖 Model Training
7. 🎯 Hyperparameter Tuning
8. 📊 Performance Evaluation
9. 💾 Model Serialization
10. 🌐 Streamlit Deployment

## 📈 Models Evaluated
- Logistic Regression
- KNN
- Decision Tree
- Random Forest
- Gradient Boosting
- AdaBoost
- SVM

## 🏆 Result Summary

✅ Gradient Boosting was selected as the final model after evaluating multiple machine learning algorithms and performing hyperparameter tuning.

### Final Model Performance
- 🎯 Accuracy: 94.23%
- 🔍 Precision: 94.30%
- 📈 Recall: 92.25%
- ⚖️ F1-Score: 93.26%
- 📊 ROC-AUC: 98.82%

### Why Gradient Boosting?
- Handles complex non-linear relationships effectively.
- Provides strong generalization on unseen passenger data.
- Delivers balanced Precision and Recall.
- Suitable for customer satisfaction prediction tasks where prediction quality is more important than training speed.

## 🚀 Business Impact
The model enables airlines to proactively identify dissatisfied passengers, improve service quality, reduce customer churn, and make data-driven decisions to enhance the overall travel experience.