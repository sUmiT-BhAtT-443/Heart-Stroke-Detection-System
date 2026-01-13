import streamlit as st
import pandas as pd
import joblib
import os

# PAGE CONFIG
st.set_page_config(
    page_title="Stroke Prediction App",
    layout="centered"
)

# UI HEADER
st.title("🧠 Heart Stroke Detection App")
st.write("Enter patient details to predict stroke risk")

# LOAD MODEL & COLUMNS
if not os.path.exists("stroke_model.pkl") or not os.path.exists("model_columns.pkl"):
    st.error("❌ Model or columns file not found")
    st.stop()

model = joblib.load("stroke_model.pkl")
columns = joblib.load("model_columns.pkl")

# Safety check
if not hasattr(model, "predict_proba"):
    st.error("❌ Loaded object is not a valid ML model")
    st.write("Loaded object type:", type(model))
    st.stop()

# USER INPUTS 
gender = st.selectbox(
    "Gender",
    ["Select Gender", "Male", "Female", "Other"]
)

age_group = st.selectbox(
    "Age Group",
    ["Select Age Group", "0-12", "13-19", "20-30", "31-60", "61+"]
)

hypertension = st.selectbox(
    "Hypertension",
    ["Select Option", "No", "Yes"]
)

heart_disease = st.selectbox(
    "Heart Disease",
    ["Select Option", "No", "Yes"]
)

ever_married = st.selectbox(
    "Ever Married",
    ["Select Option", "No", "Yes"]
)

work_type = st.selectbox(
    "Work Type",
    ["Select Work Type", "Private", "Self-employed", "Govt_job", "children", "Never_worked"]
)

residence = st.selectbox(
    "Residence Type",
    ["Select Residence", "Urban", "Rural"]
)

avg_glucose = st.number_input(
    "Average Glucose Level",
    min_value=50.0,
    max_value=300.0,
    value=120.0
)

bmi = st.number_input(
    "BMI",
    min_value=10.0,
    max_value=60.0,
    value=25.0
)

smoking = st.selectbox(
    "Smoking Status",
    ["Select Smoking Status", "never smoked", "formerly smoked", "smokes", "Unknown"]
)

# VALIDATION 
if st.button("🔍 Predict Stroke Risk"):

    if "Select" in [
        gender, age_group, hypertension, heart_disease,
        ever_married, work_type, residence, smoking
    ]:
        st.warning("⚠️ Please select all fields before prediction")
        st.stop()

    # ENCODING (SAME AS TRAINING)
    gender_map = {"Male": 1, "Female": 0, "Other": 2}
    age_map = {"0-12": 0, "13-19": 1, "20-30": 2, "31-60": 3, "61+": 4}
    binary_map = {"No": 0, "Yes": 1}
    work_map = {
        "Private": 0,
        "Self-employed": 1,
        "children": 2,
        "Govt_job": 3,
        "Never_worked": 4
    }
    res_map = {"Urban": 1, "Rural": 0}
    smoke_map = {
        "never smoked": 1,
        "formerly smoked": 0,
        "smokes": 2,
        "Unknown": 3
    }

    input_data = {
        "gender": gender_map[gender],
        "age": age_map[age_group],
        "hypertension": binary_map[hypertension],
        "heart_disease": binary_map[heart_disease],
        "ever_married": binary_map[ever_married],
        "work_type": work_map[work_type],
        "Residence_type": res_map[residence],
        "avg_glucose_level": avg_glucose,
        "bmi": bmi,
        "smoking_status": smoke_map[smoking]
    }

    input_df = pd.DataFrame([input_data])
    input_df = input_df.reindex(columns=columns, fill_value=0)

    # PREDICTION
    prob = model.predict_proba(input_df)[0][1]
    risk_percent = prob * 100

    st.markdown("---")
    st.subheader("🩺 Stroke Risk Assessment Result")

    if prob >= 0.30:
        st.markdown(
            f"""
            <div style="background-color:#3b0f0f;
                        padding:20px;
                        border-radius:10px;
                        border-left:6px solid red;">
                <h4 style="color:#ff4b4b;">⚠️ Elevated Stroke Risk Detected</h4>
                <p style="color:white;">
                    The entered health parameters indicate a <b>higher likelihood of stroke</b>.
                </p>
                <p style="color:white;"><b>Estimated Risk:</b> {risk_percent:.2f}%</p>
                <p style="color:#ffb3b3;">
                    Recommendation: Clinical evaluation is advised.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div style="background-color:#0f2f1f;
                        padding:20px;
                        border-radius:10px;
                        border-left:6px solid #00c853;">
                <h4 style="color:#00e676;">✅ Low Stroke Risk Observed</h4>
                <p style="color:white;">
                    The entered health parameters suggest a <b>lower likelihood of stroke</b>.
                </p>
                <p style="color:white;"><b>Estimated Risk:</b> {risk_percent:.2f}%</p>
                <p style="color:#b9f6ca;">
                    Recommendation: Maintain a healthy lifestyle.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
