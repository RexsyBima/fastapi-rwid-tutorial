from typing import Annotated
from app.utils import hash_password
from sqlmodel import Session, select
from app.depends import get_session
from fastapi import Form, Depends, HTTPException
from . import router
from fastapi import status
from ...forms import RegisterForm
from app.models import User


@router.post("register/", status_code=status.HTTP_201_CREATED)
def register(form: Annotated[RegisterForm, Form()], session: Annotated[Session, Depends(get_session)]) -> int:
    # handling register form masuk ke database
    # check username, n email udah ada didalam db apa blm
    # kalau udah ada, return error, jngn dimasukan kedalam DB
    # kalau username n email blm ada -> Ok, -> bikin model User berdasarkan formulir yg user, password harus di HASH!!!!!, session.add session.commit
    if form.password1 != form.password2:
        raise HTTPException(status_code=400, detail="Passwords do not match")
    user = session.exec(select(User).where(
        User.username == form.username or User.email == form.email)).first()
    if user:
        raise HTTPException(
            status_code=400, detail="Username or email already exists")
    else:
        user = User(username=form.username, email=form.email,
                    password=hash_password(form.password1))
        session.add(user)
        session.commit()
        print("User added to database")
        return status.HTTP_201_CREATED
