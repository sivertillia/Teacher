import sqlite3
from matplotlib import pyplot as plt

db = "database.db"

try:
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT "mln/2018","mln/2019","mln/2020" FROM phone')
        data = cursor.fetchall()
        print(data)
except sqlite3.Error as e:
    print("Error: ", e)

years = ["2018", "2019", "2020"]

fig = plt.subplot()
for i in range(len(data)):
    plt.bar(years, data[i])

plt.show()