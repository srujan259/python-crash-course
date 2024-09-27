pets = [{
    'kind': 'lab',
    'name': 'snoop',
    'owner': 'bob',
    'age': 5
    },
    {
    'kind': 'rabbit',
    'name': 'jimmy',
    'owner': 'ancy',
    'age': 1
    }
    ]

for pet in pets:
    print(pet)
    print(f"Details of pet {pet['name']}")

    for k, v in pet.items():
        print(f'\t {k} : {v}')