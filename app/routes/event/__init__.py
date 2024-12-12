
from fastapi import APIRouter

router = APIRouter(prefix="/api/event", tags=["Event Model"])


from . import get, create, delete, update  # noqa
