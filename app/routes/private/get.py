from . import router
from typing import Annotated
from fastapi import Header, status, Cookie
from fastapi import Request


@router.get("/", status_code=status.HTTP_200_OK)
def get_private_view(request: Request):
    print(request.headers)
    return request.headers
