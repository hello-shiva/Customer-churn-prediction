*📊 Customer Churn Prediction Project*

An end-to-end Machine Learning project that predicts whether a telecom customer is likely to churn. The goal is to help businesses identify at-risk customers and take proactive retention actions.

🚀 Problem Statement

Customer churn directly impacts company revenue. Identifying customers who are likely to leave allows companies to offer retention strategies and reduce financial loss.

This project builds a classification model to predict customer churn using customer service and billing data.

🛠️ Tech Stack

Python

Pandas & NumPy

Scikit-learn

Logistic Regression

Random Forest

Streamlit

Git & GitHub

🔎 Workflow

Data Cleaning and Preprocessing

Handling Missing Values

One-Hot Encoding

Train-Test Split

Model Training with Class Balancing

Threshold Tuning

Model Evaluation (Precision, Recall, F1-score, ROC AUC)

Deployment using Streamlit

📈 Model Performance

ROC AUC Score: 0.85

Improved Recall from 0.31 → 0.61 using threshold tuning

Balanced precision-recall tradeoff for business impact

💡 Business Insight

In churn prediction, recall is especially important because missing a churn customer results in revenue loss. The model is tuned to improve churn detection while maintaining acceptable precision.

🖥️ How to Run the Project

Clone the repository

Create and activate virtual environment

Install dependencies:

pip install -r requirements.txt

Run Streamlit app:

streamlit run app/app.py
📌 Future Improvements

Hyperparameter tuning

Full preprocessing pipeline integration

Feature importance visualization

Advanced model comparison

👨‍💻 Author

Shivam Kumar
BTech CSE | Data Science Enthusiast | Data Science
