import streamlit as st
import requests

st.title("📚 LLM FAQ Assistant")
question = st.text_input("Ask a question")
if st.button("Submit"):
    res = requests.get("https://YOUR_BACKEND_URL/ask", params={"question": question})
    st.write(res.json()["text"])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))