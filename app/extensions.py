from flask_restful import Api
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

api = Api()
db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
