from marshmallow import ValidationError

from ..models.base_model import BaseModel


def unique_validate(value, model: BaseModel, field_name: str = 'id'):
        if model.query.filter(getattr(model, field_name) == value).first():
            raise ValidationError(f'Already exists')