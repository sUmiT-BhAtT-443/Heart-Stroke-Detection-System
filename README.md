# 🧠 Heart Stroke Detection System

A machine learning–based web application that predicts stroke risk based on user health information.  
The project focuses on **practical healthcare decision-making**, handling **imbalanced data**, and providing a **probability-based risk score** instead of a simple yes/no result.

🔗 **Live Demo:**  
👉 https://heart-stroke-detection-system-fiz2kam2pvh3rc6fnhabaq.streamlit.app/

---

## 📌 Project Overview

The Heart Stroke Detection System allows users to enter basic health and lifestyle details such as:
- Age group
- Blood pressure condition
- Heart disease status
- Glucose level
- BMI
- Smoking habits
- Work and residence type

Based on these inputs, the system predicts the **stroke risk level** along with a **risk percentage**, helping users understand how risky the situation might be.

The application is built using **Machine Learning + Streamlit** and is deployed as a **live web dashboard**.

---

## 🎯 Key Features

- 🖥️ Interactive and user-friendly dashboard
- 🧪 Machine learning–based prediction
- 📊 Probability-based risk score
- ⚖️ Handles imbalanced healthcare data
- 🚫 No pre-filled inputs (real user interaction)
- 🌐 Deployed as a live web application

---

## 🧠 Machine Learning Approach

- **Dataset:** Healthcare Stroke Dataset  
- **Problem Type:** Binary Classification (Stroke / No Stroke)
- **Challenge:** Highly imbalanced data (stroke cases are rare)

### Model Used
- **Random Forest Classifier**
- Class imbalance handled during training
- Probability-based thresholding used for safer predictions

### Why Random Forest?
- Works well with mixed features
- Captures non-linear relationships
- More reliable for healthcare risk prediction

Instead of only relying on accuracy, the model focuses on **recall and safety**, ensuring that high-risk cases are not missed.

---

## 🧹 Data Preprocessing & EDA

- Removed unnecessary columns
- Handled missing values (BMI)
- Encoded categorical features
- Grouped age into meaningful ranges
- Performed Exploratory Data Analysis (EDA) to understand:
  - Age vs stroke relationship
  - Impact of glucose level, hypertension, and heart disease
  - Lifestyle patterns affecting stroke risk

---

## 🖼️ Application Screenshots

### 🔹 Dashboard View 1
![Dashboard View 1](Dashboard_view1.png)

### 🔹 Dashboard View 2
![Dashboard View 2](Dashboard_view2.png)

### 🔹 Main Dashboard View
![Main Dashboard View](Main_Dashboard_View.png)

> *(Make sure these image files are uploaded to the repository root with the same names.)*

---

## 🛠️ Tech Stack

- **Python**
- **Pandas, NumPy**
- **Scikit-learn**
- **Imbalanced-learn (SMOTE)**
- **Streamlit**
- **Joblib**
- **Matplotlib & Seaborn**

---

## 🚀 Deployment

The application is deployed using **Streamlit Cloud** and is accessible via a live URL:

👉 https://heart-stroke-detection-system-fiz2kam2pvh3rc6fnhabaq.streamlit.app/

---

## 📚 Learning Outcomes

- Handling imbalanced datasets
- Feature engineering for healthcare data
- Probability-based ML predictions
- Building and deploying ML dashboards
- Applying machine learning in real-world healthcare scenarios

---

## 👨‍💻 Author

**Sumit Bhatt**  
Machine Learning & Data Analytics Enthusiast  

---

## ⚠️ Disclaimer

This project is for **educational purposes only** and should not be used as a medical diagnostic tool. Always consult a medical professional for health-related decisions.
