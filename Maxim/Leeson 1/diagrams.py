from matplotlib import pyplot as plt
import numpy as np

s = ['one','two','three ','four' ,'five']
x = [1, 2, 3, 4, 5]
z = np.random.random(100)
z1 = [10, 17, 24, 16, 22]
z2 = [12, 14, 21, 13, 17]

# bar()
fig = plt.figure()
plt.bar(x, z1)
plt.title('Simple bar chart')

# hist()
fig = plt.figure()
plt.hist(z)
plt.title('Simple histogramm')

# pie()
fig = plt.figure()
plt.pie(z1, labels=z1)
plt.title('Simple pie chart')

# boxplot()
fig = plt.figure()
plt.boxplot([z1, z2])
plt.title('Simple box whisker chart')

# errorbar()
fig = plt.figure()
plt.errorbar(x, z1, xerr=1, yerr=0.5)
plt.title('Simple error bar chart')

plt.show()