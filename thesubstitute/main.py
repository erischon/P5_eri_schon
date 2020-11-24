from os import system, name
from views import Views

class Main:
    """ """

    def __init__(self):
        """ """
        self.views = Views()
        self.clear()



    def clear(self):
        """ I clear the terminal. """ 
  
        # for windows 
        if name == 'nt': 
            _ = system('cls') 
    
        # for mac and linux(here, os.name is 'posix') 
        else: 
            _ = system('clear') 

if __name__ == "__main__":
    main = Main()

main