import streamlit as st
import pandas as pd
import yfinance as yf
import gdown
import pickle


def load_model_from_gdrive(file_id):
    url = f"https://drive.google.com/uc?id={file_id}"
    output = '/tmp/model.pkl'
    gdown.download(url, output, quiet=False)
    with open(output, 'rb') as f:
        model = pickle.load(f)
    return model

# Google Drive IDs (update these!)
tech_model_id = 'your_tech_model_file_id_here'
fund_model_id = 'your_fund_model_file_id_here'

# Load models
tech_model = load_model_from_gdrive(tech_model_id)
fund_model = load_model_from_gdrive(fund_model_id)

# Pull from session_state
if "data" not in st.session_state or "fund_weight" not in st.session_state:
    st.error("⚠️ Please input a ticker on the Home page first!")
    st.stop()

df = st.session_state.data
fund_weight = st.session_state.fund_weight
tech_weight = st.session_state.tech_weight
ticker = st.session_state.get("stock_ticker", "Ticker Unknown")

# Very simple example features
latest_data = df.iloc[-1]  # Most recent day

# Technical Features Example
X_tech = pd.DataFrame({
    "close": [latest_data['Close']],
    "volume": [latest_data['Volume']],
    # Add more technical features here!
})

# Fundamental Features Example
# (Dummy example: assume your model expects close price)
X_fund = pd.DataFrame({
    "close": [latest_data['Close']],
    # Add more fundamental features here!
})

# Make Predictions
tech_score = tech_model.predict(X_tech)[0]
fund_score = fund_model.predict(X_fund)[0]

# Combine Based on Weights
final_score = (fund_weight * fund_score) + (tech_weight * tech_score)

st.title("🔍 Stock Rating Result")
st.subheader(f"Results for {ticker}")

col1, col2, col3 = st.columns(3)

col1.metric("📚 Fundamental Score", f"{fund_score:.2f} / 10")
col2.metric("📈 Technical Score", f"{tech_score:.2f} / 10")
col3.metric("⭐ Final Investment Rating", f"{final_score:.2f} / 10")

st.success(f"📢 {ticker} has a final investment score of **{final_score:.2f}** out of 10!")


# import streamlit as st
# import pandas as pd

# # Print out the title for Page 1: View stock info dataframe
# st.title("Page 1: View Stock Data")

# # Display the Pandas dataframe of the stock data from yfinance
# #  Note: The stock info dataframe is stored in a StreamLit "session state" that allows the data to be shared across
# #        the mutiple pages (ie, main.py, page1.py, page2.py and page4.py)

# st.dataframe(st.session_state.data, use_container_width=True)

# # The dataframe can also be displayed as an editable interactive dataframe using the StreamLit data_editor function 
# #st.session_state.data = st.data_editor(st.session_state.data)
