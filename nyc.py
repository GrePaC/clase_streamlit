import streamlit as st
import pandas as pd
import numpy as np
import codecs

@st.cache
def load_data(nrows):
    doc = codecs.open('movies.csv','rU','latin1')
    return pd.read_csv(doc, nrows=nrows)

def filter_by_title(title):
    return data[data['name'].str.upper().str.contains(title)]

def filter_by_director(name):
    return data[data['director'] == name]


st.title("Realiza una búsqueda de película")
load_state = st.text('Cargando la DB de netflix...')
data = load_data(500)
load_state.text('¿Qué peli quieres buscar?')

# -----------------------------------------------------------
# DASHBOARD
# -----------------------------------------------------------
#   Checkbox
if st.sidebar.checkbox('Listar todo'):
    st.subheader('Todas las películas')
    st.write(data)

#    Search Button (Title)
title_input = st.sidebar.text_input('Título de la película:')
search_button = st.sidebar.button('Buscar película')    
if (search_button):
   st.write(f"Filtrado por Título")
   st.write(filter_by_title(title_input.upper()))

#    Dropdown (Director's Name)
director_name = st.sidebar.selectbox("Nombre del director", data['director'].unique())
dropdown = st.sidebar.button('Filtrar por nombre')
if (dropdown):
   st.write(f"Filtrado por Director")
   st.dataframe(filter_by_director(director_name))
