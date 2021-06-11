import sqlite3

db = 'test.db'

def login():
    login = input('Логин: ')
    password = input('Пароль: ')
    data = (login, password)
    # print(data)
    try:
        with sqlite3.connect(db) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT login,password FROM auth WHERE login=? AND password=?;", data)
            result = cursor.fetchone()
            if data == result:
                print('Успешно вошли!\n')
            else:
                print('Не верный пароль или логин!')
    except:
        print("Произошла ошибка")
def register():
    login = input('Прийдумайте логин: ')
    password = input('Прийдумайте пароль: ')
    data = (login, password)
    print(data)
    try:
        with sqlite3.connect(db) as conn:
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO auth (login, password) VALUES {data}")
            conn.commit()
            print('Успешно зарегистрировались!')
    except:
        print("Произошла ошибка")

text = "Виберите:\n"
text += "1. Регистрация\n"
text += "2. Авторизация\n"
text += "3. Выйти\n"



while True:
    print('\n')
    print(text)
    inputs = int(input("What: "))
    if inputs==1:
        register()
    elif inputs==2:
        login()
    elif inputs==3:
        break