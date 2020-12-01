import datetime
from connection import Connection

class Save:
    """ """

    def __init__(self):
        self.connection = Connection()

    def saving(self, prod_id):
        """ I save the substitut into the sauvegardes table. """
        check = self.check(prod_id)

        if check == False:
            try:
                query = f"INSERT INTO sauvegardes SET save_time='{datetime.datetime.now()}', prod_id='{prod_id}'"
                self.connection.execute(query)
                self.connection.commit()
            except:
                print("La sauvegarde n'a pas pu se faire.")
        else:
            print(check) 

    def sav_listing(self):
        """ """
        query = f"SELECT * FROM sauvegardes"
        self.connection.execute(query)
        result = self.connection.fetchall()

        print(result)

    def sav_display(self):
        """ """
        pass

    def sav_delete(self, save_id):
        """ """
        pass

    def check(self, prod_id):
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
    # print(save.check('3229820019307'))
    save.sav_listing()
