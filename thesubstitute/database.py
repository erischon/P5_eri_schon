import mysql.connector

from config import *
from mysql.connector import errorcode
from tables import Tables
from views import Views


class Database:
    """ """

    def __init__(self):
        """ """
        self.host = HOST
        self.user = USER
        self.password = PASSWORD
        self.db_name = "PureBeurre"
        self.tables = Tables()
        self.view = Views()

    def connexion(self):
        """ """
        try:
            self.connexion = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.db_name,
            )

            self.mycursor = self.connexion.cursor()
            return self.mycursor

        except mysql.connector.Error as error:
            self.view.display_text("ECHEC : impossible de se connecter.", f"Type de l'erreur : {error}")

    def db_create(self):
        """ """
        mycursor = self.connexion()

        try:
            mycursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(self.db_name)
            )
            print(f"REUSSITE : création de la base {self.db_name} effectuée.")

        except mysql.connector.Error as error:
            self.view.display_text("ECHEC : impossible de créer la base.", f"Type de l'erreur : {error}")
            exit(1)

    def tables_create(self):
        """ """
        mycursor = self.connexion()

        for table_name in self.tables.TABLES:
            table_description = self.tables.TABLES[table_name]

            try:
                mycursor.execute(table_description)
                print(
                    "REUSSITE : la création de la table {} est effectuée.\n".format(
                        table_name
                    ),
                    end="",
                )

            except mysql.connector.Error as error:
                self.view.display_text("ECHEC : impossible de créer la table.", f"Type de l'erreur : {error}")

    def tables_drop(self):
        """ """
        pass

    def tables_delete(self):
        """ """
        mycursor = self.connexion()

        query = "SET FOREIGN_KEY_CHECKS = 0;"
        mycursor.execute(query)

        for n in range(len(self.tables.tab_names)):

            try:
                query = f"TRUNCATE TABLE {self.tables.tab_names[n]};"        
                mycursor.execute(query)
            
            except mysql.connector.Error as error:
                self.view.display_text("ECHEC : problème lors du delete des tables", f"Type de l'erreur : {error}")

    def load_nutriscore(self):
        """ """
        mycursor = self.connexion()

        try:
            add_nutriscore = "INSERT INTO nutriscore (nut_id, nut_type) VALUES (%s,%s)"
            values = (1, "A")
            self.mycursor.execute(add_nutriscore, values)
            values = (2, "B")
            self.mycursor.execute(add_nutriscore, values)
            values = (3, "C")
            self.mycursor.execute(add_nutriscore, values)
            values = (4, "D")
            self.mycursor.execute(add_nutriscore, values)
            values = (5, "E")
            self.mycursor.execute(add_nutriscore, values)

            self.connexion.commit()

            print("Les différents Nutriscore ont été chargés dans la base.")

        except mysql.connector.Error as error:
            self.view.display_text("ECHEC : problème lors du chargement.", f"Type de l'erreur : {error}")


if __name__ == "__main__":
    database = Database()

    # database.connexion()
    # database.db_create()
    # database.tables_create()
    # database.load_nutriscore()
    database.tables_delete()
