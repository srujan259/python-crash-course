def make_sandwich(no_of_sandwiches, *ingredients):
    """ Summarixe the sandwich you want to make """
    print(f" We are making {no_of_sandwiches} sandwiches using the follow ingredients")
    for ingredient in ingredients:
        print(f"- {ingredient}")