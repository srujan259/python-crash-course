def get_formatted_name(first_name, last_name, middle_name=''):
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

name = get_formatted_name("srujan", "kottapally", "kumar")
print(f"Full name is {name}")