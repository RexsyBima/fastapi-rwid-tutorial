from fastapi import APIRouter, Path, Response, status
from typing import Annotated


from app import data
from . import router


@router.get("/", status_code=status.HTTP_200_OK)
def homepage():
    return {"Hello": data}


@router.get("/{items_id}", status_code=status.HTTP_200_OK)
def get_todo(items_id: Annotated[int, Path(ge=1)]):
    return data[items_id - 1]


@router.get("/many/{items}", status_code=status.HTTP_200_OK)
def get_todos(items: Annotated[int, Path(ge=1, )], response: Response):
    if items > len(data):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"Error": "Invalid ID"}
    return data[:items]
