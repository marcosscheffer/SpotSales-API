from .base_model import BaseModel
from ..extensions import db

class ProductsSoldsModel(BaseModel):
    __tablename__ = 'products_solds'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    filter_op_id = db.Column(db.Integer, db.ForeignKey("filter_op.id"), nullable=False)
    product_id = db.Column(db.String(20), db.ForeignKey("product.id"), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    quantity = db.Column(db.Integer, nullable=True)