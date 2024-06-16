import os
from groq import Groq
import uuid
import pandas as pd
from share_state import get_server_state, set_server_state
import streamlit as st
from dotenv import load_dotenv
from streamlit_pills import pills
from util import hide_header_footer


load_dotenv()
st.set_page_config(page_title="Persona Chat",layout='wide', initial_sidebar_state='collapsed')

hide_header_footer()

persona_prompt = get_server_state("persona_prompt")
persona_role = get_server_state("persona_role")
description = get_server_state("description")

st.header(f"Presenting {persona_role} in your service.", divider='rainbow')

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "system", "content": persona_prompt},{"role": "assistant", "content": description}]
    st.write("EMPTY STATE")

if st.session_state["messages"][1]["content"] != description:
    st.session_state["messages"] = [{"role": "system", "content": persona_prompt},{"role": "assistant", "content": description}]
    
for msg in st.session_state.messages:
    if msg["role"] == "assistant":
        with st.chat_message("assistant"):
            pills("Assistant Role: ",[persona_role],label_visibility="collapsed",key='pill_id'+format(uuid.uuid4()))
            with st.container(border=True):
                st.write(msg["content"])
            
    elif msg["role"] == "user":
        st.chat_message(msg["role"]).write(msg["content"])

st.markdown("""
            <style>
            div[data-testid="collapsedControl"]{
                    visibility: collapse;
            }
            section[data-testid="stSidebar"]{
                   visibility: collapse;
            }
            </style>
            """,unsafe_allow_html=True)

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

user_input = st.chat_input()

if user_input and persona_prompt and persona_role:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)
    
    response = client.chat.completions.create(model="llama3-70b-8192", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content":msg})
    
    with st.chat_message("assistant"):
        pills("Assistant Role: ",[persona_role],label_visibility="collapsed",key='pill_id'+format(uuid.uuid4()))
        with st.container(border=True):
            st.write(msg)

