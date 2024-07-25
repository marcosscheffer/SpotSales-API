from .base_model import BaseModel
from .user_model import UserModel
from ..extensions import db

class PositionModel(BaseModel):
    __tablename__ = 'positions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    
    users = db.relationship(UserModel, backref='position', lazy=True)