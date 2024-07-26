from ..extensions import db
from ..models.user_model import UserModel
from ..entities.user import User


def user_update_service(id: int, user: User):
    user_db = UserModel.query.get(id)
    if not user_db:
        return {"error": "User not found"}
    
    if UserModel.query.filter(UserModel.email == user.email, UserModel.id != id).first():
        return {"error": "Email already exists"}
    
    if UserModel.query.filter(UserModel.cpf == user.cpf, UserModel.id != id).first():
        return {"error": "CPF already exists"}
    
    user_db.name = user.name
    user_db.email = user.email
    user_db.cpf = user.cpf
    if not user_db.verify_password(user.password):
        user_db.password = user.password
        user_db.encrypt_password()
    user_db.position_id = user.position_id
    user_db.active = user.active
    db.session.commit()
    
    return user_db
    
    