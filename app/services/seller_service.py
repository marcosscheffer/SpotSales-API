from ..extensions import db
from ..models import SellerModel
from ..entities.seller import Seller


def get_sellers_service():
    return SellerModel.query.all()

def get_seller_by_email_service(email):
    return SellerModel.query.filter_by(email=email).first()

def get_seller_by_id_service(id: int):
    return SellerModel.query.get(id)

def register_seller_service(data: Seller):
    seller_db = SellerModel(id=data.id, first_name=data.first_name, 
                            last_name=data.last_name, email=data.email)
    db.session.add(seller_db)
    db.session.commit()
    return seller_db

    
    