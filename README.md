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



<br>
<br>
### Scrape data buku dari [books.toscrape.com](http://books.toscrape.com)
<br>

#### Deskripsi dan Spesifikasi
_Source code_ ini digunakan untuk mengambil data dari semua buku yang ada di [books.toscrape.com](http://books.toscrape.com).

#### _How to Use_
1. _Download_ atau _clone repository_ dari [sini](https://github.com/abdashaffan/Seleksi-2019-Tugas-1).
2. Masuk ke dalam  _root_ repository ini (**_/Seleksi-2019-Tugas-1_**), lalu jalankan perintah `make` pada terminal anda.

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

`category`: Jenis kategori atau _genre_ buku.
`link`: link untuk melihat detail buku tersebut.
`price_in_euro`: Harga buku dalam euro.
`rating`: Rating buku.
`stock`: Stok buku yang masih tersedia.
`summary`: Pendahuluan dari buku.
`title`: Judul buku.
`upc`: Kode _UPC_ buku.

Data hasil _scrape_ akan disimpan di dalam dua file berbeda pada folder **_data_**, yaitu **_books.json_** dan **_books.normalized.csv_** .

#### _Reference_

1. `BeautifulSoup`: Modul  scraping menggunakan bahasa pemrograman _python_.
2. `w2n`: Modul pembantu untuk merubah string jadi angka.
3. `requests`: Modul untuk penanganan _request_ URL .
5. `pandas.io.json`: Modul pandas untuk normalisasi JSON .

