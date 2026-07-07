import streamlit as st
import pandas as pd
import joblib

# Load the saved pipeline only once
@st.cache_resource
def load_pipeline():
    return joblib.load("diamond_pipeline.pkl")

pipeline = load_pipeline()

# Extract model, encoder and columns
model = pipeline["model"]
encoder = pipeline["encoder"]
columns = pipeline["columns"]

# Title
st.title("Diamond Price Prediction")

st.write("Enter the diamond details below to predict the price.")

# User Inputs
carat = st.number_input("Carat", min_value=0.20, max_value=5.00, value=1.00)

cut = st.selectbox(
    "Cut",
    ["Fair", "Good", "Very Good", "Premium", "Ideal"]
)

color = st.selectbox(
    "Color",
    ["D", "E", "F", "G", "H", "I", "J"]
)

clarity = st.selectbox(
    "Clarity",
    ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]
)

depth = st.number_input(
    "Depth",
    min_value=40.0,
    max_value=80.0,
    value=61.8
)

table = st.number_input(
    "Table",
    min_value=40.0,
    max_value=80.0,
    value=57.0
)

x = st.number_input(
    "Length (x)",
    min_value=0.0,
    value=5.70
)

y = st.number_input(
    "Width (y)",
    min_value=0.0,
    value=5.70
)

z = st.number_input(
    "Height (z)",
    min_value=0.0,
    value=3.50
)

# Predict Button
if st.button("Predict Price"):

    # Create DataFrame
    input_data = pd.DataFrame({
        "carat": [carat],
        "cut": [cut],
        "color": [color],
        "clarity": [clarity],
        "depth": [depth],
        "table": [table],
        "x": [x],
        "y": [y],
        "z": [z]
    })

    # Encode categorical columns
    input_data[["cut", "color", "clarity"]] = encoder.transform(
        input_data[["cut", "color", "clarity"]]
    )

    # Arrange columns in correct order
    input_data = input_data[columns]

    # Predict
    prediction = model.predict(input_data)

    # Display Result
    st.success(f"Predicted Diamond Price: ${prediction[0]:,.2f}")