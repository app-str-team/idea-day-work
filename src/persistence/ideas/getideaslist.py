from .. import firestoreconnection

import json

def fetch_idea_list():
    

    collection = firestoreconnection.db.collection('idea_list')

    res = collection.document('nTxLkaWbnk3H878ZrqCr').get().to_dict()

    ideas_list = json.dumps(res)
    return ideas_list
