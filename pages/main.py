import streamlit as st
# Main Title
st.title("📊 Stock Advisory Tool")
st.subheader("Turning Smart Data into Smarter Investing")

# Introduction Story
st.markdown("""
**Investing is both an art and a science — and we're here to make it smarter and simpler for you.**

In today’s fast-moving markets, successful investing requires more than just watching the headlines.  
It demands a balanced view of a company's **long-term financial health** and its **short-term market momentum**.

That's why we built the **Stock Advisory Tool** — a data-driven platform that helps you make more informed investment decisions with just a few clicks.
""")

st.divider()

# What This App Does
st.header("🔍 What This App Does")
st.markdown("""
Our tool combines the power of **fundamental analysis** (deep dives into company financials) with **technical analysis** (studying price movements and market trends) to evaluate publicly traded companies.

Simply enter a stock ticker, and the tool will generate a **1-to-10 investment rating** based on:
- 📈 **Historical financial strength** (ROE, profit margin, debt levels)
- 📉 **Recent market behavior** (momentum, volatility, technical indicators)
""")

st.divider()

# How It Works
st.header("🧠 How It Works")
st.markdown("""
- Pulls financial data from **WRDS Compustat** (2000–2024)
- Retrieves real-time price data from **Yahoo Finance API**
- Blends **rule-based logic** with **machine learning** (logistic regression, decision trees)
""")

st.divider()

# Why It Matters
st.header("📈 Why It Matters")
st.markdown("""
Investment decisions are never black and white.  
Our app provides a clear, data-backed rating combining the **best of both worlds**:
- **What the company is** (fundamentally strong or weak)
- **How the market feels about it** (rising or falling)

You'll also be able to compare companies against **industry averages** like ROA for deeper insights.
""")

st.divider()

# Get Started
st.header("🚀 Get Started")
st.markdown("""
- Enter a stock ticker
- View the investment rating and detailed breakdown
- Customize the weight between **technical** and **fundamental** factors to match your investment style

Let's start making smarter investment decisions today!
""")
