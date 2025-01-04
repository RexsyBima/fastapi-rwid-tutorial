from fastapi import FastAPI
import os
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from .models import create_db_and_tables

app = FastAPI()
ALGORITHM = "HS256"  # menandakan bahawa VARIABELNYA JANGAN SAMPAI DIGANTI
# menandakan bahawa VARIABELNYA JANGAN SAMPAI DIGANTI
SECRET_KEY = str(os.getenv("FASTAPI_SECRET_KEY"))

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.on_event("startup")
def on_startup():
    from app.models import create_db_and_tables, session, User
    from app.enums import Role
    from app.utils import hash_password

    password = "password"
    create_db_and_tables()
    user = User(username="admin", email="admin",
                password=hash_password(password), role=Role.admin)
    session.add(user)
    session.commit()


from . import admin  # noqa
from . import routing  # noqa
