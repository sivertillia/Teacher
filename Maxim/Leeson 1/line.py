import matplotlib.pyplot as plt

fig = plt.figure()
# plt.style.use('seabornasda')
print(plt.style.available)
# Добавление на рисунок прямоугольной (по умолчанию) области рисования

# x_value = list(range(-1000, 1001))
# y_value = [x**2 for x in x_value]

a = [1, 2, 2, 4, 1]
b = ["2015", "2016", "2017", "2018", "2019"]

# scatter1 = plt.scatter(y_value, x_value)

graph1 = plt.plot(b, a, color='aqua', linestyle='--', linewidth=5)

text1 = plt.text(2, 4, 'Text on\n figure', color='red', fontsize=14)
bar = plt.bar(b, a)

plt.show()