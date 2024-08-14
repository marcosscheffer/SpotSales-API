from marshmallow import fields, validates, ValidationError

from ..extensions import ma

from ..models.lead_sale_model import LeadSaleModel
from ..models.seller_model import SellerModel

from ..validations.foreign_validate import foreign_key_validate
from ..validations.unique_validate import unique_validate

class LeadSaleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = LeadSaleModel
        load_instance = True
        fields = ('id', 'company', 'sale_date', 'value', 'seller_id', 'ts', 'filled', 'created_at', 'updated_at', 'active')
        
    
    id = fields.Int(required=True)
    company = fields.String(required=True)
    sale_date = fields.DateTime(required=True)
    value = fields.Float(required=True)
    seller_id = fields.Int(required=True)
    ts = fields.String(required=True)
    filled = fields.Boolean(required=False)
    
    
    @validates('id')
    def id_validate(self, value):
        unique_validate(value, LeadSaleModel)

    @validates('seller_id')
    def seller_id_validate(self, value):
        foreign_key_validate(value, SellerModel)
        
        