from .base_model import BaseModel
from ..extensions import db

class ChecklistModel(BaseModel):
    __tablename__ = 'checklists'
    
    # general
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    seller_id = db.Column(db.Integer, db.ForeignKey('sellers.id'), nullable=False)
    sale_date = db.Column(db.Date, nullable=False)
    value = db.Column(db.Float, nullable=False)
    ts = db.Column(db.String(20), nullable=False)
    
    # equipment
    phases = db.Column(db.Integer, nullable=True)
    voltage = db.Column(db.Integer, nullable=True)
    power = db.Column(db.Integer, nullable=True)
    special_project = db.Column(db.Integer, nullable=True)
    eletric_key = db.Column(db.Boolean, nullable=True)
    eletric_panel = db.Column(db.Boolean, nullable=True)
    description = db.Column(db.String(255), nullable=True)
    layout = db.Column(db.Boolean, nullable=True)
    
    # pipeline
    pipeline = db.Column(db.Boolean, nullable=True)
    special_paint = db.Column(db.Boolean, nullable=True)
    extra_filters = db.Column(db.Boolean, nullable=True)
    assembly = db.Column(db.String(255), nullable=True)

    # delivery
    freight = db.Column(db.String(255), nullable=True)
    pallet = db.Column(db.Boolean, nullable=True)
    adress = db.Column(db.String(255), nullable=True)
    deadline = db.Column(db.Date, nullable=True)
    
    # final
    other = db.Column(db.String(255), nullable=True)
    filled = db.Column(db.String(255), nullable=True)
    
    
     
    