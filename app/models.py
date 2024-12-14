from pydantic import BaseModel
from datetime import datetime
from sqlmodel import SQLModel, create_engine, Field


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


class Product(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    price: int = Field(ge=0.0)
    quantity: int = Field(ge=0.0)

    model_config = {  # type: ignore
        "json_schema_extra": {
            "examples": [
                {
                    "title": "Foo",
                    "price": 1000,
                    "quantity": 1,
                }
            ]
        }
    }


class User(BaseModel):
    username: str
    password: str
    login_at: datetime
    is_active: bool


class UserDB(User):
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


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


sqlite_filename = "database.db"
sqlite_url = f"sqlite:///{sqlite_filename}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
