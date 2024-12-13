from app import app
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from ...models import users
from app import oauth2_scheme
from fastapi import Depends


@app.get("/hello_token/")
def hello_token(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"message": "Hello Auth",
            "token": token}


@app.post('/token')
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = [user for user in users if user.username ==
            form_data.username and user.password == form_data.password]
    if len(user) == 1:
        user = user[0]
        return {"access_token": user.username, "token_type": "bearer"}
    else:
        raise HTTPException(
            status_code=400, detail="Incorrect username or password")
