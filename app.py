#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 18:57:04 2023

@author: yuliannyalvarez
"""

#Se importan librerías
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# Utilizar la página completa en lugar de una columna central estrecha
st.set_page_config(layout="wide")

# Título principal, h1 denota el estilo del título 1
st.markdown("<h1 style='text-align: center; color: #006600;'>🇲🇽 Análisis socioeconómico de la población de México 🇲🇽 </h1>", unsafe_allow_html=True)

# Leer archivo con extensión csv - primera base Bienes Durables
df0 = pd.read_csv('diagnostico-cdmx_2015_bienes_dur.csv')
#Segunda base de datos-Necesidades basicas insatisfechas
df1 = pd.read_csv('gnbi2020 (1).zip')

#----------------------------------------
c1, c2= st.columns((1,1)) # Dividir el ancho en 2 columnas de igual tamaño


#renombramos variables para entendimiento
df0.rename(columns={'anio':'año','nomgeo':'demarcacion', 'mun':'id_demarcacion'}, inplace= True)

#cambiamos tipos de datos, ya que no usamos decimal para mostrar un año o un id
df0['año'].astype('int')
df0['id_demarcacion'].astype('int')

# En la información general se visualiza que no hay datos nulos pero se verifica
df0.isnull().sum()

#verificamos que no haya datos duplicados
df0.duplicated()


c1.markdown("<h3 style='text-align: center; color: black;'> ¿Qué regiones presentan la mayor cantidad de individuos en estrato social calificados como pobreza alta? </h3>", unsafe_allow_html=True)
# Se analiza la descripción para las variables numéricas
df0_pobreza_alta = df0[df0['estratos'] == 'Pobreza alta']
conteo_estratos = df0_pobreza_alta.groupby('demarcacion').size().reset_index(name='conteo')

# Ordenar los valores de forma ascendente
conteo_estratos = conteo_estratos.sort_values(by='conteo', ascending=True)

fig = px.bar(conteo_estratos, x='demarcacion', y='conteo', color='demarcacion')
fig.update_layout(title='Conteo de "Pobreza alta" por Demarcación')
fig.show()
# Enviar gráfica a streamlit
c1.plotly_chart(fig)

################ ---- Segunda Gráfica
c1.markdown("<h3 style='text-align: center; color: black;'> ¿Cuáles son los espacios territoriales que cuentan con el menor numero de personas en estrato social alto? </h3>", unsafe_allow_html=True)
df0_estrato_alto = df0[df0['estratos'] == 'Estrato alto']
conteo_estratos = df0_estrato_alto.groupby('demarcacion').size().reset_index(name='conteo')

# Ordenar los valores de forma ascendente
conteo_estratos = conteo_estratos.sort_values(by='conteo', ascending=True)

fig2 = px.bar(conteo_estratos, x='demarcacion', y='conteo', color='demarcacion')
fig2.update_layout(title='Conteo de "Estrato alto" por Demarcación')
fig2.show()
c1.plotly_chart(fig2)

################ ---- Tercera Gráfica
c2.markdown("<h3 style='text-align: center; color: black;'> ¿Segun la información recolectada, cual de los generos esta mas presente en el estrato social Pobreza Alta?</h3>", unsafe_allow_html=True)
df0_pobreza_alta = df0[df0['estratos'] == 'Pobreza alta']

conteo_estratos_sexo = df0_pobreza_alta.groupby('sexo').size().reset_index(name='conteo')

fig3 = px.pie(conteo_estratos_sexo, values='conteo', names='sexo')
fig3.update_traces(textposition='inside', textinfo='percent+label')
fig3.update_layout(title='Conteo de "Pobreza alta" por Sexo')
fig3.show()
c2.plotly_chart(fig3)

################ ---- Cuarta Gráfica
c2.markdown("<h3 style='text-align: center; color: black;'> ¿Segun la información recolectada, cual de los generos esta mas presente en el estrato social Estrato Alto?</h3>", unsafe_allow_html=True)

df0_estrato_alto = df0[df0['estratos'] == 'Estrato alto']

conteo_estratos_sexo = df0_estrato_alto.groupby('sexo').size().reset_index(name='conteo')

fig4 = px.pie(conteo_estratos_sexo, values='conteo', names='sexo')
fig4.update_traces(textposition='inside', textinfo='percent+label')
fig4.update_layout(title='Conteo de "estrato alto" por Sexo')
fig4.show()
c2.plotly_chart(fig4)

################ ---- Quinta Gráfica
c1.markdown("<h3 style='text-align: center; color: black;'> ¿Cual es la media de bienes durables para cada estrato?</h3>", unsafe_allow_html=True)

conteo_estratos_total = df0.groupby('estratos')['total'].agg(count='count', mean='mean').reset_index().sort_values('mean',ascending= False)
fig5 = px.funnel(conteo_estratos_total, x='mean', y='estratos', color='count')
fig5.update_layout(title='Gráfico Funnel de Estratos', xaxis_title='Conteo', yaxis_title='Estrato')
fig5.show()
c1.plotly_chart(fig5)

################ ---- Sexta Gráfica
c2.markdown("<h3 style='text-align: center; color: black;'> ¿Que genero cuenta con la mayor acumulación de bienes durables?</h3>", unsafe_allow_html=True)
conteo_sexo_total = df0.groupby('sexo')['total'].agg(count='count', mean='mean').reset_index().sort_values('mean',ascending= False)
fig6 = px.funnel(conteo_sexo_total, x='mean', y='sexo', color='count')
fig6.update_layout(title='Gráfico Funnel de Estratos', xaxis_title='Conteo', yaxis_title='sexo')
fig6.show()
c2.plotly_chart(fig6)

################ ---- Septima Gráfica
c1.markdown("<h3 style='text-align: center; color: black;'> ¿Cual es la variación de la pobreza alta segun la demarcación y la zona?</h3>", unsafe_allow_html=True)

df0_pobreza_alta = df0[df0['edad'] == '60 y mas']
conteo_estratos = df0_pobreza_alta.groupby('estratos').size().reset_index(name='conteo')
fig7 = px.bar(conteo_estratos, x='estratos', y='conteo', color='estratos')
fig7.update_layout(title='Conteo de "Pobreza alta" por Demarcación')
fig7.show()
c1.plotly_chart(fig7)

################ ---- Octava Gráfica

# Calcular la frecuencia de cada valor en la columna 'tam_hog'
frequency = df1['tam_hog'].value_counts()

# Ordenar los valores en orden descendente
sorted_frequency = frequency.sort_values(ascending=False)

# Calcular el porcentaje acumulado
cumulative_percentage = sorted_frequency.cumsum()/sorted_frequency.sum()*100

# Crear un gráfico de barras para la frecuencia ordenada
fig8, ax = plt.subplots()
ax.bar(range(len(sorted_frequency)), sorted_frequency.values,color='blue')
ax.set_xticks(range(len(sorted_frequency)))
ax.set_xticklabels(sorted_frequency.index)

# Crear un gráfico de líneas para el porcentaje acumulado
ax2 = ax.twinx()
ax2.plot(range(len(cumulative_percentage)), cumulative_percentage.values, color='red', marker='D')

# Establecer la etiqueta del eje y para el gráfico de líneas
ax2.set_ylabel('Porcentaje acumulado')

# Establecer la etiqueta del eje x
ax.set_xlabel('tam_hog')

# Establecer el título
ax.set_title('Gráfico de Pareto')

plt.show()
st.pyplot(fig8)

################ ---- Novena Gráfica
c2.markdown("<h3 style='text-align: center; color: black;'> Ingresio promedio del hogar por grupos de edad</h3>", unsafe_allow_html=True)
# Agrupa los datos por grupos de edad y calcula el ingreso promedio del hogar
age_groups = pd.cut(df1['edad'], bins=[0, 18, 30, 40, 50, 60, 100])
avg_income_by_age = df1.groupby(age_groups)['ingtrhog'].mean()

# Crea el gráfico de línea
fig9, ax = plt.subplots()
avg_income_by_age.plot(kind='line', marker='o', ax=ax)
ax.set_xlabel('Grupo de Edad')
ax.set_ylabel('Ingreso Promedio del Hogar')
c2.plotly_chart(fig9)
