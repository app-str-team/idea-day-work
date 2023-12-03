
from .. import firestoreconnection

def get_idea_categories()->dict:
    doc_ref = firestoreconnection.db.collection('ideaday_container').document('idea_category')
    doc = doc_ref.get()
    if doc.exists:
        collection = doc.to_dict()
        return collection
    else:
        return {"error": "Check your firestoreconnection"}
    