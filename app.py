import streamlit as st
import requests
API = "http://127.0.0.1:8000"
st.set_page_config(page_title="Smart Agriculture", layout="wide")
st.title("🌱 Smart Agriculture System")
st.subheader("Add Sensor Data")
temp = st.number_input("Temperature")
hum = st.number_input("Humidity")
soil = st.number_input("Soil Moisture")
if st.button("Send Data"):
requests.post(f"{API}/sensors/", json={
"temperature": temp,
"humidity": hum,
"soil_moisture": soil
})
st.success("Sensor data sent")
if st.button("AI Crop Recommendation"):
r = requests.post(f"{API}/ai/recommend", params={
"temperature": temp,
"humidity": hum,
"soil_moisture": soil
})
st.success(f"Recommended Crop: {r.json()['recommended_crop']}")