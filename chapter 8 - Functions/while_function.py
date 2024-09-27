def formatted_name(first_name, last_name):
    """ Formatted Name """
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name")
    print("(You can press 'q' anytime you want to quit)\n")
    f_name = input("full_name:")
    if f_name == 'q':
        break
    l_name = input("last_name:")
    if l_name == 'q':
        break
        
        full_name = formatted_name(f_name, l_name)
        print(f"Hello {full_name}, How you achieve everything you wanted to!")
