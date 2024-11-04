from pathlib import Path
path = Path("learning_python.txt")
print(type(path))
contents = path.read_text()
for line in contents.splitlines():
    print(line)
