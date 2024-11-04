from pathlib import Path
import json

def get_stored_username(path):
        """ Get stored username """
        if path.exists():
            content = path.read_text()
            username = json.loads(content)
            return username
        else:
             None
def get_new_username(path):
    username = input("enter username: ")
    content = json.dumps(username)
    path.write_text(content)
    return username
     
def greetuser():
    """Greet the user by name """
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"Hi {username}, welcome back")
    else:
        get_new_username(path)
        print(f"Hey {username} we will remember you now")
greetuser()