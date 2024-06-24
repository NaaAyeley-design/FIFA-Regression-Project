#!/usr/bin/env python
# coding: utf-8

# In[8]:


import streamlit as st
import pandas as pd
import joblib

# Load the trained model
#model = joblib.load("C:\Users\nayel\Downloads\model.pkl")
model = joblib.load(r"C:\Users\nayel\Downloads\model.pkl")


# Define the function for prediction
def predict_rating(input_data):
    input_df = pd.DataFrame([input_data], columns=input_data.keys())
    prediction = model.predict(input_df)
    # Assuming the model doesn't provide confidence scores; remove this if it does
    return prediction[0]

# Set up the Streamlit interface
st.title("FIFA Player Rating Prediction")

st.write("""
         ## Predict a FIFA player's overall rating based on their profile.
         """)

# Input fields for the player's profile
movement_reactions = st.slider('Movement Reactions', 0, 100, 50)
passing = st.slider('Passing', 0, 100, 50)
wage_eur = st.number_input('Wage (EUR)', min_value=0, value=5000)
value_eur = st.number_input('Value (EUR)', min_value=0, value=100000)
dribbling = st.slider('Dribbling', 0, 100, 50)
attacking_short_passing = st.slider('Attacking Short Passing', 0, 100, 50)
mentality_vision = st.slider('Mentality Vision', 0, 100, 50)
international_reputation = st.slider('International Reputation', 1, 5, 1)

# Collect all input/s
input_data = {
    'movement_reactions': movement_reactions,
    'passing': passing,
    'wage_eur': wage_eur,
    'value_eur': value_eur,
    'dribbling': dribbling,
    'attacking_short_passing': attacking_short_passing,
    'mentality_vision': mentality_vision,
    'international_reputation': international_reputation,
}

# Button for prediction
if st.button('Predict Rating'):
    rating = predict_rating(input_data)
    st.write(f"Predicted Overall Rating: {rating}")

