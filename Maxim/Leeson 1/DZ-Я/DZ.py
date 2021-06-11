from matplotlib import pyplot as plt
from add_dia import RandomDiagram

rd = RandomDiagram(15)
rd.dia_rand()

ax = plt.subplot()
ax.bar(rd.y_values, rd.x_values, color='red')

plt.show()

if 1==1:
    print()
else:
    continue