import matplotlib.pyplot as plt

plt.style.use('dark_background')
a = [1,2,1]
# plt.figure()
# plt.title('Hello')
# print(plt.style.available)
ax = plt.subplot()

ax.plot(a, color='red', linestyle='-')

plt.show()