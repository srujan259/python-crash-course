from pathlib import Path
import json

path = Path('username.json')
if path.exists():
    content = path.read_text()
    username = json.loads(content)
    print(f"Hi {username}, welcome back")
else:
    username = input("enter username: ")
    content = json.dumps(username)
    path.write_text(content)
    print(f"Hey {username} we will remember you now")