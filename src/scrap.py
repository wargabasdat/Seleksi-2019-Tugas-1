from bs4 import BeautifulSoup
from time import sleep
import requests


page_num = 1
book_num = 1
book_list = []
while page_num <= 50:
    try:
        url = "http://books.toscrape.com/catalogue/page-{}.html".format(page_num)
        source = requests.get(url).text
        soup = BeautifulSoup(source, "lxml")
        books = soup.find_all("article", class_="product_pod")
        for book in books:
            book_title = book.img["alt"]
            rating_classes = book.p["class"]
            book_rating = rating_classes[1]
            book_link = "http://books.toscrape.com/catalogue/"
            book_link += book.find("div", class_="image_container").a["href"]
            print("{}. {} ,rating = {}".format(book_num, book_title, book_rating))
            print("link: {}".format(book_link))
            book_num += 1

            # book_dict["rating"] = book_rating
            # book_dict["title"] = book_title
            # book_dict["link"] = book_link
        page_num += 1
        sleep(1)
    except Exception as e:
        print("Something went wrong")
        break
