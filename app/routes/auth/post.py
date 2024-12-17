from app import app
from datetime import timedelta
from fastapi import HTTPException
from fastapi import status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from ...models import Token
from ...db import users
from ...utils import authenticate_user, create_accesss_token
from app import oauth2_scheme
from fastapi import Depends


@app.get("/hello_token/")
def hello_token(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"message": "Hello Auth",
            "token": token}


@app.post('/token')
def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    # TODO: fix authentication flow... now using database
    # TODO: unrelated, calculate the total price of user cart products
    user = authenticate_user(users, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect username or password", headers={"WWW-Authenticate": "Bearer"})
    access_token_expires = timedelta(minutes=30)
    access_token = create_accesss_token(
        data={"sub": user.username}, expires_delta=access_token_expires)
    return Token(access_token=access_token, token_type="bearer")

    # user = [user for user in users if user.username ==
    #         form_data.username and user.password == form_data.password]
    # if len(user) == 1:
    #     user = user[0]
    #     return {"access_token": user.username, "token_type": "bearer"}
    # else:
    #     raise HTTPException(
    #         status_code=400, detail="Incorrect username or password")
