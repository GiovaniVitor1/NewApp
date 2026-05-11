import pandas as pd
import plotly.express as px
import streamlit as st

# cabeçalho
st.header("Dashboard de Anúncios de Carros")

# descrição
st.write(
    """
    Este aplicativo permite visualizar dados de anúncios de carros.
    """
)

# ler csv
car_data = pd.read_csv("vehicles_us.csv")

# mostrar tabela
st.subheader("Dados do conjunto")
st.dataframe(car_data.head())

# botão histograma
hist_button = st.button("Criar histograma")

if hist_button:
    st.write("Histograma da quilometragem")
    
    fig = px.histogram(
        car_data,
        x="odometer"
    )

    st.plotly_chart(fig, use_container_width=True)

# botão dispersão
scatter_button = st.button("Criar gráfico de dispersão")

if scatter_button:
    st.write("Relação entre preço e quilometragem")

    fig = px.scatter(
        car_data,
        x="odometer",
        y="price"
    )

    st.plotly_chart(fig, use_container_width=True)