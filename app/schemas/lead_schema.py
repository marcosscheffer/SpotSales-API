from marshmallow import fields, validates, ValidationError

from ..extensions import ma

from ..models.lead_sale_model import LeadSaleModel
from ..models.seller_model import SellerModel

from ..validations.foreign_validate import foreign_key_validate
from ..validations.unique_validate import unique_validate

class LeadSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = LeadSaleModel
        load_instance = True
        fields = ('id','company', 'phone1', 'phone2', 'city', 'state', 'created_at', 'updated_at', 'active')
        
    
    id = fields.Int(required=True)
    company = fields.String(required=True)
    phone1 = fields.String(required=True, allow_none=True)
    phone2 = fields.String(required=True, allow_none=True)
    city = fields.String(required=False, allow_none=True)
    state = fields.String(required=False, allow_none=True)
    
    
    @validates('id')
    def id_validate(self, value):
        unique_validate(value, LeadSaleModel)

        
        