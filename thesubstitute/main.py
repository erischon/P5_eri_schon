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
        selected_cat = input("quelle cat ?")
        print(selected_cat)

if __name__ == "__main__":
    main = Main()

    main.main_menu()