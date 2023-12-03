
import os
import json
import firebase_admin
from firebase_admin import credentials, firestore, auth

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


cred = credentials.Certificate(os.path.join(__location__, 'app-str-team-6577bb093acd.json'))
config_file = os.path.join(__location__, 'firebase_config.json')

firebase_admin.initialize_app(cred)

CONFIG = None
with open(config_file, 'r') as f:
    CONFIG = json.load(f)
    
db = firestore.client() 
auth = auth
