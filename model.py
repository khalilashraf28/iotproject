import pandas as pd
from prophet import Prophet
import joblib  # For saving models
import os
df = pd.read_csv('sensor_data_2024_to_2025.csv')
# Convert 'Timestamp' to datetime format
df['Timestamp'] = pd.to_datetime(df['Timestamp'], format='%m/%d/%Y %H:%M')

# List of columns to forecast
target_columns = ['Temperature (°C)', 'Humidity (%)', 'MQ2 (%)', 'MQ5 (%)', 'MQ135 (%)']
# Directory to save models
model_dir = 'prophet_models'
os.makedirs(model_dir, exist_ok=True)  # Create directory if it doesn't exist

# Dictionary to store forecasts
forecasts = {}

# Loop through each target variable
for column in target_columns:
    print(f"Forecasting {column}...")
    
    # Prepare the data for Prophet
    df_prophet = df[['Timestamp', column]].rename(columns={'Timestamp': 'ds', column: 'y'})
    
    # Initialize and fit the Prophet model
    model = Prophet()
    model.fit(df_prophet)
    
    # Create future DataFrame for predictions
    future = model.make_future_dataframe(periods=365)  # Forecast 365 days into the future
    
    # Make predictions
    forecast = model.predict(future)
    
    # Store the forecast in the dictionary
    forecasts[column] = forecast
    
    # Save the model to disk
    model_filename = os.path.join(model_dir, f'{column}_prophet_model.joblib')
    joblib.dump(model, model_filename)
    print(f"Model for {column} saved to {model_filename}")

# Access forecasts for each variable
for column, forecast in forecasts.items():
    print(f"Forecast for {column}:")
    print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())