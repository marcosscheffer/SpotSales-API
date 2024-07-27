from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt
from flask import request
from datetime import datetime

from ..extensions import api_v1
from ..services.lead_sale_service import (get_leads_sales_service, register_lead_sale_service, 
                                          get_lead_sale_by_id_service)
from ..schemas.lead_sale_schema import LeadSaleSchema
from ..entities.lead_sale import LeadSale


class LeadsSalesView(Resource):
    @jwt_required()
    def get(self):
        claims = get_jwt()
        if claims.get("roles", "guest") not in ['admin', 'user']:
            return "Unauthorized - Only admin and user can access", 401
        
        leads_sales = get_leads_sales_service()
        lss = LeadSaleSchema(many=True)
        response = lss.dump(leads_sales)
        return response, 200
    
    @jwt_required()
    def post(self):
        claims = get_jwt()
        if claims.get("roles", "guest") not in ['admin', 'bot']:
            return "Unauthorized - Only admin and user can access", 401
        
        lss = LeadSaleSchema()
        validate = lss.validate(request.json)
        if validate:
            return validate, 400
        
        data = request.get_json()
        if isinstance(data["sale_date"], str):
            try:
                data['sale_date'] = datetime.strptime(data['sale_date'], "%Y-%m-%dT%H:%M:%SZ")
            except ValueError:
                return "Invalid date format", 400
        
        lead_sale = LeadSale(id=data['id'], sale_date=data['sale_date'],
                             value=data['value'], seller_id=data['seller_id'])
        
        response = register_lead_sale_service(lead_sale)
        return lss.dump(response), 201
    

class LeadSaleView(Resource):
    @jwt_required()
    def get(self, id):
        claims = get_jwt()
        if claims.get("roles", "guest") not in ['admin', 'user']:
            return "Unauthorized - Only admin and user can access", 401
        
        lead_sale = get_lead_sale_by_id_service(id)
        if not lead_sale:
            return "Not Found - No Lead", 404
        
        lss = LeadSaleSchema()
        return lss.dump(lead_sale), 200
        
    
api_v1.add_resource(LeadsSalesView, '/leadsSales')
api_v1.add_resource(LeadSaleView, '/leadsSales/<int:id>')