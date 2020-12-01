import datetime
import time

from connection import Connection
from model import Model


class Save:
    """ """

    def __init__(self):
        self.connection = Connection()
        self.model = Model()

    def saving(self, prod_id):
        """ I save the substitut into the sauvegardes table. """
        check = self._check(prod_id)

        if check == False:
            try:
                query = f"INSERT INTO sauvegardes SET save_time='{datetime.datetime.now()}', prod_id='{prod_id}'"
                self.connection.execute(query)
                self.connection.commit()
            except:
                print("La sauvegarde n'a pas pu se faire.")
        else:
            print(check) 

    def save_listing(self):
        """ I display the list of all the save. """
        print(
            """
            Choisissez la sauvegarde
            que vous souhaitez visualiser : \n"""
        )
        query = f"SELECT * FROM sauvegardes"
        self.connection.execute(query)
        result = self.connection.fetchall()

        for n in range(len(result)):
            save_id, prod_id, datetime = result[n]
            infos = self.model.product_infos(prod_id)
            print(f"{save_id} - Substitut : {infos['prod_name']}, sauvegardé le {datetime}")

        choice = input(
            """
            votre choix : """
        )

        if not choice.isdigit():
            print(
                """
            Vous devez entrer un chiffre
            Merci de réessayer."""
            )
            time.sleep(2)
            return self.save_listing()
        elif int(choice) >= 1 and int(choice) <= (len(result)):
            save_id = choice
            return save_id
        else:
            print(
                """
            Ce numéro de sauvegarde n'existe pas
            Merci de réessayer."""
            )
            time.sleep(2)
            return self.save_listing()

    def save_display(self, save_id):
        """ """
        query = f"SELECT * FROM sauvegardes WHERE save_id='{save_id}'"
        self.connection.execute(query)
        result = self.connection.fetchall()

        save_id, prod_id, datetime = result[0]
        infos = self.model.product_infos(prod_id)
        self.model.sub_prod_infos(infos)

    def save_delete(self, save_id):
        """ I delete a save. """
        try:
            query = f"DELETE FROM sauvegardes WHERE save_id='{save_id}'"
            self.connection.execute(query)
            self.connection.commit()
        except:
            print("L'effacement de la sauvegade n'a pas pu se faire.")

    def _check(self, prod_id):
        """ I Check if a value is in a table, if yes I return its id """
        query = f"SELECT save_id FROM sauvegardes WHERE prod_id LIKE '{prod_id}'"
        self.connection.execute(query)
        result = self.connection.fetchall()

        if len(result) == 0:
            return False
        else:
            return "Vous avez déjà sauvegardé ce substitut."

if __name__ == "__main__":
    save = Save()

    ### Tests of methods ###
    # save.saving('3229820019307')
    # print(save._check('3229820019307'))
    # save.save_listing()
    # save.save_display('1')
    # save.save_delete('1')
