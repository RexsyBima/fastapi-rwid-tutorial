# from .routes.todo import router as todo_router
# from .routes.event import router as event_router
from .routes import todo, event

from app import app

app.include_router(todo.router)
app.include_router(event.router)
