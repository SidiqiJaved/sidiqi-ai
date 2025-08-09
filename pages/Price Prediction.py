import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("📈 Price Prediction")

uploaded_file = st.file_uploader("Upload CSV with 'feature' and 'price' columns")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())

    model = LinearRegression()
    model.fit(df[['OPEN', 'HIGH', 'LOW', 'VOLUME']], df['CLOSE'])

    input_val = st.number_input("Enter feature value")
    prediction = model.predict([[input_val]])
    st.write(f"Predicted price: ${prediction[0]:.2f}")