def sandwich_toppings(*toppings):
    """ Print sandwich toppings """
    print("Toppings to be included are:")
    for topping in toppings:
        print(f"- {topping}")


sandwich_toppings('butter', 'chicken', 'pepper')
sandwich_toppings('masala', 'curry')