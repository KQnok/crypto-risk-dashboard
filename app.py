import streamlit as st
from data import get_btc_data
from analysis import add_risk_metrics

st.title("🔴 Crypto Risk Dashboard")

days = st.sidebar.slider("Period (days)", min_value=30, max_value=365, value=90)

df = get_btc_data(days=days)

df = add_risk_metrics(df)
