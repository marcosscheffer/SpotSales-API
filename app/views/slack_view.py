from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.signature import SignatureVerifier
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt
import os

from ..extensions import api_v1
from ..schemas.slack_schema import SendMessageSchema, SendFileSchema
from ..services.slack_service import send_message_service, send_file_service

load_dotenv()
bot_token = os.environ.get('SLACK_BOT_TOKEN')
signing_secret = os.environ.get('SLACK_SIGNING_SECRET')
client = WebClient(token=bot_token)
signature_verifier = SignatureVerifier(signing_secret=signing_secret)

CHANNEL_ID = os.environ.get('SLACK_CHANNEL', None)


class SendMessageView(Resource):
    @jwt_required()
    def post(self):
        claims = get_jwt()
        if claims.get("roles", "guest") not in ['admin', 'user', 'bot']:
            return "Unauthorized - Only admin, user and bot can access", 403
        
        sms = SendMessageSchema()
        validate = sms.validate(request.json)
        if validate:
            return validate, 400
        
        data = request.get_json()
        if 'ts' in data:
            response = send_message_service(client, CHANNEL_ID, 
                                            data["message"], data["ts"])
        else:
            response = send_message_service(client, CHANNEL_ID, 
                                            data["message"])

        if response["success"]:
            return {"message": "Successfully sent message", 
                    "ts": response["ts"]}, 200
        return {"message": "message not sent", 
                "error": response["error"]}, 500
    

class SendFilesView(Resource):
    @jwt_required()
    def post(self):
        claims = get_jwt()
        if claims.get("roles", "guest") not in ['admin', 'user', 'bot']:
            return "Unauthorized - Only admin, user and bot can access", 3
        
        sfs = SendFileSchema()
        validate = sfs.validate(request.form)
        if validate:
            print(validate)
            return validate, 400
        
        file = request.files.get('file')
        if not file:
            return {"message": "no selected file"}, 400
        
        data = request.form.to_dict()
        if 'ts' in data:
            response = send_file_service(client, CHANNEL_ID, 
                                         file, data["ts"])
        else:
            response = send_file_service(client, CHANNEL_ID, 
                                         file)
        
        if response["success"]:
            return {"message": "Successfully sent file", 
                    "ts": response["ts"]}, 200
        return {"message": "file not sent", 
                "error": response["error"]}, 500


api_v1.add_resource(SendMessageView, '/slack/send/message')
api_v1.add_resource(SendFilesView, '/slack/send/file/upload')


