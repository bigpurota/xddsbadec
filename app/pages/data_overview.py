
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache
def load_data():
    return pd.read_csv('data/youtube_channel_real_performance_analytics.csv')

data = load_data()

st.title("Обзор данных")
st.write("**Таблица данных:**")
st.dataframe(data)

st.write("**Основные метрики:**")
st.write(data.describe())

st.write("**Корреляционная матрица:**")
fig, ax = plt.subplots(figsize=(12, 8))
sns.heatmap(data.corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
st.pyplot(fig)
