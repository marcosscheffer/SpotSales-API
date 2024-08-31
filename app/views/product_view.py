from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt
from flask import request

from ..extensions import api_v1
from ..services.product_service import (get_products_service, register_product_service,
                                        get_product_by_id_service)
from ..schemas.product_schema import ProductSchema
from ..entities.position import Position


class ProductsView(Resource):
    def get(self):
        product = get_products_service()
        ps = ProductSchema(many=True)
        response = ps.dump(product)
        return response, 200
    
    @jwt_required()
    def post(self):
        claims = get_jwt()
        if claims.get("roles", "guest") not in ['admin']:
            return "Unauthorized - Only admin can access", 403
        
        ps = ProductSchema()
        validate = ps.validate(request.json)
        if validate:
            return validate, 400
        
        data = request.get_json()
        position = Position(title=data["title"])
        response = register_product_service(position)
        return ps.dump(response), 201
    
class PositionView(Resource):
    @jwt_required()
    def get(self, id):
        claims = get_jwt()
        if claims.get("roles", "guest") not in ['admin', 'user']:
            return "Unauthorized - Only admin and user can access", 403
        
        position = get_product_by_id_service(id)
        if not position:
            return "Not Found - No Position", 404
        
        ps = PositionSchema()
        response = ps.dump(position)
        return response, 200
    
    
api_v1.add_resource(PositionsView, '/positions')
api_v1.add_resource(PositionView, '/positions/<int:id>')
                