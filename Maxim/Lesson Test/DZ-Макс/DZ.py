from matplotlib import pyplot

# a_list = []
#
# while True:
#     a = input()
#     if a == 'q':
#         break
#     else:
#         try:
#             a = int(a)
#             a_list.append(a)
#         except ValueError:
#             print("Вы ввели не число")
#
#
# ax = pyplot.subplot()
# ax.plot(a_list, linewidth=3)
#
# pyplot.show()

"""Дз, попытка первая"""
x_value = list(range(-10, 11))
x_value_10 = []
y_value = []
for x in x_value:
    if len(x_value_10) < 100:
        # x_value_10.append(x)
        x = x/10
        x_value_10.append(x)
        y = x**2
        y = round(y, 2)
        # print(y)
        y_value.append(y)
    else:
        break

ax = pyplot.subplot()
print(f"x_value_10: {len(x_value_10)}")
print(f"y_value: {len(y_value)}")
print(f"y_value: {y_value}")
ax.scatter(x_value_10, y_value)

pyplot.show()

"""Дз, попытка вторая"""
# x_value = list(range(-10, 11))
# y_value = []
# for x in x_value:
#     y = x**2
#     y_value.append(y)

# ax = pyplot.subplot()
# ax.plot(x_value, y_value)
# pyplot.show()
