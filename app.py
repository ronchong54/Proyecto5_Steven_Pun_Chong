import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Crear un encabezado
st.header('Análisis de Datos de Vehículos Usados')

# Casilla de verificación para construir un histograma del precio
build_histogram_price = st.checkbox('Construir histograma del precio')

if build_histogram_price:
    st.write(
        'Construcción de un histograma para la distribución del precio de los vehículos')
    fig_hist_price = px.histogram(
        car_data, x="price", title='Distribución del Precio de los Vehículos')
    st.plotly_chart(fig_hist_price, use_container_width=True)

# Casilla de verificación para construir un gráfico de dispersión del precio vs. año del modelo
build_scatter = st.checkbox(
    'Construir gráfico de dispersión del precio vs. año del modelo')

if build_scatter:
    st.write(
        'Construcción de un gráfico de dispersión para el precio vs. año del modelo')
    fig_scatter = px.scatter(car_data, x='model_year',
                             y='price', title='Precio vs. Año del Modelo')
    st.plotly_chart(fig_scatter, use_container_width=True)

# Casilla de verificación para construir un box plot del precio según la condición del vehículo
build_box = st.checkbox('Construir box plot del precio según la condición')

if build_box:
    st.write(
        'Construcción de un box plot para el precio según la condición del vehículo')
    fig_box = px.box(car_data, x='condition', y='price',
                     title='Precio según la Condición del Vehículo')
    st.plotly_chart(fig_box, use_container_width=True)

# Casilla de verificación para construir un gráfico de barras del número de vehículos por tipo de combustible
build_bar = st.checkbox('Construir gráfico de barras por tipo de combustible')

if build_bar:
    st.write(
        'Construcción de un gráfico de barras para el número de vehículos por tipo de combustible')
    fig_bar = px.bar(car_data, x='fuel',
                     title='Número de Vehículos por Tipo de Combustible')
    st.plotly_chart(fig_bar, use_container_width=True)

# Casilla de verificación para construir un gráfico de dispersión del precio vs. kilometraje
build_scatter_km = st.checkbox(
    'Construir gráfico de dispersión del precio vs. kilometraje')

if build_scatter_km:
    st.write('Construcción de un gráfico de dispersión para el precio vs. kilometraje')
    fig_scatter_km = px.scatter(
        car_data, x='odometer', y='price', title='Precio vs. Kilometraje')
    st.plotly_chart(fig_scatter_km, use_container_width=True)
