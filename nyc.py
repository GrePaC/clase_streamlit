import streamlit as st
import pandas as pd
import numpy as np
import codecs

@st.cache
def load_data(nrows):
    doc = codecs.open('citibike-tripdata.csv','rU','latin1')
    data = pd.read_csv(doc, nrows=nrows)
    data['started_at'] = pd.to_datetime(data['started_at'])
    data.rename({'start_lat': 'lat', 
                 'start_lng': 'lon'}, axis=1, inplace=True)
    return data

st.title("City Bike Trips")
load_state = st.text('Cargando la DB...')
data = load_data(500)
load_state.text('¿Qué quieres visualizar?')


# -----------------------------------------------------------
# DASHBOARD
# -----------------------------------------------------------
#   Checkbox listar todo
if st.sidebar.checkbox('Listar todo'):
    st.subheader('Todas los trips')
    st.write(data)
#   Checkbox gráfica de barras
if st.sidebar.checkbox('Recorridos por hora'):
    st.subheader('Numero de recorridos por hora en que empezaron')
    st.bar_chart(np.histogram(data['started_at'].dt.hour, bins=24, range=(0,24))[0])

#   Slider hora del día
filter_time = st.sidebar.slider('Hora del día', 0, 23, 17)
st.subheader(f'Viajes de las {filter_time}:00')
st.map(data[data["started_at"].dt.hour == filter_time])
