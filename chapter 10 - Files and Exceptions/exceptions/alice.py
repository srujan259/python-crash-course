from pathlib import Path
path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print('Sorry file is not found')
else:
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")