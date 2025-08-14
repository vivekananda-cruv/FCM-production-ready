import os
import firebase_admin
from firebase_admin import credentials, messaging
from dotenv import load_dotenv
import logging

load_dotenv()
logger = logging.getLogger(__name__)

if not firebase_admin._apps:
    cred_path = os.getenv("FIREBASE_CREDENTIALS_PATH")
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)

def send_push_notification(token, title, body, data=None):
    try:
        message = messaging.Message(
            notification=messaging.Notification(title=title, body=body),
            data=data or {},
            token=token,
        )
        response = messaging.send(message)
        logger.info(f"Notification sent: {response}")
        return {"success": True, "response": response}
    except Exception as e:
        logger.error(str(e))
        return {"success": False, "error": str(e)}
