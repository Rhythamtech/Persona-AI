import pandas as pd
import streamlit as st
from streamlit_pills import pills


st.set_page_config(page_title="Persona ~AI",layout='wide', initial_sidebar_state='collapsed')

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

if 'persona_id' not in st.session_state:
    st.session_state.persona_id = None

if 'persona_role' not in st.session_state:
    st.session_state.persona_role = None

if 'persona_prompt' not in st.session_state:
    st.session_state.persona_prompt = None

def open_chat(id,role,prompt):
    st.session_state.persona_id = id
    st.session_state.persona_role = role
    st.session_state.persona_prompt = prompt

def persona_grid_cell(id,role,description,prompt):
    st.markdown(f"**ID: :** psn_id_{id}{role[:4]}")
    st.markdown(f"**Role**: {role}")
    st.markdown(f"**Description:** {description}")
    
    if st.button('💬 Chat Now',key=f"psn_id_{id}{role[:4]}",on_click=open_chat,args=(id,role,prompt)):
         st.switch_page('pages/chat.py')

st.header("Persona ~AI")
st.caption("A persona is a fictional representation of a person, character, or concept. In Generative AI using Groq Provider")

df = pd.read_csv('persona.csv')
categories_list  = df["Category"].unique().tolist()
selected = pills("Category: ", categories_list,['🧑‍💼','⛪','🦉','🤔','😎','🔡','🪴'])

row1 = st.columns(4) 
row2 =  st.columns(4) 
row3 =  st.columns(4) 
row4 = st.columns(4) 
row5 = st.columns(4)

grid  = [ cell.container(border=True) for cell in row1+row2+row3+row4+row5]


# import csv
# with open('persona.csv', 'r') as file:
#     csv_file = csv.DictReader(file)
#     for row in csv_file:
#         grid[int(row["Id"]) -1].markdown(row["Role"])



df =  df[df['Category'] == format(selected)]
i = 0
for index,cell in df.iterrows():
    with grid[i]:
        persona_grid_cell(cell["Id"],cell["Role"],cell["Description"],cell["Prompt"])
    i = i + 1

