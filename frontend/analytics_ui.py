import streamlit as st
from datetime import datetime
import requests

API_URL = "http://localhost:8000"

def analytics_tab():
    start_date = st.date_input("Start Date", datetime(2024, 8, 1))
    end_date = st.date_input("End Date", datetime(2024, 8, 5))