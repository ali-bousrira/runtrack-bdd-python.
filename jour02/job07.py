import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2879",
    database="travaille"
)

#pour l'affichade des employe avec un salaire supérieur a 3000
'''cursor = db.cursor()

table_name = "employe"
cursor.execute(f"SELECT * FROM {table_name} where salaire > 3000")

rows = cursor.fetchall()

for row in rows:
    print(f"{row}")'''


#info + nom du service

'''cursor = db.cursor()


cursor.execute(f"SELECT * FROM employe")

rows = cursor.fetchall()

for row in rows:
    service_cursor = db.cursor()

    service_cursor.execute (f"select nom from service where {row [4]} = id")

    print(f"employe id {row[0]}, nom et prnom {row[1]} {row[2]}, salaire {row[3]} et le nom du service est {service_cursor.fetchall() [0] [0]}")'''


#classe salaire
class salaire () :
    def __init__ (self) :
        import mysql.connector

        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="2879",
        database="travaille"
        )

        self.cursor = db.cursor()

    #creer des employer
    def creat (self) :
        nom = input ("donner le nom du nouveau employe : \n")
        prenom = input ("donner le prenom du nouveau employe : \n")
        salaire = self.get_int ("donner le salaire du nouveau employe : \n")
        id_service = self.get_int ("donner l'id_service du nouveau employe : \n")

        info = (nom, prenom, salaire, id_service)
        command = """INSERT INTO employe (nom, prenom, salaire, id_service)
          VALUES 
          (%s, %s, %s, %s)"""

        self.cursor.execute(command, info)

        self.db.commit ()

    #lire la tables 
    def read (self) :
        command = f"select * from employe"

        self.cursor.execute(command)

        rows = self.cursor.fetchall()

        return rows

    #controle de saisie
    def cont_saisie (self, control) :
        chaine = input (control)
        while not (chaine.upper () == 'OUI') and not (chaine.upper () == 'NON') :
            chaine = input (control)
        return chaine

    #controle de saisie entier
    def get_int(self, prompt):
        while True:
            try:
                value = int(input(prompt))
                return value
            except ValueError:
                print("c'est pas un int")

    #mettre a jour d'un employe
    def update (self) :
        choix = self.get_int ("donner l'id de l'employe a update : \n")

        command = f" select * from employe where id = {choix}"

        self.cursor.execute (command)

        rows = self.cursor.fetchall ()

        '''print (rows)'''

        test_nom = self.cont_saisie("vouler vous changer le nom de l'employe a update : \n")

        test_prenom = self.cont_saisie("vouler vous changer le prenom de l'employe a update : \n")

        test_salaire = self.cont_saisie("vouler vous changer le salaire de l'employe a update : \n")

        test_id_service = self.cont_saisie("vouler vous changer le id_service de l'employe a update : \n")

        if test_nom == 'oui':
            nom = input ("donner le nouveau nom de l'employe : \n")
        else:
            nom = rows [0][1]
        if test_prenom == 'oui' :
            prenom = input ("donner le nouveau prenom de l'employe : \n")
        else:
            prenom = rows [0][2]
        if test_salaire == 'oui' :
            salaire = int (input ("donner le nouveau salaire de l'employe : \n"))
        else :
            salaire = rows [0][3]
        if test_id_service == 'oui' :
            id_service = int (input ("donner le nouveau id de srvice de l'employe : \n"))
        else :
            id_service = rows [0][4]

        command = """UPDATE employe SET nom = %s, prenom = %s, salaire = %s, id_service = %s WHERE id = %s;"""

        self.cursor.execute (command, (nom, prenom, salaire, id_service, choix))

        self.db.commit ()

    #suprimer un employer
    def delete (self) :
        choix = self.get_int ("donner l'id de l'employe a suprimer : \n")

        command = f"DELETE FROM employe WHERE id = {choix}"

        self.cursor.execute (command)

        self.db.commit ()


test = salaire ()

test.creat ()

test.update ()

test.delete ()

print (test.read ())


db.close()

