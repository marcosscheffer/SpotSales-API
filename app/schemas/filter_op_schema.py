from marshmallow import fields

from ..extensions import ma
from ..models.products_solds_model import ProductsSoldsModel

class PositionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProductsSoldsModel
        load_instance = True
        fields = ('id', 'seller_id', 'sale_date', 'value', 'ts', 'deadline', 'carrier', 'created_at', 'updated_at', 'active')
        
    
    id = fields.Integer(required=True)
    seller_id = fields.Integer(required=True)
    sale_date = fields.DateTime(required=True)
    value = fields.Float(required=True)
    ts = fields.String(required=True)
    
    deadline = fields.DateTime(required=False)
    carrier = fields.String(required=False)