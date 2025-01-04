from fastapi import APIRouter


router = APIRouter(prefix="/api/user", tags=["User Model"])

from . import post, get, create, delete  # noqa
