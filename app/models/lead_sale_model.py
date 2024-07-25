from datetime import datetime

from .base_model import BaseModel
from ..extensions import db



class LeadSaleModel(BaseModel):
    __tablename__ = 'lead_sales'
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    sale_date = db.Column(db.DateTime, nullable=False)
    value = db.Column(db.Float, nullable=False)
    
    seller_id = db.Column(db.Integer, db.ForeignKey('sellers.id'), nullable=False)
    