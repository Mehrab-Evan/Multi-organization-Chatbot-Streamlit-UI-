import streamlit as st
import requests
import pandas as pd

def fetch_organization_data():
    url = 'http://localhost:5000/organization_list'  # Replace with the URL of your Flask app
    response = requests.get(url)
    return response.json()

def view_organizations():
    st.set_page_config(
        page_title="Organizations",
        page_icon="🏢"
    )
    st.title("Organization List")
    organization_data = fetch_organization_data()

    if not organization_data:
        st.warning("No organization data found.")
    else:
        # Convert the organization_data (list of dictionaries) to a DataFrame
        df = pd.DataFrame(organization_data)

        # Add the 'Status' column to the DataFrame if it's not present
        if 'org_status' not in df.columns:
            df['Status'] = None

        # Rename the columns with custom names
        df = df.rename(columns={
            'org_name': 'Name',
            'org_started_date': 'Started Date',
            'org_expired_date': 'Expiration Date',
            'org_prompt': 'Prompt',
            'org_msg_counter': 'Message Counter',
            'org_msg_limit': 'Message Limit',
            'org_monthly_limit': 'Monthly Limit',
            'org_api': 'API-Key',
            'org_status': 'Status',
            'org_pdf_1': 'PDF 1',
            'org_pdf_2': 'PDF 2',
        })

        # Set the desired column order
        column_order = [
            'Name',
            'Started Date',
            'Expiration Date',
            'Prompt',
            'Message Counter',
            'Message Limit',
            'Monthly Limit',
            'API-Key',
            'Status',
            'PDF 1',
            'PDF 2'
        ]

        # Reorder the columns based on the desired column order
        df = df[column_order]

        # Adjust the width of the table to 1000 pixels and set font-size to 20px
        st.dataframe(df.set_index('Name'), width=1200).write()

if __name__ == "__main__":
    view_organizations()



# import streamlit as st
# import requests
# import pandas as pd
#
# def fetch_organization_data():
#     url = 'http://localhost:5000/organization_list'  # Replace with the URL of your Flask app
#     response = requests.get(url)
#     return response.json()
#
# def view_organizations():
#     st.set_page_config(
#         page_title="Organizations",
#         page_icon="🏢"
#     )
#     st.title("Organization List")
#     organization_data = fetch_organization_data()
#
#     if not organization_data:
#         st.warning("No organization data found.")
#     else:
#         # Convert the organization_data (list of dictionaries) to a DataFrame
#         df = pd.DataFrame(organization_data)
#
#         # Rename the columns with custom names
#         df = df.rename(columns={
#             'org_name': 'Name',
#             'org_started_date': 'Started Date',
#             'org_expired_date': 'Expiration Date',
#             'org_prompt': 'Prompt',
#             'org_msg_counter': 'Message Counter',
#             'org_msg_limit': 'Message Limit',
#             'org_monthly_limit': 'Monthly Limit',
#             'org_api': 'API-Key',
#             'org_pdf_1': 'PDF 1',
#             'org_pdf_2': 'PDF 2',
#         })
#
#         # Set the desired column order
#         column_order = [
#             'Name',
#             'Started Date',
#             'Expiration Date',
#             'Prompt',
#             'Message Counter',
#             'Message Limit',
#             'Monthly Limit',
#             'API-Key',
#             'PDF 1',
#             'PDF 2'
#         ]
#
#         # Reorder the columns based on the desired column order
#         df = df[column_order]
#
#         # Adjust the width of the table to 1000 pixels and set font-size to 20px
#         st.dataframe(df.set_index('Name'), width=1200).write()
#
#
# if __name__ == "__main__":
#     view_organizations()

