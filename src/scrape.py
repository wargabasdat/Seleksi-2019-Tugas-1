"""
Tugas Seleksi 1 Lab Basdat
NIM/Nama: 13517021/Abda Shaffan Diva
Nama File: scrape.py
"""

# Modul utama untuk scraping
from bs4 import BeautifulSoup

# Modul buat convert string jadi angka
from word2number import w2n

# Modul untuk get request ke URL
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# Modul buat ngolah data JSON
import json
from pandas.io.json import json_normalize

import time

import os
from pathlib import Path


def requests_retry_session(
    # Fungsi buat handle request dan error handling-nya
    retries=3,
    backoff_factor=0.3,
    status_forcelist=(500, 502, 504),
    session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session


page_num = 1
book_list = []
json_filename = "books.json"
csv_filename = "books_normalized.csv"
root = Path(__file__).parent.parent
base_data_path = (root / "data/").resolve()
json_path = (base_data_path / json_filename).resolve()

while page_num <= 50:
    t0 = time.time()
    try:
        # Ambil semua isi HTML dari books.toscrape.com
        url = "http://books.toscrape.com/catalogue/page-{}.html".format(page_num)
        response = requests_retry_session().get(url)

    except Exception as e:
        # Gagal request
        print("{} Connection failed: {}".format(url, e.__class__.__name__))

    else:
        print("{} connected. Status: {}".format(url, response.status_code))
        soup = BeautifulSoup(response.text, "lxml")
        # Mencari data-data yang dibutuhkan dari container div "product_pod"
        books = soup.find_all("article", class_="product_pod")
        for book in books:
            # Dictionary untuk menyimpan data-data setiap buku
            book_dict = {}

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

        page_num += 1

    finally:
        # Waktu request
        t1 = time.time()
        print("took {} seconds\n\n".format(t1 - t0))


for book in book_list:
    # Loop untuk mengambil detail tambahan dari setiap buku yang sudah diambil linknya
    t0 = time.time()
    try:
        # Ambil semua isi HTML dari buku
        url = book["link"]
        response = requests_retry_session().get(url)

    except Exception as e:
        # Gagal request
        print("{} Connection failed: {}".format(url, e.__class__.__name__))

    else:
        print("{} connected. Status: {}".format(url, response.status_code))
        soup = BeautifulSoup(response.text, "lxml")

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
        summary_el = soup.find("div", id="product_description")
        if summary_el is None:
            summary = "-"
        else:
            summary_el = summary_el.findNext("p")
            summary = summary_el.text.split("...")[0].strip()
        book["summary"] = summary

        # Ambil kode UPC buku
        upc = soup.find("tr").td.text
        book["upc"] = upc

        # Menyimpan dict buku ke dalam file "books.json"
        if not os.path.exists(base_data_path):
            os.makedirs(base_data_path)
        with open(json_path, "w") as f:
            json.dump(book_list, f, sort_keys=True, indent=4)

    finally:
        # Waktu request
        t1 = time.time()
        print("took {} seconds\n\n".format(t1 - t0))


# Buat data csv dari JSON
csv_path = (base_data_path / csv_filename).resolve()
normalized_data = json_normalize(book_list)
normalized_data.to_csv(csv_path, encoding="utf-8")
print("Data disimpan di ./data/books.json dan ./data/books_normalized.csv")
