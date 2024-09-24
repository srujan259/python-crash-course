peoples = [{'first_name': 'ancy', 'last_name':'john', 'age': 30, 'city': 'hyderabad'}, {'first_name': 'srujan', 'last_name':'k', 'age': 30, 'city': 'kerala'}]
for user in peoples:
    name = f"{user['first_name']} {user['last_name']}"
    age = f"{user['age']}"
    location = f"{user['city']}"

    print(f'{name} is of age {age} in {location}')