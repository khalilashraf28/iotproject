import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from plotly import graph_objects as go
import joblib
import subprocess

#  Load CSV file 
@st.cache_data
def load_user_data():
    return pd.read_csv("sensor_data_2024_to_2025.csv")  # Ensure this CSV exists with columns 'Username' and 'Password'
@st.cache_resource
def load_model(file_path):
    return joblib.load(file_path)
st.set_page_config(page_title="Air Quality Dashboard",initial_sidebar_state="collapsed")

df = load_user_data()
st.markdown("""
        <style>
        #root > div:nth-child(1) > div.withScreencast > div > div > section{
            background: linear-gradient(to right, lightcyan, skyblue);

        }
        #root > div:nth-child(1) > div.withScreencast > div > div > section > div.stMainBlockContainer > div > div > div > div:nth-child(2) > div > div > div > h1{
            text-align: center;
        }
        #root > div:nth-child(1) > div.withScreencast > div > div > section > div.stMainBlockContainer.block-container.st-emotion-cache-yw8pof.ekr3hml4 > div > div > div > div:nth-child(3) > div > div > p{
            background-color: white;
            border-radius: 10px; /* Adjust the radius value as needed */
            padding: 10px; /* Optional: adds padding for better appearance */
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); 
        }
        #root > div:nth-child(1) > div.withScreencast > div > div > section > div.stMainBlockContainer.block-container > div > div > div > div.stHorizontalBlock,
        #root > div:nth-child(1) > div.withScreencast > div > div > section > div.stMainBlockContainer.block-container > div > div > div > div:nth-child(6){
                margin-left: -200px;
                margin-right: -200px;
        }
           #root > div:nth-child(1) > div.withScreencast > div > div > section > div.stMainBlockContainer > div > div > div > div.stHorizontalBlock > div:nth-child(1) > div > div > div > div > div > div > div,
           #root > div:nth-child(1) > div.withScreencast > div > div > section > div.stMainBlockContainer > div > div > div > div.stHorizontalBlock > div:nth-child(2) > div > div > div > div > div > div > div,
           #root > div:nth-child(1) > div.withScreencast > div > div > section > div.stMainBlockContainer.block-container.st-emotion-cache-yw8pof.ekr3hml4 > div > div > div > div.st-emotion-cache-0.eiemyj5 > div > div > div > div{
                background: linear-gradient(135deg, #2b50d5, #82f573);/* Gradient with neon-like colors */
                border: none; /* Remove the border for a cleaner look */
                border-radius: 15px; /* Rounded corners */
                padding: 20px; /* Spacing inside the box */
                box-shadow: 0 4px 30px rgba(0, 0, 0, 0.2), 0 0 15px rgba(120, 115, 245, 0.7); /* Subtle shadow and neon glow */
                margin: 10px 0; /* Spacing around the box */
                font-family: 'Arial', sans-serif; /* Professional font */
                text-align: center; /* Center content */
                color: #fff; /* White text for contrast */
                text-shadow: 0 0 10px rgba(255, 255, 255, 0.8); /* Neon glow on text */
           }
           #root > div:nth-child(1) > div.withScreencast > div > div > section > div.stMainBlockContainer > div > div > div > div.stHorizontalBlock > div:nth-child(1) > div > div > div > div > div > div > div:hover,
           #root > div:nth-child(1) > div.withScreencast > div > div > section > div.stMainBlockContainer > div > div > div > div.stHorizontalBlock > div:nth-child(2) > div > div > div > div > div > div > div:hover,
           #root > div:nth-child(1) > div.withScreencast > div > div > section > div.stMainBlockContainer.block-container.st-emotion-cache-yw8pof.ekr3hml4 > div > div > div > div.st-emotion-cache-0.eiemyj5 > div > div > div > div:hover{
               background: linear-gradient(135deg, #7873f5, #ff6ec4); /* Reverse the gradient */
                box-shadow: 0 8px 40px rgba(0, 0, 0, 0.4), 0 0 30px rgba(255, 110, 196, 0.9); /* Intensify the shadow and glow */
                transform: translateY(-5px); /* Lift the box slightly */
                text-shadow: 0 0 15px rgba(255, 255, 255, 1); /* In
           }
           #root > div:nth-child(1) > div.withScreencast > div > div > section > div.stMainBlockContainer.block-container.st-emotion-cache-yw8pof.ekr3hml4 > div > div > div > div.st-emotion-cache-0.eiemyj5 > div > div > div > div > div > div{
               color:white;
           }
           #root > div:nth-child(1) > div.withScreencast > div > div > section > div.stMainBlockContainer.block-container.st-emotion-cache-yw8pof.ekr3hml4 > div > div > div > div:nth-child(6) > details{
               background-color: white;
           }
        </style>
    """, unsafe_allow_html=True)
