# import streamlit as st
# import requests
# # def dashboard(org_api_key):
# #     st.empty()
# #
# #     st.title("Dashboard")
# #     st.write("Welcome to the dashboard!")
# #
# #     # Display the org_api_key
# #     st.write(f"Organization API Key: {org_api_key}")
# #
# #     # Add your dashboard content here
# #
# #
# # if __name__ == "__main__":
# #     org_api_key = st.experimental_get_query_params()["org_api_key"][0]  # Get the org_api_key from query parameters
# #     dashboard(org_api_key)
# #
#
#
# def chat_page():
#     st.title("Chat")
#
#     if shared_state["org_api_key"] and shared_state["user_api_key"]:
#         org_api_key = shared_state["org_api_key"]
#         user_api_key = shared_state["user_api_key"]
#         st.write(org_api_key)
#         st.write(user_api_key)
#
#         # Input field for sending messages
#         new_message = st.text_input("Enter your message")
#         if st.button("Send"):
#             headers = {
#                 "ORG-API-Key": org_api_key,
#                 "USER-API-Key": user_api_key
#             }
#             data = {"user_question": new_message}
#             response = requests.post("http://127.0.0.1:5000/get_answer/company/using_header", headers=headers,
#                                      json=data)
#
#             if response.status_code == 200 and response.json().get("success"):
#                 received_message = response.json().get("received_message")
#                 st.text("You: " + new_message)
#                 st.text("Server: " + received_message)
#             else:
#                 st.write(data)
#                 st.write(headers)
#                 st.warning("Message sending failed.")
#
#     else:
#         st.warning("Please login first.")
#
#
# if __name__ == "__main__": # Get the org_api_key from query parameters
#     chat_page()