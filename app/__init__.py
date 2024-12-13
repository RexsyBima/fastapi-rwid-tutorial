from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from .models import new

data = new()
app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

from . import routing  # noqa
