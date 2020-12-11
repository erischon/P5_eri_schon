import time

from .tables import Tables
from .views import Views
from .connection import Connection


class Database:
    """ I'm the database. """

    def __init__(self):
        """ """
        self.connection = Connection()
        self.db_name = self.connection.db_name
        self.tables = Tables()
        self.view = Views()

    def db_create(self):
        """ I create the database. """
        try:
            self.connection.execute(
                "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(
                    self.db_name
                )
            )
            self.view.display_text("REUSSITE : la base est crée.")

        except Exception as error:
            self.view.display_text_error("ECHEC : la base n'est pas crée.", f"Type de l'erreur : {error}")

    def tables_create(self):
        """ I create tables in the database. """
        for table_name in self.tables.TABLES:
            table_description = self.tables.TABLES[table_name]

            try:
                self.connection.execute(table_description)
                self.view.display_text(
                    f"REUSSITE : la table {table_name.upper()} est active."
                )

            except Exception as error:
                self.view.display_text_error("ECHEC : les tables ne sont pas crées.", f"Type de l'erreur : {error}")

    def tables_delete(self):
        """ I delete all the tables in the database. """
        # self.connection.close()
        # self.connection = Connection()

        query = "SET FOREIGN_KEY_CHECKS = 0;"
        self.connection.execute(query)

        for n in range(len(self.tables.tab_names)):

            try:
                query = f"TRUNCATE TABLE {self.tables.tab_names[n]};"
                self.connection.execute(query)
                self.view.display_text(
                    f"REUSSITE : la table {self.tables.tab_names[n].upper()} est remise à zéro."
                )
                time.sleep(1)

            except Exception as error:
                self.view.display_text_error("ECHEC : problème lors du delete des tables", f"Type de l'erreur : {error}")


if __name__ == "__main__":
    database = Database()

    # === Tests of methods ===
    # database.db_create()
    # database.tables_create()
    database.tables_delete()
