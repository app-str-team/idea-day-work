
from .. import firestoreconnection

def get_judgment_tracker()->dict:
    doc_ref = firestoreconnection.db.collection('ideaday_container').document('judgement_tracker')
    doc = doc_ref.get()
    if doc.exists:
        collection = doc.to_dict()
        return collection
    else:
        return {"error": "Check your firestoreconnection"}
    
