import sqlite3

db = 'book_database.db'
# books = []
# book_id = 0
# book_quantity = 0
def getBook():
    # global books
    try:
        with sqlite3.connect(db) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM books")
            books = cursor.fetchall()
            for i in books:
                print(i)
            return books
    except sqlite3.Error as e:
        print('Ошибка:', e)

def setBook():
    # global book_id, book_quantity
    while True:
        try:
            book_id = int(input("Введите код книги: "))
            for i in books:
                if book_id == i[0]:
                    book_quantity = i[3]
                    book_quantity = book_quantity - 1
                    break
            break
        except:
            print("Вы ввели!")
    return book_quantity, book_id
def updateBook(data):
    try:
        with sqlite3.connect(db) as conn:
            cursor = conn.cursor()
            cursor.execute(f"UPDATE books SET quantity = ? WHERE id = ?", data)
            conn.commit()
    except sqlite3.Error as e:
        print('Ошибка:', e)
books = getBook()
data = setBook()
updateBook(data)