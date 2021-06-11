from mysql import connector as mysql

with mysql.connect(host="localhost", port=3306, user="root", password="root", database="online_movie_rating") as conn:
    cursor = conn.cursor()