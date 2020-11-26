# from model import Model

class Views:
    """ """

    def __init__(self):
        pass
        # self.requests = Model()

    # def menu_cat(self):
    #     """ I display the categories menu. """
        
    #     for n in range(len(self.requests.cat_popular())):
    #         print(f" {self.requests.cat_popular()[n][2]+1} - {self.requests.cat_popular()[n][1]}")

    # def list_prod(self, cat_id):
    #     """ I display the list of products. """
        
    #     for n in range(len(self.requests.product_list(cat_id))):
    #         print(f" {self.requests.product_list(cat_id)[n][2]+1} - {self.requests.product_list(cat_id)[n][1]}")

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

    def header_admin(self):
        print("""
            ========================================
            ========================================
            =======                          =======
            =======      THE SUBSTITUTE      =======
            =======         DB ADMIN         =======
            =======                          =======
            ========================================
            ========================================
            """)

    def admin_choice(self):
        menu = input(f"""
            0 : Menu principal
            1 : Créer la base de données
            2 : Créer les tables
            3 : Effacer toutes les tables
            4 : Extract
            5 : Transform
            6 : Load
            7 : Extract / Transform / Load
            Q : Exit

            Votre choix : """)

        return menu

    # def extract(self, n):
    #     print(f"""
    #         C'EST UN SUCCES !\n
    #         {n} produits ont été téléchargés dans le fichier off_data_extract.json.\n"""
    #     )

    ######

    def display_text(self, text):
        
        print(f"""              {text}""")

    def display_text_error(self, text, error=''):
        
        print(f"""
            {text}
            {error}
            """)

    def pause(self):
        input("""
            Appuyez sur Entrée pour continuer...
            """)

    ######

if __name__ == "__main__":
    view = Views()

    # view.list_prod("11")