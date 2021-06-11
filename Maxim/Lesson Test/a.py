import matplotlib.pyplot as plt

x_value = list(range(1, 1001))
y_value = []
for x in x_value:
    x=x**2
    y_value.append(x)


ax = plt.subplot()
ax.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Blues, s=5)


plt.show()