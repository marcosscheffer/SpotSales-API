from marshmallow import ValidationError

from ..models.base_model import BaseModel


def foreign_key_validate(value, model: BaseModel):
    if not model.query.get(value):
        raise ValidationError(f"Invalid foreign key value")