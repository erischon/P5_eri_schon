from os import system, name
from views import Views

class Main:
    """ """

    def __init__(self):
        """ """
        self.views = Views()

    def clear(self):
        """ I clear the terminal. """  
        if name == 'nt': 
            _ = system('cls')  
        else: 
            _ = system('clear')

    def main_menu(self):
        """ I display the categories menu. """
        self.clear()
        self.views.header()
        self.views.menu_cat()
        self.select_cat()

    def select_cat(self):
        self.selected_cat = input("quelle cat ?")
        # self.selected_cat = '11'
        return self.selected_cat

    def list_of_products(self, cat_id):
        self.views.list_prod(cat_id)

if __name__ == "__main__":
    main = Main()

    main.list_of_products(main.select_cat())