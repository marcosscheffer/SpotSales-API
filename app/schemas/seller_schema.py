from marshmallow import fields, validates

from ..extensions import ma
from ..models.seller_model import SellerModel

from ..validations.unique_validate import unique_validate
from ..validations.length_validate import length_validate

class SellerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = SellerModel
        load_instance = True
        fields = ('id', 'first_name', 'email', 'last_name', 'created_at', 'updated_at', 'active')
    
    
    id = fields.Int(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.Email(required=True, load_only=True)
    
    
    @validates('id')
    def id_validate(self, value):
        unique_validate(value, SellerModel)
        
    @validates('first_name')
    def first_name_validate(self, value):
        length_validate(value, min_length=3)

    @validates('last_name')
    def last_name_validate(self, value):
        length_validate(value, min_length=3)
    