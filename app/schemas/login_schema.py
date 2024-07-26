from marshmallow import fields, fields

from ..extensions import ma
from ..models.position_model import PositionModel

class PositionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PositionModel
        load_instance = True
        fields = ('id', 'title', 'created_at', 'updated_at', 'active')
        
        
    title = fields.String(required=True)