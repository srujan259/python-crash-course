print("Give me 2 numbers, and I'll divide them.")
print("Press 'q' if you want to exit.")

while True:
    first_number = input("Enter the first number: ")
    if first_number.lower() == 'q':
        break

    second_number = input("Enter the second number: ")
    if second_number.lower() == 'q':
        break

    try:
        # Convert inputs to integers and perform division
        num1 = int(first_number)
        num2 = int(second_number)
        result = num1 / num2

    except ZeroDivisionError:
        print("Can't divide by 0. Please enter a different second number.")

    except ValueError:
        print("Please enter valid integers.")

    else:
        print(f"Result of {num1} / {num2} = {result}")
