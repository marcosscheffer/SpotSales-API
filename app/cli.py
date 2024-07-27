from flask.cli import AppGroup

from .extensions import db
from .models.user_model import UserModel
from .schemas.user_schema import UserSchema
from .entities.user import User

from .models.position_model import PositionModel
from .schemas.position_schema import PositionSchema
from .entities.position import Position


def create_user_admin(data: dict):
    us = UserSchema()
    validate = us.validate(data)
    if validate:
        return validate
    
    user = User(name=data["name"], email=data["email"], 
                cpf=data["cpf"], password=data["password"], 
                position_id=data["position_id"], active=data["active"], 
                admin=data["admin"], bot=data["bot"])
    
    user_db = UserModel(name=user.name, email=user.email, cpf=user.cpf,
                        password=user.password, position_id=user.position_id, 
                        active=user.active, admin=user.admin, bot=user.bot)
    user_db.encrypt_password()
    db.session.add(user_db)
    db.session.commit()
    return "Admin User created successufuly"

def create_position_primary(data):
    ps = PositionSchema()
    validate = ps.validate(data)
    if validate:
        return validate
    
    position = Position(title=data["title"])
    position_db = PositionModel(title=position.title, active=True)
    db.session.add(position_db)
    db.session.commit()
    
    return f"Position {position.title} created successufuly"


user_cli = AppGroup('user')


@user_cli.command('createadminuser')
def create_admin_user():
    print("### User Data ###")
    name = input("Name: ")
    email = input("Email: ")
    cpf = input("CPF: ")
    password = input("Password: ")
    repeat_password = input("Repeat password: ")
    
    if password == repeat_password:
        data = {
            "name": name,
            "email": email,
            "cpf": cpf,
            "password": password,
            "position_id": 1,
            "active": True,
            "admin": True,
            "bot": False
        }
        
        response = create_user_admin(data)
        print(response)
        
@user_cli.command('createprimaryposition')
def create_primary_position():
    print("### Position Data ###")
    title = input("Title: ")
    
    data = {
        "title": title
    }
    
    response = create_position_primary(data)
    print(response)
    
    
