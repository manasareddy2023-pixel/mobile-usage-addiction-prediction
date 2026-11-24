
import streamlit as st
import sys
from pathlib import Path

# Add project root to Python path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from src.predict import predict_usage


# Page configuration
st.set_page_config(
    page_title="Mobile Usage Addiction Prediction",
    page_icon="📱",
    layout="centered"
)

# Application title
st.title("📱 Mobile Usage Prediction")

st.write(
    "Enter your mobile usage details "
    "to predict the usage score."
)

st.divider()

# User input section
st.subheader("Enter Your Details")

col1, col2 = st.columns(2)

with col1:
    daily_usage = st.number_input(
        "Daily Usage Hours",
        min_value=0.0,
        value=6.5,
        step=0.5
    )

    sleep_hours = st.number_input(
        "Sleep Hours",
        min_value=0.0,
        value=7.0,
        step=0.5
    )

    intellectual_performance = st.number_input(
        "Intellectual Performance",
        value=8.0
    )

    apps_used = st.number_input(
        "Apps Used Daily",
        min_value=0,
        value=25
    )

    phone_checks = st.number_input(
        "Phone Checks Per Day",
        min_value=0,
        value=80
    )

with col2:
    social_media_time = st.number_input(
        "Time on Social Media",
        min_value=0.0,
        value=2.5,
        step=0.5
    )

    gaming_ratio = st.number_input(
        "Gaming Usage Ratio",
        min_value=0.0,
        value=0.2
    )

    social_media_ratio = st.number_input(
        "Social Media Usage Ratio",
        min_value=0.0,
        value=0.3
    )

    non_educational_hours = st.number_input(
        "Non Educational Usage Hours",
        min_value=0.0,
        value=3.0
    )

    education_ratio = st.number_input(
        "Education Usage Ratio",
        min_value=0.0,
        value=0.2
    )


# Prediction button
if st.button("Predict Usage Score", type="primary"):

    user_input = {
        "Daily_Usage_Hours": daily_usage,
        "Sleep_Hours": sleep_hours,
        "Intellectual_Performance": intellectual_performance,
        "Apps_Used_Daily": apps_used,
        "Phone_Checks_Per_Day": phone_checks,
        "Time_on_Social_Media": social_media_time,
        "Gaming_Usage_Ratio": gaming_ratio,
        "Social_Media_Usage_Ratio": social_media_ratio,
        "Non_Educational_Usage_Hours": non_educational_hours,
        "Education_Usage_Ratio": education_ratio
    }

    try:
        prediction = predict_usage(user_input)

        st.success("Prediction Completed!")

        st.metric(
            label="Predicted Usage Score",
            value=f"{prediction:.3f}"
        )

    except Exception as e:
        st.error(f"Prediction Error: {e}")
