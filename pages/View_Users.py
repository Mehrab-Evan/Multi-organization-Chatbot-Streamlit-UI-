# import streamlit as st
# import requests
#
# def fetch_user_data():
#     url = 'http://localhost:5000/user_list'  # Replace with the URL of your Flask app
#     response = requests.get(url)
#     return response.json()
#
# def view_users():
#     st.set_page_config(
#         page_title="Users",
#         page_icon="👩‍🎓👨‍🎓"
#     )
#     st.title("User List")
#     user_data = fetch_user_data()
#
#     if not user_data:
#         st.warning("No user data found.")
#     else:
#         st.table(user_data)
#
# if __name__ == "__main__":
#     view_users()


import streamlit as st
import requests
import pandas as pd


def fetch_user_data():
    url = 'http://localhost:5000/user_list'  # Replace with the URL of your Flask app
    response = requests.get(url)
    # print(response)
    return response.json()


def view_users():
    st.set_page_config(
        page_title="Users",
        page_icon="👩‍🎓👨‍🎓"
    )
    st.title("User List")
    user_data = fetch_user_data()
    st.write(user_data)
    if not user_data:
        st.warning("No user data found.")
    else:
        # Convert the user_data (list of dictionaries) to a DataFrame
        df = pd.DataFrame(user_data)

        # Set the column names and display the table
        df = df.rename(columns={
            'username': 'Name',
            'user_org': 'Organization',
            'user_email': 'Email',
            'org_api_key': 'API-Key',
            # 'msg_history': 'Message History'
        })

        # Adjust the width of the table
        st.dataframe(df.set_index('Name'), width=12000)


if __name__ == "__main__":
    view_users()

