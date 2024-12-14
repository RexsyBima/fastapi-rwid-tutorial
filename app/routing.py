# from .routes.todo import router as todo_router
# from .routes.event import router as event_router
from .routes import product, user, private, auth
from .depends import query_parameter_function
from fastapi import Depends

from app import app

# query, path, body, header parameter
# app.include_router(todo.router)
# app.include_router(event.router)
app.include_router(product.router)
app.include_router(user.router)
app.include_router(private.router)

# ada form password, n username -> user fill form, lalu cek username  blm ada di db, maka Diperbolehkan, [add: pw kurang mantap/aman ulangi lagi]

# login -> cek username, pw, jika username dan pw betul -> login, login -> ada (state) cara supaya fastapi tahu jika user login apa nggk (somehow)
