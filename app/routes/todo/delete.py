from app import data
from typing import Annotated
from app.models import new_todo
from . import router
from fastapi import APIRouter, Path, status, Response


@router.delete("/todo/{items_id}", status_code=status.HTTP_202_ACCEPTED)
def remove_todo(items_id: Annotated[int, Path(ge=1)], response: Response):
    if items_id > len(data):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"Error": "Invalid ID"}
    data.pop(items_id - 1)
    return {"Success": "Todo removed"}
