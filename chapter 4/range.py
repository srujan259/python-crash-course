#to print from 1-5, in range value starts with the first number and stop when it reaches the second number
for value in range(1,6):
    print(value)

#convert range to list 

num_list = list(range(1,6))
print(num_list)

#print event numbers using range and step

even = list(range(2, 11, 2))
print(f'even numbers : {even}')

#square number first 10

sq_numbers = []
for value in range(1, 11):
    square = value**2
    sq_numbers.append(square)

print(f'sq numbers between 1-10 : {sq_numbers}')