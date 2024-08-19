from app.models import users

def authenticate_user(username, password):
    user = users.get(username)
    if user and user.password == password:
        return True
    return False
 
