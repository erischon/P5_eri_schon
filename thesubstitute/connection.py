import mysql.connector

from config import *


class Connection:
    """ """

    def __init__(self):
        """ """
        self._host = HOST
        self._user = USER
        self._password = PASSWORD
        self.db_name = "PureBeurre"

        self._connect = self.db_connection()
        self._cursor = self._connect.cursor()
        
    def db_connection(self):
        """ """
        try:
            connection = mysql.connector.connect(
                host=self._host,
                user=self._user,
                password=self._password,
                database=self.db_name,
            )
            return connection

        except mysql.connector.Error as error:
            print("ECHEC : impossible de se connecter.", f"Type de l'erreur : {error}")
            exit()

    @property
    def connection(self):
        return self._connect

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()


if __name__ == "__main__":
    connection = Connection()

    print(connection.close)