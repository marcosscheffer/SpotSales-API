from flask import Flask
from .extensions import api, db, ma, migrate
from .models import SellerModel, LeadSaleModel

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    
    api.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    
    # Register Resources
    
    return app