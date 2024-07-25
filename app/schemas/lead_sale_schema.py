from marshmallow import fields

from ..extensions import ma
from ..models.lead_sale_model import LeadSaleModel

class LeadSaleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = LeadSaleModel
        load_instance = True
        fields = ('id','sale_date', 'value', 'seller_id', 'created_at', 'updated_at', 'active')
        
    
    id = fields.Int(required=True)
    sale_date = fields.DateTime(required=True)
    value = fields.Float(required=True)
    seller_id = fields.Int(required=True)