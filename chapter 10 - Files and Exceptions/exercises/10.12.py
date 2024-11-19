from pathlib import Path
import json

path = Path('fav_number.json')
if path.exists():
    content = path.read_text()
    fav_number = json.loads(content)
    print(f"we know your fav number is {fav_number}")
else:
    fav_number = input("Enter your favourite number : ")
    content = json.dumps(fav_number)
    path.write_text(content)
    print(f"Thanks we will remember your fav number as {fav_number}")


