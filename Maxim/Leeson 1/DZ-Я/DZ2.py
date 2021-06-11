import numpy as np
import matplotlib.pyplot as plt


params = ['O1', 'O2', 'O3', 'O4', 'O5', 'O6']
results = [25, 3.5, 4, 2, 3, 2]

theta = np.linspace(start=0, stop=2*np.pi, num=len(results), endpoint=False)
theta = np.concatenate((theta, [theta[0]]))
results = np.append(results, results[0])
fig = plt.figure(figsize=(5, 5), facecolor='#f3f3f3')
ax = fig.add_subplot(111, projection='polar')
ax.plot(theta, results, linewidth=2, color="red")
ax.set_thetagrids(range(0, 360, int(360 / len(params))), (params))
plt.yticks(np.arange(0, 10, 1.0), fontsize=8)
ax.set(facecolor='#f3f3f3')
ax.set_theta_offset(np.pi / 2)

pl = ax.yaxis.get_gridlines()
for line in pl:
    line.get_path()._interpolation_steps = 5

plt.show()