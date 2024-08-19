from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt
from flask import request
from datetime import datetime

from ..extensions import api_v1
from ..services.lead_sale_service import (get_leads_sales_service, register_lead_sale_service, 
                                          get_lead_sale_by_id_service)
from ..services.seller_service import get_seller_by_id_service
from ..schemas.lead_sale_schema import LeadSaleSchema
from ..paginate import paginate
from ..models.lead_sale_model import LeadSaleModel


class LeadsSalesView(Resource):
    @jwt_required()
    def get(self):
        claims = get_jwt()
        if claims.get("roles", "guest") not in ['admin', 'user']:
            return "Unauthorized - Only admin and user can access", 403
        lss = LeadSaleSchema(many=True)
        return paginate(LeadSaleModel, lss)
    

class LeadSaleView(Resource):
    @jwt_required()
    def get(self, id):
        claims = get_jwt()
        if claims.get("roles", "guest") not in ['admin', 'user']:
            return "Unauthorized - Only admin and user can access", 403
        
        lead_sale = get_lead_sale_by_id_service(id)
        if not lead_sale:
            return "Not Found - No Lead", 404
        
        lss = LeadSaleSchema()
        response = lss.dump(lead_sale)
        
        seller = get_seller_by_id_service(response.get("seller_id", None))
        response["seller_name"] = f"{seller.first_name} {seller.last_name}"
        return response, 200
        
    
api_v1.add_resource(LeadsSalesView, '/leadsSales')
api_v1.add_resource(LeadSaleView, '/leadsSales/<int:id>')