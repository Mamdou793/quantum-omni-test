import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Quantum Omni-Twin Dashboard", layout="wide")

st.title("🛡️ Quantum System Command Center")
st.markdown("Monitoring Real-Time Fidelity and Shielding Requirements")

# 1. Check if file exists to prevent crash
if not os.path.exists("dashboard_metrics.csv"):
    st.error("Waiting for data... Please run agent_analysis.py first.")
else:
    df = pd.read_csv("dashboard_metrics.csv")

    # Top Row: Key Metrics
    col1, col2, col3 = st.columns(3)
    
    # Logic to handle the 'Delta' only if we have 2+ rows
    if len(df) > 1:
        fid_delta = f"{df['Fidelity'].iloc[-1] - df['Fidelity'].iloc[-2]:.2f}%"
    else:
        fid_delta = None # No comparison available yet

    col1.metric("Current Fidelity", f"{df['Fidelity'].iloc[-1]}%", delta=fid_delta)
    col2.metric("Shielding Level", df['Shielding'].iloc[-1])
    col3.metric("Critical Height", f"{df['Critical_Height'].iloc[-1]}m")

    # 2. Main Chart: Only show if data is available
    st.subheader("System Stability Trends")
    fig = px.line(df, x="Timestamp", y=["Fidelity", "Shielding"], markers=True)
    st.plotly_chart(fig, use_container_width=True)

    # 3. Data Table View
    with st.expander("View Raw Log Data"):
        st.dataframe(df)