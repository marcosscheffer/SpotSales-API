from marshmallow import fields, validates

from ..extensions import ma

from ..models.user_model import UserModel
from ..models.position_model import PositionModel

from ..validations.unique_validate import unique_validate
from ..validations.length_validate import length_validate
from ..validations.foreign_validate import foreign_key_validate

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_instance = True
        fields = ('id', 'name', 'email', 'cpf', 'password', 'position_id', 'active', 'admin', 'bot')
    
    
    name = fields.String(required=True)
    email = fields.Email(required=True, load_only=True)
    cpf = fields.String(required=True, load_only=True, )
    password = fields.String(required=True, load_only=True)
    position_id = fields.Int(required=True)
    active = fields.Boolean(required=True)
    admin = fields.Boolean(required=True)
    bot = fields.Boolean(required=True)
    
    
    @validates('email')
    def email_validate(self, value):
        instance_id = self.context.get('id', None)
        unique_validate(value, UserModel, 'email', instance_id)
        
    
    @validates('cpf')
    def cpf_validate(self, value):
        instance_id = self.context.get('id', None)
        length_validate(value, 11, 11)
        unique_validate(value, UserModel, 'cpf', instance_id)
        
    @validates('position_id')
    def position_id_validate(self, value):
        foreign_key_validate(value, PositionModel)
        
        