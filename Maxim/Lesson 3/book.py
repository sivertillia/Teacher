import sqlite3

db = "database_books.db"


def getBook():
    try:
        with sqlite3.connect(db) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM books")
            books = cursor.fetchall()
            print("id", "Name", "Author", "Count")
            for i in books:
                for k in i:
                    print(k, " ", end="")
                print("\n")
            setBook(books)
    except sqlite3.Error as e:
        print("Error: ", e)

def setBook(books):
    while True:
        try:
            book_id = input("Введите код книги q чтобы выйти: ")
            if book_id == "q":
                break
            book_id = int(book_id)
            for i in books:
                if book_id == i[0]:
                    book_count = i[3]
                    book_count = book_count - 1
                    updateBooks(book_id, book_count)

        except ValueError:
            print("Вы ввели не число!")

def updateBooks(id, count):
    try:
        with sqlite3.connect(db) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE books SET count = ? WHERE id = ?", (count, id))
            conn.commit()
            print("Вы успешно купили книжку")
    except sqlite3.Error as e:
        print("Error: ", e)

getBook()