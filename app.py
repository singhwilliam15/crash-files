"""The Crash Files: a Streamlit wrapper around the interactive casebook page."""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="The Crash Files",
    page_icon="📉",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit's own chrome so the casebook fills the screen.
st.markdown(
    """
    <style>
      #MainMenu, header[data-testid="stHeader"], footer {display: none !important;}
      [data-testid="stAppViewContainer"], [data-testid="stMain"] {padding-top: 0 !important;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      [data-testid="stAppViewContainer"] > .main {padding: 0 !important;}
      iframe {display: block; width: 100%; height: 100vh !important; border: 0;}
    </style>
    """,
    unsafe_allow_html=True,
)

PAGE = (Path(__file__).parent / "crash_files.html").read_text(encoding="utf-8")

# The page is written as body content, so give it a minimal document shell.
SHELL = (
    "<!doctype html><html><head><meta charset='utf-8'>"
    "<meta name='viewport' content='width=device-width,initial-scale=1'>"
    "<style>body{margin:0}[hidden]{display:none!important}img{max-width:100%}</style>"
    "</head><body>" + PAGE + "</body></html>"
)

components.html(SHELL, height=1000, scrolling=True)
