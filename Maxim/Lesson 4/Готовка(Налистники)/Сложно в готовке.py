from matplotlib import pyplot as plt
from sqlite3 import connect, Error

db = "database.db"
models = []
data = []
try:
    with connect(db) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT model FROM phone")
        models_db = cursor.fetchall()
        print(models_db)
        # print("id\t", "Model\t", "2018\t", "2019\t", "2020")
        for i in models_db:
            print(i)
            for k in i:
                models.append(k)
except Error as e:
    print("Error: ", e)
try:
    with connect(db) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT "mln/2018","mln/2019","mln/2020" FROM phone')
        data_db = cursor.fetchall()
        print(data_db)
        for i in data_db:
            i_temp = []
            for k in i:
                i_temp.append(float(k))
            data.append(list(i_temp))
except Error as e:
    print("Error: ", e)

    
fig = plt.figure()
# plt.style.use('seabornasda')
# print(plt.style.available)
# Добавление на рисунок прямоугольной (по умолчанию) области рисования

# x_value = list(range(-1000, 1001))
# y_value = [x**2 for x in x_value]

a = [2, 4, 1]
b = ["2018", "2019", "2020"]

# scatter1 = plt.scatter(y_value, x_value)
# plt.plot(b, data[0], '-', b, data[1], '--', b, data[2], '-.', b, data[3], ':',)
plt.plot(b, data_db[0], b, data_db[1], b, data_db[2], b, data_db[3])
# graph1 = plt.plot(b, data_db[0], color='aqua', linestyle='--', linewidth=5)
# graph1 = plt.plot(b, data_db[1], color='aqua', linestyle='--', linewidth=5)
# graph1 = plt.plot(b, data_db[2], color='aqua', linestyle='--', linewidth=5)
# graph1 = plt.plot(b, data[3], color='aqua', linestyle='--', linewidth=5)

plt.show()