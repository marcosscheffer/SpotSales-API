from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity
from flask import request

from ..extensions import api_v1
from ..services.user_service import user_update_service
from ..services.user_auth_service import get_user_by_id
from ..schemas.user_schema import UserSchema
from ..entities.user import User

class UserUpdateView(Resource):
    
    @jwt_required()
    def get(self, id):
        claims = get_jwt()
        if claims.get("roles", "guest") not in ['admin']:
            return "Unauthorized - Only admin and user can access", 401
        
        us = UserSchema()
        user = get_user_by_id(id)
        if not user:
            return "Not Found - No user", 404
        return us.dump(user), 200
    
    @jwt_required()
    def put(self, id):
        claims = get_jwt()
        if claims.get("roles", "guest") not in ['admin']:
            return "Unauthorized - Only admin and user can access", 401
        
        us = UserSchema(context={'id': id}, partial=True)
        validate = us.validate(request.json)
        if validate:
            return validate, 400
        
        data = request.get_json()
        user = User(name=data.get("name", None),
                    email=data.get("email", None),
                    cpf=data.get("cpf", None), 
                    password=data.get("password", None),
                    position_id=data.get("position_id", None), 
                    active=data.get("active", None),
                    admin=data.get("admin", None),
                    bot=data.get("bot", None)
                    )
        response = user_update_service(id, user)
        if isinstance(response, dict):
            return response, 404
        
        return us.dump(response), 200
    

class UserView(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        us = UserSchema()
        user = get_user_by_id(user_id)
        return us.dump(user), 200

        
    
    
api_v1.add_resource(UserUpdateView, '/user/<int:id>')
api_v1.add_resource(UserView, '/user/me')
        