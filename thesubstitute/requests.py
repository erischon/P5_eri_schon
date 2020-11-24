from database import Database
from itertools import chain


class Requests:
    """ """

    def __init__(self):
        self.database = Database()
        self.mycursor = self.database.connection()

    def cat_popular(self):
        """ """
        # requete dans la base pour savoir quels sont les catégories les plus utilisées
        # retourner une liste

        query = f"SELECT cat_id FROM prodcat GROUP BY cat_id ORDER BY COUNT(*) DESC LIMIT 10;"

        self.mycursor.execute(query)
        result = self.mycursor.fetchall()

        result = [[str(x) for x in tup] for tup in result]
        result = [''.join(i) for i in result]
        result = [int(i) for i in result]

        cat_popular = []

        for n in range(len(result)):
            query = f"SELECT cat_id, cat_nom FROM categories WHERE cat_id = '{result[n]}'"
            self.mycursor.execute(query)
            categorie = self.mycursor.fetchall()
            categorie = categorie[0]
            x = list(categorie)
            x.append(n)
            categorie = tuple(x)
            cat_popular.append(categorie)

        return cat_popular


if __name__ == "__main__":
    requests = Requests()

print(requests.cat_popular())