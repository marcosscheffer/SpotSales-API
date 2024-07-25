from marshmallow import fields

from ..extensions import ma
from ..models.lead_sale_model import LeadSaleModel

class LeadSaleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = LeadSaleModel
        load_instance = True
        
    
    id = fields.Int(required=True)
    sale_date = fields.DateTime(required=True)
    value = fields.Float(required=True)
    seller_id = fields.Int(required=True)