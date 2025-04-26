# Import Streamlit
import streamlit as st

# Page layout setup
App_home = st.Page(
    "pages/main.py",
    title="🏠 Home",
    default=True
)

App_stock_input = st.Page(
    "pages/stock_input.py",
    title="🔍 Stock Input & Score"
)

App_technical = st.Page(
    "pages/technical_analysis.py",
    title="📈 Technical Analysis"
)

App_fundamentals = st.Page(
    "pages/fundamentals.py",
    title="📑 Fundamentals"
)

App_model_insights = st.Page(
    "pages/model_insights.py",
    title="🤖 Model Insights"
)

App_docs = st.Page(
    "pages/docs.py",
    title="📚 Docs"
)

# Set up navigation with new sections
pg = st.navigation(
    {
        "🏢 Investment Advisory App": [App_home],
        "Navigate:": [
            App_stock_input,
            App_technical,
            App_fundamentals,
            App_model_insights,
            App_docs
        ],
    }
)

# Sidebar shared elements (optional)
st.sidebar.markdown("---")
st.sidebar.markdown("📄 **Sidebar Prompts:**")
st.sidebar.markdown("- Enter stock tickers")
st.sidebar.markdown("- Adjust technical/fundamental weights")
st.sidebar.markdown("- View score breakdowns")

# Execute the navigation
pg.run()


# # Import Streamlit
# import streamlit as st

# # **** Page layout setup ****
# App_page_0 = st.Page(
#     "pages/main.py",
#     title="Click here to select stock",
#     default=True
# )
# App_page_1 = st.Page(
#     "pages/page1.py",
#     title="Page 1: See Raw Stock Data"
# )
# App_page_2 = st.Page(
#     "pages/page2.py",
#     title="Page 2: See Data Statistics"
# )
# App_page_3 = st.Page(
#     "pages/page3.py",
#     title="Page 3: See Stock Price Graph"
# )

# # **** Set up navigation with section headers ****
# pg = st.navigation(
#     {
#         "Start Here:": [App_page_0],
#         "Dashboard Options": [App_page_1, App_page_2, App_page_3],
#     }
# )


# # **** text/images shared on all pages ****
# st.sidebar.markdown("Sidebar Prompts:")


# # **** Execute the navigation code ****
# pg.run()
