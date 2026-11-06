import streamlit as st
from supabase import create_client, Client

url = st.secrets["supabase_url"]
key = st.secrets["supabase_key"]
supabase: Client = create_client(url, key)
