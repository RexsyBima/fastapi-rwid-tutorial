from pydantic import BaseModel
from datetime import datetime
from sqlmodel import SQLModel, create_engine, Field


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


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(unique=True)
    email: str = Field(unique=True)
    password: str  # hashed password
    login_at: datetime | None = Field(default=None)
    is_active: bool = Field(default=False)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


sqlite_filename = "database.db"
sqlite_url = f"sqlite:///{sqlite_filename}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
