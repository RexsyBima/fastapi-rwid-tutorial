from . import pwd_context
from app import ALGORITHM, SECRET_KEY
from datetime import timedelta, datetime
import jwt
from fastapi import HTTPException
from .models import User


def get_user(users: list[User], username: str | None) -> User | None:
    user = [user for user in users if user.username == username]
    if len(user) == 1:
        return user[0]
    else:
        return None


def authenticate_user(users: list[User], username: str, password: str) -> User:
    user = [user for user in users if user.username == username]
    if len(user) == 1:
        user = user[0]
    else:
        raise HTTPException(
            status_code=400, detail="Incorrect username or password")
    if not verify_password(password, user.password):
        # return False
        raise HTTPException(
            status_code=400, detail="Incorrect username or password")
    return user


def hash_password(password: str) -> str:
    return pwd_context.hash(password)  # return hashed password


def verify_password(user_input_password: str, hashed_password: str) -> bool:
    # return bool value of user password and input password
    return pwd_context.verify(secret=user_input_password, hash=hashed_password)


def create_accesss_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY,
                             algorithm=ALGORITHM)
    return encoded_jwt
