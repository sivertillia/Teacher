from matplotlib import pyplot as plt
import numpy as np
# from random import randint

y = [1,2,1,5,1]
x = ["q","1","asd","aasd","dd"]
z = np.random.random(100)

a = [1, 2, 3, 4, 5]
z1 = [10, 17, 24, 16, 22]
z2 = [12, 14, 21, 13, 17]

ax = plt.subplot()
# ax.bar(x, y, color='red')
# ax.hist(z)
# ax.pie(y, labels=y)
# ax.boxplot([z1, z2])
# ax.errorbar(a, z1, xerr=1, yerr=0.5)
ax.fill(x, y)

plt.show()