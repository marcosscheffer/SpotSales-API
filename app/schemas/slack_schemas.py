from marshmallow import fields

from ..extensions import ma


class SendMessageSchema(ma.Schema):
    channel_id = fields.String(required=True)
    message = fields.String(required=True)
    ts = fields.String(required=False)
    

