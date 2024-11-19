from pathlib import Path
import json

def get_stored_user_details(path):
        """ Get stored user_details """
        if path.exists():
            content = path.read_text()
            user_details = json.loads(content)
            return user_details
        else:
             None
def get_new_user_details(path):
    username = input("enter username: ")
    age = input("enter age: ")
    profession = input("enter profession: ")
    user_details = {"username": username, "age": age, "profession": profession}
    content = json.dumps(user_details)
    path.write_text(content)
    return user_details
     
def greetuser():
    """Greet the user by name """
    path = Path('user_details.json')
    user_details = get_stored_user_details(path)
    if user_details:
        print(f"Hi {user_details['username']}, working as {user_details['profession']} and {user_details['age']} years old welcome back")
    else:
        user_details = get_new_user_details(path)
        print(f"Hey {user_details['username']} we will remember you now")
greetuser()