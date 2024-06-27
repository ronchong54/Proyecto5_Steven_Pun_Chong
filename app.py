import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')


# Crear un encabezado
st.header('Análisis de Datos de Vehículos Usados')

# Botón para construir un histograma del precio
hist_button = st.button('Construir histograma del precio')

if hist_button:
    fig_hist_price = px.histogram(
        car_data, x="price", title='Distribución del Precio de los Vehículos')
    st.plotly_chart(fig_hist_price, use_container_width=True)

# Botón para construir un gráfico de dispersión del precio vs. año del modelo
scatter_button = st.button(
    'Construir gráfico de dispersión del precio vs. año del modelo')

if scatter_button:
    fig_scatter = px.scatter(car_data, x='model_year',
                             y='price', title='Precio vs. Año del Modelo')
    st.plotly_chart(fig_scatter, use_container_width=True)

# Botón para construir un box plot del precio según la condición del vehículo
box_button = st.button('Construir box plot del precio según la condición')

if box_button:
    fig_box = px.box(car_data, x='condition', y='price',
                     title='Precio según la Condición del Vehículo')
    st.plotly_chart(fig_box, use_container_width=True)

# Botón para construir un gráfico de barras del número de vehículos por tipo de combustible
bar_button = st.button('Construir gráfico de barras por tipo de combustible')

if bar_button:
    fig_bar = px.bar(car_data, x='fuel',
                     title='Número de Vehículos por Tipo de Combustible')
    st.plotly_chart(fig_bar, use_container_width=True)

# Botón para construir un gráfico de dispersión del precio vs. kilometraje
scatter_km_button = st.button(
    'Construir gráfico de dispersión del precio vs. kilometraje')

if scatter_km_button:
    fig_scatter_km = px.scatter(
        car_data, x='odometer', y='price', title='Precio vs. Kilometraje')
    st.plotly_chart(fig_scatter_km, use_container_width=True)
