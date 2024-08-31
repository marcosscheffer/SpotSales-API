from ..extensions import db
from ..models.product_model import ProductModel
from ..entities.products import Product


def get_products_service():
    return ProductModel.query.all()

def get_product_by_id_service(product_id: int):
    return ProductModel.query.get(product_id)

def register_product_service(product: Product):
    product_db = ProductModel(id=product.id,
                               name=product.name)
    db.session.add(product_db)
    db.session.commit()
    return product_db

def delete_product_service(product):
    product_db = ProductModel.query.get(product)
    db.session.delete(product_db)
    db.session.commit()
    return product_db
    

