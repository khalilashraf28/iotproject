import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Function to generate random sensor data
def generate_sensor_data():
    temperature = round(random.uniform(20, 35), 1)  # Temperature in °C
    humidity = round(random.uniform(30, 70), 1)     # Humidity in %
    mq2 = round(random.uniform(0, 50), 1)          # MQ2 Gas Level in %
    mq5 = round(random.uniform(0, 60), 1)          # MQ5 Gas Level in %
    mq135 = round(random.uniform(0, 70), 1)        # MQ135 Gas Level in %
    return temperature, humidity, mq2, mq5, mq135

# Generate timestamps from 2024-01-01 to 2025-01-31 (every hour)
start_date = datetime(2024, 1, 1, 0, 0, 0)
end_date = datetime(2025, 1, 31, 23, 59, 59)
timestamps = pd.date_range(start=start_date, end=end_date, freq='H')

# Create the dataset
data = []
for timestamp in timestamps:
    temperature, humidity, mq2, mq5, mq135 = generate_sensor_data()
    data.append([timestamp, temperature, humidity, mq2, mq5, mq135])

# Convert to DataFrame
df = pd.DataFrame(data, columns=["Timestamp", "Temperature (°C)", "Humidity (%)", "MQ2 (%)", "MQ5 (%)", "MQ135 (%)"])

# Save to CSV
df.to_csv("sensor_data_2024_to_2025.csv", index=False)

print("Dataset generated and saved as 'sensor_data_2024_to_2025.csv'")