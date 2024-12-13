from fastapi import Query, Depends
from app import oauth2_scheme
from datetime import datetime
from ..models import User
from fastapi import Request, HTTPException
from typing import Annotated


def query_parameter_function(start: Annotated[int, Query(ge=0)], end: Annotated[int, Query(le=10)]):
    return {
        "start": start,
        "end": end
    }


class QueryParameter:
    def __init__(self, start: Annotated[int, Query(ge=0)], end: Annotated[int, Query(le=10)]):
        self.start = start
        self.end = end


def allow_private_view(request: Request):
    if request.headers.get("auth") == "1":
        return True
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")


def decode_token(token):  # fake decode token
    return User(username="user1", password="user1", login_at=datetime.now())


def get_current_user(user: Annotated[User, Depends(oauth2_scheme)]):
    user = decode_token(user)
    return user
