import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('stacking_model.pkl')
scaler = joblib.load('scaler.pkl')

# Title of the app
st.title('⚽ Player Rating Prediction ⚽')

# Sidebar for user input
st.sidebar.header('Enter Player Attributes 🏅')


st.markdown(
    """
    <style>
    body {
        background: url('https://media.giphy.com/media/l0HlObIKcJDA8aHWM/giphy.gif');
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add a button to play the UCL anthem
if st.sidebar.button('Play UCL Anthem'):
    st.markdown(
        """
        <audio controls autoplay>
            <source src="https://raw.githubusercontent.com/username/path/to/ucl_anthem.mp3" type="audio/mpeg">
        </audio>
        """,
        unsafe_allow_html=True
    )

# Customize header and footer colors
st.markdown(
    """
    <style>
    header, footer {
        background-color: #4CAF50;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)
