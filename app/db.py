from .models import UserDB
from datetime import datetime
from .utils import hash_password

users: list[UserDB] = [
    UserDB(username="user1", password="user1",
           login_at=datetime.now(), is_active=True, hashed_password=hash_password("user1")),
    UserDB(username="user2", password="user2", hashed_password=hash_password("user2"),
           login_at=datetime.now(), is_active=False),
    UserDB(username="user3", password="user3", hashed_password=hash_password("user3"),
           login_at=datetime.now(), is_active=False),
    UserDB(username="user4", password="user4", hashed_password=hash_password("user4"),
           login_at=datetime.now(), is_active=True),
    UserDB(username="user5", password="user5", hashed_password=hash_password("user5"),
           login_at=datetime.now(), is_active=True),
]
