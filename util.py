import streamlit as st

def hide_header_footer():
    hide_streamlit_style = """
            <style>
            [data-testid="stToolbar"] {visibility: hidden !important;}
            footer {visibility: hidden !important;}
            header[data-testid="stHeader"]{visibility: hidden !important;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 