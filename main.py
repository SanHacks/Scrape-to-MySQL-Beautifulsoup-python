from bs4 import BeautifulSoup
import requests
import time
import mysql.connector



# REQUEST HTML THROUGH REQUEST.GET
pages = requests.get('https://www.game.co.za/game-za/en/All-Game-Categories/Groceries-%26-Household/Baby/c/G0066?q=%3Arelevance&page=17').text
shop = BeautifulSoup(pages, 'lxml')
items = shop.find_all('div', class_='product-item productListerGridDiv')
# LOOP FOUND PRODUCTS
for products in items:
    brand = products.find('a', class_='brand gtmProductLink').text
    product = products.find('a', class_='name gtmProductLink').text
    price = products.find('span', class_='finalPrice').text
    valid_until = products.find('span', class_='valid-until-text').text
    link = products.find('img')
    photo = link.attrs['src']
    shop = "https://www.game.com"
    source = photo
    remote = shop+source
    store = "Game"

    # Submit Data TO MYSQL DATABASE
    now = time.time()
    pipe = mysql.connector.connect(user='USER', database='NAME')
    cursor = pipe.cursor()

    add_products = ("INSERT INTO posts "
                    "(price, post, brand, shop, image, timestamp) "
                    "VALUES (%s, %s, %s, %s, %s, %s)")
    data_products = (price, product, brand, store, remote, now)
    cursor.execute(add_products, data_products)

    pipe.commit()

    cursor.close()
    pipe.close()
