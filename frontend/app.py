import streamlit as st
import requests
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Add this line

@app.route('/ask')
def ask():

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

try:
    res = requests.get(
        f"{BACKEND_URL}/ask",
        params={"question": question},
        timeout=10  # Add timeout
    )
    res.raise_for_status()  # Raises exception for 4XX/5XX responses
    st.success(res.json()["text"])
except requests.exceptions.RequestException as e:
    st.error(f"Backend error: {str(e)}")
    st.json({"url": f"{BACKEND_URL}/ask", "params": {"question": question}})