from requests import Requests

class Views:
    """ """

    def __init__(self):
        self.requests = Requests()


    def menu_cat(self):
        """ I display the categories menu. """
        
        for n in range(len(self.requests.cat_popular())):
            print(f" {self.requests.cat_popular()[n][2]+1} - {self.requests.cat_popular()[n][1]}")

    def list_prod(self, cat_id):
        """ I display the list of products. """
        
        for n in range(len(self.requests.product_list(cat_id))):
            print(f" {self.requests.product_list(cat_id)[n][2]+1} - {self.requests.product_list(cat_id)[n][1]}")

    def menu_main(self):
        pass

    def header(self):
        print("""
            ========================================
            ========================================
            =======      THE SUBSTITUTE      =======
            ========================================
            ========================================
            """)

    def main_choice(self):
        choice = input("""
            A : Administrer les données OpenFoodFacts
            Q : Exit

            Votre choix : """)

        return choice


if __name__ == "__main__":
    view = Views()

    view.list_prod("11")