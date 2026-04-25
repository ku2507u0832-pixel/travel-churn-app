import streamlit as st
import pandas as pd
import pickle

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

st.set_page_config(page_title="Travel Churn Predictor")

st.title("🚢 Customer Travel Churn Prediction")
st.markdown("Enter details below to check if a customer will stay or leave.")

# User Inputs
age = st.slider("Age", 18, 50, 30)
services = st.selectbox("Services Opted", [1, 2, 3, 4, 5, 6])
flyer = st.radio("Frequent Flyer (0: No, 1: Yes, 2: Rare)", [0, 1, 2])
income = st.radio("Income Class (0: Low, 1: Middle, 2: High)", [0, 1, 2])
social = st.selectbox("Social Media Synced (0: No, 1: Yes)", [0, 1])
hotel = st.selectbox("Booked Hotel (0: No, 1: Yes)", [0, 1])

if st.button("Predict Churn Status"):
    # Arrange features in the exact order used during training
    features = pd.DataFrame([[age, flyer, income, services, social, hotel]], 
                           columns=['Age', 'FrequentFlyer', 'AnnualIncomeClass', 'ServicesOpted', 'AccountSyncedToSocialMedia', 'BookedHotelOrNot'])
    
    prediction = model.predict(features)
    
    if prediction[0] == 1:
        st.error("⚠️ Prediction: This customer is likely to CHURN.")
    else:
        st.success("✅ Prediction: This customer is likely to stay LOYAL.")
