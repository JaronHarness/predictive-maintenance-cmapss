import joblib
import pandas as pd

# Load the model
model = joblib.load("models/final_model.pkl")

# Load feature list (same order as training)
def load_feature_columns():
    import json
    with open("models/feature_columns.json", "r") as f:
        return json.load(f)

feature_cols = load_feature_columns()

def predict_rul(input_data: dict):
    # Convert input dict to DataFrame
    df = pd.DataFrame([input_data])

    # Ensure correct column order
    df = df[feature_cols]

    # Predict
    prediction = model.predict(df)[0]

    return prediction
