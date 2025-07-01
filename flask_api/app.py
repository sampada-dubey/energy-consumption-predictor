from flask import Flask, render_template, request, jsonify
import requests
import joblib
import numpy as np
import pandas as pd

# Initialize the Flask App
app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')

# Function to get weather data
def get_weather_data(location):
    api_key = "a181a62a126d8ca5b77ebaf0ead541e6"
    geo_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"

    geo_response = requests.get(geo_url)
    geo_data = geo_response.json()

    if geo_response.status_code == 200:
        lat = geo_data['coord']['lat']
        lon = geo_data['coord']['lon']

        weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()

        if weather_response.status_code == 200:
            temperature = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']

            return {
                'temperature': temperature,
                'humidity': humidity,
                'wind_speed': wind_speed
            }
    return None

# Prediction Route
@app.route('/predict', methods=['POST'])
def predict():
    location = request.form.get('location', 'Delhi')

    # Get weather data
    weather_data = get_weather_data(location)
    if weather_data is None:
        return jsonify({"error": "Could not fetch weather data. Please check the location or try again."})

    # User inputs
    hour = int(request.form.get('hour', 14))
    day = int(request.form.get('day', 18))
    month = int(request.form.get('month', 4))
    day_of_week = int(request.form.get('day_of_week', 4))
    is_weekend = int(request.form.get('is_weekend', 0))

    # Weather inputs
    temperature = weather_data['temperature']
    humidity = weather_data['humidity']
    wind_speed = weather_data['wind_speed']

    # Prepare feature vector (make sure it matches model training!)
    columns = ['hour', 'day', 'month', 'day_of_week', 'is_weekend','temperature', 'humidity', 'wind_speed']
    features = pd.DataFrame([[hour, day, month, day_of_week, is_weekend, temperature, humidity, wind_speed]],
                        columns=columns)
    # Predict
    prediction = model.predict(features)
    predicted_value = round(prediction[0], 2)

    # Friendly message
    message = f"🔋 Predicted Energy Consumption for {location}: {predicted_value} kWh ⚡"

    return render_template('result.html', prediction=predicted_value, location=location, message=message)

# Home page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)