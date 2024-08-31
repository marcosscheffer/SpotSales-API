from .base_model import BaseModel
from .products_solds_model import ProductsSoldsModel
from ..extensions import db

class FilterOpModel(BaseModel):
    __tablename__ = 'filter_op'
    
    # general
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    seller_id = db.Column(db.Integer, db.ForeignKey('sellers.id'), nullable=False)
    sale_date = db.Column(db.Date, nullable=False)
    value = db.Column(db.Float, nullable=False)
    ts = db.Column(db.String(20), nullable=False)
    
    #filter op
    deadline = db.Column(db.Date, nullable=True)
    carrier = db.Column(db.String(255), nullable=True)
    
    products = db.relationship(ProductsSoldsModel, backref='filter_op', lazy=True)
    
    
    

    
    