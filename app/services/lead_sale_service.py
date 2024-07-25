from ..extensions import db
from ..models.lead_sale_model import LeadSaleModel
from ..entities import lead_sale


def get_leads_sales_service():
    return LeadSaleModel.query.all()

def get_lead_sale_by_id_service(id: int):
    return LeadSaleModel.query.get(id)

def register_lead_sale_service(data: lead_sale):
    lead_sale_db = LeadSaleModel(id=data.id, sale_date=data.sale_date, 
                                 value=data.value, seller_id=data.seller_id)
    db.session.add(lead_sale_db)
    db.session.commit()
    return lead_sale_db
    