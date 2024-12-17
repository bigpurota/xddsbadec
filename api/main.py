from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from catboost import CatBoostRegressor, Pool

app = FastAPI()

# Загружаем модель CatBoost
model = CatBoostRegressor()
model.load_model(
    "model/catboost_model.cbm")

# Обработчик для корневого пути


@app.get("/")
def read_root():
    return {"message": "Welcome to the YouTube Analytics Prediction API!"}

# Модель для запроса данных


class PredictionRequest(BaseModel):
    Subscribers: int
    Video_Duration: int
    Day_of_Week: int

# Обработчик для предсказания


@app.post("/predict/")
def predict(request: PredictionRequest):
    features = np.array(
        [request.Subscribers, request.Video_Duration, request.Day_of_Week]).reshape(1, -1)

    # Создайте Pool с правильными индексации для категориальных признаков, если они есть
    

    prediction = model.predict(features)
    return {"prediction": prediction[0]}
