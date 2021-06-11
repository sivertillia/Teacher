import sqlite3

db = 'test.db'


with sqlite3.connect(db) as conn:
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO auth (login, password) VALUES ('sivert', '123456')")
    conn.commit()