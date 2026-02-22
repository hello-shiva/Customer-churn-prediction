import streamlit as st
import joblib
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "models", "churn_model.pkl")


model = joblib.load(model_path)

st.title("Customer Churn Prediction")

tenure=st.number_input("Tenure")
monthly_charges = st.number_input("Monthly Charges")

if st.button("Predict"):
    input_data = np.array([[tenure,monthly_charges]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.write("Customer is likely to Churn")
    else:
        st.write("Customer is likely to stay")