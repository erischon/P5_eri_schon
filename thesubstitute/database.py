import mysql.connector

from config import *
from mysql.connector import errorcode
from tables import Tables

class Database:
    """ """

    def __init__(self):
        """ """
        self.host = HOST
        self.user = USER
        self.password = PASSWORD
        self.db_name = 'PureBeurre'
        self.tables = Tables()

    def connection(self):
        """ """

        try:
            self.connection = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.db_name)

            self.mycursor = self.connection.cursor()

            if (self.connection.is_connected()):
                print(f"REUSSITE : Connection à la base {self.db_name} effectuée.")
            
            return self.mycursor

        except mysql.connector.Error as error:
            print("ECHEC : impossible de me connecter, erreur : {}".format(error))

    def db_create(self):
        """ """
        mycursor = self.connection()
        
        try:
            mycursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(self.db_name))
            print(f"REUSSITE : création de la base {self.db_name} effectuée.")
        
        except mysql.connector.Error as err:
            print("ECHEC : impossible de créer la base, erreur : {}".format(err))
            exit(1)

    def tables_create(self):
        """ """
        mycursor = self.connection()

        for table_name in self.tables.TABLES:
            table_description = self.tables.TABLES[table_name]
            
            try:
                mycursor.execute(table_description)
                print("REUSSITE : la création de la table {} est effectuée.\n".format(table_name), end='')
            
            except mysql.connector.Error as err:
                print("ECHEC : impossible de créer la table, erreur : {}".format(error))

    def load_nutriscore(self):
        mycursor = self.connection()

        try:
            add_nutriscore = ("INSERT INTO nutriscore (nut_id, nut_type) VALUES (%s,%s)")
            values = (1, 'A')
            self.mycursor.execute(add_nutriscore, values)
            values = (2, 'B')
            self.mycursor.execute(add_nutriscore, values)      
            values = (3, 'C')
            self.mycursor.execute(add_nutriscore, values) 
            values = (4, 'D')
            self.mycursor.execute(add_nutriscore, values) 
            values = (5, 'E')
            self.mycursor.execute(add_nutriscore, values) 
            
            self.connection.commit()

            print("Les différents Nutriscore ont été chargés dans la base.")

        except mysql.connector.Error as error:
            print("Erreur lors du chargement : {}".format(error))

if __name__ == "__main__":
    database = Database()
