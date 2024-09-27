glossary = {'lists':'list of items like an array', 
            'for': 'to loop through a specific range', 
            'if':'conditionaly check a given range of elements', 
            'slice': 'to cut a list', 
            'tuples': 'lists that cant change'}
print(f'Lists: {glossary["lists"]}')

for key, value in glossary:
    print(key)
    print(value)
    print('------')