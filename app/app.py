import sys
from pathlib import Path

import streamlit as st

# Allow Python to find the src folder
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from src.prediction import predict_waiting_time
from src.analysis import get_feature_importance


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="SmartQueue",
    page_icon="⏳",
    layout="wide"
)


# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("⏳ SmartQueue")
st.subheader("Smart Queue Waiting-Time Prediction System")

st.write(
    "Enter the current queue information to estimate the expected "
    "waiting time."
)


# --------------------------------------------------
# Input section
# --------------------------------------------------

st.header("Queue Information")

col1, col2 = st.columns(2)

with col1:
    queue_length = st.number_input(
        "Queue Length",
        min_value=0,
        max_value=100,
        value=20,
        step=1
    )

    active_counters = st.number_input(
        "Active Counters",
        min_value=1,
        max_value=10,
        value=2,
        step=1
    )

    avg_service_time = st.number_input(
        "Average Service Time (minutes)",
        min_value=1.0,
        max_value=30.0,
        value=5.0,
        step=0.5
    )

    service_type = st.selectbox(
        "Service Type",
        [
            "Fee Payment",
            "Scholarship",
            "Document Verification",
            "Bonafide Certificate",
            "Exam Form",
            "ID Card",
            "Enquiry"
        ]
    )


with col2:
    hour = st.number_input(
        "Current Hour",
        min_value=9,
        max_value=17,
        value=12,
        step=1
    )

    day_of_week = st.selectbox(
        "Day of Week",
        [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
        ]
    )

    day_number = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6
    }

    day_of_week_value = day_number[day_of_week]

    is_peak_hour = st.selectbox(
        "Peak Hour?",
        ["Yes", "No"]
    )

    peak_value = 1 if is_peak_hour == "Yes" else 0


# --------------------------------------------------
# Prediction
# --------------------------------------------------

# --------------------------------------------------
# Prediction
# --------------------------------------------------

if st.button("🔮 Predict Waiting Time", width="stretch"):

    waiting_time = predict_waiting_time(
        queue_length,
        active_counters,
        avg_service_time,
        service_type,
        hour,
        day_of_week_value,
        peak_value
    )

    st.success("Prediction generated successfully!")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Estimated Waiting Time",
            f"{waiting_time} minutes"
        )

    with col2:
        if waiting_time <= 15:
            queue_status = "🟢 Low"
        elif waiting_time <= 30:
            queue_status = "🟡 Moderate"
        else:
            queue_status = "🔴 High"

        st.metric(
            "Queue Status",
            queue_status
        )
    

# --------------------------------------------------
# What-If Analysis
# --------------------------------------------------

st.header("🔄 What-If Analysis")

st.write(
    "Explore how changing the number of active counters "
    "may affect the estimated waiting time."
)

what_if_counters = st.slider(
    "What if the number of active counters is:",
    min_value=1,
    max_value=10,
    value=active_counters,
    step=1
)

what_if_waiting_time = predict_waiting_time(
    queue_length,
    what_if_counters,
    avg_service_time,
    service_type,
    hour,
    day_of_week_value,
    peak_value
)

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Current Estimated Waiting Time",
        f"{waiting_time if 'waiting_time' in locals() else predict_waiting_time(queue_length, active_counters, avg_service_time, service_type, hour, day_of_week_value, peak_value)} minutes"
    )

with col2:
    st.metric(
        "What-If Estimated Waiting Time",
        f"{what_if_waiting_time} minutes"
    )
# --------------------------------------------------
# Factor Analysis
# --------------------------------------------------

st.header("📊 Waiting-Time Factor Analysis")

feature_importance = get_feature_importance()

st.dataframe(
    feature_importance,
    width="stretch"
)

st.bar_chart(
    feature_importance.set_index("feature")["importance"],
    horizontal=True
)


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    "SmartQueue uses a machine-learning model to estimate waiting time. "
    "Predictions are model-based estimates and may differ from actual waiting times."
)