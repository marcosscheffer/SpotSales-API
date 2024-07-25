from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.signature import SignatureVerifier
from flask import request
from flask_restful import Resource
import os

from ..extensions import api
from ..schemas.slack_schemas import SendMessageSchema
from ..services.slack_services import send_message_service

load_dotenv()
bot_token = os.environ.get('SLACK_BOT_TOKEN')
signing_secret = os.environ.get('SLACK_SIGNING_SECRET')
client = WebClient(token=bot_token)
signature_verifier = SignatureVerifier(signing_secret=signing_secret)


class send_message_view(Resource):
    def post(self):
        ss = SendMessageSchema()
        validate = ss.validate(request.json)
        if validate:
            return validate, 400
        
        data = request.get_json()
        if 'ts' in data:
            response = send_message_service(client, data["channel_id"], data["message"], data["ts"])
        else:
            response = send_message_service(client, data["channel_id"], data["message"])

        if response["success"]:
            return {"message": "Successfully sent message", "ts": response["ts"]}
        return {"message": "message not sent", "error": response["error"]}
    

api.add_resource(send_message_view, '/slack/send')
