from marshmallow import fields

from ..extensions import ma
from ..models.user_model import UserModel

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_instance = True
        fields = ('id', 'name', 'position_id')
    
    name = fields.String(required=True)
    email = fields.Email(required=True)
    cpf = fields.String(required=True)
    password = fields.String(required=True)
    position_id = fields.Int(required=True)
        