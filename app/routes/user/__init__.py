from fastapi import APIRouter
from ...models import User
from datetime import datetime


router = APIRouter(prefix="/api/user", tags=["User Model"])
users: list[User] = [
    User(username="user1", password="user1", login_at=datetime.now()),
    User(username="user2", password="user2", login_at=datetime.now()),
    User(username="user3", password="user3", login_at=datetime.now()),
    User(username="user4", password="user4", login_at=datetime.now()),
    User(username="user5", password="user5", login_at=datetime.now()),
]

from . import post, get  # noqa
