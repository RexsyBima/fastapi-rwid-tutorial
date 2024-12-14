from fastapi import Query, Depends
from fastapi import status
from app import SECRET_KEY, ALGORITHM
from .utils import get_user
from .db import users
import jwt
from jwt.exceptions import InvalidTokenError
from app import oauth2_scheme
from datetime import datetime
from .models import User, TokenData, engine
from sqlmodel import Session
from fastapi import Request, HTTPException
from typing import Annotated


def query_parameter_function(
    start: Annotated[int, Query(ge=0)], end: Annotated[int, Query(le=10)]
):
    return {"start": start, "end": end}


class QueryParameter:
    def __init__(
        self, start: Annotated[int, Query(ge=0)], end: Annotated[int, Query(le=10)]
    ):
        self.start = start
        self.end = end


def allow_private_view(request: Request):
    if request.headers.get("auth") == "1":
        return True
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")


def decode_token(token):  # fake decode token
    return User(
        username="user1", password="user1", login_at=datetime.now(), is_active=True
    )


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    http_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise http_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise http_exception
    user = get_user(users=users, username=token_data.username)
    if user is None:
        raise http_exception
    return user


def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)]):
    if current_user.is_active is False:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def get_session():
    with Session(engine) as session:
        yield session
