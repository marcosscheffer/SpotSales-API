from flask_restful import Resource
from flask import request

from ..extensions import api_v1
from ..services.user_service import (user_register_service)
from ..schemas.user_schema import UserSchema
from ..entities.user import User

class UserRegisterView(Resource):
    def post(self):
        us = UserSchema()
        validate = us.validate(request.json)
        if validate:
            return validate, 400
        
        data = request.get_json()
        user = User(name=data['name'], email=data['email'], cpf=data['cpf'],
                    password=data['password'], position_id=data['position_id'])
        response = user_register_service(user)
        return us.dump(response), 201
    

api_v1.add_resource(UserRegisterView, '/register')
        