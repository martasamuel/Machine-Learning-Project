#streamlit app to predict the NObeyesdad using the model
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
# Load the xgb model
model = pickle.load(open('xgb_model.pkl', 'rb'))
#No need for the scaler
st.title('Obesity Prediction App')
st.write('This is a web app to predict the obesity level of a person based on their gender and BMI')
st.write('Please adjust the values of the features on the left and the predicted obesity level will be displayed on the right.')
# Collect user input features (BMI, Gender, FAVC) to directly predict NOobeyesdad using our model:
Gender_input = st.selectbox("Select Gender", ["Male", "Female"])
Weight_input = st.number_input('Weight in kg')
Height_input = st.number_input('Height in cm')

# Encode categorical inputs
Gender_encoded = 1 if Gender_input == "Male" else 0

# Calculate BMI
if Height_input == 0:
    st.error("Height cannot be zero. Please enter a valid height.")
    bmi = 0  # Assign a default value to avoid further errors
else:
    bmi = Weight_input / ((Height_input / 100) ** 2)


# Prepare input data
input_data = np.array([[bmi, Gender_encoded]])

    # Ensure the input data is valid
if np.any(np.isnan(input_data)) or np.any(np.isinf(input_data)):
    st.error("Invalid input data. Please check your inputs.")

# Predict the output

if st.button("Predict"):
    prediction = model.predict(input_data)
    # Reverse the encoded prediction to the original labels
    label_mapping = {0: "Insufficient Weight", 1: "Normal Weight", 2: "Overweight", 3: "Obesity"}
    original_label = label_mapping.get(prediction[0], "Unknown")
    st.success(f"Predicted Obesity Class (NObesitydad): {original_label}")


    # Provide additional information or explanation about the prediction
    st.write("The prediction is based on the input features you provided.")
    st.write("Obesity levels are classified into categories such as Insufficient Weight, Normal Weight, Overweight, and Obesity.")
    st.write("Please note that this prediction is for informational purposes only and should not be considered medical advice.")


    # To run this Streamlit app, save the file and execute the following command in your terminal:
    # streamlit run "/Users/martakarnaschodkiewicz/Documents/Machine Learning Project/streamlit.py"
