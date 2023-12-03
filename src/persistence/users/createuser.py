from .. import firestoreconnection
from  ..ideacategories import getideacategories


def create_user(email: str, password: str, display_name:str):
    
    response = firestoreconnection.auth.create_user(email=email, password=password,  display_name=display_name)

    #if display_name in request for user creation is same in the list of judges
    idea_categories = getideacategories.get_idea_categories()
    list_all_judges = []
 
    for key, value in idea_categories.items():
        for key2,value2 in value.items():
            if key2 == 'judges':
                list_all_judges = [judge for judge in value2]
    
    if display_name in list_all_judges:
        firestoreconnection.auth.set_custom_user_claims(response.__dict__['_data']['localId'], {'Judge': True})
    else:
        print("the request user creation is an ordinary user")

    

    