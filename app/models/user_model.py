from passlib.hash import pbkdf2_sha256

from .base_model import BaseModel
from ..extensions import db

class UserModel(BaseModel):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean, default=False)
    admin = db.Column(db.Boolean, default=False, nullable=False)
    bot = db.Column(db.Boolean, default=False, nullable=False)

    position_id = db.Column(db.Integer, db.ForeignKey("positions.id"), nullable=False)
    
    
    def encrypt_password(self):
        self.password = pbkdf2_sha256.hash(self.password)
        
    def verify_password(self, password):
        return pbkdf2_sha256.verify(password, self.password)
        