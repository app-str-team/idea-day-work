
import os
import firebase_admin
from firebase_admin import credentials, firestore

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


cred = credentials.Certificate(os.path.join(__location__, 'app-str-team-6577bb093acd.json'))
firebase_admin.initialize_app(cred)


db = firestore.client() 

