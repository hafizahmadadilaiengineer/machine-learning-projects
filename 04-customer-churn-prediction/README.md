# 📞 Customer Churn Prediction System

A professional Machine Learning web application that predicts whether a telecom customer is likely to churn based on customer demographics, subscribed services, and billing information.

The project uses the **IBM Telco Customer Churn Dataset**, a **Gradient Boosting Classifier**, and an interactive **Streamlit** dashboard with a modern user interface.

---

# 🚀 Live Demo

🔗 **Streamlit App:** *(Add your deployed Streamlit link here)*

🔗 **GitHub Repository:** https://github.com/hafizahmadadilaiengineer/machine-learning-projects

---

# 📌 Project Overview

Customer churn is one of the biggest challenges for subscription-based businesses.

This project predicts customer churn using machine learning so companies can identify high-risk customers and take proactive retention actions.

The application provides:

- Customer churn prediction
- Churn probability
- Model confidence score
- Business recommendation
- Interactive dashboard
- Professional UI

---

# 🎯 Problem Statement

Telecommunication companies lose significant revenue when customers discontinue their services.

The objective of this project is to build a machine learning system capable of predicting customer churn before it happens.

---

# 👥 Target Users

- Telecom Companies
- Business Analysts
- Data Scientists
- Machine Learning Engineers
- Students learning Classification

---

# 📂 Dataset

**Dataset Name**

IBM Telco Customer Churn Dataset

Dataset contains information such as:

- Customer demographics
- Services subscribed
- Internet service
- Contract type
- Billing information
- Payment methods
- Customer churn status

Dataset Size:

- **Rows:** 7,043
- **Columns:** 50

Target Variable:

```
Churn Label
```

---

# 🛠 Tech Stack

### Programming

- Python

### Machine Learning

- Scikit-Learn
- Gradient Boosting Classifier

### Data Analysis

- Pandas
- NumPy

### Visualization

- Matplotlib
- Seaborn

### Web Application

- Streamlit

### Model Serialization

- Joblib

---

# 📁 Project Structure

```text
04-customer-churn-prediction
│
├── data
│   ├── raw
│   └── processed
│
├── models
│   └── churn_prediction_model.pkl
│
├── notebooks
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   └── 03_model_training.ipynb
│
├── screenshots
│
├── src
│   ├── train.py
│   └── predict.py
│
├── ui
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📊 Exploratory Data Analysis

Performed:

- Dataset inspection
- Missing value analysis
- Duplicate checking
- Feature distributions
- Correlation analysis
- Churn distribution
- Outlier analysis

---

# ⚙ Data Preprocessing

Performed:

- Missing value handling
- Removed unnecessary columns
- Removed data leakage columns
- Label Encoding
- Feature Scaling
- Train/Test Split

---

# 🤖 Models Trained

The following models were evaluated:

| Model | Accuracy |
|---------|----------|
| Gradient Boosting | **96.38%** |
| Random Forest | 95.67% |
| Decision Tree | 94.61% |
| Logistic Regression | 79.28% |

### ✅ Best Model

**Gradient Boosting Classifier**

Chosen because it achieved the highest overall performance on the test dataset.

---

# 📈 Model Performance

**Accuracy**

```
96.38%
```

The application also displays:

- Prediction
- Churn Probability
- Confidence Score
- Business Recommendation

---

# 💻 Application Features

- Professional dashboard
- Modern UI
- Customer Information Form
- Services Section
- Billing Section
- Summary Cards
- Loading Indicator
- Prediction Confidence
- Recommendation Engine
- Responsive Layout

---

# 📸 Screenshots

## Home Page

(Add Screenshot)

---

## Customer Information

(Add Screenshot)

---

## Prediction Result

(Add Screenshot)

---

## Churn Prediction

(Add Screenshot)

---

## About Section

(Add Screenshot)

---

# ▶ Installation

Clone the repository

```bash
git clone https://github.com/hafizahmadadilaiengineer/machine-learning-projects.git
```

Go to project folder

```bash
cd 04-customer-churn-prediction
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run application

```bash
streamlit run app.py
```

---

# 📌 Future Improvements

- SHAP Explainability
- Feature Importance Dashboard
- Customer Retention Suggestions
- Download Prediction Report
- Batch Prediction using CSV
- Docker Support
- Cloud Deployment with CI/CD
- Database Integration

---

# 🎓 Learning Outcomes

Through this project, I learned:

- Classification Algorithms
- Gradient Boosting
- Data Cleaning
- Feature Engineering
- Model Evaluation
- Streamlit Development
- Professional Project Structure
- Git & GitHub Workflow

---

# 👨‍💻 Author

**Hafiz Ahmad Adil**

MS Computer Science

AI Engineer (Aspiring)

Founder — Learn with Adil

GitHub

https://github.com/hafizahmadadilaiengineer

LinkedIn

https://www.linkedin.com/in/hafizahmadadildurrani

---

# ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.