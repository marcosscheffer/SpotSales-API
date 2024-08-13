import os
from flask_restful import Resource
from flask import request
from dotenv import load_dotenv
from slack_sdk import WebClient
from datetime import datetime


from ..extensions import api_v1
from ..services.leads_service import register_lead_service
from ..services.seller_service import get_seller_by_email_service, get_seller_by_id_service
from ..services.lead_sale_service import register_lead_sale_service
from ..services.slack_service import send_message_service
from ..schemas.lead_schema import LeadSchema
from ..schemas.lead_sale_schema import LeadSaleSchema
from ..entities.lead import Lead
from ..entities.lead_sale import LeadSale

def create_message_sold(data):
    date_obj = datetime.strptime(data["Sale"].get("SaleDate", '0000-00-00T00:00:00'), "%Y-%m-%dT%H:%M:%S")
    formatted_date = date_obj.strftime("%d/%m/%Y %H:%M:%S")
    
    message = f"""
    --------------------------------------------------
    - *Nova Venda*
    - ID: {data["Sale"].get("LeadId", None)}
    - Cliente: {data["Lead"].get("Company", None)}
    - Vendedor: {data["Sale"]["SalesRep"].get("Name", None)} {data["Sale"]["SalesRep"].get("LastName", None)}
    - Data da Venda: {formatted_date}
    - Valor: R$ {data["Sale"].get("TotalDealValue", None)}
    - Checklist: {CHECKLIST_URL}{data["Sale"].get("LeadId", None)}
    """
    
    return message


load_dotenv()
SLACK_BOT_TOKEN = os.environ.get('SLACK_BOT_TOKEN')
SLACK_CHANNEL = os.environ.get('SLACK_CHANNEL')
CHECKLIST_URL = os.environ.get("CHECKLIST_URL", "http://localhost:5000/checklist/0/")
client = WebClient(SLACK_BOT_TOKEN)

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
        
        #send sold message to slack channel
        message = create_message_sold(data)
        response_message = send_message_service(client, SLACK_CHANNEL, message)
        print(SLACK_BOT_TOKEN)
        #send whatsapp url to ts of message sold
        if response_message["success"]:
            message_whatsapp_url = "https://wa.me/"
            send_message_service(client, SLACK_CHANNEL, message_whatsapp_url, response_message["ts"])
        
        seller = get_seller_by_email_service(data["Sale"]["SalesRep"].get("Email", None))
        data_lead = {"id": data["Sale"].get("LeadId", None),
                     "company": data["Lead"].get("Company", None),
                     "sale_date": data["Sale"].get("SaleDate", None),
                     "seller_id": seller.id,
                     "value": data["Sale"].get("TotalDealValue", None),
                     "ts": response_message.get("ts")
                     }
        
        
        lss = LeadSaleSchema()
        validate = lss.validate(data_lead)
        if validate:
            return validate, 400
        lead = LeadSale(id=data_lead["id"],
                        company=data_lead["company"],
                        sale_date=data_lead["sale_date"],
                        seller_id=seller.id,
                        value=data_lead["value"],
                        ts=data_lead["ts"]
                        )
        
        response = register_lead_sale_service(lead)
        return lss.dump(response), 201
        

api_v1.add_resource(LeadWebhookView, '/webhook/exact/new-lead')
api_v1.add_resource(LeadSoldWebhookView, '/webhook/exact/lead-sold')

