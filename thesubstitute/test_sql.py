from connection import Connection

connection = Connection()

def product(id):

    query = ("SELECT prod_id FROM produits WHERE prod_id LIKE '%s'")
    id = (value,)
    connection.execute(query, tuple(id))
    result = connection.fetchall()

    return result

print(product("3068320115160"))