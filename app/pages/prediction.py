import streamlit as st
import requests

# Адрес вашего FastAPI сервера
API_URL = "http://127.0.0.1:8000/predict/"

st.title("Предсказания")

st.write("Введите значения для предсказания:")
input_data = {
    "Subscribers": st.number_input("Кол-во подписчики:", min_value=0),
    "Video_Duration": st.number_input("Длительность видео:", min_value=0),
    "Day_of_Week": st.number_input("День недели:", min_value=0),
}

if st.button("Предсказать"):
    # Отправка данных на сервер FastAPI
    response = requests.post(API_URL, json=input_data)

    if response.status_code == 200:
        prediction = response.json().get('prediction')
        st.write(f"Прогноз: {prediction}")
    else:
        st.error("Произошла ошибка при получении прогноза.")

