from sqladmin import Admin, ModelView
# from fastapi import HTTPException
import os
from app.utils import verify_password
from .enums import Role
from sqlmodel import select
from starlette.requests import Request
from sqladmin.authentication import AuthenticationBackend
from .utils import hash_password
from . import app
from .models import User, Product, engine, session, Cart


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request):
        form = await request.form()
        username, password = form['username'], form['password']
        print(username, password)
        user = session.exec(select(User).where(
            User.username == username and User.role == Role.admin)).first()
        if user is None:
            return False
        if not verify_password(password, user.password):  # type: ignore
            return False
        request.session.update({'token': user.username})
        return True

    async def logout(self, request: Request):
        request.session.clear()
        return True

    async def authenticate(self, request: Request):
        token = request.session.get('token')
        user = session.exec(select(User).where(
            User.username == token)).first()
        if user is None or user.role != Role.admin:
            return False
        return True


authentication_backend = AdminAuth(
    os.getenv("FASTAPI_SECRET_KEY"))  # type: ignore
admin = Admin(app, engine, authentication_backend=authentication_backend)


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.username,  # type: ignore
                   User.email, User.login_at, User.is_active, User.password, User.role]

    async def insert_model(self, request, data):
        data['password'] = hash_password(data['password'])
        return await super().insert_model(request, data)

    async def update_model(self, request, pk: str, data: dict):
        user = session.exec(select(User).where(
            User.username == data['username'])).first()
        if user.password != data['password']:  # type: ignore
            data['password'] = hash_password(data['password'])
        return await super().update_model(request, pk, data)

    async def on_model_delete(self, model: User, request: Request) -> None:
        # send_email(model.email)
        return await super().on_model_delete(model, request)


class ProductAdmin(ModelView, model=Product):
    column_list = [Product.id, Product.title,  # type: ignore
                   Product.price, Product.quantity]


class CartAdmin(ModelView, model=Cart):
    column_list = [Cart.user_id, Cart.product_id]  # type: ignore


admin.add_view(UserAdmin)
admin.add_view(ProductAdmin)
admin.add_view(CartAdmin)
