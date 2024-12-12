from pydantic import BaseModel
from datetime import datetime


class Event(BaseModel):
    name: str


class Item(BaseModel):
    name: str


class Todo(BaseModel):
    id: int
    title: str
    is_important: bool
    is_completed: bool = False
    date: datetime


def new() -> list[Todo]:
    return [
        Todo(id=1, title="Todo 1", is_important=False, date=datetime.now()),
        Todo(id=2, title="Todo 2", is_important=False, date=datetime.now()),
        Todo(id=3, title="Todo 3", is_important=True, date=datetime.now()),
        Todo(id=4, title="Todo 4", is_important=True, date=datetime.now()),
        Todo(id=5, title="Todo 5", is_important=True, date=datetime.now()),
        Todo(id=6, title="Todo 6", is_important=True, date=datetime.now()),
        Todo(id=7, title="Todo 7", is_important=True, date=datetime.now()),
    ]


def new_todo(id: int) -> Todo:
    return Todo(id=id, title=f"Todo {id}", is_important=True, date=datetime.now())
