from marshmallow import fields

from ..extensions import ma
from ..models.seller_model import SellerModel

class SellerSchema(ma.SQLAlchemyAutoSchema):
    model = SellerModel
    load_instance = True
    fields = ('id', 'first_name', 'last_name', 'email', 'created_at', 'updated_at', 'active')
    
    id = fields.Int(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.Email(required=True)
    