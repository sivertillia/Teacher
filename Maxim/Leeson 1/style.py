from matplotlib import pyplot as plt

plt.figure(figsize=(10,10))
plt.style.use('seaborn')
x_value = list(range(-1000, 1001))
y_value = [x**2 for x in x_value]
ax = plt.subplot()
ax.scatter(x_value, y_value, s=5, color='black')
# ax.plot(x_value, y_value)


plt.show()