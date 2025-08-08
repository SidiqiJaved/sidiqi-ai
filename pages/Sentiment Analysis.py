import streamlit as st
import pandas as pd
from textblob import TextBlob

st.title("🧠 Sentiment Analysis")

text = st.text_area("Enter text to analyze sentiment")

if text:
    blob = TextBlob(text)
    sentiment = blob.sentiment
    st.write(f"Polarity: `{sentiment.polarity}`")
    st.write(f"Subjectivity: `{sentiment.subjectivity}`")