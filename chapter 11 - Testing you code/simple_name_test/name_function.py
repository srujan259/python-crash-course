def get_formatted_name(firstname, lastname, middle = ""):
    """ Simple function to concat name"""
    if middle:
        name = f"{firstname} {middle} {lastname}"
    else:
        name = f"{firstname} {lastname}"
    return name.title()
