from flask import Flask, render_template, request
import numpy as np # type: ignore
import joblib # type: ignore

app = Flask(__name__)

# Load models
rf_hour_model = joblib.load("rf_hour_model.pkl")
rf_day_model = joblib.load("rf_day_model.pkl")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # All input values from the form
        season = float(request.form['season'])
        yr = float(request.form['yr'])
        mnth = float(request.form['mnth'])
        hr = float(request.form['hr'])
        holiday = float(request.form['holiday'])
        weekday = float(request.form['weekday'])
        workingday = float(request.form['workingday'])
        weathersit = float(request.form['weathersit'])
        temp = float(request.form['temp'])
        atemp = float(request.form['atemp'])
        hum = float(request.form['hum'])
        windspeed = float(request.form['windspeed'])

        # For hourly prediction (with hr)
        features_hour = np.array([
            season, yr, mnth, hr, holiday, weekday,
            workingday, weathersit, temp, atemp, hum, windspeed
        ]).reshape(1, -1)

        # For daily prediction (without hr)
        features_day = np.array([
            season, yr, mnth, holiday, weekday,
            workingday, weathersit, temp, atemp, hum, windspeed
        ]).reshape(1, -1)

        # Predictions
        hourly_pred = int(rf_hour_model.predict(features_hour)[0])
        daily_pred = int(rf_day_model.predict(features_day)[0])

        return render_template('index.html',
                               hourly_prediction=hourly_pred,
                               daily_prediction=daily_pred)

    except Exception as e:
        return f"Error: {e}"
