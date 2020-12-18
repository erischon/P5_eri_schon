import sys
import time
from os import system, name

from views import Views
from extract import Extract
from transform import Transform
from load import Load
from database import Database
from model import Model
from save import Save


class Main:
    """ """

    def __init__(self):
        """ """
        self.views = Views()
        self.db = Database()
        self.model = Model()
        self.save = Save()

    def main_menu(self):
        """ I display the main menu. """
        self.clear()
        self.views.header()
        choice = self.views.main_choice().lower()

        if choice == "b":
            self.back_menu()
        elif choice == "f":
            self.front_menu()
        elif choice == "q":
            sys.exit
        else:
            self.views.display_text("""
            Vous devez taper B, F ou Q
            Merci de réessayer.""")
            time.sleep(2)
            self.main_menu()

    def back_menu(self):
        """ I display the back-office menu. """
        self.clear()
        self.views.header_admin()
        option = self.views.admin_choice()

        if option == "0":
            self.main_menu()
        elif option == "1":
            self.clear()
            self.views.header_admin()
            self.db.db_create()
            self.views.pause()
            self.back_menu()
        elif option == "2":
            self.clear()
            self.views.header_admin()
            self.db.tables_create()
            self.views.pause()
            self.back_menu()
        elif option == "3":
            self.clear()
            self.views.header_admin()
            self.db.tables_delete()
            self.views.pause()
            self.back_menu()
        elif option == "4":
            self.clear()
            self.views.header_admin()
            extraction = Extract()
            extraction.extract()
            self.views.pause()
            self.back_menu()
        elif option == "5":
            self.clear()
            self.views.header_admin()
            transform = Transform()
            transform.transform_basic()
            self.views.pause()
            self.back_menu()
        elif option == "6":
            self.clear()
            self.views.header_admin()
            load = Load()
            load.load_data()
            self.views.pause()
            self.back_menu()
        elif option == "7":
            self.clear()
            self.views.header_admin()
            extraction = Extract()
            transform = Transform()
            load = Load()
            extraction.extract()
            transform.transform_basic()
            load.load_data()
            self.views.pause()
            self.back_menu()
        elif option == "Q" or option == "q":
            sys.exit
        else:
            print(
                """
            Vous devez taper A ou Q
            Merci de réessayer."""
            )
            time.sleep(2)
            self.back_menu()

    def front_menu(self):
        """ I display the front-office menu. """
        self.clear()
        self.views.header_front()
        option = self.views.app_choice()

        if option == "0":
            self.main_menu()
        elif option == "1":
            cat = self.fos_s1()
            cat_id, prod = self.fos_s2(cat)
            prod_id = self.fos_s3(cat_id, prod)
            self.fos_s4(prod_id)
        elif option == "2":
            self.clear()
            self.views.header_front()
            save_id = self.save.save_listing()
            if save_id == "0":
                self.front_menu()
            self.clear()
            self.views.header_front()
            self.save.save_display(save_id)
            if self.save.option_delete() is True:
                self.save.save_delete(save_id)
            self.views.pause()
            self.front_menu()

        elif option == "Q" or option == "q":
            sys.exit
        else:
            print(
                """
            Vous devez taper A ou Q
            Merci de réessayer."""
            )
            time.sleep(2)
            self.front_menu()

    def clear(self):
        """ I clear the terminal. """
        if name == "nt":
            _ = system("cls")
        else:
            _ = system("clear")

    def fos_s1(self):
        """ Front-Office Substitute step 1 : categorie choice. """
        self.clear()
        self.views.header_front()
        cat = self.model.cat_options(self.model.cat_popular())
        return cat

    def fos_s2(self, cat):
        """ Front-Office Substitute step 2 : product to substitute choice. """
        self.clear()
        self.views.header_front()
        prod_list, cat_id = self.model.product_list(cat)
        cat_id, prod = self.model.prod_options(prod_list, cat_id)
        return cat_id, prod

    def fos_s3(self, cat_id, prod):
        """ Front-Office Substitute step 3 : substitute choice. """
        self.clear()
        self.views.header_front()
        sub_list = self.model.sub_list(cat_id, prod)
        prod_id = self.model.sub_options(sub_list)
        if prod_id is None:
            self.front_menu()
        return prod_id

    def fos_s4(self, prod_id):
        """ Front-Office Substitute step 4 : product infos. """
        self.clear()
        self.views.header_front()
        prod_infos = self.model.product_infos(prod_id)
        self.model.sub_prod_infos(prod_infos)
        if self.save.option_save() is True:
            if self.save.saving(prod_id) is not False:
                self.views.display_text("Ce substitut a été sauvegardé.")
        self.views.pause()
        self.front_menu()       


if __name__ == "__main__":
    main = Main()
    main.main_menu()

    # === Tests of methods ===
    # main.main_menu()
    # main.admin_menu()
    # main.front_menu()
