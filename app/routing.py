# from .routes.todo import router as todo_router
# from .routes.event import router as event_router
from .routes import todo, event, product, user, private
from .routes.depends import query_parameter_function
from fastapi import Depends

from app import app

# query, path, body, header parameter
# app.include_router(todo.router)
# app.include_router(event.router)
app.include_router(product.router, dependencies=[
                   Depends(query_parameter_function)])
app.include_router(user.router)
app.include_router(private.router)
