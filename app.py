from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app)

# Load model
model = joblib.load("heart_model.pkl")

# Define feature columns (must match training data order)
FEATURES = ['age','sex','cp','trestbps','chol','fbs','restecg',
            'thalach','exang','oldpeak','slope','ca','thal']

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json  # Expecting JSON input
        df = pd.DataFrame([data], columns=FEATURES)
        prediction = model.predict(df)[0]
        prob = model.predict_proba(df)[0][1]
        return jsonify({
            "prediction": int(prediction),
            "probability": float(prob)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Add a root route for health check/homepage
@app.route("/")
def home():
    return "Heart Disease Prediction API is running. Use /predict endpoint for predictions."

if __name__ == "__main__":
    app.run(debug=True, port=5000)

