import json

def get_user_name():
    """如果储存过用户名就返回用户名"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)

    except FileNotFoundError:
        return None

    else:
        return username

def get_new():
    username = input('Plz create your user name: ')
    filename = 'username.json'
    with open(filename, "w") as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """问候用户"""
    username = get_user_name()
    if username:
        print('Hello ' + username + '!')

    else:
        username = get_new()
        print('We will remember u when u come back again ' + username + '!')


greet_user()
