"""
Iain Muir, iam9ez

PROJECT DESCRIPTION

PROJECT STRUCTURE

# TODO
    • Make Newspage more robust (single data source)
    • Overhead ticker (ex. WSJ)
    • Expand / Collapse (containers?)
    •

streamlit run /Users/iainmuir/PycharmProjects/Desktop/streamlitApp/main.py
"""

import streamlit as st

# from espnFantasyFootball import fantasy_app
from sportsHighlights import sports_app
from stockMarket import market_app

import home_page

# st.set_page_config(layout="wide")

PAGES = {
    "Home": home_page,
    "Marketplace Info": market_app,
    "Sports Center": sports_app
    # "Fantasy": fantasy_app
}

st.sidebar.title("Main Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.launch()
