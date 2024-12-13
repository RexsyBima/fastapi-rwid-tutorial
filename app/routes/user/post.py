from typing import Annotated
from fastapi import Form
from . import router
from fastapi import status
from ...forms import RegisterForm


@router.post("register/", status_code=status.HTTP_201_CREATED)
def register(form: Annotated[RegisterForm, Form()]) -> int:
    # handling register form masuk ke database

    return status.HTTP_201_CREATED
