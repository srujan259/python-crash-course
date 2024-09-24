pizzas = ['bbq', 'periperi', 'chicken-tikka', 'classic']
friend_pizzas = pizzas[:]
pizzas.append('chilli')
friend_pizzas.append('cheese')
print('My pizzas are:')
for pizza in pizzas:
    print(f' - {pizza}')
print('My Friend pizzas are:')
for pizza in friend_pizzas:
    print(f' - {pizza}')