{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "A6P4jkqKD0YV"
      },
      "outputs": [],
      "source": [
        "import streamlit as st\n",
        "\n",
        "st.set_page_config(page_title=\"Stock Advisory Tool\", layout=\"centered\")\n",
        "\n",
        "st.title(\"📊 Stock Advisory Tool\")\n",
        "st.subheader(\"Built with Financial + Technical Analysis\")\n",
        "\n",
        "st.markdown(\"\"\"\n",
        "Welcome to our **Investment Advisory App** — a smart tool that analyzes both **fundamental financial health** and **recent market behavior** to generate a 1-to-10 investment rating for any publicly traded stock.\n",
        "\n",
        "---\n",
        "\n",
        "### 🔍 What This App Does\n",
        "- 🔢 **Rates stocks from 1 to 10** based on long-term fundamentals and short-term technicals\n",
        "- 📈 **Visualizes stock price trends**, momentum, and volume signals\n",
        "- 🧮 **Compares financial ratios to industry averages**\n",
        "- ⚙️ **Lets you adjust the weight** between technical and fundamental metrics\n",
        "\n",
        "---\n",
        "\n",
        "### 💡 How It Works\n",
        "- We use **WRDS Compustat data (2000–2024)** for historical financial analysis\n",
        "- Real-time stock data is pulled from **Yahoo Finance**, including prices, RSI, and volatility\n",
        "- Our model combines **rule-based logic** with **machine learning** (logistic regression, decision trees)\n",
        "\n",
        "---\n",
        "\n",
        "### 🚀 Try It Out\n",
        "1. Enter a stock ticker (e.g., `AAPL`, `MSFT`, `TSLA`)\n",
        "2. Get a 1–10 score with explanation\n",
        "3. Explore visual charts, ratios, and model insights\n",
        "\n",
        "---\n",
        "\n",
        "### 🧠 Why It Matters\n",
        "Whether you're a beginner investor or a data-driven analyst, this tool helps you make more informed decisions using both qualitative and quantitative insights.\n",
        "\n",
        "\"\"\")"
      ]
    }
  ]
}