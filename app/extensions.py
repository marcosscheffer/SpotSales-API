from flask_restful import Api
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

api_v1 = Api(prefix="/api/v1")
db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
