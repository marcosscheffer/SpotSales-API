from datetime import datetime
from datetime import UTC

from ..extensions import db


class BaseModel(db.Model):
    __abstract__ = True
    
    created_at = db.Column(db.DateTime, default=datetime.now(UTC))
    Updated_at = db.Column(db.DateTime, default=datetime.now(UTC), onupdate=datetime.now(UTC))
    active = db.Column(db.Boolean, default=True)