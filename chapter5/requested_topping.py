#requested_toppings = ['mushrooms', 'green peppers', 'extra_cheese']
requested_toppings = []

if requested_toppings:
    for topping in requested_toppings:
        if(topping=='green peppers'):
            print('Sorry we ran out of green peppers')
        else:
            print(f'Adding {topping} to the Pizza!')
    print('pizza done')
else:
    print('Are you sure you want a plain pizza')
