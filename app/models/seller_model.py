from .base_model import BaseModel
from ..extensions import db
from . import lead_sale_model


class SellerModel(BaseModel):
    __tablename__ ='sellers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    
    sales = db.relationship(lead_sale_model, backref='seller', lazy=True)
    