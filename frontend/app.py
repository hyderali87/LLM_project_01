import streamlit as st
import requests
import os

# Configure backend URL (set via environment variable)
BACKEND_URL = os.getenv('BACKEND_URL', 'https://your-backend-service.a.run.app')

st.title("📚 LLM FAQ Assistant")
st.markdown(f"*Connected to backend at: `{BACKEND_URL}`*")

question = st.text_input("Ask a question")
if st.button("Submit"):
    with st.spinner('Getting answer...'):
        try:
            res = requests.get(
                f"{BACKEND_URL}/ask", 
                params={"question": question},
                timeout=10
            )
            st.success(res.json()["text"])
        except Exception as e:
            st.error(f"Error calling backend: {str(e)}")
