import streamlit as st
from datetime import datetime
import requests
import pandas as pd 

API_URL = "http://localhost:8000"

def month_analytics_tab():
    col1, col2 = st.columns(2)
    with col1:
        start_month = st.selectbox("Start Month", [
            "2024-08", "2024-09", "2024-10", "2024-11", "2024-12",
            "2025-01", "2025-02", "2025-03"
        ])
    with col2:
        end_month = st.selectbox("End Month", [
            "2024-08", "2024-09", "2024-10", "2024-11", "2024-12",
            "2025-01", "2025-02", "2025-03"
        ], index=7)

    response = requests.get(f"{API_URL}/analytics/monthly", params={
        "start_month": start_month,
        "end_month": end_month})

    if response.status_code != 200:
        st.error("Failed to fetch monthly data")
        return
    
    response = response.json()

    data = {
        "Month": list(response.keys()),
        "Total": [response[month]['total'] for month in response],
        "Percentage": [response[month]['percentage'] for month in response]
    }

    

    df = pd.DataFrame(data)
    df_sorted = df.sort_values(by="Month", ascending=True)

    st.title("Expense Breakdown by Month")
    st.bar_chart(data=df.set_index("Month")["Total"])
    df_sorted["Total"] = df_sorted["Total"].map("${:.2f}".format)
    df_sorted["Percentage"] = df_sorted["Percentage"].map("{:.2f}%".format)
    st.table(df_sorted)
    