import mysql.connector

cnx = mysql.connector.connect(user='root', password='mysql', host='mysql', database='university')
cursor = cnx.cursor()
cursor.execute("Use university;")
cursor.execute("SELECT lesson, COUNT(*) as num_students FROM recordBook GROUP BY lesson;")
answer = cursor.fetchall()
for (subject, num_students) in answer:
    print(f'{subject}: {num_students} students')

cursor.close()
cnx.close()
