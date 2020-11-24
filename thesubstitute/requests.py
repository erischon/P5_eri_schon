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

        cat_choice = []

        for n in range(len(result)):
            query = f"SELECT cat_id, cat_nom FROM categories WHERE cat_id = '{result[n]}'"
            self.mycursor.execute(query)
            result_name = self.mycursor.fetchall()
            result_name = result_name[0]
            print(result_name)
            cat_choice.append(result_name)

        return cat_choice


if __name__ == "__main__":
    requests = Requests()

print(requests.cat_popular())