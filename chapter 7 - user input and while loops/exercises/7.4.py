prompt = "Hey Enter the Pizza topping you want to add! \nOnce done you can 'quit'"
while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f'Awesome will add {topping} to the pizza')
    else:
        break