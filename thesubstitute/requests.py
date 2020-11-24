from database import Database
from itertools import chain


class Requests:
    """ """

    def __init__(self):
        self.database = Database()
        self.mycursor = self.database.connection()

    def cat_popular(self):
        """ I return the list of the 10 most popular categories """
        # Search the most popular categories (categories with the most products)
        query = f"SELECT cat_id FROM prodcat GROUP BY cat_id ORDER BY COUNT(*) DESC LIMIT 10;"

        self.mycursor.execute(query)
        result = self.to_list_of_integer(self.mycursor.fetchall())

        cat_popular = []

        # Create the list of tuple and add the ranking
        for n in range(len(result)):
            query = (
                f"SELECT cat_id, cat_nom FROM categories WHERE cat_id = '{result[n]}'"
            )
            self.mycursor.execute(query)
            categorie = self.mycursor.fetchall()
            categorie = categorie[0]
            # add ranking
            rank = list(categorie)
            rank.append(n)
            categorie = tuple(rank)
            cat_popular.append(categorie)

        return cat_popular

    def product_list(self, cat):
        """ """
        # query = f"SELECT p.prod_id, p.prod_nom FROM produits p INNER JOIN prodcat pc ON pc.prod_id = p.prod_id;"
        query = f"SELECT prod_id FROM prodcat WHERE cat_id = '{cat}';"

        self.mycursor.execute(query)
        result = self.mycursor.fetchall()

        result = [[str(x) for x in tup] for tup in result]
        result = ["".join(i) for i in result]
        result = [int(i) for i in result]

        prod_list = []

        for n in range(len(result)):
            query = (f"SELECT prod_id, prod_nom FROM produits WHERE prod_id = '{result[n]}'")
            self.mycursor.execute(query)
            product = self.mycursor.fetchall()
            product = product[0]
            # add a ranking
            rank = list(product)
            rank.append(n)
            product = tuple(rank)
            prod_list.append(product)

        return prod_list

    def to_list_of_integer(self, l_o_t):
        """ Transform a list of tuple (l_o_t) to a list of integer (l_o_i) """

        l_o_i = [[str(x) for x in tup] for tup in l_o_t]
        l_o_i = ["".join(i) for i in l_o_i]
        l_o_i = [int(i) for i in l_o_i]

        return l_o_i


if __name__ == "__main__":
    requests = Requests()

    # print(requests.product_list(11))
    print(requests.cat_popular())
