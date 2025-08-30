from flask import Flask, request, render_template
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load model and selected features
model = joblib.load('xgb_model.pkl')
selected_features = joblib.load('selected_features.pkl')

# Function to format Indian currency
def format_indian_currency(value):
    if value >= 1e7:
        return f"₹ {round(value / 1e7, 2)} Crores"
    elif value >= 1e5:
        return f"₹ {round(value / 1e5, 2)} Lakhs"
    else:
        return f"₹ {round(value):,}"


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST','GET'])
def predict():
    try:
        # Collect data from form
        input_data = {feature: float(request.form[feature]) for feature in selected_features}
        
        # Create DataFrame
        input_df = pd.DataFrame([input_data])

        # Predict
        log_prediction = model.predict(input_df)
        prediction = np.expm1(log_prediction)  # Convert log-scale back to original

        # Format prediction
    #    formatted_prediction = format_indian_currency(prediction[0])
        prediction_value = round(prediction[0] / 1e5, 2)

        # Return result
        return render_template('index.html', prediction=prediction_value)

    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
