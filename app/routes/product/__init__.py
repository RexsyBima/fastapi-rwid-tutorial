from fastapi import APIRouter

router = APIRouter(prefix="/api/product", tags=["Product Model"])

from . import get, create, delete, update  # noqa
