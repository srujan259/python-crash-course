from pathlib import Path
import json

fav_number = input("Enter your favourite number : ")
path = Path('fav_number.json')
content = json.dumps(fav_number)
path.write_text(content)


