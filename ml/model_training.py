import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import numpy as np
import os

# Load the dataset
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(base_dir, 'data', 'energy_data.csv')

# Try reading the CSV file
try:
    df = pd.read_csv(file_path)
    print("CSV loaded successfully.")
except Exception as e:
    print("Failed to load CSV:", e)
    exit()

# Check columns
print("📊 Available columns:", df.columns)

# Step 1: Convert types (optional, for safety)
df['temperature'] = df['temperature'].astype(float)
df['humidity'] = df['humidity'].astype(float)
df['wind_speed'] = df['wind_speed'].astype(float)

# Step 2: Define features and target
features = ['hour', 'day', 'month', 'day_of_week', 'is_weekend', 'temperature', 'humidity', 'wind_speed']
target = 'energy_consumption'

X = df[features]
y = df[target]

# Step 3: Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 5: Evaluate the model
y_pred = model.predict(X_test)
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# Step 6: Save the model
joblib.dump(model, 'model.pkl')
print("Model saved successfully as model.pkl")