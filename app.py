import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("My Data Journey 🚀")
st.write("Exploring data with Python and sharing the process.")

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Preview of your data:")
    st.dataframe(df.head())

    st.write("Basic Stats:")
    st.write(df.describe())

    st.write("Column Distribution:")
    column = st.selectbox("Choose a column", df.columns)
    fig, ax = plt.subplots()
    sns.histplot(df[column], kde=True, ax=ax)
    st.pyplot(fig)