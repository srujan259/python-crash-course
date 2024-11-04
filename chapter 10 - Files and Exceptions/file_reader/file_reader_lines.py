from pathlib import Path
path = Path('pi_digit.txt') # Path object
contents = path.read_text()
lines = contents.splitlines()
print(type(lines)) # get type of lines
for line in lines:
    print(line)
