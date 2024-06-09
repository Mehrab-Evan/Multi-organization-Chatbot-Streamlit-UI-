# streamlit_app.py
import streamlit as st
import requests
# import View_Users
#
# View_Users.view_users()

# def go_to_view_users():
#     view_users()

API_BASE_URL = "http://127.0.0.1:5000"  # Replace with your Flask API endpoint

st.title("User Sign Up 🙌👋")

# Fetch existing organization names from the API
response = requests.get(API_BASE_URL + "/get_organization_names")
if response.status_code == 200:
    existing_organizations = response.json()
else:
    existing_organizations = []

# Input fields
username = st.text_input("Username")
user_org = st.selectbox("Organization", existing_organizations)
user_email = st.text_input("Email")
user_password = st.text_input("Password", type="password")

submit_button = st.button("Submit")

if submit_button:
    data = {
        "username": username,
        "user_org": user_org,
        "user_email": user_email,
        "user_password": user_password,
    }
    response = requests.post(API_BASE_URL + "/user_register", json=data)
    # st.write(response)
    # st.write(data)
    if response.status_code == 200:
        st.success("User added successfully!")
        # go_to_view_users()
    else:
        st.error("Failed to add user. Please try again later.")

