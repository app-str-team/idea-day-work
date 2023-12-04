import json
import requests
from .. import firestoreconnection


def process_signin(email: str, password: str, return_secure_token: bool = True) ->dict:
    payload = json.dumps({
        "email": email,
        "password": password,
        "returnSecureToken": True
    })

    r = requests.post(firestoreconnection.CONFIG['API_URL'],
                      params={"key": firestoreconnection.CONFIG['FIREBASE_WEB_API_KEY']},
                      data=payload)
    
    resp_fields = r.json()
    claims = firestoreconnection.auth.verify_id_token(resp_fields['idToken'])
    if 'Judge' in claims:
        if claims['Judge'] is True:
            resp_fields['userRole'] = 'Judge'
        else:
            resp_fields['userRole'] = 'noRole' 
    else:
        resp_fields['userRole'] = 'noRole'
    return resp_fields


    
