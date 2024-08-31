from .base_model import BaseModel
from .products_solds_model import ProductsSoldsModel
from ..extensions import db

class ProductModel(BaseModel):
    __tablename__ = 'product'
    
    # general
    id = db.Column(db.String(20), primary_key=True, autoincrement=False)

    name = db.Column(db.String(255), nullable=False)
    products_solds = db.relationship(ProductsSoldsModel, backref='product', lazy=True)

    
    
    

    
    