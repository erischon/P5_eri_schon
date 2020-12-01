import datetime
from connection import Connection

class Save:
    """ """

    def __init__(self):
        self.connection = Connection()

    def saving(self, prod_id):
        """ """
        try:
            query = f"INSERT INTO sauvegardes SET save_time='{datetime.datetime.now()}', prod_id='{prod_id}'"
            print(query)
            self.connection.execute(query)
            self.connection.commit()
        except:
            print("La sauvegarde n'a pas pu se faire.") 

    def sav_listing(self):
        """ """
        pass

    def sav_display(self):
        """ """
        pass

    def sav_delete(self, save_id):
        """ """
        pass

if __name__ == "__main__":
    save = Save()

    ### Tests of methods ###
    save.saving('3229820019307')
