import streamlit as st
import requests
import time

@st.cache(allow_output_mutation=True)
def get_shared_state():
    return {"org_api_key": None, "user_api_key": None}


def login_page(shared_state):
    st.title("User Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        response = requests.post("http://127.0.0.1:5000/User_login", json={"email": email, "password": password})

        if response.status_code == 200 and response.json().get("success"):
            org_api_key = response.json().get("org_api_key")
            user_api_key = response.json().get("user_api_key")
            user_name = response.json().get("user_name")
            # msg_history = response.json().get("msg_history")

            shared_state["org_api_key"] = org_api_key
            shared_state["user_api_key"] = user_api_key
            shared_state["user_name"] = user_name
            # shared_state["msg_history"] = msg_history

            st.success("Login successful!")
            st.write("Redirecting to the chat...")
        else :
            st.error("Wrong ID or Password")


def chat_page(shared_state):
    st.title("Chat")

    if shared_state["org_api_key"] and shared_state["user_api_key"]:
        org_api_key = shared_state["org_api_key"]
        user_api_key = shared_state["user_api_key"]
        # st.write(org_api_key)
        # st.write(user_api_key)
        # st.write(msg_history)
        # if "chat_history" not in shared_state:
        #     shared_state["chat_history"] = []

        # Input field for sending messages
        new_message = st.text_input("Enter your message")
        if st.button("Send"):
            headers = {
                "ORG-API-Key": org_api_key,
                "USER-API-Key": user_api_key
            }
            data = {"user_question": new_message}
            response = requests.post("http://127.0.0.1:5000/get_answer/company/using_header", headers=headers,
                                     json=data)

            # st.write(response)

            if response.status_code == 200:
                received_message = response.json().get("answer")
                # st.text("You: " + new_message)
                # st.text("Server: " + received_message)
                shared_state["chat_history"].append({"You": new_message, "Server": received_message})
            else:
                # st.write(data)
                # st.write(headers)
                st.warning("Message sending failed.")

        # msg_history = shared_state["msg_history"]

        # msg_history = shared_state.get("msg_history", [])
        # st.write(msg_history)
        # for message in reversed(msg_history):
        #     role = message["role"]
        #     content = message["content"]
        #
        #     if role == "user":
        #         st.text("User: " + content)
        #     elif role == "bot":
        #         st.text("Solvrz: " + content)
        #     st.text("\n")  # Add spacing between messages
        #     st.text("\n")  # Add spacing between messages
        chat_history = shared_state["chat_history"]
        user_name = shared_state["user_name"]
        # Assuming each message has a "You" and "Server" key
        for message in reversed(chat_history):
            col1, col2 = st.columns(2)  # Create two columns
            with col1:
                st.markdown(user_name+" : " + message["You"])  # Display "You" message in the left column
            with col2:
                st.text("\n")
                st.text("\n")
                st.text("\n")
                st.markdown("Bot: " + message["Server"])  # Display "Bot" message in the right column

            st.text("\n")  # Add spacing between messages

        # msg_history = shared_state["msg_history"]
        # st.write(msg_history)  # Print the msg_history to check its structure

        # for msg in reversed(msg_history):
        #     st.write(msg)  # Print each message to check its structure
        #
        #     col1, col2 = st.columns(2)
        #     with col1:
        #         st.markdown(f"**User:** {msg}")
            # with col2:
            #     st.markdown(f"**Bot:** {msg['bot'][0]}")

        #     st.text("")  # Add empty line between message pairs
            # st.write("You: " + message["You"])
            # st.write("Bot: " + message["Server"])

    else:
        st.warning("Please login first.")


def main():
    st.set_page_config(page_title="Login and Chat App")
    shared_state = get_shared_state()

    page = st.sidebar.selectbox("Select a page", ["Login", "Chat"])

    if page == "Login":
        st.empty()
        time.sleep(0.01)
        shared_state["chat_history"] = []
        login_page(shared_state)
    elif page == "Chat":
        st.empty()
        time.sleep(0.01)
        chat_page(shared_state)

if __name__ == "__main__":
    main()
