from flask_restful import Resource
from flask import request

from ..extensions import api_v1
from..schemas.seller_schema import SellerSchema
from ..entities.seller import Seller
from ..services.seller_service import (get_sellers_service, get_seller_by_id_service, 
                                       register_seller_service)


class SellersView(Resource):
    def get(self):
        sellers = get_sellers_service()
        ss = SellerSchema(many=True)
        return ss.dump(sellers), 200
    
    def post(self):
        ss = SellerSchema()
        validate = ss.validate(request.json)
        if validate:
            return validate, 400
        
        data = request.get_json()
        seller = Seller(id=data["id"], first_name=data["first_name"], 
                        last_name=data["last_name"], email=data["email"])
        response = register_seller_service(seller)
        
        return ss.dump(response), 201
    
class SellerView(Resource):
    def get(self, id):
        seller = get_seller_by_id_service(id)
        if not seller:
            return "Not Found - No Seller", 404
        ss = SellerSchema()
        return ss.dump(seller), 200
 
    
api_v1.add_resource(SellersView, '/sellers')
api_v1.add_resource(SellerView, '/sellers/<int:id>')
        
