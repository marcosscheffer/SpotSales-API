from flask import Flask
from .extensions import api_v1, db, ma, migrate

# add Models
from .models.lead_sale_model import LeadSaleModel
from .models.seller_model import SellerModel
from .models.checklist_model import ChecklistModel

# Add Resources
from .views.lead_sale_view import LeadsSalesView, LeadSaleView
from .views.seller_view import SellersView, SellerView
from .views.slack_view import SendFilesView, SendMessageView


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    
    api_v1.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    
    return app