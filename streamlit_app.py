import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('stacking_model.pkl')
scaler = joblib.load('scaler.pkl')

# Set the title of the Streamlit app
st.title('⚽ Player Rating Prediction ⚽')

# Sidebar for user input
st.sidebar.header('Enter Player Attributes 🏅')


# Function to get user input for player attributes via sliders
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
    attribute_12 = st.sidebar.slider('Shot Power 💥', 0.0, 100.0, 50.0)
    attribute_13 = st.sidebar.slider('Physic 💪', 0.0, 100.0, 50.0)
    attribute_14 = st.sidebar.slider('Age 🎂', 15, 45, 30)
    attribute_15 = st.sidebar.slider('Ball Control 🏀', 0.0, 100.0, 50.0)
    attribute_16 = st.sidebar.slider('Left Defensive Midfielder (LDM) 🛡️', 0.0, 100.0, 50.0)
    attribute_17 = st.sidebar.slider('Right Defensive Midfielder (RDM) 🛡️', 0.0, 100.0, 50.0)
    attribute_18 = st.sidebar.slider('Central Defensive Midfielder (CDM) 🛡️', 0.0, 100.0, 50.0)
    attribute_19 = st.sidebar.slider('Right Midfielder (RM) 🎽', 0.0, 100.0, 50.0)
    attribute_20 = st.sidebar.slider('Left Wing Back (LWB) 🏃‍♂️', 0.0, 100.0, 50.0)

    # Create a dictionary to store the input data
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
        'ldm': attribute_16,
        'rdm': attribute_17,
        'cdm': attribute_18,
        'power_shot_power': attribute_12,
        'rm': attribute_19,
        'physic': attribute_13,
        'age': attribute_14,
        'skill_ball_control': attribute_15,
        'lwb': attribute_20
    }

    # Convert the dictionary to a DataFrame
    features = pd.DataFrame(data, index=[0])
    return features

# Get the user input
input_df = user_input_features()

# Display user input
st.subheader('User Input Parameters ⚙️')
st.write(input_df)

# Ensure the input features match the training data
try:
    # Scale the input data
    input_df_scaled = scaler.transform(input_df)

    # Predict the rating using the trained model
    prediction = model.predict(input_df_scaled)

    # Display the prediction
    st.subheader('Prediction 📊')
    st.write(f'🏅 Predicted Rating: {prediction[0]}')
except Exception as e:
    st.error(f"Error in prediction: {e}")

# Add an animation in the sidebar
st.sidebar.image("https://th.bing.com/th/id/R.6da89904177277ea98383eceff14c2db?rik=oQDCtY3dhnuOAQ&riu=http%3a%2f%2fmedia.giphy.com%2fmedia%2f120Zj5Kb5ugtRS%2fgiphy.gif&ehk=PEsT1M919HpBjlmpsYppaR1DhXp5aE%2b8NPwQHMIqXa8%3d&risl=&pid=ImgRaw&r=0", caption='Football Animation', use_column_width=True)
