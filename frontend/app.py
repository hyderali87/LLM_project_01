import streamlit as st
import requests
import os
from flask import Flask, jsonify, request
from flask_cors import CORS

# Flask Backend Setup
app = Flask(__name__)
CORS(app)

@app.route('/ask')
def ask():
    question = request.args.get('question', '')
    # Add your question processing logic here
    return jsonify({
        "text": f"Response to: {question}",  # Replace with actual response
        "status": "success"
    })

# Streamlit Frontend
def main():
    # Configure backend URL (set via environment variable)
    BACKEND_URL = os.getenv('BACKEND_URL', 'http://localhost:8080')  # Default to local if not set
    
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
                res.raise_for_status()  # Raises exception for 4XX/5XX responses
                response_data = res.json()
                if "text" in response_data:
                    st.success(response_data["text"])
                else:
                    st.error("Unexpected response format")
                    st.json(response_data)
            except requests.exceptions.RequestException as e:
                st.error(f"Backend error: {str(e)}")
                st.json({
                    "request_url": f"{BACKEND_URL}/ask",
                    "params": {"question": question},
                    "error": str(e)
                })

if __name__ == '__main__':
    # When running as main, start Streamlit frontend
    if os.getenv('RUN_STREAMLIT', 'true').lower() == 'true':
        main()
    else:
        # Run Flask backend if not running Streamlit
        app.run(host='0.0.0.0', port=int(os.getenv('PORT', 8080)))