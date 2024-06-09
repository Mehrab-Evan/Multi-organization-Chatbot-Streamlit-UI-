# streamlit_chat_ui.py

import streamlit as st
import requests


def get_answer_from_api(api_key, api_header, user_question):
    url = 'http://localhost:5000/get_answer/company/using_header'
    headers = {'API-Key': api_key, 'API-Header': api_header}
    data = {'user_question': user_question}
    response = requests.post(url, headers=headers, json=data)
    return response.json()


def main():
    st.title("Chatbot Demo")

    # Collect API Key and API Header from the user
    api_key = st.text_input("Enter API Key:")
    api_header = st.text_input("Enter API Header:")

    # Collect user's question
    user_question = st.text_area("Ask a question:")

    if st.button("Submit"):
        if api_key and api_header and user_question:
            # Call the API endpoint to get the answer
            response_data = get_answer_from_api(api_key, api_header, user_question)

            # Display the answer
            st.success(response_data.get('answer', 'No answer available.'))
        else:
            st.warning("Please provide both API Key, API Header, and ask a question.")


if __name__ == "__main__":
    main()
