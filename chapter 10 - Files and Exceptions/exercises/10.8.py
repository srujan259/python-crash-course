from pathlib import Path
def read_contents(filepath):
    """ Read file Contents"""
    try:
        path = Path(filepath)
        contents = path.read_text()
    except FileNotFoundError:
        print('-----------------')
        print("Please enter the right file path")
    else:
        print('-----------------')
        print(contents)

files = ['dogs.txt','rats.txt','cats.txt']
for file in files:
    read_contents(file)

