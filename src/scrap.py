# Modul utama untuk scrapping
from bs4 import BeautifulSoup

# Modul buat convert string jadi angka
from word2number import w2n

# Modul untuk get request ke URL
import requests

# Modul buat ngolah data JSON
import json

# Modul tidur
from time import sleep

page_num = 1
book_list = []
book_num = 0
book_id = 1000

while page_num <= 50:
    try:
        # Ambil semua isi HTML dari books.toscrape.com
        url = "http://books.toscrape.com/catalogue/page-{}.html".format(page_num)
        source = requests.get(url).text
        soup = BeautifulSoup(source, "lxml")

        # Mencari data-data yang dibutuhkan dari container div "product_pod"
        books = soup.find_all("article", class_="product_pod")
        for book in books:
            # Dictionary untuk menyimpan data-data setiap buku
            book_dict = {}
            # Kasih ID Buku
            book_dict["id"] = book_id
            book_id -= 1
            # Ambil Judul buku
            book_title = book.img["alt"]
            book_dict["title"] = book_title
            # Ambil rating buku
            rating_classes = book.p["class"]
            book_rating = rating_classes[1]
            book_dict["rating"] = w2n.word_to_num(book_rating)
            # Ambil link detail buku
            book_link = "http://books.toscrape.com/catalogue/"
            book_link += book.find("div", class_="image_container").a["href"]
            book_dict["link"] = book_link
            # Masukkan dict ke dalam list semua buku pada katalog
            book_list.append(book_dict)
            # Tracker (supaya gak bosen nunggunya)
            book_num += 1
            print("books loaded: {}".format(book_num))

        page_num += 1
        # Supaya gak limit requestnya
        sleep(0.5)

    except Exception as e:
        # print(e.__class__.__name__)
        print(e)
        break

for book in book_list:
    # Loop untuk mengambil detail tambahan dari setiap buku yang sudah diambil linknya
    try:
        # Ambil semua isi HTML dari buku
        url = book["link"]
        source = requests.get(url).text
        soup = BeautifulSoup(source, "lxml")
        # Ambil kategori buku dari ul dengan class breadcrumb
        breadcrumb = soup.find("ul", class_="breadcrumb")
        breadcrumb_list = breadcrumb.find_all("li")
        book_category = breadcrumb_list[2].a.text
        book["category"] = book_category
        # Ambil harga buku
        price = soup.find("p", class_="price_color").text
        book_price_in_euro = float(price[2:])
        book["price_in_euro"] = book_price_in_euro
        # Ambil jumlah stok buku yang tersedia
        instock = soup.select("p.instock.availability")[0].text.strip()
        book_stock = int("".join(filter(str.isdigit, instock)))
        book["stock"] = book_stock
        # Ambil summary dari buku
        summary_el = soup.find("div", id="product_description").findNext("p")
        if summary_el is None:
            summary = "-"
        else:
            summary = summary_el.text.split("...")[0].strip()

        book["summary"] = summary
        # Ambil kode UPC buku
        upc = soup.find("tr").td.text
        book["upc"] = upc

        print(json.dumps(book, sort_keys=True, indent=3))
        # Supaya gak limit requestnya
        sleep(2)

    except Exception as e:
        # print(e.__class__.__name__)
        print(e)
        break


# Menyimpan dict buku ke dalam file "books.json"
filename = "books.json"
with open(filename, "w") as f:
    json.dump(book_list, f, sort_keys=True, indent=4)
