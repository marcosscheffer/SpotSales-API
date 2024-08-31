from marshmallow import fields

from ..extensions import ma
from ..models.products_solds_model import ProductsSoldsModel

class PositionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProductsSoldsModel
        load_instance = True
        fields = ('id', 'filter_op_id', 'product_id', 'description', 'quantity' 'created_at', 'updated_at', 'active')
        
    
    id = fields.Integer(required=True)
    filter_op_id = fields.Integer(required=True)
    product_id = fields.String(required=True)
    description = fields.String(required=True)
    quantity = fields.Integer(required=True)