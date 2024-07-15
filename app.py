"""
Entry point for the Outsmart Arena LLM Battle
"""

from dotenv import load_dotenv
import logging
from game.arenas import Arena
import streamlit as st
from util.setup import setup_logger, STYLE
from views.displays import Display

root = logging.getLogger()
if "root" not in st.session_state:
    st.session_state.root = root
    setup_logger(root)

load_dotenv()

st.set_page_config(layout="wide")
st.markdown(STYLE, unsafe_allow_html=True)

if "arena" not in st.session_state:
    st.session_state.arena = Arena.default()
arena = st.session_state.arena

Display(arena).display_page()
