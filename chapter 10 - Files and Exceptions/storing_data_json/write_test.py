from pathlib import Path
import json

numbers = [1,2,3,4,5,6,7,8]
path = Path('numbers_test.json')
# print(type(contents))
# print(contents)
path.write_text(str(numbers))

