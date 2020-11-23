import requests
import json 

class Extract:
    """ Extract data from OpenFoodFacts. """

    def __init__(self):
        self.URL = "https://fr.openfoodfacts.org/cgi/search.pl"
        self.HEADERS = {"User-Agent": "OC-P5 - GNU/Windows - Version 0.1"}
        self.PARAMS = {
            "search_simple": 1,
            "action": "process",
            "json": 1,
            "tagtype_0": "countries",
            "tag_contains_0": "contains",
            "tag_0": "france",
            "page_size": 20, 
            "page": 1,
            "sort_by": "unique_scans_n",
            "fields": "generic_name_fr",
        }

        self.extract()

    def extract(self):
        """ I extract product from OpenFoodFacts """
        request = requests.get(url = self.URL, params = self.PARAMS, headers = self.HEADERS) 
        products = request.json() 

        with open("off_data_extract.json", "w") as f:
            json.dump(products, f)

        print(f"{len(products['products'])} produits ont été téléchargés dans le fichier.")

if __name__ == "__main__":
    extract = Extract()