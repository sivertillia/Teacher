import matplotlib.pyplot as plt

x = [12, 5, 10, 7, 5]
y = [12, 7, 5, 7, 12]

plt.figure(figsize=(6, 5))
ax = plt.subplot()
ax.scatter(x, y, s=100)
ax.set_xlabel("Кординаты Х", fontsize=15)
ax.set_ylabel("Кординаты Y")

plt.show()