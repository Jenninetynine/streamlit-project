import streamlit as st
import os

def load_css():
    css_path = os.path.join("static", "css", "style.css")
    if os.path.exists(css_path):
        with open(css_path, "r") as f:
            css = f.read()
            st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    else:
        st.warning("CSS文件未找到")