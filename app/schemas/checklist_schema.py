from marshmallow import fields, validates

from ..extensions import ma

from ..models.checklist_model import ChecklistModel
from ..models.seller_model import SellerModel

from ..validations.foreign_validate import foreign_key_validate
from ..validations.unique_validate import unique_validate
class ChecklistSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ChecklistModel
        load_instance = True

    # general
    id = fields.Int(required=True)
    seller_id = fields.Int(required=True)
    sale_date = fields.DateTime(required=True)
    value = fields.Float(required=True)
    ts = fields.String(required=True)
    
    # equipments
    phases = fields.Int(required=False)
    voltage = fields.Int(required=False)
    power = fields.Int(required=False)
    special_project = fields.Boolean(required=False)
    eletric_key = fields.Boolean(required=False)
    eletric_panel = fields.Boolean(required=False)
    description_panel = fields.String(required=False)
    layout = fields.Boolean(required=False)
    
    # pipeline
    pipeline = fields.Boolean(required=False)
    description_pipeline = fields.String(required=False)
    special_paint = fields.Boolean(required=False)
    extra_filters = fields.Boolean(required=False)
    assembly = fields.Boolean(required=False)
    responsible_assembly = fields.String(required=False)

    # delivery
    freight = fields.String(required=False)
    pallet = fields.Boolean(required=False)
    address = fields.String(required=False)
    type_address = fields.String(required=False)
    deadline = fields.Date(required=False)
    
    # final
    other = fields.String(required=False)
    filled = fields.String(required=False)
    
    
    @validates('seller_id')
    def seller_id_validate(self, value):
        foreign_key_validate(value, SellerModel)
        
    @validates('id')
    def id_validate(self, value):
        unique_validate(value, ChecklistModel)