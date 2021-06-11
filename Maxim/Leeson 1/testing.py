from matplotlib import pyplot as plt

from rand_walk import RandowWalk

rw = RandowWalk(100)
rw.fill_walk()

ax = plt.subplot()
ax.scatter(rw.x_values, rw.y_values)

plt.show()