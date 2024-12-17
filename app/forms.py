from pydantic import BaseModel, EmailStr


class RegisterForm(BaseModel):
    username: str
    email: EmailStr
    password1: str  # hashing
    password2: str
