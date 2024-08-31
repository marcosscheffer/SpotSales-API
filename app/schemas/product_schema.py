from marshmallow import fields

from ..extensions import ma
from ..models.product_model import ProductModel

class PositionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProductModel
        load_instance = True
        fields = ('id', 'name', 'created_at', 'updated_at', 'active')
        
    
    id = fields.String(required=True)
    name = fields.String(required=True)