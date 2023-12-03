
from .. import firestoreconnection

def update_judgment_tracker(updated_data:dict):
    doc_ref = firestoreconnection.db.collection('ideaday_container').document('judgement_tracker')
    doc_ref.set(updated_data)