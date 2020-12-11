import json
from itertools import chain

from .connection import Connection
from .views import Views


class Load:
    def __init__(self):
        """ """
        self.views = Views()
        self.connection = Connection()
        self.open_json()

    def open_json(self):
        """ I open the json. """
        with open(
            "thesubstitute/off_data_transform.json", encoding="utf-8"
        ) as json_file:
            self.my_products = json.load(json_file)

    def load_nutriscore(self):
        """ I load the nutriscore and their id into the table. """
        try:
            query = "INSERT INTO nutriscore (nut_id, nut_type) VALUES (1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'E')"
            self.connection.execute(query)
            self.connection.commit()

            self.views.display_text(
                """
            REUSSITE :
            Les différents Nutriscore ont été chargés dans la base."""
            )

        except:
            self.views.display_text_error("REUSSITE : Les Nutriscore étaient dans la base.")

    def load_data(self):
        """ I load all the data from transform.json to their table. """
        # Loading the nutriscore
        self.load_nutriscore()

        for prod_key in list(self.my_products.keys()):
            prod_to_load = self.my_products[prod_key]

            # Insert Products
            if self.read_produits(prod_key) is False:
                nut_id = self.read_nutriscore(prod_to_load["nutriscore_grade"][0])
                add_product = ("INSERT INTO produits SET prod_id=%s, prod_nom=%s, prod_url=%s, nut_id=%s")
                data_product = (prod_key, prod_to_load['product_name_fr'], prod_to_load['url'], nut_id)
                self.connection.execute(add_product, data_product)
                self.connection.commit()
            else:
                pass

            # Insert Categories
            for n in range(len(prod_to_load["categories"])):
                # In categories table
                if self.read_categorie(prod_to_load["categories"][n]) is False:
                    add_categorie = ("INSERT INTO categories SET cat_nom=%s")
                    self.connection.execute(add_categorie, (prod_to_load['categories'][n],))
                    self.connection.commit()
                # In prodcat table
                cat_id = self.read_categorie(prod_to_load["categories"][n])
                check = self.search_id(
                    f"SELECT * FROM prodcat WHERE cat_id='{cat_id}' AND prod_id='{prod_key}' "
                )
                if not (check):
                    add_prodcat = ("INSERT INTO prodcat SET cat_id=%s, prod_id=%s")
                    self.connection.execute(add_prodcat, (cat_id, prod_key))
                    self.connection.commit()

            # Insert Marques
            for n in range(len(prod_to_load["brands"])):
                # In marques table
                if self.read_marque(prod_to_load["brands"][n]) is False:
                    add_marque = ("INSERT INTO marques SET marq_nom=%s")
                    self.connection.execute(add_marque, (prod_to_load['brands'][n],))
                    self.connection.commit()
                # In prodmarq table
                marq_id = self.read_marque(prod_to_load["brands"][n])
                check = self.search_id(
                    f"SELECT * FROM prodmarq WHERE marq_id='{marq_id}' AND prod_id='{prod_key}' "
                )
                if not (check):
                    add_prodmarq = ("INSERT INTO prodmarq SET marq_id=%s, prod_id=%s")
                    self.connection.execute(add_prodmarq, (marq_id, prod_key))
                    self.connection.commit()

            # Insert Shops
            for n in range(len(prod_to_load["stores"])):
                # In shops table
                if self.read_shop(prod_to_load["stores"][n]) is False:
                    add_shop = ("INSERT INTO shops SET shop_nom=%s")
                    self.connection.execute(add_shop, (prod_to_load['stores'][n],))
                    self.connection.commit()
                # In prodshop table
                shop_id = self.read_shop(prod_to_load["stores"][n])
                check = self.search_id(
                    f"SELECT * FROM prodshop WHERE shop_id='{shop_id}' AND prod_id='{prod_key}' "
                )
                if not (check):
                    add_prodshop = ("INSERT INTO prodshop SET shop_id=%s, prod_id=%s")
                    self.connection.execute(add_prodshop, (shop_id, prod_key))
                    self.connection.commit()

        self.views.display_text(
            f"""
            REUSSITE du chargement des produits :
            {len(self.my_products.keys())} produits sont entrés en base."""
        )

    def read_categorie(self, value):
        """ I search if the category is already in the table. """
        query = ("SELECT cat_id FROM categories WHERE cat_nom LIKE %s")
        self.connection.execute(query, (value,))
        result = self.connection.fetchall()
        if len(result) < 1:
            return False
        else:
            return int(result[0][0])

    def read_marque(self, value):
        """  I search if the brand is already in the table.  """
        query = ("SELECT marq_id FROM marques WHERE marq_nom LIKE %s")
        self.connection.execute(query, (value,))
        result = self.connection.fetchall()
        if len(result) < 1:
            return False
        else:
            return int(result[0][0])

    def read_shop(self, value):
        """  I search if the shop is already in the table. """
        query = ("SELECT shop_id FROM shops WHERE shop_nom LIKE %s")
        self.connection.execute(query, (value,))
        result = self.connection.fetchall()
        if len(result) < 1:
            return False
        else:
            return int(result[0][0])

    def read_produits(self, value):
        """  I search if the product is already in the table. """
        query = ("SELECT prod_id FROM produits WHERE prod_id LIKE '%s'")
        self.connection.execute(query, (int(value),))
        result = self.connection.fetchall()
        if len(result) < 1:
            return False
        else:
            return int(result[0][0])
    
    def read_nutriscore(self, value):
        """  I search if the nutriscore is already in the table. """
        query = ("SELECT nut_id FROM nutriscore WHERE nut_type LIKE %s")
        self.connection.execute(query, (value,))
        result = self.connection.fetchall()
        if len(result) < 1:
            return False
        else:
            return int(result[0][0])

    def search_id(self, query):
        """ I search an ID. """
        self.connection.execute(query)
        rows = self.connection.fetchall()
        return rows

if __name__ == "__main__":
    loader = Load()

    # === Tests of methods ===
    # loader.open_json()
    # loader.load_nutriscore()
    # loader.load_data()
