from connection import Connection

connection = Connection()

# def read_produits(value):

#     query = ("SELECT prod_id FROM produits WHERE prod_id LIKE '%s'")
#     id = (value,)
#     connection.execute(query, id)
#     result = connection.fetchall()

#     return result

# print(read_produits(3068320115160))

def read_nutriscore(value):
    """  I search if the product is already in the table. """
    query = ("SELECT nut_id FROM nutriscore WHERE nut_type LIKE %s")
    print(value)
    connection.execute(query, (value,))
    result = connection.fetchall()
    print(result)
    if len(result) < 1:
        return False
    else:
        return int(result[0][0])

print(read_nutriscore("b"))