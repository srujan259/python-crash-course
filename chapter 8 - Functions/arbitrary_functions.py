def pizza_toppings(size, *toppings):
    """ Pizza toppings """
    print(f'Toppings of {size} inch pizza are:')
    for topping in toppings:
        print(f"\t - {topping}")

pizza_toppings('6','cheese', 'paneer', 'bbq')


