available_toppings = ['mushrooms', 'pineapple', 'green peppers', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'Adding {requested_topping} to the pizza')
    else:
        print(f'Sorry topping {requested_topping} unavailable')