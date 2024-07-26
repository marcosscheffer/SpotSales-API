from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask import request

from ..extensions import api_v1
from ..services.user_service import user_update_service
from ..schemas.user_schema import UserSchema
from ..entities.user import User

class UserUpdateView(Resource):
    def put(self, id):
        us = UserSchema()
        validate = us.validate(request.json)
        if validate:
            return validate, 400
        
        data = request.get_json()
        user = User(name=data["name"], email=data["email"], cpf=data["cpf"], 
                    password=data["password"], position_id=data["position_id"], 
                    active=data["active"])
        response = user_update_service(id, user)
        if isinstance(response, dict):
            return response, 400
        
        return us.dump(response), 200
    
    
api_v1.add_resource(UserUpdateView, '/user/update/<int:id>')
        