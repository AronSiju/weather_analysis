import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open("model.pkl", "rb"))
le = pickle.load(open("encoder.pkl", "rb"))

st.title("🌤️ Weather Prediction App")

temp = st.number_input("Temperature")
humidity = st.number_input("Humidity")
wind = st.number_input("Wind Speed")
precip = st.number_input("Precipitation -d(%)")
pressure = st.number_input("Atmospheric Pressure")

if st.button("Predict"):
    data = {
        "Temperature": temp,
        "Humidity": humidity,
        "Wind Speed": wind,
        "Precipitation (%)": precip,
        "Atmospheric Pressure": pressure
    }

    input_df = pd.DataFrame([data])
    prediction = model.predict(input_df)
    result = le.inverse_transform(prediction)
    weather = result[0]

    

    st.markdown("---")
    st.subheader(f"Prediction: {weather}")

    if weather == "Sunny":
        st.success("☀️ Sunny")
    elif weather == "Rainy":
        st.info("🌧️ Rainy")
    elif weather == "Cloudy":
        st.warning("☁️ Cloudy")
    else:
        st.success(f"🌤️ {weather}")