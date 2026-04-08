import streamlit as st
from model import predict_sentiment

st.title("Sentiment Analyzer 😊😐😠")

text = st.text_area("Enter your text:")

if st.button("Analyze"):
    if text:
        result = predict_sentiment(text)
        st.success(f"Sentiment: {result}")
    else:
        st.warning("Please enter some text!")
