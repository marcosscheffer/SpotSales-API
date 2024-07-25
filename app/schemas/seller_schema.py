from marshmallow import fields

from ..extensions import ma
from ..models.seller_model import SellerModel

class SellerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = SellerModel
        load_instance = True
        fields = ('id', 'first_name', 'last_name')
    
    id = fields.Int(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.Email(required=True)
    