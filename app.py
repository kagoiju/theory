from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)