import matplotlib.pyplot as plt

x_value = list(range(-1000, 1001))
y_value = [x**2 for x in x_value]
ax = plt.subplot()
ax.scatter(x_value, y_value, s=5, color='red')


plt.show()