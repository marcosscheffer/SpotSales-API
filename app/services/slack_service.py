import io

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


def send_message_service(client: WebClient, channel_id: str, 
                         message: str, ts: str = None) -> dict:
    try:
        response = client.chat_postMessage(channel=channel_id, text=message, 
                                           thread_ts=ts)
        return {"success": True, "ts": response["ts"]}
    except SlackApiError as e:
        return {"success": False, "error": e.response["error"]}
    
def send_file_service(client: WebClient, channel_id: str, file, 
                      ts: str=None) -> dict:
    buffer = io.BytesIO()
    file.save(buffer)
    buffer.seek(0)
    try:
        response = client.files_upload_v2(channel=channel_id, file=buffer, 
                                          thread_ts=ts)
        return {"success": True, "ts": response["ts"]}
    except SlackApiError as e:
        return {"success": False, "error": e.response["error"]}
    
    

    
    


