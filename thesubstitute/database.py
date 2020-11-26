import mysql.connector
import time

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
        self.mycursor = self.db_connection()

    def db_connection(self):
        """ """
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.db_name,
            )

            self.cursor = self.connection.cursor()
            return self.cursor

        except mysql.connector.Error as error:
            self.view.display_text_error("ECHEC : impossible de se connecter.", f"Type de l'erreur : {error}")

    def db_create(self):
        """ """
        try:
            self.mycursor.execute(
                "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(self.db_name)
            )
            self.view.display_text("REUSSITE : la base est crée.")

        except mysql.connector.Error as error:
            self.view.display_text_error("ECHEC : impossible de créer la base.", f"Type de l'erreur : {error}")

    def tables_create(self):
        """ """
        for table_name in self.tables.TABLES:
            table_description = self.tables.TABLES[table_name]

            try:
                self.mycursor.execute(table_description)
                self.view.display_text(f"REUSSITE : la table {table_name.upper()} est active.")

            except mysql.connector.Error as error:
                self.view.display_text_error("ECHEC : impossible de créer la table.", f"Type de l'erreur : {error}")

    def tables_delete(self):
        """ """
        query = "SET FOREIGN_KEY_CHECKS = 0;"
        self.mycursor.execute(query)

        for n in range(len(self.tables.tab_names)):

            try:
                query = f"TRUNCATE TABLE {self.tables.tab_names[n]};"        
                self.mycursor.execute(query)
                self.view.display_text(f"REUSSITE : la table {self.tables.tab_names[n].upper()} est remise à zéro.")
                time.sleep(1)
            
            except mysql.connector.Error as error:
                self.view.display_text_error("ECHEC : problème lors du delete des tables", f"Type de l'erreur : {error}")


if __name__ == "__main__":
    database = Database()

    # database.connection()
    # database.db_create()
    # database.tables_create()
    # database.load_nutriscore()
    # database.tables_delete()
    # database.disconnect()
