from .models import User
from datetime import datetime
from .utils import hash_password

users: list[User] = [
    User(
        username="user1", password=hash_password("user1"),
        login_at=datetime.now(), is_active=True
    ),
    User(
        username="user2", password=hash_password("user2"),
        login_at=datetime.now(), is_active=True
    ),
    User(
        username="user3", password=hash_password("user3"),
        login_at=datetime.now(), is_active=True
    ),
]