st.title("Air Quality Dashboard")
st.write("Group Member: Muhammad Khalil Ashraf, Inshara Ahmed, Rija Javed, Muhammad Huzaifa Aslam")
col1, col2= st.columns([1,1])
with col1:
    with st.container():
        st.metric(label="TimeStamp", value=df['Timestamp'].iloc[-1])
        st.metric(label="Humidity (%)", value=df['Humidity (%)'].iloc[-1])
        st.metric(label="MQ5 (%)", value=df['MQ5 (%)'].iloc[-1])
with col2:
    with st.container():
        st.metric(label="Temperature (°C)", value=df['Temperature (°C)'].iloc[-1])
        st.metric(label="MQ2 (%)", value=df['MQ2 (%)'].iloc[-1])
        st.metric(label="MQ135 (%)", value=df['MQ135 (%)'].iloc[-1])
with st.container():
    airq = (df['MQ5 (%)'].iloc[-1]+df['MQ2 (%)'].iloc[-1]+df['MQ135 (%)'].iloc[-1])/3
    st.metric(label="Air Quality", value=airq.round())
with st.expander("Air Quality Info"):
    with st.container():
        st.write("""𝐆𝐞𝐧𝐞𝐫𝐚𝐥 𝐈𝐧𝐭𝐞𝐫𝐩𝐫𝐞𝐭𝐚𝐭𝐢𝐨𝐧 𝐟𝐨𝐫 𝐀𝐢𝐫 𝐐𝐮𝐚𝐥𝐢𝐭𝐲:\n
                \t𝐆𝐨𝐨𝐝 (0–25%): Clean air, safe for breathing.\n
                𝐌𝐨𝐝𝐞𝐫𝐚𝐭𝐞 (26–50%): Acceptable air quality; some pollutants present.\n
                𝐔𝐧𝐡𝐞𝐚𝐥𝐭𝐡𝐲 𝐟𝐨𝐫 𝐒𝐞𝐧𝐬𝐢𝐭𝐢𝐯𝐞 𝐆𝐫𝐨𝐮𝐩𝐬 (51–75%): Potential health risks for individuals with respiratory issues.\n
                𝐔𝐧𝐡𝐞𝐚𝐥𝐭𝐡𝐲 (76–100%): Poor air quality, unsafe for prolonged exposure.""")

with st.expander("last Five data"):
    with st.container():
        st.dataframe(df.tail())
with st.expander("Temperature"):        
    with st.container():
        # Load the model
        model_file = "prophet_models/Temperature (°C)_prophet_model.joblib"
        model = load_model(model_file)

        # Sidebar for user input
        st.sidebar.header("Forecast Settings")
        forecast_days = 7  

        # Generate future dates
        future_dates = pd.date_range(start=datetime.now(), periods=forecast_days, freq="D").to_frame(index=False, name="ds")

        # Main App
        st.title("Temperature Forecast")

        # Predict Temperature
        forecast = model.predict(future_dates)

        # Display Forecast
        st.write(f"Forecast for the next {forecast_days} day(s):")
        st.dataframe(forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]])

        # Create Plotly line graph
        fig = go.Figure()

        # Add forecast line
        fig.add_trace(go.Scatter(
            x=forecast["ds"],
            y=forecast["yhat"],
            mode="lines",
            name="Forecast",
            line=dict(color="blue")
        ))

        # Add uncertainty intervals using pd.concat()
        upper_lower_combined = pd.concat([forecast["ds"], forecast["ds"][::-1]])
        upper_lower_values = pd.concat([forecast["yhat_upper"], forecast["yhat_lower"][::-1]])

        fig.add_trace(go.Scatter(
            x=upper_lower_combined,
            y=upper_lower_values,
            fill="toself",
            name="Uncertainty Interval",
            line=dict(color="rgba(0,0,0,0)"),
            fillcolor="rgba(173,216,230,0.4)"
        ))

        # Update layout
        fig.update_layout(
            title="Temperature Forecast",
            xaxis_title="Date",
            yaxis_title="Temperature (%)",
            template="plotly_white"
        )

        # Show the graph in Streamlit
        st.plotly_chart(fig)        
        

