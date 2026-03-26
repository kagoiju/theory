from pydantic import BaseModel

class User(BaseModel):
    name: str
    id: int

# Новая модель для отзывов
class Feedback(BaseModel):
    name: str
    message: str