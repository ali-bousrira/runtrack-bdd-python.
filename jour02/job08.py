
class zoo () :
    def __init__(self) :
        #si la db existe deja
        import mysql.connector
        try :
            self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="2879",
            database="zoo"

            )

            self.cursor = self.db.cursor ()

        #conection pour la creation de la db avec def initialisation ()
        except :

            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="2879"
                )

            self.cursor = self.connection.cursor ()


    #creation de la db
    def initialisation (self) :
        import mysql.connector

        command = f"CREATE DATABASE zoo"

        self.cursor.execute (command)

        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="2879",
        database="zoo"

        )

        self.cursor = self.db.cursor ()

        self.crea_table_animaux ()

        self.crea_table_cage ()

    #affichager des tables 
    def verif (self) :
        command = f"show tables;"

        self.cursor.execute (command)

        return (self.cursor.fetchall ())
        
        
    #creation de table animal
    def crea_table_animaux (self) :
        command = f"create table animal (id int not null auto_increment primary key, nom varchar (255) not null, race varchar (255) not null, id_cage int not null, date varchar (25) not null, pays varchar (25) not null)"

        self.cursor.execute (command)

    #creation de table cage
    def crea_table_cage (self) :
        command = f"create table cage (id int not null auto_increment primary key, superficie decimal not null, capacite int not null, contenu varchar(25))"

        self.cursor.execute (command)

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
    #creation du nouveau animal
    def crea_animal (self) :
        
        nom = input ("donner le nom du nouveau animal : \n")
        race = input ("donner la race du nouveau animal : \n")
        id_cage = self.get_int ("donner l'id de cage du nouveau animal : \n")
        date = input ("donner la date de naissance du nouveau animal : \n")
        pays = input ("donner le pays du nouveau animal : \n")
        
        command = """insert into animal (nom, race, id_cage, date, pays)
        values
        (%s,%s,%s,%s,%s);
        """

        self.cursor.execute (command, (nom, race, id_cage, date, pays))

        self.db.commit ()

    #changement des valeur d'un animal
    def update_animal (self) :
        choix = self.get_int ("donner l'id de l'animale a update : \n")

        command = f" select * from animal where id = {choix}"

        self.cursor.execute (command)

        rows = self.cursor.fetchall ()

        '''print (rows)'''

        test_nom = self.cont_saisie("vouler vous changer le nom de l'animal : \n")

        test_race = self.cont_saisie("vouler vous changer la race de l'animal : \n")

        test_id_cage = self.cont_saisie("vouler vous changer lid de cage de l'animal : \n")

        test_date = self.cont_saisie("vouler vous changer la date de naissance de l'animal : \n")

        test_pays = self.cont_saisie("vouler vous changer le pays de l'animal : \n")

        if test_nom == 'oui':
            nom = input ("donner le nouveau nom de l'animal : \n")
        else:
            nom = rows [0][1]
        if test_race == 'oui' :
            race = input ("donner le nouveau race de l'animal : \n")
        else:
            race = rows [0][2]
        if test_id_cage == 'oui' :
            id_cage = self.get_int ("donner le nouveau id de cage de l'animal : \n")
        else :
            id_cage = rows [0][3]
        if test_date == 'oui' :
            date = input ("donner le nouvel date de naissance de l'animal : \n")
        else :
            date = rows [0][4]
        if test_pays == 'oui' :
            pays = input ("donner le nouveau pays de l'animal : \n")
        else :
            pays = rows [0][5]

        command = """UPDATE animal SET nom = %s, race = %s, id_cage = %s, date = %s, pays = %s WHERE id = %s;"""

        self.cursor.execute (command, (nom, race, id_cage, date, pays, choix))

        self.db.commit ()

    #lire la tables animal
    def read_animal (self) :
        test = self.get_int ("donner l'id de l'animal a affficher ou 0 pour tout afficher : \n")

        if test == 0 :
            print (test)
            command = f"select * from animal"

            self.cursor.execute(command)

            rows = self.cursor.fetchall()

            for row in rows :
                print (f"info animal \n id = {row [0]}, nom = {row [1]}, race = {row [2]}, id_cage = {row [3]}, date de naissance = {row [4]}, pays d'origine = {row [5]}")

        else :
            self.read_animal_simple (str (test))

    #lecture simple 
    def read_animal_simple (self, id) :
        for i in range (len (id)) :
            command = f"select * from animal where id = {int (id [i])}"

            self.cursor.execute(command)

            row = self.cursor.fetchall()

            print (f"info animal \n id = {row [0][0]}, nom = {row [0][1]}, race = {row [0][2]}, id_cage = {row [0][3]}, date de naissance = {row [0][4]}, pays d'origine = {row [0][5]}")

    #suprimer un employer
    def delete_animal (self) :
        try :
            choix = self.get_int ("donner l'id de l'animal a suprimer : \n")

            command = f"DELETE FROM animal WHERE id = {choix}"

            self.cursor.execute (command)

            self.db.commit ()
        except :
            print ("erreur")

    #creation du nouvel cage
    def crea_cage (self) :
        
        superficie = input ("donner la superficie du nouvl cage : \n")
        capacite = input ("donner la capacite du nouvel cage : \n")

        test_contenue = self.cont_saisie ("esque cette cage contien un ou plusieure animaux : \n")

        if test_contenue.upper () == 'OUI' :
            contenu = input ("donner l'id des animlaux dans cette cage sous form ididid: \n")
        
            command = """insert into cage (superficie, capacite, contenu)
            values
            (%s,%s,%s);
            """

            self.cursor.execute (command, (superficie, capacite, contenu))

        else :
            command = """insert into cage (superficie, capacite)
            values
            (%s,%s);
            """
            self.cursor.execute (command, (superficie, capacite))


        self.db.commit ()

    #lire la tables 
    def read_cage (self) :
        command = f"select * from cage"

        self.cursor.execute(command)

        rows = self.cursor.fetchall()

        for row in rows :
            print (f"info cage id = {row [0]} \n superficie = {row [1]}, capacite = {row [2]}, contenu = ",end = '')
            if not (row [3] == None) :
                print ("")
                self.read_animal_simple (row [3])
            else :
                print ("la cage est vide")

    #suprimer un employer
    def delete_cage (self) :
        try :
            choix = self.get_int ("donner l'id de la cage a suprimer : \n")

            command = f"DELETE FROM cage WHERE id = {choix}"

            self.cursor.execute (command)

            self.db.commit ()
            
        except :
            print ("erreur")

    #update cage 
    def update_cage (self) :
        choix = self.get_int ("donner l'id de l'animale a update : \n")

        command = f" select * from animal where id = {choix}"

        self.cursor.execute (command)

        rows = self.cursor.fetchall ()

        '''print (rows)'''

        test_superficie = self.cont_saisie("vouler vous changer la superficie de la cage : \n")

        test_capacite = self.cont_saisie("vouler vous changer la capaciter de la cage : \n")

        test_contenu = self.cont_saisie("vouler vous changer le contenue de la cage : \n")
    
        if test_superficie == 'oui':
            superficie = input ("donner la nouvel superficie de la cage : \n")
        else:
            superficie = rows [0][1]
        if test_capacite == 'oui' :
            capacite = input ("donner la nouvel capacite de la cage : \n")
        else:
            capacite = rows [0][2]
        if test_contenu == 'oui' :
            contenu = self.get_int ("donner le nouveau contenue de la cage : \n")
        else:
            contenu = rows [0][3]

        command = """UPDATE cage SET superficie = %s, capacite = %s, contenu = %s WHERE id = %s;"""

        self.cursor.execute (command, (superficie, capacite, contenu, choix))

        self.db.commit ()

    #calcule la superficie total des cages
    def cal_superficie (self) :
        command = "SELECT SUM(superficie) FROM cage"

        self.cursor.execute(command)

        total_superficie = self.cursor.fetchone()[0]

        return total_superficie

test = zoo ()
#executer si la db nexiste pas
#test.initialisation ()
#test.crea_animal ()
#test.crea_cage ()
#test.update_animal ()
#print (test.verif ())
#test.read_animal ()
#test.read_cage ()
#test.delete_cage ()
#test.update_cage ()
#print (f"la superficie total des cages est : {test.cal_superficie ()}")