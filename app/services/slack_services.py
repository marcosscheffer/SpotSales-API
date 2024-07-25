from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


def send_message_service(client: WebClient, channel_id: str, message: str, ts: str = None):
    try:
        response = client.chat_postMessage(channel=channel_id, text=message, thread_ts=ts)
        return {"success": True, "ts": response["ts"]}
    except SlackApiError as e:
        return {"success": False, "error": e.response["error"]}


