fav_number = {'bob':1, 'sujay':47, 'kiara': 7}

people = ['bob', 'sujay', 'kiara', 'ancy', 'sowmya']

for p in people:
    if p in fav_number:
        print(f'THanks {p} for taking the poll')
    else:
        print(f'{p} please take the poll')