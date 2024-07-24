from marshmallow import fields

from ..extensions import ma
from ..models.seller_model import SellerModel

class SellerSchema(ma.SQLAlchemyAutoSchema):
    model = SellerModel
    load_instance = True
    fields = ('id', 'sale_date', 'value', 'created_at', 'updated_at', 'active')
    
    id = fields.Int(required=True)
    sale_date = fields.DateTime(required=True)
    value = fields.Float(required=True)
    