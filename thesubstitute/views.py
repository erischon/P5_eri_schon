from requests import Requests

class Views:
    """ """

    def __init__(self):
        self.requests = Requests()


    def menu_cat(self):
        """ I display the categories menu. """
        
        for n in range(len(self.requests.cat_popular())):
            print(f" {self.requests.cat_popular()[n][2]+1} - {self.requests.cat_popular()[n][1]}")

    def menu_main(self):
        pass

    def header(self):
        print(
            " ========================================\n"
            " ========================================\n"
            " =======      THE SUBSTITUTE      =======\n"
            " ========================================\n"
            " ========================================\n"
        )


if __name__ == "__main__":
    view = Views()

    menu.header()