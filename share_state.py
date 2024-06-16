import streamlit as st
from streamlit_server_state import server_state, server_state_lock 

def set_server_state(key, value):
    with server_state_lock[key]:
        server_state[key] = value
def get_server_state(key):
    with server_state_lock[key]:
        if key in server_state:
            return server_state[key]
        else:
            None
