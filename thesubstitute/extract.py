import requests
import json

from views import Views


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
            "page_size": 40,
            "page": 1,
            "sort_by": "unique_scans_n",
            "fields": "generic_name_fr",
        }

        self.views = Views()

    def extract(self):
        """ I extract product from OpenFoodFacts """
        try:
            request = requests.get(
                url=self.URL, params=self.PARAMS, headers=self.HEADERS
            )
            products = request.json()

            with open("thesubstitute/off_data_extract.json", "w") as f:
                json.dump(products, f)

            self.views.display_text(
                f"""
            REUSSITE de l'Extraction :
            {len(products['products'])} produits ont été téléchargés dans le fichier off_data_extract.json."""
            )

        except:
            print("erreur")


if __name__ == "__main__":
    extract = Extract()

    # extract.extract()
