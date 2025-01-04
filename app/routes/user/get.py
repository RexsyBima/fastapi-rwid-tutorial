from . import router
from fastapi import Depends
from app import oauth2_scheme
from typing import Annotated
from ...models import User
from ...depends import get_current_active_user
from fastapi import status


@router.get('/me/', status_code=status.HTTP_200_OK)
def get_me(current_user: Annotated[User, Depends(get_current_active_user)]) -> User:
    return current_user


@router.get('/whoami/', status_code=status.HTTP_200_OK)
def read_me(token: Annotated[str, Depends(oauth2_scheme)]):
    # TODO: explain this shit
    # token = jwt.decode(token, key=SECRET_KEY, algorithms=[ALGORITHM])

    return {"token": token}
