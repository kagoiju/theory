from pydantic import BaseModel, Field, field_validator, EmailStr
from typing import Optional

# версия User (с возрастом)
class User(BaseModel):
    name: str
    age: int

# Вложенная модель для контактов
class Contact(BaseModel):
    email: EmailStr
    phone: Optional[str] = Field(None, min_length=7, max_length=15, pattern=r"^\d+$")

# Финальная версия Feedback (с валидацией и контактами)
class Feedback(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    message: str = Field(..., min_length=10, max_length=500)
    contact: Contact 

    @field_validator("message")
    @classmethod
    def check_bad_words(cls, v: str):
        bad_words = ["редиска", "бяка", "козявка"]
        v_lower = v.lower()
        for word in bad_words:
            if word in v_lower:
                raise ValueError("Использование недопустимых слов")
        return v