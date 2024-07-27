from ..extensions import db
from ..models.user_model import UserModel
from ..entities.user import User


def user_update_service(id: int, user: User):
    user_db = UserModel.query.get(id)
    if not user_db:
        return {"error": "User not found"}
    
    
    user_db.name = user.name
    user_db.email = user.email
    user_db.cpf = user.cpf
    if not user_db.verify_password(user.password):
        user_db.password = user.password
        user_db.encrypt_password()
    user_db.position_id = user.position_id
    user_db.active = user.active
    user_db.admin = user.admin
    user_db.bot = user.bot
    db.session.commit()
    
    return user_db
    
    