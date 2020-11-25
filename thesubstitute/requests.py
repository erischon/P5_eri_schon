from database import Database
from itertools import chain


class Requests:
    """ """

    def __init__(self):
        self.database = Database()
        self.mycursor = self.database.connection()

    def cat_popular(self):
        """ I return the list of the 10 most popular categories """
        list_of_tuple = []

        query = f"SELECT cat_id FROM prodcat GROUP BY cat_id ORDER BY COUNT(*) DESC LIMIT 10;"
        result = self.to_list_of_integer(self.query(query))   

        for n in range(len(result)):
            query = (f"SELECT cat_id, cat_nom FROM categories WHERE cat_id = '{result[n]}'")
            cat_popular = self.to_list_of_tuple(list_of_tuple, query, n)

        return cat_popular

    def product_list(self, cat_id):
        """ I return the list of product for un categorie. """
        list_of_tuple = []

        query = f"SELECT prod_id FROM prodcat WHERE cat_id = '{cat_id}';"
        result = self.to_list_of_integer(self.query(query))

        for n in range(len(result)):
            query = (f"SELECT prod_id, prod_nom FROM produits WHERE prod_id = '{result[n]}'")
            prod_list = self.to_list_of_tuple(list_of_tuple, query, n)

        return prod_list

    def product_infos(self, prod_id):
        """ I return all the infos for a product. """

        # Select in produits table.
        query_prod = f"SELECT prod_id, prod_nom, prod_url, nut_id FROM produits WHERE prod_id ='{prod_id}';"
        result = self.query(query_prod)
        prod_id, nom, url, nutriscore = result[0]

        # Select in shops table.
        query_shop = f"SELECT s.shop_nom FROM shops s INNER JOIN prodshop ps ON ps.prod_id = '{prod_id}' AND ps.shop_id = s.shop_id;"
        result = self.query(query_shop)       
        shop_name = [result[n][0] for n in range(len(result))]

        # Select in marques table.
        query_marque = f"SELECT m.marq_nom FROM marques m INNER JOIN prodmarq pm ON pm.prod_id = '{prod_id}' AND pm.marq_id = m.marq_id;"
        result = self.query(query_marque)
        marque_name = [result[n][0] for n in range(len(result))]

        # Select the nutriscore
        query_nutri = f"SELECT nut_type FROM nutriscore WHERE nut_id = '{nutriscore}';"
        result = self.query(query_nutri)
        nut_type = result[0][0]

        prod_infos = {'prod_id':prod_id, 'prod_name': nom, 'prod_url': url, 'prod_nut':nutriscore, 'prod_shop': shop_name, 'prod_marq': marque_name }

        return prod_infos

    def substitute(self, cat_id, prod_nut):
        """ """
        query_sub = f"SELECT p.prod_id, p.prod_nom, p.nut_id FROM produits p INNER JOIN prodcat pc WHERE pc.cat_id ='11' AND p.prod_id = pc.prod_id AND p.nut_id <= '2' ORDER BY p.nut_id, p.prod_nom ASC LIMIT 5;"
        result = self.query(query_sub)

        print(result)

    ########## Methods ########## ########## ########## ##########

    def query(self, query):
        """ """
        self.mycursor.execute(query)
        result = self.mycursor.fetchall()
        return result 

    def to_list_of_integer(self, l_o_t):
        """ Transform a list of tuple (l_o_t) to a list of integer (l_o_i) """
        l_o_i = [[str(x) for x in tup] for tup in l_o_t]
        l_o_i = ["".join(i) for i in l_o_i]
        l_o_i = [int(i) for i in l_o_i]

        return l_o_i
    
    def to_list_of_tuple(self, list_of_tuple, query, n):
        """ Create the list of tuple and add the ranking """ 
        value = self.query(query)      
        value = value[0]
        rank = list(value)
        rank.append(n)
        value = tuple(rank)
        list_of_tuple.append(value)

        return list_of_tuple

if __name__ == "__main__":
    requests = Requests()

    # print(requests.product_list(11))
    # print(requests.cat_popular())
    # print(requests.product_infos('3268840001008'))
    print(requests.substitute('11', '3'))

    # query = f"SELECT p.prod_id, p.prod_nom, p.prod_url, s.shop_nom, m.marq_nom FROM produits p, shops s, marques m INNER JOIN prodcat pc, prodshop ps, prodmarq pm ON pc.cat_id = '11' AND pc.prod_id = p.prod_id AND ps.prod_id = p.prod_id AND pm.prod_id = p.prod_id;"

    # SELECT p.prod_id FROM produits p INNER JOIN prodcat pc WHERE pc.cat_id ='{prod_id}' AND p.prod_id = pc.prod_id AND p.nut_id <= '3'
    # SELECT p.prod_id, p.prod_nom, p.nut_id FROM produits p INNER JOIN prodcat pc WHERE pc.cat_id ='11' AND p.prod_id = pc.prod_id AND p.nut_id <= '2' ORDER BY p.nut_id, p.prod_nom ASC;
    
    
