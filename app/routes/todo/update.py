# add new todo

from typing import Annotated
from app import data
from fastapi import APIRouter, Response, status, Path

from . import router


@router.put("/{item_id}/{status}")
def update_todo(item_id: Annotated[int, Path(ge=1)], is_completed: bool, response: Response):
    item_id = item_id - 1
    # 0 1 2 3
    if item_id < len(data):
        data[item_id].is_completed = is_completed
        return {"Success": "Todo updated"}
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"Error": "Invalid ID"}
