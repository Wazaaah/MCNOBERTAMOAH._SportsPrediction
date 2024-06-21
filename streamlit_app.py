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

def user_input_features():
    attribute_1 = st.sidebar.slider('Potential 🌟', 0.0, 100.0, 50.0)
    attribute_2 = st.sidebar.slider('Value in Euros 💶', 9000.0, 185500000.0, 92750000.0, step=1000000.0)
    attribute_3 = st.sidebar.slider('Wage in Euros 💰', 500.0, 560000.0, 280000.0, step=10000.0)
    attribute_4 = st.sidebar.slider('Shot Power 🔥', 0.0, 100.0, 50.0)
    attribute_5 = st.sidebar.slider('Short Passing 🎯', 0.0, 100.0, 50.0)
    attribute_6 = st.sidebar.slider('Passing 🅿️', 0.0, 100.0, 50.0)
    attribute_7 = st.sidebar.slider('Dribbling 🕺', 0.0, 100.0, 50.0)
    attribute_8 = st.sidebar.slider('Reactions ⚡', 0.0, 100.0, 50.0)
    attribute_9 = st.sidebar.slider('Composure 😌', 0.0, 100.0, 50.0)
    attribute_10 = st.sidebar.slider('Vision 👀', 0.0, 100.0, 50.0)

    data = {'movement_reactions': attribute_8,
            'mentality_composure': attribute_9,
            'passing': attribute_6,
            'potential': attribute_1,
            'dribbling': attribute_7,
            'wage_eur': attribute_3,
            'power_shot_power': attribute_4,
            'value_eur': attribute_2,
            'mentality_vision': attribute_10,
            'attacking_short_passing': attribute_5
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
