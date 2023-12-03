
from ....persistence.users import createuser

def create_user(request:dict)-> dict:
    createuser.create_user(request['email'], request['password'], request['display_name'])
    return {"status":"OK"}


