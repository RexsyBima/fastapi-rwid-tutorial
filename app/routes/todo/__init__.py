from fastapi import APIRouter

router = APIRouter(prefix="/api/todo", tags=["Todo Model"])


from . import get, create, delete, update  # noqa
