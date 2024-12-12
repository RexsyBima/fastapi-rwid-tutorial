from app import data
from typing import Annotated
from app.models import Todo
from fastapi import APIRouter, Path, status, Response
from . import router


@router.post("/create_todo/", status_code=status.HTTP_201_CREATED)
def add_todo(response: Response, todo: Todo | None = None):
    if todo is not None:
        data.append(todo)
        return {"Success": "Todo added"}
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"Error": "Invalid data"}
