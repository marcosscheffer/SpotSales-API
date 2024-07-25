from flask import Flask
from .extensions import api, db, ma, migrate
from .models import SellerModel, LeadSaleModel


# Add Resources
from .views.lead_sale_view import LeadsSalesView, LeadSaleView
from .views.seller_view import SellersView


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    
    api.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    

    
    return app