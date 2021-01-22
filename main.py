"""
Iain Muir, iam9ez

PROJECT DESCRIPTION

streamlit run /Users/iainmuir/PycharmProjects/Desktop/streamlitApp/main.py
"""

import streamlit as st

# from espnFantasyFootball import app as fantasy_app
from sportsHighlights import app as sh_app
from stockMarket import app as sm_app

import home

# st.set_page_config(layout="wide")

PAGES = {
    "Home": home,
    "Marketplace Info": sm_app,
    "Sports Center": sh_app
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.launch()
