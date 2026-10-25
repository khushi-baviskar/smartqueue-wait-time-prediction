import pandas as pd
import numpy as np

# Make results reproducible
np.random.seed(42)

# Number of records
n = 5000

# -----------------------------
# Generate basic queue features
# -----------------------------

queue_length = np.random.randint(0, 41, n)

active_counters = np.random.randint(1, 6, n)

avg_service_time = np.random.uniform(2, 10, n)

service_types = [
    "Fee Payment",
    "Scholarship",
    "Document Verification",
    "Bonafide Certificate",
    "Exam Form",
    "ID Card",
    "Enquiry"
]

service_type = np.random.choice(service_types, n)

hour = np.random.randint(9, 18, n)

day_of_week = np.random.randint(0, 7, n)

# Peak hours: 11 AM–1 PM and 3 PM–4 PM
is_peak_hour = (
    ((hour >= 11) & (hour <= 13)) |
    ((hour >= 15) & (hour <= 16))
).astype(int)

# -----------------------------
# Generate waiting time
# -----------------------------

service_effect = {
    "Fee Payment": 2,
    "Scholarship": 5,
    "Document Verification": 4,
    "Bonafide Certificate": 3,
    "Exam Form": 5,
    "ID Card": 3,
    "Enquiry": 1
}

service_effect_values = np.array(
    [service_effect[x] for x in service_type]
)

# Main waiting-time relationship
waiting_time = (
    2
    + (queue_length * avg_service_time / active_counters)
    + (is_peak_hour * 5)
    + service_effect_values
    + np.random.normal(0, 4, n)
)

# Waiting time cannot be negative
waiting_time = np.maximum(waiting_time, 1)

# -----------------------------
# Create DataFrame
# -----------------------------

df = pd.DataFrame({
    "queue_length": queue_length,
    "active_counters": active_counters,
    "avg_service_time": np.round(avg_service_time, 2),
    "service_type": service_type,
    "hour": hour,
    "day_of_week": day_of_week,
    "is_peak_hour": is_peak_hour,
    "waiting_time": np.round(waiting_time, 2)
})

# -----------------------------
# Save dataset
# -----------------------------

output_path = "data/raw/queue_data.csv"

df.to_csv(output_path, index=False)

print("SmartQueue dataset created successfully!")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")
print(f"Saved to: {output_path}")

print("\nFirst 5 rows:")
print(df.head())