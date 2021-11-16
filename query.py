import mysql.connector
from mysql.connector import errorcode

cnx = mysql.connector.connect(user='USERNAME', database='NAME')
cursor = cnx.cursor()

query = ("SELECT brand, post, price FROM posts ")


cursor.execute(query)

for (brand, post, price) in cursor:
    print("{}, {} {}".format(
            brand, post, price))

cursor.close()
cnx.close()
