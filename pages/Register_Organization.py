# streamlit_app.py
import streamlit as st
import requests

API_BASE_URL = "http://127.0.0.1:5000"  # Replace with your Flask API endpoint

st.title("💼Create Organization💼")

company_name = st.text_input("Organization Name")
company_prompt = st.text_area("Prompt")
msg_limit = st.number_input("Message Limit", min_value=0)
monthly_limit = st.number_input("Monthly Limit", min_value=0)
started_date = st.date_input("Started Date")
expired_date = st.date_input("Expired Date")
pdf1_file = st.file_uploader("Common PDF", type=["pdf"])
pdf2_file = st.file_uploader("Classified PDF", type=["pdf"])

submit_button = st.button("Submit")

if submit_button:
    data = {
        "company_name": company_name,
        "company_prompt": company_prompt,
        "msg_limit": msg_limit,
        "monthly_limit": monthly_limit,
        "started_date": str(started_date),
        "expired_date": str(expired_date),
    }

    files = {}

    # Only add PDFs if they are uploaded
    if pdf1_file:
        files["org_pdf1"] = pdf1_file
    if pdf2_file:
        files["org_pdf2"] = pdf2_file

    response = requests.post(API_BASE_URL + "/org_register", data=data, files=files)

    # st.write(data)
    # st.write(files)

    if response.status_code == 200:
        st.success("Organization added successfully!")
    else:
        st.error("Failed to add organization. Please try again later.")
