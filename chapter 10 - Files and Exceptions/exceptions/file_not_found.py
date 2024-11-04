from pathlib import Path

path = Path("dummy.txt")
try:
    contents = path.read_text()
except FileNotFoundError as e:
    print(f"Sorry the path {path} is not found\n {e}")
else:
    print(contents)