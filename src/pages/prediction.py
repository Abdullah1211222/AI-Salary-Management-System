import streamlit as st
import pandas as pd
import joblib
from pathlib import Path


def show_prediction(df):

    st.title("🤖 AI Salary Prediction")

    st.write("Enter employee details to predict the expected salary.")

    # ----------------------------
    # Load Trained Model
    # ----------------------------

    BASE_DIR = Path(__file__).resolve().parents[2]

    model_path = BASE_DIR / "models" / "salary_model.pkl"

    if not model_path.exists():

        st.error("❌ Trained model not found. Please train the model first.")

        return

    model = joblib.load(model_path)

    # ----------------------------
    # User Inputs
    # ----------------------------

    job_title = st.selectbox(
        "Job Title",
        sorted(df["job_title"].unique())
    )

    experience_years = st.number_input(
        "Experience (Years)",
        min_value=0,
        max_value=50,
        value=5
    )

    education_level = st.selectbox(
        "Education Level",
        sorted(df["education_level"].unique())
    )

    skills_count = st.number_input(
        "Skills Count",
        min_value=0,
        max_value=100,
        value=5
    )

    industry = st.selectbox(
        "Industry",
        sorted(df["industry"].unique())
    )

    company_size = st.selectbox(
        "Company Size",
        sorted(df["company_size"].unique())
    )

    location = st.selectbox(
        "Location",
        sorted(df["location"].unique())
    )

    remote_work = st.selectbox(
        "Remote Work",
        sorted(df["remote_work"].unique())
    )

    certifications = st.number_input(
        "Certifications",
        min_value=0,
        max_value=20,
        value=0
    )

    # ----------------------------
    # Prediction
    # ----------------------------

    if st.button("💰 Predict Salary"):

        input_data = pd.DataFrame({
            "job_title": [job_title],
            "experience_years": [experience_years],
            "education_level": [education_level],
            "skills_count": [skills_count],
            "industry": [industry],
            "company_size": [company_size],
            "location": [location],
            "remote_work": [remote_work],
            "certifications": [certifications]
        })

        prediction = model.predict(input_data)[0]

        st.success(f"💰 Predicted Salary: ${prediction:,.2f}")

        st.balloons()