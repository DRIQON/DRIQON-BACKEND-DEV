import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from config import FIREBASE_CREDENTIALS

def firebase_connect():

  cred = credentials.Certificate("driqon-5e57a-firebase-adminsdk-fbsvc-2a18998db4.json")

  firebase_admin.initialize_app(cred)

  print("Firebase Connected Successfully!")

def verify_token(id_token):
    try:
        decoded_token = auth.verify_id_token(id_token)

        return decoded_token

    except Exception:
        return None