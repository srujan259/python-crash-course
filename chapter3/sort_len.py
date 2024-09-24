fruits = ['banana', 'apple', 'orange', 'grape', 'mango']
sorted_fruits = fruits.copy()
sorted_fruits.sort()

print(fruits)
print(sorted_fruits)

# temporary sorting

print(f"original list")
print(fruits)

print(f'here is the sorted list')
print(sorted(fruits))

# Printing in reverse order
fruits.reverse()
print(f"Reverse order is {fruits}")

#len of list

print(f"length of fruits list is {len(fruits)}")