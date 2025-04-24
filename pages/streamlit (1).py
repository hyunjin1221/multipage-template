import streamlit as st
import pandas as pd
import yfinance as yf

# ✅ This must be first Streamlit command
st.set_page_config(page_title="Stock Advisory Tool", layout="centered")

# Now all other Streamlit commands
st.title("📊 Stock Advisory Tool")
st.markdown("Welcome to your investment insights dashboard...")
