from ....persistence.users import signin

def signin_user(request:dict)-> dict:  
    return signin.process_signin(request['email'], request['password'])
