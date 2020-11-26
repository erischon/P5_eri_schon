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
        self.mycursor = self.connection()

    def connection(self):
        """ """
        try:
            self.connect = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.db_name,
            )

            self.cursor = self.connect.cursor()
            return self.cursor

        except mysql.connector.Error as error:
            self.view.display_text_error("ECHEC : impossible de se connecter.", f"Type de l'erreur : {error}")

    def disconnect(self, connection):
        if (connection.is_connected()):
            self.mycursor.close()
            connection.close()

    def db_create(self):
        """ """
        # mycursor = self.connection()

        try:
            self.mycursor.execute(
                "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(self.db_name)
            )
            self.view.display_text("REUSSITE : la base est crée.")

        except mysql.connector.Error as error:
            self.view.display_text_error("ECHEC : impossible de créer la base.", f"Type de l'erreur : {error}")

    def tables_create(self):
        """ """
        # mycursor = self.connection()

        for table_name in self.tables.TABLES:
            table_description = self.tables.TABLES[table_name]

            try:
                self.mycursor.execute(table_description)
                self.view.display_text(f"REUSSITE : la table {table_name.upper()} est active.")

            except mysql.connector.Error as error:
                self.view.display_text_error("ECHEC : impossible de créer la table.", f"Type de l'erreur : {error}")

    def tables_drop(self):
        """ """
        pass

    def tables_delete(self):
        """ """
        mycursor = self.connection()

        query = "SET FOREIGN_KEY_CHECKS = 0;"
        mycursor.execute(query)

        for n in range(len(self.tables.tab_names)):

            try:
                query = f"TRUNCATE TABLE {self.tables.tab_names[n]};"        
                mycursor.execute(query)
            
            except mysql.connector.Error as error:
                self.view.display_text_error("ECHEC : problème lors du delete des tables", f"Type de l'erreur : {error}")

    def load_nutriscore(self):
        """ """
        mycursor = self.connection()

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

            self.connection.commit()

            print("Les différents Nutriscore ont été chargés dans la base.")

        except mysql.connector.Error as error:
            self.view.display_text_error("ECHEC : problème lors du chargement.", f"Type de l'erreur : {error}")


if __name__ == "__main__":
    database = Database()

    # database.connection()
    # database.db_create()
    # database.tables_create()
    # database.load_nutriscore()
    # database.tables_delete()
