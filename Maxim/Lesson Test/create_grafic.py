import matplotlib.pyplot as plt

data = []
while True:
    a = input("Введите число или q чтобы выйти: ")
    if a == 'q':
        break
    try:
        a = int(a)
        data.append(a)
    except ValueError:
        print("Вы ввели не число")


plt.style.use('seaborn')
ax = plt.subplot()
ax.plot(data)
plt.show()