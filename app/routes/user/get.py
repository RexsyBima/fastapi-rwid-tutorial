from . import router, users
from fastapi import Query, Depends
from typing import Annotated
from ...models import User
from ..depends import QueryParameter
from fastapi import status


@router.get('/get_users/', status_code=status.HTTP_202_ACCEPTED)
def get_users(params: Annotated[QueryParameter, Depends()]) -> list[User]:
    return users[params.start:params.end]