with st.expander("Humidity"):        
    with st.container():
        # Load the model
        model_file = "prophet_models/Humidity (%)_prophet_model.joblib"
        model = load_model(model_file)

        # Sidebar for user input
        st.sidebar.header("Forecast Settings")
        forecast_days = 7  

        # Generate future dates
        future_dates = pd.date_range(start=datetime.now(), periods=forecast_days, freq="D").to_frame(index=False, name="ds")

        # Main App
        st.title("Humidity Forecast")
        
        # Predict humidity
        forecast = model.predict(future_dates)

        # Display Forecast
        st.write(f"Forecast for the next {forecast_days} day(s):")
        st.dataframe(forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]])

        # Create Plotly line graph
        fig = go.Figure()

        # Add forecast line
        fig.add_trace(go.Scatter(
            x=forecast["ds"],
            y=forecast["yhat"],
            mode="lines",
            name="Forecast",
            line=dict(color="blue")
        ))

        # Add uncertainty intervals using pd.concat()
        upper_lower_combined = pd.concat([forecast["ds"], forecast["ds"][::-1]])
        upper_lower_values = pd.concat([forecast["yhat_upper"], forecast["yhat_lower"][::-1]])

        fig.add_trace(go.Scatter(
            x=upper_lower_combined,
            y=upper_lower_values,
            fill="toself",
            name="Uncertainty Interval",
            line=dict(color="rgba(0,0,0,0)"),
            fillcolor="rgba(173,216,230,0.4)"
        ))

        # Update layout
        fig.update_layout(
            title="Humidity Forecast",
            xaxis_title="Date",
            yaxis_title="Humidity (%)",
            template="plotly_white"
        )

        # Show the graph in Streamlit
        st.plotly_chart(fig)
        
        
with st.expander("MQ2"):        
    with st.container():
        # Load the model
        model_file = "prophet_models/MQ2 (%)_prophet_model.joblib"
        model = load_model(model_file)

        # Sidebar for user input
        st.sidebar.header("Forecast Settings")
        forecast_days = 7  

        # Generate future dates
        future_dates = pd.date_range(start=datetime.now(), periods=forecast_days, freq="D").to_frame(index=False, name="ds")

        # Main App
        st.title("MQ2 Forecast")
        
        # Predict MQ2
        forecast = model.predict(future_dates)

        # Display Forecast
        st.write(f"Forecast for the next {forecast_days} day(s):")
        st.dataframe(forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]])

        # Create Plotly line graph
        fig = go.Figure()

        # Add forecast line
        fig.add_trace(go.Scatter(
            x=forecast["ds"],
            y=forecast["yhat"],
            mode="lines",
            name="Forecast",
            line=dict(color="blue")
        ))

        # Add uncertainty intervals using pd.concat()
        upper_lower_combined = pd.concat([forecast["ds"], forecast["ds"][::-1]])
        upper_lower_values = pd.concat([forecast["yhat_upper"], forecast["yhat_lower"][::-1]])

        fig.add_trace(go.Scatter(
            x=upper_lower_combined,
            y=upper_lower_values,
            fill="toself",
            name="Uncertainty Interval",
            line=dict(color="rgba(0,0,0,0)"),
            fillcolor="rgba(173,216,230,0.4)"
        ))

        # Update layout
        fig.update_layout(
            title="MQ2 Forecast",
            xaxis_title="Date",
            yaxis_title="MQ2 (%)",
            template="plotly_white"
        )

        # Show the graph in Streamlit
        st.plotly_chart(fig)

