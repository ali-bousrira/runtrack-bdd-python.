import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2879",
    database="laplateforme"
)

cursor = db.cursor()

table_name = "etage"
cursor.execute(f"SELECT sum(superficie) FROM {table_name}")

rows = cursor.fetchall()

for row in rows:
    print(f"La superficie de La Plateforme est de {row[0]} m2")
db.close()