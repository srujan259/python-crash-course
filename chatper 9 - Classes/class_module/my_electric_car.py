from car import Car, ElectricCar

my_electric_car = ElectricCar('tata', 'nexon', 2024)

print(my_electric_car.battery.battery_size)
my_electric_car.battery.describe_battery()
my_car = Car('jaguar', 'XF', 2024)
my_car.read_odometer()