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

# Add background image
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
            <source src="https://www.fesliyanstudios.com/musicfiles/2019-09-05_-_Epic_Boss_Battle_-_David_Fesliyan.mp3" type="audio/mpeg">
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

def user_input_features():
    attribute_1 = st.sidebar.slider('Potential 🌟', 0.0, 100.0, 50.0)
    attribute_2 = st.sidebar.slider('Value in Euros 💶', 9000.0, 185500000.0, 92750000.0, step=1000000.0)
    attribute_3 = st.sidebar.slider('Wage in Euros 💰', 500.0, 560000.0, 280000.0, step=10000.0)
    attribute_4 = st.sidebar.slider('Reactions ⚡', 0.0, 100.0, 50.0)
    attribute_5 = st.sidebar.slider('Short Passing 🎯', 0.0, 100.0, 50.0)
    attribute_6 = st.sidebar.slider('Passing 🅿️', 0.0, 100.0, 50.0)
    attribute_7 = st.sidebar.slider('Dribbling 🕺', 0.0, 100.0, 50.0)
    attribute_8 = st.sidebar.slider('Composure 😌', 0.0, 100.0, 50.0)
    attribute_9 = st.sidebar.slider('Vision 👀', 0.0, 100.0, 50.0)
    attribute_10 = st.sidebar.slider('International Reputation 🌍', 0.0, 5.0, 3.0)
    attribute_11 = st.sidebar.slider('Long Passing 🎌', 0.0, 100.0, 50.0)


    data = {
        'movement_reactions': attribute_4,
        'potential': attribute_1,
        'passing': attribute_6,
        'wage_eur': attribute_3,
        'mentality_composure': attribute_8,
        'value_eur': attribute_2,
        'dribbling': attribute_7,
        'attacking_short_passing': attribute_5,
        'mentality_vision': attribute_9,
        'international_reputation': attribute_10,
        'skill_long_passing': attribute_11,
    }
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

# Display user input
st.subheader('User Input Parameters ⚙️')
st.write(input_df)

# Ensure the input features match the training data
try:
    # Scale the input data
    input_df_scaled = scaler.transform(input_df)

    # Predict and display result
    prediction = model.predict(input_df_scaled)
    st.subheader('Prediction 📊')
    st.write(f'🏅 Predicted Rating: {prediction[0]}')
except Exception as e:
    st.error(f"Error in prediction: {e}")

# Add an animation or image
st.sidebar.image("https://th.bing.com/th/id/R.6da89904177277ea98383eceff14c2db?rik=oQDCtY3dhnuOAQ&riu=http%3a%2f%2fmedia.giphy.com%2fmedia%2f120Zj5Kb5ugtRS%2fgiphy.gif&ehk=PEsT1M919HpBjlmpsYppaR1DhXp5aE%2b8NPwQHMIqXa8%3d&risl=&pid=ImgRaw&r=0", caption='Football Animation', use_column_width=True)
