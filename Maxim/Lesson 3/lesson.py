import sqlite3

db = 'my_db.db'

data = ("Illya", "Sivert")

name = "Illya"
name2 = "asdasda"

with sqlite3.connect(db) as conn:
    cursor = conn.cursor()
    cursor.execute('UPDATE people SET name = ? WHERE id = 1', (name,))
    conn.commit()