from sqladmin import Admin, ModelView
from . import app
from .models import User, Product, engine

admin = Admin(app, engine)


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.username,  # type: ignore
                   User.email, User.login_at, User.is_active, User.password]


class ProductAdmin(ModelView, model=Product):
    column_list = [Product.id, Product.title,  # type: ignore
                   Product.price, Product.quantity]


admin.add_view(UserAdmin)
admin.add_view(ProductAdmin)
