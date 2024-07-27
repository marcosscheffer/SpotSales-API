from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt
from flask import request

from ..extensions import api_v1
from ..services.user_service import user_update_service
from ..services.user_auth_service import get_user_by_id
from ..schemas.user_schema import UserSchema
from ..entities.user import User

class UserUpdateView(Resource):
    
    def get(self, id):
        us = UserSchema()
        user = get_user_by_id(id)
        if not user:
            return "Not Found - No user", 404
        return us.dump(user), 200
    
    @jwt_required()
    def put(self, id):
        roles = get_jwt.get("roles", "guest")
        if roles not in ['admin']:
            return "Unauthorized - Only admin and user can access", 401
        
        us = UserSchema(context={'id': id})
        validate = us.validate(request.json)
        if validate:
            return validate, 400
        
        data = request.get_json()
        user = User(name=data["name"], email=data["email"], cpf=data["cpf"], 
                    password=data["password"], position_id=data["position_id"], 
                    active=data["active"], admin=data["admin"], bot=data["bot"])
        response = user_update_service(id, user)
        if isinstance(response, dict):
            return response, 400
        
        return us.dump(response), 200
    
    
api_v1.add_resource(UserUpdateView, '/user/update/<int:id>')
        