from name_function import get_formatted_name

print (" Enter q at any time to quit ")
while True:
    first = input("\nFirst Name:")
    if first == 'q':
        break
    last = input("Last Name:")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\t Neatly formatted name is {formatted_name}")