import gdown
import pickle
import streamlit as st

# Streamlit caching to avoid redownloading every time
@st.cache_resource
def load_model_from_gdrive(file_id):
    url = f"https://drive.google.com/uc?id={file_id}"
    output = '/tmp/model.pkl'  # Temporary file path
    gdown.download(url, output, quiet=False)
    
    with open(output, 'rb') as f:
        model = pickle.load(f)
    return model

# IDs from your Google Drive
tech_model_id = 'your_tech_model_file_id_here'
fund_model_id = 'your_fund_model_file_id_here'

# Load models
tech_model = load_model_from_gdrive(tech_model_id)
fund_model = load_model_from_gdrive(fund_model_id)



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
