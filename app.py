# app.py
from fastapi import FastAPI
from pydantic import BaseModel
from models import User, Feedback  # Импортируем модели

app = FastAPI()

# Создаем экземпляр (объект) пользователя
fake_user = User(name="John Doe", id=1)

# База данных для отзывов
fake_feedbacks = []

# 4. фидбэк
app = FastAPI()
@app.post("/feedback")
async def send_feedback(feed: Feedback):
    # 1. Сохраняем полученный отзыв в наш список
    fake_feedbacks.append({"name": feed.name, "message": feed.message})
    
    # 2. Возвращаем ответ по шаблону из задания
    return {"message": f"Feedback received. Thank you, {feed.name}."}

# 1. Создаем модель данных, которую ожидаем от пользователя
class CalculationRequest(BaseModel):
    num1: int
    num2: int

# 2. Создаем маршрут /calculate, который принимает POST-запрос
@app.post("/calculate")
async def calculate(data: CalculationRequest):
    result = data.num1 + data.num2
    return {"result": result}

#  старый код для приветствия 
@app.get("/")
async def read_root():
    return {"message": "App is running!"}

# 3. Новый маршрут /users
@app.get("/users")
async def get_user():
    # Просто возвращаем объект, FastAPI сам превратит его в JSON
    return fake_user

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)