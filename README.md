# SmartQueue – Smart Queue Waiting-Time Prediction System

SmartQueue is a machine learning project developed to estimate the waiting time of students in a college service queue. It uses queue details such as the number of people waiting, active counters, average service time, and service type to predict the expected waiting time.

The project also provides queue status, feature importance analysis, and a What-If Analysis feature to compare estimated waiting times under different queue conditions.

The current version uses a synthetic dataset created for this project and an interactive web interface built with Streamlit.

## Features

- **Waiting-Time Prediction:** Estimate waiting time from queue information.
- **Queue Status:** Categorize the estimated wait as Low, Moderate, or High.
- **What-If Analysis:** Compare estimated waiting times under different active-counter scenarios.
- **Factor Analysis:** Display feature importance from the trained model.
- **Data Visualization:** Explore patterns and relationships in the dataset.
- **Interactive Web App:** Use a Streamlit interface to enter inputs and view results.

## Technologies Used

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook
- Git and GitHub

## Dataset

The project uses a synthetic dataset of 5,000 records with eight columns:

- `queue_length`
- `active_counters`
- `avg_service_time`
- `service_type`
- `hour`
- `day_of_week`
- `is_peak_hour`
- `waiting_time` — the prediction target in minutes

The dataset is generated using `src/generate_dataset.py` and saved to `data/raw/queue_data.csv`.

## Machine Learning

This is a regression problem. The models evaluated include:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

Evaluation metrics include MAE, MSE, RMSE, and R². Random Forest performed best in the current experiment on the synthetic dataset. These results do not establish real-world predictive accuracy.

## Project Structure

```text
SmartQueue/
├── app/
│   └── app.py
├── data/
│   ├── raw/
│   └── processed/
├── images/
├── models/
├── notebooks/
│   └── 01_data_understanding.ipynb
├── src/
│   ├── analysis.py
│   ├── generate_dataset.py
│   └── prediction.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/khushi-baviskar/smartqueue-wait-time-prediction.git
cd smartqueue-wait-time-prediction
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

On Windows Command Prompt, activate it with:

```cmd
.venv\Scripts\activate.bat
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Generate the dataset if needed

```bash
python src/generate_dataset.py
```

### 5. Run the application

Make sure the trained model and feature-column files exist in `models/`, then run:

```bash
python -m streamlit run app/app.py
```

Open the local URL shown in the terminal, usually `http://localhost:8501`.

## How to Use

1. Start the Streamlit application.
2. Enter the queue details, service type, time, and peak-hour information.
3. Click **Predict Waiting Time**.
4. Review the estimated waiting time and queue status.
5. Use **What-If Analysis** to compare estimates for different numbers of active counters.
6. Review the feature-importance chart.

## Limitations

- The dataset is synthetic and does not represent measured college queue data.
- Predictions are estimates, not guarantees.
- Feature importance describes model reliance, not proof of causation.
- Real-world use requires representative observations and further validation.

## Future Enhancements

- Collect real queue data.
- Validate and retrain the model on real observations.
- Add live queue monitoring.
- Improve features and evaluate additional models.
- Deploy the application online.

## Author

**Khushi Baviskar**

## License

For educational and academic purposes.
