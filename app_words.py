import pandas as pd
import re
import dhlab.api.dhlab_api as api
import dhlab as dh
import sqlite3
import streamlit as st
from PIL import Image
import re
from IPython.display import HTML
import sim_api as sa

        

@st.cache_data(show_spinner = False)
def get_words(word="", hits = 10, collection_name="vss_1850_cos"):
    return sa.words(word=word, collection_name=collection_name)



st.set_page_config(page_title="Words", layout="wide", initial_sidebar_state="auto", menu_items=None)
st.session_state.update(st.session_state)

st.header("Nærliggende ord")

if 'model' not in st.session_state:
    st.session_state['model'] = "vss_1850_cos"

#st.write(sa.collections())
#st.write(sa.words("han", collection_name="vss_1850_cos"))
# Test med most_similar for forskjellige ord for evaluering.
word_col, anta_col = st.columns([5, 2])
if "words" not in st.session_state:
    st.session_state.words = 'Qvinde Kvinde Kvinne'
    
with word_col:
    words = st.text_input("Listen med ord blir koblet de som ligger nærmest i bruk", st.session_state.words, key="words")
    if ',' in words:
        words = [x.strip() for x in words.split(',')]
    else:
        words = words.split()
        
with anta_col:
    antall_ord = st.number_input("Antall nærliggende ord", min_value=1, max_value=30, value=10, key="antall_ord")

T = ""
for x in words:
    #st.write(sa.words(x))
    T += f"""### {x} \n {', '.join([
        x['word'] for _, x in get_words(x, hits=antall_ord, collection_name=st.session_state.model).iterrows()
    ])}\n\n"""
    
        
    
st.markdown(T)
    

st.session_state.update()