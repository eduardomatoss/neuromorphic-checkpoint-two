import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

from app.database.dataframe import create_dataframe

st.set_option("deprecation.showPyplotGlobalUse", False)


def load_page():
    df = create_dataframe()

    st.title("Neuromorphic Computing and Supercomputers")

    sns.scatterplot(x="temperature", y="moisture", data=df)

    plt.title("Relação temperatura x umidade")
    st.pyplot()
