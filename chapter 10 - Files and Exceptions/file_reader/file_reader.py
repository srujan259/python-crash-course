from pathlib import Path
path = Path('pi_digit.txt') # Path object
print(path.exists()) # Check if the file exists
contents = path.read_text().rstrip()
print(contents) # Read the contents of the file
