
import joblib
import pandas as pd

from pathlib import Path
from src.preprocessing import select_features


# Get project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Model path
MODEL_PATH = BASE_DIR / "models" / "final_model.pkl"


# Load trained model
def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Model file not found: {MODEL_PATH}"
        )

    return joblib.load(MODEL_PATH)


# Make prediction
def predict_usage(input_data):

    # Convert user input into DataFrame
    input_df = pd.DataFrame([input_data])

    # Select required features
    processed_data = select_features(input_df)

    # Load model
    model = load_model()

    # Predict
    prediction = model.predict(processed_data)

    return prediction[0]


if __name__ == "__main__":

    sample_input = {
        "Daily_Usage_Hours": 6.5,
        "Sleep_Hours": 7,
        "Intellectual_Performance": 8,
        "Apps_Used_Daily": 25,
        "Phone_Checks_Per_Day": 80,
        "Time_on_Social_Media": 2.5,
        "Gaming_Usage_Ratio": 0.2,
        "Social_Media_Usage_Ratio": 0.3,
        "Non_Educational_Usage_Hours": 3,
        "Education_Usage_Ratio": 0.2
    }

    result = predict_usage(sample_input)

    print("Predicted Usage Score:", result)

