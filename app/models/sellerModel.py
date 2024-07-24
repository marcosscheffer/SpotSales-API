from .baseModel import BaseModel
from ..extensions import db
from . import leadSaleModel



class SellerModel(BaseModel):
    __tablename__ ='sellers'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    
    sales = db.relationship(leadSaleModel, backref='seller', lazy=True)
    