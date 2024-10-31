from pathlib import Path
path = Path('pi_digit.txt')
print(path.exists())
contents = path.read_text().rstrip()
print(contents) 