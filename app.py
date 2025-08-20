import pandas as pd
import streamlit as st
import plotly as pl
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')

st.header("Proyecto Sprint 7")
st.dataframe(car_data)

build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    st.write('Construyendo histograma para la columna odómetro...')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer", title='Histograma del odómetro')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Casilla para construir gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter:
    st.write('Construyendo gráfico de dispersión: precio vs odómetro...')

    # crear un histograma
    fig2 = px.scatter(car_data, x="odometer", y='price',
                      title='Relación entre odómetro y precio')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)
