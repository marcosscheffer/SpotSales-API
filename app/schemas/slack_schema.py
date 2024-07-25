from marshmallow import fields

from ..extensions import ma

class SendFileSchema(ma.Schema):
    channel_id = fields.String(required=True)
    ts = fields.String(required=False)

class SendMessageSchema(SendFileSchema):
    message = fields.String(required=True)


    
    
    

    
    

    

