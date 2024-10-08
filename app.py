from flask import Flask, render_template, request
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load('electricity_price_prediction_model.pkl')

# Define USD to INR conversion rate
USD_TO_INR = 83  # You can update this value if needed

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the data from the form
        forecast_wind = float(request.form['forecast_wind'])
        system_load_ea = float(request.form['system_load_ea'])
        temperature = float(request.form['temperature'])
        windspeed = float(request.form['windspeed'])
        co2_intensity = float(request.form['co2_intensity'])
        actual_wind = float(request.form['actual_wind'])
        system_load_ep2 = float(request.form['system_load_ep2'])

        # Prepare the input for the model (it expects a 2D array)
        features = np.array([[forecast_wind, system_load_ea, temperature, windspeed, 
                              co2_intensity, actual_wind, system_load_ep2]])

        # Make prediction
        prediction_usd = model.predict(features)[0]

        # Convert USD to INR
        prediction_inr = prediction_usd * USD_TO_INR

        return render_template('index.html', prediction_usd=prediction_usd, prediction_inr=prediction_inr)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)