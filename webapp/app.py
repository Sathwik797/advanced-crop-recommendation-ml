# Streamlit app code will go here
import streamlit as st
import numpy as np
import joblib

model = joblib.load('models/crop_model.pkl')

st.title("🌾 Crop Recommendation System")
st.markdown("Enter your soil and climate values:")

features = ['N', 'P', 'K', 'Temperature', 'Humidity', 'pH', 'Rainfall']
user_inputs = []

for feature in features:
    value = st.number_input(f"{feature}:", value=0.0)
    user_inputs.append(value)

if st.button("Predict Crop"):
    prediction = model.predict([np.array(user_inputs)])
    st.success(f"✅ Recommended Crop: *{prediction[0]}*")