from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import timedelta

from ..extensions import db
from ..models.user_model import UserModel
from ..entities.user import User


def gen_tokens(identity, expire_time):
    access_token = create_access_token(identity, 
                                       expires_delta=timedelta(seconds=expire_time))
    refresh_token = create_refresh_token(identity)
    
    return {"access_token": access_token, "refresh_token": refresh_token}
    

def user_register_service(user: User):
    user_db = UserModel(name=user.name, email=user.email, cpf=user.cpf,
                        password=user.password, position_id=user.position_id)
    user_db.encrypt_password()
    db.session.add(user_db)
    db.session.commit()
    return user_db

def user_login_service(login, password):
    user_db = UserModel.query.filter_by(cpf=login).first()
    if not user_db or not user_db.verify_password(password):
        return {"message": "Credentials invalid"}
    
    tokens = gen_tokens(user_db.id, 100)
    return {**tokens, 'message': "Login successful"}

def user_refresh_service(identity):
    refreshed_token = gen_tokens(identity, 100)
    return {**refreshed_token, "message": "Refreshed token successfully"}


def get_user_by_id(user_id):
    return UserModel.query.get(user_id)

    
    
    
    

