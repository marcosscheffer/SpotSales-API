from ..extensions import db
from ..models.lead_model import LeadModel
from ..entities.lead import Lead


def get_leads_service():
    return LeadModel.query.all()

def get_lead_by_id_service(id: int):
    return LeadModel.query.get(id)

def register_lead_service(data: Lead):
    lead_db = LeadModel(id=data.id, 
                             phone1=data.phone1, 
                             phone2=data.phone2, 
                             company=data.company,
                             city=data.city,
                             state=data.state)
    db.session.add(lead_db)
    db.session.commit()
    return lead_db
    