'''
import firebase_admin
import os
import json
from firebase_admin import credentials, auth
import requests

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


cred = credentials.Certificate(os.path.join(__location__, 'app-str-team-6577bb093acd.json'))
    
firebase = firebase_admin.initialize_app(cred)
#auth = firebase_admin.auth()

response1 = auth.create_user(email='dipakborse@gmail.com', password='P@$$w0rd')
print(response1.__dict__['_data']['localId'])

response3 = auth.set_custom_user_claims(response1.__dict__['_data']['localId'], {'Judge': True})

FIREBASE_WEB_API_KEY = 'AIzaSyAmFTaQhnyDPMAHvepnBgSpnyjSFgiOuVI'
rest_api_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"

payload = json.dumps({
        "email": 'dipakborse@gmail.com',
        "password": 'P@$$w0rd',
        "returnSecureToken": True
    })

r = requests.post(rest_api_url,
                      params={"key": FIREBASE_WEB_API_KEY},
                      data=payload)

print(r.json())

claims = auth.verify_id_token(r.json()['idToken'])

print(r.json()['localId'])

if claims['Judge'] is True:
    print("The user is judge")    
'''

import requests

response = requests.post(url="http://127.0.0.1:5000/createuser",
                         json={
                               "email":"viv@gmail.com", 
                               "password":"P@$$w0rd",
                               "display_name":"vivek vardhan",
                              },
                         headers={"Content-Type":"application/json"})

print(response.status_code)
print(response.json())