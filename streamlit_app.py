import streamlit as st
import joblib
import pandas as pd


# Load the trained model
model = joblib.load('final_stacking_model.pkl')
scaler = joblib.load('scaler.pkl')

# Title of the app
st.title('Player Rating Prediction')

# Sidebar for user input
st.sidebar.header('Enter Player Attributes')


def user_input_features():
    attribute_1 = st.sidebar.number_input('Potential', min_value=0.0, max_value=100.0, value=50.0)
    attribute_2 = st.sidebar.number_input('Value in Euros', min_value=9000.0, max_value=185500000.0, value=92750000.0)
    attribute_3 = st.sidebar.number_input('Wage in Euros', min_value=500.0,
                                          max_value=560000.0, value=280000.0)
    attribute_4 = st.sidebar.number_input('Shot Power', min_value=00.0, max_value=100.0, value=50.0)
    attribute_5 = st.sidebar.number_input('Short Passing', min_value=00.0, max_value=100.0, value=50.0)
    attribute_6 = st.sidebar.number_input('Passing', min_value=00.0, max_value=100.0, value=50.0)
    attribute_7 = st.sidebar.number_input('Dribbling', min_value=00.0, max_value=100.0, value=50.0)
    attribute_8 = st.sidebar.number_input('Reactions', min_value=00.0, max_value=100.0, value=50.0)
    attribute_9 = st.sidebar.number_input('Composure', min_value=00.0, max_value=100.0, value=50.0)
    attribute_10 = st.sidebar.number_input('Vision', min_value=00.0, max_value=100.0, value=50.0)

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
st.subheader('User Input parameters')
st.write(input_df)

# Ensure the input features match the training data
try:
    # Scale the input data
    input_df_scaled = scaler.transform(input_df)

    # Predict and display result
    prediction = model.predict(input_df_scaled)
    st.subheader('Prediction')
    st.write(f'Predicted Rating: {prediction[0]}')
except Exception as e:
    st.error(f"Error in prediction: {e}")
