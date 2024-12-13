from fastapi import APIRouter
from ...models import User
from datetime import datetime


router = APIRouter(prefix="/api/user", tags=["User Model"])

from . import post, get  # noqa
