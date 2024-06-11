import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('stacking_model.pkl')

# Title of the app
st.title('Player Rating Prediction')

# Sidebar for user input
st.sidebar.header('Enter Player Attributes')


def user_input_features():
    attribute_1 = st.sidebar.number_input('Potential', min_value=0.0, max_value=100.0, value=50.0)
    attribute_2 = st.sidebar.number_input('Value in Euros', min_value=0.0,
                                          max_value=1000000000000000000000000000000000000000000000000.0, value=50.0)
    attribute_3 = st.sidebar.number_input('Wage in Euros', min_value=0.0,
                                          max_value=10000000000000000000000.0, value=50.0)
    attribute_4 = st.sidebar.number_input('Age', min_value=0.0, max_value=60.0, value=25.0)
    attribute_5 = st.sidebar.number_input('Height(cm)', min_value=0.0, max_value=300.0, value=50.0)
    attribute_6 = st.sidebar.number_input('Weight(kg)', min_value=0.0, max_value=300.0, value=50.0)

    # ...

    data = {'potential': attribute_1,
            'value_eur': attribute_2,
            'wage_eur': attribute_3,
            'age': attribute_4,
            'height_cm': attribute_5,
            'weight_kg': attribute_6,
            }
    features = pd.DataFrame(data, index=[0])
    return features


input_df = user_input_features()

# Display user input
st.subheader('User Input parameters')
st.write(input_df)

# Predict and display result
prediction = model.predict(input_df)
st.subheader('Prediction')
st.write(f'Predicted Rating: {prediction[0]}')

