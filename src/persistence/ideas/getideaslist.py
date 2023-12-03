from .. import firestoreconnection

import json

def fetch_idea_list():

    collection = firestoreconnection.db.collection('ideaday_container')

    res = collection.document('idea_list').get().to_dict()["idea_list"]

    return res
