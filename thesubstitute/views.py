class Views:
    """ """

    def __init__(self):
        pass

    # def list_prod(self, cat_id):
    #     """ I display the list of products. """

    #     for n in range(len(self.requests.product_list(cat_id))):
    #         print(f" {self.requests.product_list(cat_id)[n][2]+1} - {self.requests.product_list(cat_id)[n][1]}")

    def menu_main(self):
        pass

    def header(self):
        print(
            """
            ========================================
            ========================================
            =======                          =======
            =======      THE SUBSTITUTE      =======
            =======                          =======
            ========================================
            ========================================
            """
        )

    def header_front(self):
        print(
            """
            ========================================
            ========================================
            =======                          =======
            =======      THE SUBSTITUTE      =======
            =======       FRONT-OFFICE       =======
            =======                          =======
            ========================================
            ========================================
            """
        )

    def main_choice(self):
        choice = input(
            """
            A : Administrer les données OpenFoodFacts
            B : Front-Office
            Q : Exit

            Votre choix : """
        )

        return choice

    def header_admin(self):
        print(
            """
            ========================================
            ========================================
            =======                          =======
            =======      THE SUBSTITUTE      =======
            =======        BACK-OFFICE       =======
            =======                          =======
            ========================================
            ========================================
            """
        )

    def admin_choice(self):
        menu = input(
            f"""
            0 : Menu principal
            1 : Créer la base de données
            2 : Créer les tables
            3 : Effacer toutes les tables
            4 : Extract
            5 : Transform
            6 : Load
            7 : Extract / Transform / Load
            Q : Exit

            Votre choix : """
        )

        return menu

    def app_choice(self):
        menu = input(
            f"""
            0 : Menu principal
            1 : Chercher un substitut
            Q : Exit

            Votre choix : """
        )

        return menu

    def cat_menu(self, cat_choice):
        menu = input(
            f"""
            0 : Menu principal
            1 : Créer la base de données
            2 : Créer les tables
            3 : Effacer toutes les tables
            4 : Extract
            5 : Transform
            6 : Load
            7 : Extract / Transform / Load
            Q : Exit

            Votre choix : """
        )

        return menu

    def display_text(self, text):
        """ """
        print(f"""              {text}""")

    def display_text_error(self, text, error=""):
        """ """
        print(
            f"""
            {text}
            {error}"""
        )

    def pause(self):
        input(
            """
            Appuyez sur Entrée pour continuer...
            """
        )


if __name__ == "__main__":
    view = Views()

    # view.list_prod("11")
