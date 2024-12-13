from fastapi import FastAPI
import os
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from .models import new

data = new()
app = FastAPI()
ALGORITHM = "HS256"  # menandakan bahawa VARIABELNYA JANGAN SAMPAI DIGANTI
# menandakan bahawa VARIABELNYA JANGAN SAMPAI DIGANTI
SECRET_KEY = str(os.getenv("FASTAPI_SECRET_KEY"))

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

from . import routing  # noqa
