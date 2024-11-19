from pathlib import Path
import json


path = Path('fav_number.json')
content = path.read_text()
fav_number = json.loads(content)
print(f'your fav number is {fav_number}')


