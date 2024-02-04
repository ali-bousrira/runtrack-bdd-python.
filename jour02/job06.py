import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2879",
    database="laplateforme"
)

cursor = db.cursor()

table_name = "salle"
cursor.execute(f"SELECT sum(capacite) FROM {table_name}")

rows = cursor.fetchall()

for row in rows:
    print(f"La capacité de toutes les salle est de : {row[0]}")
db.close()