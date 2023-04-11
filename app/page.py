import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

from app.database.dataframe import create_dataframe
from app.services.linear_regression import predict_model

st.set_option("deprecation.showPyplotGlobalUse", False)


def load_page():
    df = create_dataframe()

    st.title("Neuromorphic Computing and Supercomputers")

    sns.scatterplot(x="temperature", y="moisture", data=df)

    plt.title("Relação temperatura x umidade")
    st.pyplot()

    plt.figure(figsize=(10, 10))
    sns.heatmap(df.corr(), annot=True)
    plt.title("Correlação Dados")
    st.pyplot()

    X_test, y_test, y_pred, r2, mse, mae = predict_model(df)

    st.text(f"Coeficiente de Determinação (R²): {r2}")
    st.text(f"Erro Quadrático Médio (MSE): {mse}")
    st.text(f"Erro Absoluto Médio (MAE): {mae}")
