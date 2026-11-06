# import streamlit as st

# def style_background_home():
#     st.markdown(
#         """
#         <style>
#         .stApp {
#             background: #5865F2 !important;
#         }
#         .stApp  div[data-testid="stColumn"] {
#             background: #E0E3FF !important;
#             border-radius: 5rem !important;
#             padding: 2.5rem !important;
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# def style_background_dashboard():
#     st.markdown(
#         """
#         <style>
#         .stApp {
#             background: #E0E3FF !important;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# def style_base_layout():
#     st.markdown(
#         """
#         <style> 
# @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Outfit:wght@100..900&display=swap');
# @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Outfit:wght@100..900&display=swap');

#         /* hide top bar of the streamlit app */
#         #MainMenu, footer, header {
#             visibility: hidden;
#         }
#         .block-container {
#             padding-top: 1.5rem !important;
#         }
#         h1{
#             font-family: 'Climate Crisis', sans-serif !important;
#             font-size: 3.5rem !important;
#             line-height: 1.1 !important;
#             margin-bottom: 0rem !important;
           
#         }

#         h2{
#             font-family: 'Outfit', sans-serif !important;
#             font-size: 2rem !important;
#             line-height: 0.9 !important;
#             margin-bottom: 0rem !important;
            
#         }
#         h3,h4,p,{
#             font-family: 'Outfit', sans-serif;
#         }
#         button{
#         border-radius: 1.5rem !important;
#         background: #FF1493 !important;
#         color: white !important;
#         padding: 10px 20px !important;
#         border : none !important;
#         transition: transform 0.25s ease-in-out !important;

#         button[kind="secondary"] {
#         border-radius: 1.5rem !important;
#         background: #EB459E !important;
#         color: white !important;
#         padding: 10px 20px !important;
#         border : none !important;
#         transition: transform 0.25s ease-in-out !important;

#         button[kind="tertiary"] {
#         border-radius: 1.5rem !important;
#         background: black !important;
#         color: white !important;
#         padding: 10px 20px !important;
#         border : none !important;
#         transition: transform 0.25s ease-in-out !important;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )





















import streamlit as st

def style_background_home():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%) !important;
        }
        .stApp div[data-testid="stColumn"] {
            background: rgba(30, 41, 59, 0.7) !important;
            backdrop-filter: blur(12px);
            border: 1px solid rgba(51, 65, 85, 0.8) !important;
            border-radius: 2rem !important;
            padding: 2.5rem !important;
            box-shadow: 0 16px 40px rgba(0, 0, 0, 0.5);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def style_background_dashboard():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(135deg, #090d16 0%, #0f172a 100%) !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def style_base_layout():
    st.markdown(
        """
        <style> 
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Outfit:wght@100..900&display=swap');

        /* Hide top bar and footer of the streamlit app */
        #MainMenu, footer, header {
            visibility: hidden;
        }
        
        .block-container {
            padding-top: 2rem !important;
            color: #f8fafc !important;
        }
        
        /* Main Heading (Climate Crisis Font) */
        h1 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 3.2rem !important;
            line-height: 1.1 !important;
            margin-bottom: 0.5rem !important;
            color: #ffffff !important;
            text-shadow: 0 2px 10px rgba(59, 130, 246, 0.3);
        }

        /* Subheadings and regular text font enforcement */
        h2, h3, h4, p, span {
            font-family: 'Outfit', sans-serif !important;
        }

        /* --- Dialog / Modal Navy Theme Override --- */
        div[data-baseweb="modal"] {
            background-color: rgba(3, 7, 18, 0.8) !important;
        }

        div[role="dialog"], 
        [data-testid="stModal"],
        div[data-baseweb="modal"] > div {
            background-color: #1e293b !important;
            color: #f8fafc !important;
            border: 1px solid #334155 !important;
            border-radius: 1.2rem !important;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.7) !important;
        }

        div[role="dialog"] h1, div[role="dialog"] h2, div[role="dialog"] h3, 
        div[role="dialog"] h4, div[role="dialog"] p, div[role="dialog"] span, 
        div[role="dialog"] label, [data-testid="stModal"] * {
            color: #f8fafc !important;
        }

        /* General Streamlit Buttons */
        .stButton > button {
            border-radius: 1rem !important;
            background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%) !important;
            color: white !important;
            padding: 0.6rem 1.2rem !important;
            border: none !important;
            font-weight: 600 !important;
            font-family: 'Outfit', sans-serif !important;
            transition: all 0.2s ease-in-out !important;
            box-shadow: 0 4px 15px rgba(37, 99, 235, 0.4);
        }

        .stButton > button:hover {
            background: linear-gradient(135deg, #2563eb 100%, #1d4ed8 0%) !important;
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(37, 99, 235, 0.6);
        }

        /* Input Fields Styling for Navy Theme */
        .stTextInput input, .stSelectbox div[data-baseweb="select"] {
            background-color: #0f172a !important;
            color: white !important;
            border-radius: 0.8rem !important;
            border: 1px solid #334155 !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )