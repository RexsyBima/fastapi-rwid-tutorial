from app.models import create_db_and_tables, session, User
from app.enums import Role
from app.utils import hash_password

password = "password"
create_db_and_tables()
user = User(username="admin", email="admin",
            password=hash_password(password), role=Role.admin)
session.add(user)
session.commit()
