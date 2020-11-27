import sys
import time

from os import system, name
from views import Views
from extract import Extract
from transform import Transform
from load import Load
from database import Database
from model import Model


class Main:
    """ """

    def __init__(self):
        """ """
        self.views = Views()
        self.db = Database()
        self.extraction = Extract()
        self.transform = Transform()
        self.load = Load()
        self.model = Model()

    def main_menu(self):
        self.clear()
        self.views.header()
        choice = self.views.main_choice()

        if choice == "A" or choice == "a":
            self.admin_menu()
        elif choice == "Q" or choice == "q":
            sys.exit
        else:
            print(
                """
            Vous devez taper A ou Q
            Merci de réessayer."""
            )
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
            self.views.pause()
            self.admin_menu()
        elif option == "2":
            self.clear()
            self.views.header_admin()
            self.db.tables_create()
            self.views.pause()
            self.admin_menu()
        elif option == "3":
            self.clear()
            self.views.header_admin()
            self.db.tables_delete()
            self.views.pause()
            self.admin_menu()
        elif option == "4":
            self.clear()
            self.views.header_admin()
            self.extraction.extract()
            self.views.pause()
            self.admin_menu()
        elif option == "5":
            self.clear()
            self.views.header_admin()
            self.transform.transform_basic()
            self.views.pause()
            self.admin_menu()
        elif option == "6":
            self.clear()
            self.views.header_admin()
            self.load.load_data()
            self.views.pause()
            self.admin_menu()
        elif option == "7":
            self.clear()
            self.views.header_admin()
            self.extraction.extract()
            self.transform.transform_basic()
            self.load.load_data()
            self.views.pause()
            self.admin_menu()
        elif option == "Q" or option == "q":
            sys.exit
        else:
            print(
                """
            Vous devez taper A ou Q
            Merci de réessayer."""
            )
            time.sleep(2)
            self.admin_menu()



    def app_menu(self):
        """ I display the categories menu. """
        self.clear()
        self.views.header()
        option = self.views.app_choice()

        if option == "0":
            self.main_menu()
        if option == "1":
            self.clear()
            self.views.header_admin()
            self.model.cat_options()

        else:
            print(
                """
            Vous devez taper A ou Q
            Merci de réessayer."""
            )
            time.sleep(2)
            self.app_menu()

    def clear(self):
        """ I clear the terminal. """
        if name == "nt":
            _ = system("cls")
        else:
            _ = system("clear")


    # def select_cat(self):
    #     self.selected_cat = input("quelle cat ?")
    #     # self.selected_cat = '11'
    #     return self.selected_cat

    # def list_of_products(self, cat_id):
    #     self.views.list_prod(cat_id)


if __name__ == "__main__":
    main = Main()

    # main.main_menu()
    # main.admin_menu()
    main.app_menu()

    # main.etl()
