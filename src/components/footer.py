# import streamlit as st

# def footer_home():
#     logo_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQlsHtwRdipLbtBqe8tsQzXd1r6Sbj4MGo0vTcU9ECZIE2wJddJ_scXrHjP&s=10"
#     st.markdown(
#         f"""
#         <div style="margin-top: 2rem; text-align: center; display: flex; justify-content: center; align-items: center; gap: 8px;">  
#             <p style="font-weight: bold; color: white; margin: 0;">Created with ❤️ by </p>
#             <img src="{logo_url}" style="max-height: 25px;" />
#         </div>
#         """,
#         unsafe_allow_html=True
#     )


import streamlit as st

def footer_dashboard():
    logo_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQlsHtwRdipLbtBqe8tsQzXd1r6Sbj4MGo0vTcU9ECZIE2wJddJ_scXrHjP&s=10"
    st.markdown(
        f"""
        <div style="margin-top: 2rem; text-align: center; display: flex; justify-content: center; align-items: center; gap: 8px;">  
            <p style="font-weight: bold; color: gray; margin: 0;">Created with ❤️ by </p>
            <img src="{logo_url}" style="max-height: 25px;" />
        </div>
        """,
        unsafe_allow_html=True
    )

def footer_home():
    footer_dashboard()