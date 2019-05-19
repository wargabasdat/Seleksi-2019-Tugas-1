from bs4 import BeautifulSoup
from time import sleep
import requests
import json


page_num = 1
book_list = []
book_num = 0
while page_num <= 50:
    try:
        url = "http://books.toscrape.com/catalogue/page-{}.html".format(page_num)
        source = requests.get(url).text
        soup = BeautifulSoup(source, "lxml")
        books = soup.find_all("article", class_="product_pod")
        for book in books:
            book_dict = {}
            book_title = book.img["alt"]
            rating_classes = book.p["class"]
            book_rating = rating_classes[1]
            book_link = "http://books.toscrape.com/catalogue/"
            book_link += book.find("div", class_="image_container").a["href"]
            book_dict["rating"] = book_rating
            book_dict["title"] = book_title
            book_dict["link"] = book_link
            book_list.append(book_dict)
            book_num += 1
            print("books loaded: {}".format(book_num))
        page_num += 1
        sleep(0.5)
    except Exception as e:
        print(e.__class__.__name__)
        break

for book in book_list:
    # print(json.dumps(book, sort_keys=True, indent=3))
    try:
        url = book["link"]
        source = requests.get(url).text
        soup = BeautifulSoup(source, "lxml")
        breadcrumb = soup.find("ul", class_="breadcrumb")
        breadcrumb_list = breadcrumb.find_all("li")
        book_category = breadcrumb_list[2].a.text
        book["category"] = book_category
        price = soup.find("p", class_="price_color").text
        book_price = float(price[2:])
        book["price"] = book_price
        # int(''.join(filter(str.isdigit, your_string)))
        sleep(3)
    except Exception as e:
        print(e.__class__.__name__)
        break
