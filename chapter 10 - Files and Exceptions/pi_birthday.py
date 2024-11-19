## check if my birthday is present in the pi digits
from pathlib import Path

path = Path('pi_million_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(pi_string)
birthday = input("Enter your birthday in mmddyy format:")
if birthday in pi_string:
    print("Yay your birthday is in pi")
else:
    print("da da daaaaa")
    