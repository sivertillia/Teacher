import mysql.connector as mysql
try:
    with mysql.connect(host="localhost",user="root",password="root", database="online_movie_rating",) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ")
        conn.commit()

except mysql.Error as e:
    print("Error: ", e)