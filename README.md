<h1 align="center">
  <br>
  Seleksi 1 Warga Basdat 2019
</h1>

<h2 align="center">
  Data Scraping
</h2>

<h5 align="center">
  <em>Oleh: Abda Shaffan Diva 13517021</em>
</h5>



### Scrape data buku dari [books.toscrape.com](http://books.toscrape.com)


#### Deskripsi dan Spesifikasi
_Source code_ ini digunakan untuk mengambil data dari semua buku yang ada di [books.toscrape.com](http://books.toscrape.com), dan dijalankan menggunakan `python3`.

#### _How to Use_
1. _Download_ atau _clone repository_ dari [sini](https://github.com/abdashaffan/Seleksi-2019-Tugas-1).
2. Masuk ke dalam  _root_ repository ini (**_/Seleksi-2019-Tugas-1_**). 
3. Install _dependencies_ dengan perintah `pip install -r requirements.txt` 
4. Jalankan perintah `make` pada terminal anda.

#### _Using the data_

Data dapat digunakan sebagai referensi untuk membeli suatu buku, atau mencari buku berdasarkan _genre_-nya. (Data lain seperti harga dan jumlah stok tidak dapat dijadikan referensi karena data pada website hanya berupa _dummy data_ saja).

#### _JSON Structure_
Contoh _instance_ data JSON: 
```
 {
        "category": "Poetry",
        "link": "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
        "price_in_euro": 51.77,
        "rating": 3,
        "stock": 22,
        "summary": "It's hard to imagine a world without A Light in the Attic. This now-classic collection of poetry...",
        "title": "A Light in the Attic",
        "upc": "a897fe39b1053632"
    },
```
<br>

`category`: Jenis kategori atau _genre_ buku.<br>
`link`: link untuk melihat detail buku tersebut.<br>
`price_in_euro`: Harga buku dalam euro.<br>
`rating`: Rating buku.<br>
`stock`: Stok buku yang masih tersedia.<br>
`summary`: Pendahuluan dari buku.<br>
`title`: Judul buku.<br>
`upc`: Kode _UPC_ buku.<br>

Data hasil _scrape_ akan disimpan di dalam dua file berbeda pada folder **_data_**, yaitu **_books.json_** dan **_books.normalized.csv_** .

#### _Reference_

1. `BeautifulSoup`: Modul  scraping menggunakan bahasa pemrograman _python_.
2. `w2n`: Modul pembantu untuk merubah string jadi angka.
3. `requests`: Modul untuk penanganan _request_ URL .
5. `pandas.io.json`: Modul pandas untuk normalisasi JSON .

#### _Screenshots_

![SC1](https://github.com/abdashaffan/Seleksi-2019-Tugas-1/blob/master/screenshots/Screenshot_20190529_145619.png)
![SC2](https://github.com/abdashaffan/Seleksi-2019-Tugas-1/blob/master/screenshots/Screenshot_20190529_145647.png)
![SC3](https://github.com/abdashaffan/Seleksi-2019-Tugas-1/blob/master/screenshots/Screenshot_20190529_145700.png)
![SC4](https://github.com/abdashaffan/Seleksi-2019-Tugas-1/blob/master/screenshots/Screenshot_20190529_145713.png)
![SC5](https://github.com/abdashaffan/Seleksi-2019-Tugas-1/blob/master/screenshots/Screenshot_20190529_145721.png)
![SC6](https://github.com/abdashaffan/Seleksi-2019-Tugas-1/blob/master/screenshots/Screenshot_20190529_145730.png)

