import json

from itertools import chain
from database import Database
from tab_modeles import ModProduits, ModCategories, ModMarques, ModShops

class Loader:

    def __init__(self):
        """ """
        self.prod = ModProduits()
        self.cat = ModCategories()
        self.marq = ModMarques()
        self.shop = ModShops()
        self.database = Database()
        self.mycursor = self.database.connection()
        self.open_json()
        
    def open_json(self):
        with open('off_data_transform.json', encoding='utf-8') as json_file:
            self.my_products = json.load(json_file)

    def load_data(self):
        """ """
        print(list(self.my_products.keys()))

        for prod_key in list(self.my_products.keys()):
            # prod_key = list(self.my_products.keys())[3]
            prod_to_load = self.my_products[prod_key]
            # print(prod_to_load)

            # Produits
            if self.read_produits(prod_key) == False:
                nut_id = self.check_product('nut_id', 'nutriscore', 'nut_type', prod_to_load['nutriscore_grade'][0])          
                add_product = (f"INSERT INTO produits SET prod_id='{prod_key}', prod_nom='{prod_to_load['product_name_fr']}', prod_url='{prod_to_load['url']}', nut_id='{nut_id}'")
            
                self.insert(add_product)
            else:
                print(f"Le produit : {prod_to_load['product_name_fr']}, avec le code : {prod_key}, existe déjà")

            # Insert Categories in Tables : categories & prodcat
            for n in range(len(prod_to_load['categories'])):
                if self.read_categorie(prod_to_load['categories'][n]) == False:                
                    add_categorie = (f"INSERT INTO categories SET cat_nom='{prod_to_load['categories'][n]}'")
                    self.insert(add_categorie)

                cat_id = self.read_categorie(prod_to_load['categories'][n])
                check = self.search_id(f"SELECT * FROM prodcat WHERE cat_id='{cat_id}' AND prod_id='{prod_key}' ")
                if not(check):     
                    add_prodcat = (f"INSERT INTO prodcat SET cat_id='{cat_id}', prod_id='{prod_key}' ")
                    self.insert(add_prodcat)

            # Insert Marques in Tables : marques & prodmarq
            for n in range(len(prod_to_load['brands'])):
                if self.read_marque(prod_to_load['brands'][n]) == False:                
                    add_marque = (f"INSERT INTO marques SET marq_nom='{prod_to_load['brands'][n]}'")
                    self.insert(add_marque)

                marq_id = self.read_marque(prod_to_load['brands'][n])
                check = self.search_id(f"SELECT * FROM prodmarq WHERE marq_id='{marq_id}' AND prod_id='{prod_key}' ")
                if not(check):     
                    add_prodmarq = (f"INSERT INTO prodmarq SET marq_id='{marq_id}', prod_id='{prod_key}' ")
                    self.insert(add_prodmarq)

            # Insert Shops in Tables : shops & prodshop
            for n in range(len(prod_to_load['stores'])):
                if self.read_shop(prod_to_load['stores'][n]) == False:                
                    add_shop = (f"INSERT INTO shops SET shop_nom='{prod_to_load['stores'][n]}'")
                    self.insert(add_shop)

                shop_id = self.read_shop(prod_to_load['stores'][n])
                check = self.search_id(f"SELECT * FROM prodshop WHERE shop_id='{shop_id}' AND prod_id='{prod_key}' ")
                if not(check):     
                    add_prodshop = (f"INSERT INTO prodshop SET shop_id='{shop_id}', prod_id='{prod_key}' ")
                    self.insert(add_prodshop)


    def read_categorie(self, value):
        """ """
        result = self.check_product(self.cat.id_target, self.cat.table_target, self.cat.column_target, value)
        return result

    def read_marque(self, value):
        """ """
        result = self.check_product(self.marq.id_target, self.marq.table_target, self.marq.column_target, value)
        return result

    def read_shop(self, value):
        """ """
        result = self.check_product(self.shop.id_target, self.shop.table_target, self.shop.column_target, value)
        return result

    def read_produits(self, value):
        """ """
        result = self.check_product(self.prod.id_target, self.prod.table_target, self.prod.column_target, value)
        return result

    def check_product(self, id_target, table_target, column_target, product_target):
        """ I Check if a value is in a table, if yes I return its id """
        query = (f"SELECT {id_target} FROM {table_target} WHERE {column_target} LIKE '{product_target}'")
        
        self.mycursor.execute(query)
        result = self.mycursor.fetchall()

        if len(result) < 1:
            return False
        elif len(result) > 1:
            return print("ca va pas")
        else:
            for id in chain.from_iterable(result):
                return id

    def insert(self, query):
        self.mycursor.execute(query)
        self.connection.commit()

    def search_id(self, query):
        self.mycursor.execute(query)
        rows = self.mycursor.fetchall()
        return rows


# ============================================================

if __name__ == "__main__":
    loader = Loader()

# loader.open_json()
print(loader.load_data())


