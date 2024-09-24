fav_languages = {
    'srujan': ['python', 'go'],
    'sarah': ['java'],
    'sujay': ['c', 'c++']
}

for name, languages in fav_languages.items():
    print(f'{name.title()} fav languages are :')
    for l in languages:
        print(f'\t{l}')