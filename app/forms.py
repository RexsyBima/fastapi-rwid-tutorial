from pydantic import BaseModel


class RegisterForm(BaseModel):
    username: str
    password1: str  # hashing
    password2: str
