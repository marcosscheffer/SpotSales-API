from marshmallow import fields

from ..extensions import ma


class SendFileSchema(ma.Schema):
    ts = fields.String(required=False)

class SendMessageSchema(SendFileSchema):
    message = fields.String(required=True)


    
    
    

    
    

    

