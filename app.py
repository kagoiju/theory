from fastapi import FastAPI, Query
from pydantic import BaseModel
from models import User, Feedback  # Импортируем модели

app = FastAPI()

# Данные
fake_user = User(name="John Doe", age=25)
feedbacks_db = [] # Единая база для отзывов

# СТАРЫЕ ЗАДАНИЯ

@app.get("/")
async def read_root():
    return {"message": "App is running!"}

class CalculationRequest(BaseModel):
    num1: int
    num2: int

@app.post("/calculate")
async def calculate(data: CalculationRequest):
    result = data.num1 + data.num2
    return {"result": result}

@app.get("/users")
async def get_user():
    return fake_user

# НОВЫЕ ЗАДАНИЯ (ЛР5)

# Задание 2.2: Проверка возраста
@app.post("/user")
async def check_user_age(user: User):
    is_adult = user.age >= 18
    return {
        "name": user.name,
        "age": user.age,
        "is_adult": is_adult
    }

# Задание 2.3: Отзывы (финальная версия)
@app.post("/feedback")
async def create_feedback(fb: Feedback, is_premium: bool = Query(False)):
    feedbacks_db.append(fb)
    msg = f"Спасибо, {fb.name}! Ваш отзыв сохранён."
    if is_premium:
        msg += " Ваш отзыв будет рассмотрен в приоритетном порядке."
    return {"message": msg}

@app.get("/feedback")
async def get_all_feedbacks():
    return feedbacks_db

# Запуск
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)