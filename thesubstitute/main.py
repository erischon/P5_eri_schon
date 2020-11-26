import sys
import time

from os import system, name
from views import Views
from extract import Extract
from transform import Transform
from load import Load
from database import Database

class Main:
    """ """

    def __init__(self):
        """ """
        self.views = Views()
        self.db = Database()
        self.extraction = Extract()
        self.transform = Transform()
        self.load = Load()
        # self.state = True

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
        """ """

        self.clear()
        self.views.header_admin()
        option = self.views.admin_choice()

        if option == "0":
            self.main_menu()
        if option == "1":
            self.clear()
            self.views.header_admin()
            self.db.db_create()
            time.sleep(2)
            self.admin_menu()           
        elif option == "2":
            self.clear()
            self.views.header_admin()
            self.db.tables_create()
            time.sleep(2)
            self.admin_menu()
        elif option == "3":
            self.clear()
            self.views.header_admin()
            self.db.tables_delete()
            time.sleep(2)
            self.admin_menu()
        elif option == "4":
            self.clear()
            self.views.header_admin()
            self.extraction.extract()
            time.sleep(2)
            self.admin_menu()
        elif option == "5":
            self.clear()
            self.views.header_admin()
            self.transform.transform_basic()
            time.sleep(2)
            self.admin_menu()
        elif option == "6":
            self.clear()
            self.views.header_admin()
            self.load.load_data()
            time.sleep(2)
            self.admin_menu()
        elif option=="Q" or option=="q":
            sys.exit
        else:
            print("""
            Vous devez taper A ou Q
            Merci de réessayer.""")
            time.sleep(2)
            self.admin_menu()        

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

    # main.main_menu()
    main.admin_menu()

    # main.etl()