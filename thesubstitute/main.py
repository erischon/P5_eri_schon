import sys
import time

from os import system, name
from views import Views
from extract import Extract
from transform import Transform

class Main:
    """ """

    def __init__(self):
        """ """
        self.views = Views()
        self.state = True

    def main_menu(self):
        self.clear()
        self.views.header()
        choice = self.views.main_choice()

        if choice == "A" or choice == "a":
            self.admin_menu()
        elif choice=="Q" or choice=="q":
            sys.exit
        else:
            print("""
            Vous devez taper A ou Q
            Merci de réessayer.""")
            time.sleep(2)
            self.main_menu()

    def admin_menu(self):
        self.clear()
        self.views.header_admin()
        choice = self.views.admin_choice()

        if choice == "A" or choice == "a":
            self.etl()
        elif choice=="Q" or choice=="q":
            sys.exit
        else:
            print("""
            Vous devez taper A ou Q
            Merci de réessayer.""")
            time.sleep(2)
            self.admin_db()        

    def etl(self):
        self.clear()
        self.views.header_admin()
        extract = Extract()
        time.sleep(2)
        transform = Transform()
        self.admin_menu()



    def clear(self):
        """ I clear the terminal. """  
        if name == 'nt': 
            _ = system('cls')  
        else: 
            _ = system('clear')


    # def main_menu(self):
    #     """ I display the categories menu. """
    #     self.clear()
    #     self.views.header()
    #     self.views.menu_cat()
    #     self.select_cat()

    # def select_cat(self):
    #     self.selected_cat = input("quelle cat ?")
    #     # self.selected_cat = '11'
    #     return self.selected_cat

    # def list_of_products(self, cat_id):
    #     self.views.list_prod(cat_id)

if __name__ == "__main__":
    main = Main()

    main.main_menu()

    # main.etl()