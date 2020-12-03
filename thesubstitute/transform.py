import json

from views import Views


class Transform:
    def __init__(self):
        """ """
        self.fields = (
            "product_name_fr",
            "code",
            "categories",
            "nutriscore_grade",
            "url",
            "brands",
            "stores",
        )
        self.data_clean = {}
        self.views = Views()
        self.open_json()

    def open_json(self):
        """ I open the extract json. """
        with open("off_data_extract.json", encoding="utf-8") as json_file:
            self.data_extract = json.load(json_file)

    def transform_basic(self):
        """ I take the fields I want from the extract json. """
        for n in range(len(self.data_extract["products"])):

            self.data_clean[
                self.data_extract["products"][n][self.fields[1]].lower()
            ] = {}

            for field in self.fields:
                if field != self.fields[1]:
                    self.data_clean[
                        self.data_extract["products"][n][self.fields[1]].lower()
                    ][field] = self.data_extract["products"][n][field].lower()

        self.transform_field(self.data_clean)

    def transform_field(self, data_clean):
        """ I try to clean the data. """
        for code in data_clean:
            # Product
            # data_clean[code]["product_name_fr"] = data_clean[code][
            #     "product_name_fr"
            # ].replace("'", " ")

            # Categories
            list_values = data_clean[code]["categories"].split(",")
            list_values = [value.strip(" ") for value in list_values]
            data_clean[code]["categories"] = list_values

            # for n in range(len(data_clean[code]["categories"])):
            #     data_clean[code]["categories"][n] = data_clean[code]["categories"][
            #         n
            #     ].replace("'", " ")

            # Brands
            list_values = data_clean[code]["brands"].split(",")
            list_values = [value.strip(" ") for value in list_values]
            data_clean[code]["brands"] = list_values

            # Stores
            list_values = data_clean[code]["stores"].split(",")
            list_values = [value.strip(" ") for value in list_values]
            data_clean[code]["stores"] = list_values

        self.create_json(data_clean)

    def create_json(self, data_clean):
        """ I create the transform json. """
        with open("off_data_transform.json", "w") as fp:
            json.dump(data_clean, fp)

        self.views.display_text(
            f"""
            REUSSITE de la Transformation :
            Les produits ont été téléchargés dans le fichier off_data_transform.json."""
        )


if __name__ == "__main__":
    transform = Transform()

    transform.transform_basic()
