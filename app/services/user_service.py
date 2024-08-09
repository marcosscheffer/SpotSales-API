from ..extensions import db
from ..models.user_model import UserModel
from ..entities.user import User


def user_update_service(id: int, user: User):
    user_db = UserModel.query.get(id)
    if not user_db:
        return {"error": "User not found"}
    
    if user.name:
        user_db.name = user.name
    if user.email:
        user_db.email = user.email
    if user.cpf:
        user_db.cpf = user.cpf
    if user.password:
        if not user_db.verify_password(user.password):
            user_db.password = user.password
            user_db.encrypt_password()
    if user.position_id:
        user_db.position_id = user.position_id
    if user.active != None:
        user_db.active = user.active
    if user.admin:
        user_db.admin = user.admin
    if user.bot:
        user_db.bot = user.bot
    db.session.commit()
    
    return user_db
    
    