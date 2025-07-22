import streamlit as st
import joblib
import numpy as np

# Load model and features
model = joblib.load("best_model.pkl")
feature_columns = joblib.load("feature_columns.pkl")

st.title("💼 Developer Salary Predictor")

st.markdown("### Enter your details:")

age = st.slider("Age", 16, 80, 30)
ed_level = st.selectbox("Education Level", [
    'Primary school', 'Secondary school', 'Bachelor’s degree',
    'Master’s degree', 'Doctoral degree'
])
employment = st.selectbox("Employment Status", [
    'Employed full-time', 'Independent contractor', 'Student', 'Unemployed'
])
years_code_pro = st.slider("Years of Professional Coding", 0, 50, 5)
country = st.selectbox("Country", [
    'United States', 'India', 'Germany', 'United Kingdom', 'Canada', 'Other'
])
remote_work = st.selectbox("Remote Work", ['Fully remote', 'Hybrid', 'On-site'])

# Prepare input
input_data = np.array([[age, ed_level, employment, years_code_pro, country, remote_work]], dtype=object)

if st.button("Predict Salary"):
    prediction = model.predict(input_data)
    st.success(f"💰 Estimated Salary: ${int(prediction[0]):,} per year")
