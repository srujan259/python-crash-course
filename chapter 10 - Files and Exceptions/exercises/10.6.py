print("Addition of 2 numbers")
print("Enter q to quit at any time")
while True:
    number1 = input("Enter number1 : ")
    if number1 == 'q':
        break
    number2 = input("Enter number2 : ")
    if number2 == 'q':
        break


    try:
        result = int(number1) + int(number2)
    except ValueError:
        print(f"Please enter only numbers, you entered '{number1}' and '{number2}' ")
    else:
        print(f"Addition of {number1} and {number2} is {result}")