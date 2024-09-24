favourite_food = {'srujan':'pancakes', 'ancy':'pizza', 'kiara':'apple'}

for name,food in favourite_food.items():
    print(f'{name.title()} favourite food is {food}')


#keys() method

for names in favourite_food.keys():
    print(f'{names.title()}')

#default looping is done on keys itself with for

for name in favourite_food:
    print(name)

friends = ['ancy', 'sujay']

for name in sorted(favourite_food.keys()):
    print(f'Hi {name}')

    if name in friends:
        print(f' fav food is {favourite_food[name]}')