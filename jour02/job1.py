import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2879",
    database="laplateforme"
)

cursor = db.cursor()

table_name = "etudiant"
cursor.execute(f"SELECT * FROM {table_name}")

rows = cursor.fetchall()

for row in rows:
    print(row)

db.close()