rivers = {'nile':'egypt', 'ganga': 'india', 'amazon':'africa'}

for river, country in rivers.items():
    print(f'{river} flows through {country}\n')

for river in river:
    print(river)

for country in rivers.values():
    print(country)