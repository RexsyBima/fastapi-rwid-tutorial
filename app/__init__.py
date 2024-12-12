from fastapi import FastAPI
from .models import new

data = new()
app = FastAPI()

from . import routing  # noqa
