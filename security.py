from werkzeug.security import safe_str_cmp
from User import User

users = [
    User(1, 'stradtkt', 'password'),
    User(2, 'dkel', 'password')
]

username_mapping = {u.username: u for u in users}
userId_mapping = {u.id: u for u in users}

def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return userId_mapping.get(user_id, None)