with st.expander("MQ5"):        
    with st.container():
        # Load the model
        model_file = "prophet_models/MQ5 (%)_prophet_model.joblib"
        model = load_model(model_file)

        # Sidebar for user input
        st.sidebar.header("Forecast Settings")
        forecast_days = 7  

        # Generate future dates
        future_dates = pd.date_range(start=datetime.now(), periods=forecast_days, freq="D").to_frame(index=False, name="ds")

        # Main App
        st.title("MQ5 Forecast")
        
        # Predict MQ5
        forecast = model.predict(future_dates)

        # Display Forecast
        st.write(f"Forecast for the next {forecast_days} day(s):")
        st.dataframe(forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]])

        # Create Plotly line graph
        fig = go.Figure()

        # Add forecast line
        fig.add_trace(go.Scatter(
            x=forecast["ds"],
            y=forecast["yhat"],
            mode="lines",
            name="Forecast",
            line=dict(color="blue")
        ))

        # Add uncertainty intervals using pd.concat()
        upper_lower_combined = pd.concat([forecast["ds"], forecast["ds"][::-1]])
        upper_lower_values = pd.concat([forecast["yhat_upper"], forecast["yhat_lower"][::-1]])

        fig.add_trace(go.Scatter(
            x=upper_lower_combined,
            y=upper_lower_values,
            fill="toself",
            name="Uncertainty Interval",
            line=dict(color="rgba(0,0,0,0)"),
            fillcolor="rgba(173,216,230,0.4)"
        ))

        # Update layout
        fig.update_layout(
            title="MQ5 Forecast",
            xaxis_title="Date",
            yaxis_title="MQ5 (%)",
            template="plotly_white"
        )

        # Show the graph in Streamlit
        st.plotly_chart(fig)

with st.expander("MQ135"):        
    with st.container():
        # Load the model
        model_file = "prophet_models/MQ135 (%)_prophet_model.joblib"
        model = load_model(model_file)

        # Sidebar for user input
        st.sidebar.header("Forecast Settings")
        forecast_days = 7  

        # Generate future dates
        future_dates = pd.date_range(start=datetime.now(), periods=forecast_days, freq="D").to_frame(index=False, name="ds")

        # Main App
        st.title("MQ135 Forecast")
        
        # Predict MQ5
        forecast = model.predict(future_dates)

        # Display Forecast
        st.write(f"Forecast for the next {forecast_days} day(s):")
        st.dataframe(forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]])

        # Create Plotly line graph
        fig = go.Figure()

        # Add forecast line
        fig.add_trace(go.Scatter(
            x=forecast["ds"],
            y=forecast["yhat"],
            mode="lines",
            name="Forecast",
            line=dict(color="blue")
        ))

        # Add uncertainty intervals using pd.concat()
        upper_lower_combined = pd.concat([forecast["ds"], forecast["ds"][::-1]])
        upper_lower_values = pd.concat([forecast["yhat_upper"], forecast["yhat_lower"][::-1]])

        fig.add_trace(go.Scatter(
            x=upper_lower_combined,
            y=upper_lower_values,
            fill="toself",
            name="Uncertainty Interval",
            line=dict(color="rgba(0,0,0,0)"),
            fillcolor="rgba(173,216,230,0.4)"
        ))

        # Update layout
        fig.update_layout(
            title="MQ135 Forecast",
            xaxis_title="Date",
            yaxis_title="MQ135 (%)",
            template="plotly_white"
        )

        # Show the graph in Streamlit
        st.plotly_chart(fig)


import sys
import os
# Function to run model.py within the virtual environment
def run_model_in_venv():
    # Define the path to the virtual environment's python executable
    venv_python = os.path.join('.venv', 'Scripts', 'python.exe') if sys.platform == 'win32' else os.path.join('.venv', 'bin', 'python')
    
    # Run model.py using the virtual environment's python
    result = subprocess.run([venv_python, 'model.py'], capture_output=True, text=True)

    # Display the output from running model.py
    if result.returncode == 0:
        st.success("Model ran successfully!")
        st.text(result.stdout)  # Display standard output
    else:
        st.error("Error running model.")
        st.text(result.stderr)  # Display error output

# Button to run model.py
if st.button('Run Model'):
    run_model_in_venv()
