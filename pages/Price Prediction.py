import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("Price Prediction App")

uploaded_file = st.file_uploader("Upload CSV with columns: OPEN, HIGH, LOW, VOLUME, CLOSE")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Preview of uploaded data:")
    st.write(df.head())

    # Train the model
    model = LinearRegression()
    model.fit(df[['OPEN', 'HIGH', 'LOW', 'VOLUME']], df['CLOSE'])

    st.subheader("Enter values to predict CLOSE price")

    # 🧮 Input fields for prediction
    open_val = st.number_input("Enter OPEN value")
    high_val = st.number_input("Enter HIGH value")
    low_val = st.number_input("Enter LOW value")
    volume_val = st.number_input("Enter VOLUME value")

    input_features = [[open_val, high_val, low_val, volume_val]]

    # 🧠 Predict only when button is clicked
    if st.button("Predict"):
        prediction = model.predict(input_features)
        st.success(f"Predicted CLOSE price: ${prediction[0]:.2f}")
