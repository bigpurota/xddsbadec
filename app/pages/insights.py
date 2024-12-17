import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Загрузка данных


@st.cache
def load_data():
    return pd.read_csv('data/youtube_channel_real_performance_analytics.csv')


data = load_data()

st.title("📊 Инсайты и Аналитика YouTube Канала")

# 1. График зависимости просмотров от подписчиков
st.subheader("1. Зависимость просмотров от количества подписчиков")
st.write("График показывает, как количество просмотров зависит от числа подписчиков.")
fig1 = px.scatter(
    data,
    x='Subscribers',
    y='Views',
    color='Month',
    size='Views',
    hover_data=['Views'],
    title="Зависимость просмотров от подписчиков",
    labels={"Subscribers": "Подписчики", "Views": "Просмотры"}
)
st.plotly_chart(fig1)

# 2. График распределения заработка по месяцам
st.subheader("2. Заработок по месяцам")
st.write("Столбчатая диаграмма отображает заработок за каждый месяц.")
if 'Month' in data.columns and 'Estimated Revenue (USD)' in data.columns:
    fig2 = px.bar(
        data,
        x='Month',
        y='Estimated Revenue (USD)',
        title="Распределение заработка по месяцам",
        labels={"Month": "Месяц", "Estimated Revenue (USD)": "Доход (USD)"},
        color='Month'
    )
    st.plotly_chart(fig2)
else:
    st.write("Данные о заработке по месяцам недоступны.")

# 3. График распределения количества просмотров
st.subheader("3. Распределение количества просмотров")
st.write("Гистограмма, отображающая, как распределяется количество просмотров на канале.")
fig3 = px.histogram(
    data,
    x='Views',
    nbins=50,
    title="Распределение количества просмотров",
    labels={"Views": "Просмотры"}
)
st.plotly_chart(fig3)

# 4. Зависимость количества комментариев от подписчиков
st.subheader("4. Зависимость количества комментариев от подписчиков")
st.write("Показывает, сколько комментариев оставляют пользователи в зависимости от числа подписчиков.")
if 'New Comments' in data.columns:
    fig4 = px.scatter(
        data,
        x='Subscribers',
        y='New Comments',
        color='Month',
        size='Views',
        hover_data=['New Comments'],
        title="Зависимость количества комментариев от подписчиков",
        labels={"Subscribers": "Подписчики", "New Comments": "Комментарии"}
    )
    st.plotly_chart(fig4)
else:
    st.write("Данные о комментариях недоступны.")

# 5. Boxplot просмотров по месяцам
st.subheader("5. Распределение просмотров по месяцам")
st.write("Boxplot показывает, как просмотры варьируются в зависимости от месяца.")
if 'Month' in data.columns:
    fig5 = px.box(
        data,
        x='Month',
        y='Views',
        color='Month',
        title="Boxplot просмотров по месяцам",
        labels={"Month": "Месяц", "Views": "Просмотры"}
    )
    st.plotly_chart(fig5)
else:
    st.write("Нет данных для построения графика распределения просмотров по месяцам.")

# 6. Изменение просмотров по времени
st.subheader("6. Изменение просмотров по времени")
st.write("Линейный график, показывающий изменение просмотров со временем.")
if 'Video Publish Time' in data.columns:
    data['Video Publish Time'] = pd.to_datetime(data['Video Publish Time'])
    fig6 = px.line(
        data,
        x='Video Publish Time',
        y='Views',
        title="Изменение просмотров по времени",
        labels={"Video Publish Time": "Время публикации", "Views": "Просмотры"}
    )
    st.plotly_chart(fig6)
else:
    st.write("Данные о времени публикации недоступны.")
