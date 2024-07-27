from marshmallow import fields, validates

from ..extensions import ma

from ..models.user_model import UserModel
from ..models.position_model import PositionModel

from ..validations.unique_validate import unique_validate
from ..validations.length_validate import length_validate
from ..validations.foreign_validate import foreign_key_validate



class RegisterSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_instance = True
        fields = ('id', 'name', 'email', 'cpf', 'password', 'position_id')
    
    
    name = fields.String(required=True)
    email = fields.Email(required=True, load_only=True)
    cpf = fields.String(required=True, load_only=True, )
    password = fields.String(required=True, load_only=True)
    position_id = fields.Int(required=True)
    
    @validates('name')
    def name_validate(self, value):
        length_validate(value, min_length=3)
    
    @validates('cpf')
    def cpf_validate(self, value):
        unique_validate(value, UserModel, 'cpf')
        length_validate(value, 11, 11) 
    
    @validates('email')
    def email_validate(self, value):
        unique_validate(value, UserModel, 'email')
        
    @validates('password')
    def password_validate(self, value):
        length_validate(value, min_length=8)
        
    @validates('position_id')
    def position_id_validate(self, value):
        foreign_key_validate(value, PositionModel)
        
class LoginSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_instance = True
        fields = ('cpf', 'password')
    cpf = fields.String(required=True, load_only=True)
    password = fields.String(required=True, load_only=True)
    
    @validates('cpf')
    def cpf_validate(self, value):
        length_validate(value, 11, 11)