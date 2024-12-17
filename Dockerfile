# Используем Python 3.10 как базовый образ
FROM python:3.10-slim

# Установим рабочую директорию
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r app/requirements.txt

# Открываем порты для FastAPI и Streamlit
EXPOSE 8501
EXPOSE 8000

# Запускаем приложение Streamlit и FastAPI
CMD ["sh", "-c", "streamlit run app/insights.py & uvicorn app.main:app --reload"]