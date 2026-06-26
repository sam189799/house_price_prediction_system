import streamlit as st
import pickle
import pandas as pd

# Load Model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🏠 House Price Prediction")

st.write("Enter house details:")

MedInc = st.number_input("Median Income", value=3.0)
HouseAge = st.number_input("House Age", value=20.0)
AveRooms = st.number_input("Average Rooms", value=5.0)
AveBedrms = st.number_input("Average Bedrooms", value=1.0)
Population = st.number_input("Population", value=1000.0)
AveOccup = st.number_input("Average Occupancy", value=3.0)
Latitude = st.number_input("Latitude", value=34.0)
Longitude = st.number_input("Longitude", value=-118.0)

if st.button("Predict Price"):

    data = pd.DataFrame([[
        MedInc,
        HouseAge,
        AveRooms,
        AveBedrms,
        Population,
        AveOccup,
        Latitude,
        Longitude
    ]], columns=[
        'MedInc',
        'HouseAge',
        'AveRooms',
        'AveBedrms',
        'Population',
        'AveOccup',
        'Latitude',
        'Longitude'
    ])

    prediction = model.predict(data)

    st.success(
        f"Predicted House Value: ${prediction[0]*100000:.2f}"
    )