fav_bikes = []

def add_to_list(bike):
    fav_bikes.append(bike)


num_of_fav_bikes= input("how many fav bikes:")

for i in range(int(num_of_fav_bikes)):
    a = input(f"which is your {i + 1} favourite bike:  ")
    add_to_list(a)

print(fav_bikes)

