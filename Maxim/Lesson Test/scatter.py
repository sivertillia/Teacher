import matplotlib.pyplot as plt

input_values = [1, 2, 9, 13, 13]
squares = [1, 2, 9, 25, 13]
fig, ax = plt.subplots()
print(max(squares))
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.scatter(input_values, squares, s=100)
# ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()