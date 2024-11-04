from pathlib import Path
import json

username = input("Enter your username:")
path = Path('username.json')
content = json.dumps(username)
path.write_text(content)
print(f"Hi {username} we will remember you now!")

