from bs4 import BeautifulSoup
import requests
import time
import mysql.connector
# THIS IS JUST FOR TESTING PURPOSES ONLY, YOU MAY MODIFY THE CLASSES WHERE IT IS FIT
# REMEMBER TO ALWAYS CHECK WITH THE LATEST SPECIFICATIONS OF THE WEBSITE YOU ARE TRYING TO SCRAPE DATA FROM

# REQUEST HTML THROUGH REQUEST.GET

pages = requests.get('https://www.game.co.za/game-za/en/All-Game-Categories/Groceries-%26-Household/Baby/c/G0066?q=%3Arelevance&page=17').text
shop = BeautifulSoup(pages, 'lxml')
items = shop.find_all('div', class_='productCarouselItem js-product-carousel-item')
# LOOP FOUND PRODUCTS ADD ALL THE RECORDS TO MYSQL DATABASE
for products in items:
    brand = products.find('a', class_='brand gtmProductLink').text
    product = products.find('a', class_='item-name').text
    price = products.find('span', class_='currentPrice  hasSavings').text
    oldproductprice = products.find('span', class_='oldPrice').text
    valid_until = products.find('span', class_='valid-until-text').text
    link = products.find('img')
    photo = link.attrs['src']
    shop = "https://www.picknpay.co.za"
    source = photo
    remote = shop+source
    store = "PicknPay"

    # Submit Data TO MYSQL DATABASE
    now = time.time()
    pipe = mysql.connector.connect(user='DATABASE_USERNAME', database='DATABASE_NAME', password='PASSWORD', host="LOCALHOST")
    cursor = pipe.cursor()

    add_products = ("INSERT INTO posts "
                    "(price, post, brand, shop, image, timestamp) "
                    "VALUES (%s, %s, %s, %s, %s, %s)")
    data_products = (price, product, brand, store, remote, now)
    cursor.execute(add_products, data_products)
    Print("Product successfully added to database.")
    pipe.commit()

    cursor.close()
    pipe.close()
