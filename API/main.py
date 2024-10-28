import joblib
import pandas as pd
from flask import Flask, request, jsonify
from pydantic import ValidationError

# Load the trained machine learning model
model_filename = "../Models/fraud_model.pkl"
model = joblib.load(model_filename)

# Create a Flask instance
app = Flask(__name__)

@app.route("/", methods=["GET"])
def root():
    return {
        "message": "To use this API to predict a credit score, make a POST request to /predict with a body format of {purchase_value:float, age=int, transaction_count_per_day_x=float, transaction_velocity_past_hour=float, transaction_count_per_day_y=float, source_Ads:int, source_Direct:int, source_SEO:int, browser_Chrome:int, browser_FireFox:int, browser_IE:int, browser_Opera:int, browser_Safari:int, sex_F:int, sex_M:int, country_Albania:int} and Add other country categorical features with 0 or 1 values"
        }

# Define the prediction endpoint
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Validate and parse the incoming JSON data
        data = request.get_json(force=True)
        # Prepare the input data for prediction
        
        required_features = model.feature_names_in_
        for feature in required_features:
            if feature not in data:
                data[feature] = 0
        
        input_data_df = pd.DataFrame([data])
        
        input_data_df = input_data_df[required_features]
        
        prediction = model.predict(input_data_df)
        return jsonify({
            "message": "0: Not fraud, 1: Fraud",
            "prediction": int(prediction[0])
            }) 
    except ValidationError as e:
        return jsonify({"error": e.errors()}),400

if __name__ == "__main__":
    app.run(debug=True)