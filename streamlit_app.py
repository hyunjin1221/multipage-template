import streamlit as st

st.set_page_config(page_title="ESG Analytics Suite”,layout="wide")

App_page_intro  = st.Page("pages/intro.py",              title="Welcome",            default=True)
App_page_main   = st.Page("pages/main.py",               title="Dataset Overview",  )
App_page_eda    = st.Page("pages/eda.py",                title="Exploratory Analysis")
App_page_ind    = st.Page("pages/industry.py",           title="Industry ESG", )
App_page_trend  = st.Page("pages/trends.py",             title="Time-Series Trends")

pg = st.navigation({
    "Start":  [App_page_intro, App_page_main],
    "EDA":    [App_page_eda, App_page_ind, App_page_trend],
})
