from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask import request

from ..extensions import api_v1, jwt
from ..services.user_auth_service import (user_register_service, user_login_service,
                                     user_refresh_service, get_user_by_id)
from ..schemas.user_auth_schema import RegisterSchema, LoginSchema
from ..entities.user import User


class UserRegisterView(Resource):
    def post(self):
        rs = RegisterSchema()
        validate = rs.validate(request.json)
        if validate:
            return validate, 400
        
        data = request.get_json()
        user = User(name=data['name'], email=data['email'], cpf=data['cpf'],
                    password=data['password'], position_id=data['position_id'])
        response = user_register_service(user)
        return rs.dump(response), 201
    

class UserLoginView(Resource):
    
    @jwt.additional_claims_loader
    def additional_claims_to_access_token(identity):
        user_token = get_user_by_id(identity)
        
        if user_token.active and user_token.admin:
            roles = 'admin'
        elif user_token.active and user_token.bot:
            roles = 'bot'
        elif user_token.active:
            roles = 'user'
        else:
            roles = 'guest'
        
        return {'roles': roles}
        
    
    def post(self):
        ls = LoginSchema()
        validate = ls.validate(request.json)
        if validate:
            return validate, 400
        
        data = request.get_json()
        response = user_login_service(data["cpf"], data["password"])
        return response, 200
    

class UserRefreshView(Resource):
    @jwt_required(refresh=True)
    def post(self):
        user = get_jwt_identity()
        response = user_refresh_service(user)
        return response, 200
    

api_v1.add_resource(UserRegisterView, '/user/register')
api_v1.add_resource(UserLoginView, '/user/login')
api_v1.add_resource(UserRefreshView, '/user/refresh')