from setup import Setup

class Menu:
    """ """

    def __init__(self):
        self.setup = Setup()


    def menu_cat(self):
        """ """
        
        for n in range(len(self.setup.cat_choice())):
            print(f"{n+1} - {self.setup.cat_choice()[n][1]}")

if __name__ == "__main__":
    menu = Menu()

menu.menu_cat()