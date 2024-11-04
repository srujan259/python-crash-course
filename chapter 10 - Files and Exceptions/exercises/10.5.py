from pathlib import Path
path = Path('guest_book.txt')
names = ''
while True:
    name = input('Please enter your name: ')
    names += f"{name}\n"
    moreusers = input("are there more users: yes/no")
    if moreusers == 'yes':
        continue
    else:
        break
    
path.write_text(names)