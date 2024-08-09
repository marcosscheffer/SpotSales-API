from flask_restful import Resource
from flask import request
import logging

from ..extensions import api_v1
from ..services.leads_service import register_lead_service
from ..services.seller_service import get_seller_by_email_service
from ..services.lead_sale_service import register_lead_sale_service
from ..schemas.lead_schema import LeadSchema
from ..schemas.lead_sale_schema import LeadSaleSchema
from ..entities.lead import Lead
from ..entities.lead_sale import LeadSale


class LeadWebhookView(Resource):
    def post(self):
        ls = LeadSchema()
        data = request.get_json()
        data_lead = {
            "id": data["Lead"]["Id"],
            "company": data["Lead"].get("Company", None),
            "phone1": data["Lead"].get("Phone", None),
            "phone2": data["Lead"].get("Phone2", None),
            "city": data["Lead"].get("City", None),
            "state": data["Lead"].get("State", None),
        }
        validate = ls.validate(data_lead)
        if validate:
            return validate, 400
        lead = Lead(id=data_lead["id"],
                    phone1=data_lead["phone1"],
                    phone2=data_lead["phone2"],
                    city=data_lead["city"],
                    state=data_lead["state"],
                    company=data_lead["company"])
        response = register_lead_service(lead)
        return ls.dump(response), 201
    

class LeadSoldWebhookView(Resource):
    def post(self):
        data = request.get_json()
        seller = get_seller_by_email_service(data["Sale"]["SalesRep"].get("Email", None))
        print(seller.id)
        data_lead = {"id": data["Sale"].get("LeadId", None),
                     "sale_date": data["Sale"].get("SaleDate", None),
                     "seller_id": seller.id,
                     "value": data["Sale"].get("TotalDealValue", None)
                     }
        
        
        lss = LeadSaleSchema()
        validate = lss.validate(data_lead)
        if validate:
            print(validate)
            return validate, 400
        lead = LeadSale(id=data_lead["id"],
                        sale_date=data_lead["sale_date"],
                        seller_id=seller.id,
                        value=data_lead["value"]
                        )
        
        response = register_lead_sale_service(lead)
        return lss.dump(response), 201
        

api_v1.add_resource(LeadWebhookView, '/webhook/exact/new-lead')
api_v1.add_resource(LeadSoldWebhookView, '/webhook/exact/lead-sold')

