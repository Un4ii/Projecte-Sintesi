import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Admin123.",
    database="foodmatch"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM Usuarios")
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()
