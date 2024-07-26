from ..extensions import db
from ..models.user_model import UserModel
from ..entities.user import User

def user_register_service(user: User):
    user_db = UserModel(name=user.name, email=user.email, cpf=user.cpf,
                        password=user.password, position_id=user.position_id)
    user_db.encrypt_password()
    db.session.add(user_db)
    db.session.commit()
    return user_db

def login_service():
    ...

