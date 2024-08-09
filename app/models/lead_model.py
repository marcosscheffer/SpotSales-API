from .base_model import BaseModel
from ..extensions import db


class LeadModel(BaseModel):
    __tablename__ = 'leads'
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    company = db.Column(db.String(255), nullable=False)
    phone1 = db.Column(db.String(255), nullable=True)
    phone2 = db.Column(db.String(255), nullable=True)
    city = db.Column(db.String(255), nullable=True)
    state = db.Column(db.String(255), nullable=True)
        