import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Stock Prediction System", layout="wide")

st.title("📈 Stock Market Prediction & Recommendation System")

# Sidebar
st.sidebar.header("Options")
option = st.sidebar.selectbox("Select Feature", ["Prediction", "Recommendation"])

# ------------------- PREDICTION -------------------
if option == "Prediction":
    st.header("📈 Stock Price Prediction (LSTM Output)")

    stock = st.selectbox("Select Stock", ["Reliance", "Tata Motors", "Meta"])

    if st.button("Show Prediction"):
        if stock == "Reliance":
            st.image("assets/Reliance_Prediction.png")
        elif stock == "Tata Motors":
            st.image("assets/TataMotors_Prediction.png")
        elif stock == "Meta":
            st.image("assets/Meta_Prediction.png")

# ------------------- RECOMMENDATION -------------------
elif option == "Recommendation":
    st.header("📊 Stock Recommendation")

    rec_type = st.radio("Choose Recommendation Type", ["Growth", "Similarity"])

    if rec_type == "Growth":
        st.image("assets/growth_recommendation.png")

    elif rec_type == "Similarity":
        st.image("assets/similarity_recommendation.png")