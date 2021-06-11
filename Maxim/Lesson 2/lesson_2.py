import sqlite3

db = 'my_database.db'

def login():
    login = input("Логин: ")
    password = input("Пароль: ")
    data = (login, password)
    try:
        with sqlite3.connect(db) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT login,password FROM accounts WHERE login=? AND password=?", data)
            result = cursor.fetchone()
            if data == result:
                print('Успешно вошли')
            else:
                print("Не верный пароль или логин!")
    except sqlite3.Error as e:
        print('Ошибка:', e)
    


text = "Виберите:\n"
text += "1. Авторизация\n"
text += "2. Регистрация\n"
text += "3. Выход\n"

while True:
    print("\n"+text)
    inputs = int(input("Выберите вариант: "))
    if inputs==1:
        login()
    elif inputs==2:
        register()
    elif inputs==3:
        break