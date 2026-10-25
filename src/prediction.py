import joblib
import pandas as pd
from pathlib import Path


# Get the main SmartQueue project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Paths to saved model files
MODEL_PATH = BASE_DIR / "models" / "queue_model.pkl"
FEATURES_PATH = BASE_DIR / "models" / "feature_columns.pkl"


# Load the trained Random Forest model
model = joblib.load(MODEL_PATH)

# Load the exact feature columns used during training
feature_columns = joblib.load(FEATURES_PATH)


def predict_waiting_time(
    queue_length,
    active_counters,
    avg_service_time,
    service_type,
    hour,
    day_of_week,
    is_peak_hour
):
    """
    Predict waiting time for a queue situation.
    """

    # Create input data
    data = pd.DataFrame([{
        "queue_length": queue_length,
        "active_counters": active_counters,
        "avg_service_time": avg_service_time,
        "service_type": service_type,
        "hour": hour,
        "day_of_week": day_of_week,
        "is_peak_hour": is_peak_hour
    }])

    # Convert service_type into one-hot encoded columns
    data = pd.get_dummies(
        data,
        columns=["service_type"],
        drop_first=True
    )

    # Make sure input has exactly the same columns
    # and order as the training data
    data = data.reindex(
        columns=feature_columns,
        fill_value=0
    )

    # Make prediction
    prediction = model.predict(data)[0]

    # Return prediction rounded to 2 decimal places
    return round(float(prediction), 2)