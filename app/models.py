from pydantic import BaseModel, EmailStr
from .enums import Role
from datetime import datetime
from sqlmodel import SQLModel, create_engine, Field, Session, Relationship


class Cart(SQLModel, table=True):
    user_id: int | None = Field(
        default=None, foreign_key="user.id", primary_key=True)
    product_id: int | None = Field(
        default=None, foreign_key="product.id", primary_key=True)


class Product(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    price: int = Field(ge=0.0, default=0)
    quantity: int = Field(ge=0.0, default=0)

    users: list["User"] = Relationship(
        back_populates="products", link_model=Cart)
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
    email: EmailStr = Field(unique=True)
    password: str  # hashed password
    login_at: datetime | None = Field(default=None)
    is_active: bool = Field(default=False)
    role: Role = Field(default=Role.user)
    products: list["Product"] = Relationship(
        back_populates="users", link_model=Cart)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


sqlite_filename = "database.db"
sqlite_url = f"sqlite:///{sqlite_filename}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)

session = Session(engine)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
