from matplotlib import pyplot
from diaramma import create_diagramm

cd = create_diagramm()
cd.fill_array()
ax = pyplot.subplot()
ax.bar(cd.x_value, cd.y_value, color= '#63ffdd')

pyplot.show()