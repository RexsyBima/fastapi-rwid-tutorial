from . import router
from ...db import users
from fastapi import Query, Depends
from typing import Annotated
from ...models import User
from ...depends import QueryParameter, get_current_user, get_current_active_user
from fastapi import status


@router.get('/get_users/', status_code=status.HTTP_202_ACCEPTED)
def get_users(params: Annotated[QueryParameter, Depends()]) -> list[User]:
    return users[params.start:params.end]


@router.get('/me/', status_code=status.HTTP_200_OK)
def get_me(current_user: Annotated[User, Depends(get_current_active_user)]) -> User:
    return current_user
