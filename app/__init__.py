from flask import Flask
from flask_cors import CORS

from .extensions import api_v1, db, ma, migrate, jwt

# add Models
from .models.lead_sale_model import LeadSaleModel
from .models.seller_model import SellerModel
from .models.checklist_model import ChecklistModel
from .models.user_model import UserModel
from .models.position_model import PositionModel
from .models.lead_model import LeadModel

# Add Resources
from .views.lead_sale_view import LeadsSalesView, LeadSaleView
from .views.seller_view import SellersView, SellerView
from .views.slack_view import SendFilesView, SendMessageView
from .views.position_view import PositionsView, PositionView
from .views.user_auth_view import (UserRegisterView, UserLoginView, 
                                   UserRefreshView)
from .views.user_view import UserUpdateView, UserView
from .views.webhook_view import LeadSoldWebhookView
from .views.checklist_view import ChecklistsView

def create_app(config):
    app = Flask(__name__)
    CORS(app, resources={
        r"/*": {"origins": "*",
                "methods": ["GET", "POST", "PUT", "DELETE", "PATCH"],
                "allow_headers": ["Content-Type", "Authorization", "X-Requested-With"]
                }
    })
    app.config.from_object(config)
    api_v1.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    # Register CLI commands
    from .cli import user_cli
    
    app.cli.add_command(user_cli)
    
    return app