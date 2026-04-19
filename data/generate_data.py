import os
import numpy as np
import pandas as pd

np.random.seed(42)

n = 5000

data = pd.DataFrame({
    "hour": np.random.randint(0, 24, n),
    "day": np.random.randint(1, 31, n),
    "month": np.random.randint(1, 13, n),
    "day_of_week": np.random.randint(0, 7, n),
    "temperature": np.random.uniform(10, 40, n),
    "humidity": np.random.uniform(20, 90, n),
    "wind_speed": np.random.uniform(0, 10, n)
})

data["is_weekend"] = data["day_of_week"].apply(lambda x: 1 if x >= 5 else 0)

daily_pattern = 3 * np.sin((data["hour"] - 8) / 24 * 2 * np.pi)
seasonal_effect = data["month"].apply(lambda x: 2 if x in [5, 6, 7] else 0)
weekend_effect = data["is_weekend"].apply(lambda x: -1 if x == 1 else 0)

temp_effect = 0.4 * data["temperature"]
humidity_effect = 0.1 * data["humidity"]
wind_effect = -0.2 * data["wind_speed"]

noise = np.random.normal(0, 1.5, n)

data["energy_consumption"] = (
    daily_pattern +
    seasonal_effect +
    weekend_effect +
    temp_effect +
    humidity_effect +
    wind_effect +
    noise
)

data = data.round(2)

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(base_dir, "data", "energy_data.csv")

data.to_csv(file_path, index=False)

print("✅ Dataset saved at:", file_path)
print(data.head())