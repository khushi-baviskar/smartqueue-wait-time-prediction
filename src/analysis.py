import joblib
from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "queue_model.pkl"
FEATURES_PATH = BASE_DIR / "models" / "feature_columns.pkl"

model = joblib.load(MODEL_PATH)
feature_columns = joblib.load(FEATURES_PATH)


def get_feature_importance():
    """
    Return model feature importance as a DataFrame.
    """

    importance = pd.Series(
        model.feature_importances_,
        index=feature_columns
    ).sort_values(ascending=False)

    result = importance.reset_index()

    result.columns = ["feature", "importance"]

    return result