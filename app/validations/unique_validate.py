from marshmallow import ValidationError

from ..models.base_model import BaseModel


def unique_validate(value, model: BaseModel, field_name: str = 'id', instance_id: int = None):
    query = model.query.filter(getattr(model, field_name) == value).first()
    if query and (instance_id is None or query.id != instance_id):
        raise ValidationError(f'Already exists')
        