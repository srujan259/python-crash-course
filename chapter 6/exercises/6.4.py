glossary = {'lists':'list of items like an array', 
            'for': 'to loop through a specific range', 
            'if':'conditionaly check a given range of elements', 
            'slice': 'to cut a list', 
            'tuples': 'lists that cant change'}

for concept, meaning in glossary.items():
    print(f'{concept}: {meaning}\n')