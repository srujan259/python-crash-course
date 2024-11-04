from pathlib import Path
path = Path('guest.txt')
name = input('Please enter your name: ')
path.write_text(name)