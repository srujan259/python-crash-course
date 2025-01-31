import matplotlib.pyplot as plt

input_values = range(1,5001)
cubes = [x**3 for x in input_values]
# print(cubes)

fig, ax = plt.subplots()
ax.plot(input_values, cubes, linewidth=3)
ax.set_title("Cubes", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)
ax.tick_params(axis='both', labelsize=14)
plt.show()