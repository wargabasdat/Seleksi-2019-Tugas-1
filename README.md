<h1 align="center">
  <br>
  _Data Scraping_ Part PC dari NanoKomputer
  <br>
  <br>
</h1>


##Description
Script ini melakukan _data scraping_ pada laman http://www.nanokomputer.com/. NanoKomputer merupakan salah satu toko komputer terbesar dan terlengkap yang berada di wilayah Jakarta dengan tingkat kredibilitas yang tinggi. Beberapa komponen utama dalam perakitan PC yang akan dilakukan _data scraping_, yaitu :
- Processor
- Motherboard
- Memory
- Graphic Cards
- Storage
- Power Supply
- CPU Cooling
- Optical Drive
- Cases

Untuk setiap komponen akan didapatkan data informasi dari katalog NanoKomputer berupa :
- ID
- Nama
- Deskripsi
- Harga
- Link Gambar


##Specification
Program dibuat dalam bahasa pemograman python3, dan dapat dijalankan menggunakan sistem operasi linux. Untuk setiap kali melakukan _request_, program akan melakukan _sleep_ selama 5 detik agar tidak memberatkan server. Program akan mengambil data dari setiap laman part pc berupa id barang, nama barang, deskripsi barang, harga barang, dan link gambar barang yang dituju. Data yang diambil kemudian disimpan dalam suatu _dataframe_ dan kemudian akan diexport ke dalam file dengan format _json_. Setiap komponen part PC akan diexport kedalam file _json_ masing-masing.


##How to Use
Penginstallan library yang diperlukan dengan perintah pada Command Line Interface (CLI) :
'''
$ apt-get install python3-requests
$ apt-get install python3-bs4
$ apt-get install pandas
'''

Menjalankan program dengan perintah pada Command Line Interface (CLI) :
'''
$ python3 src/Tugas1.py
'''

File hasil _data scraping_ scraping akan disimpan dalam direktori '''/data''' dalam bentuk file _json_.


##Ideas and Innovations in utilizing data
- Data informasi part PC dari NanoKomputer dapat digunakan sebagai salah satu referensi daftar harga untuk perhitungan bagi orang-orang yang ingin merakit pc atau membeli komoonen untuk mengupgrade PC.
- Data informasi part PC dari NanoKomputer dapat digunakan sebagai salah satu referensi daftar barang komponen pc yang masuk dan dijual secara resmi di Indonesia


##Json Structure
Sampel struktur _json_ yang digunakan dengan orient column dan hasil penulisan file dengan _json_ formatter :
'''
{
    "ID": {
        "0": "[BW-16D1HT]",
        "1": "[BC-12D2HT]",
        "2": "[DRW-24D5MT]"
    },
    "Nama OpticalDrive": {
        "0": "Asus - BW-16D1HT with BLURAY MDISC support",
        "1": "Asus - BC-12D2HT with BLURAY MDISC support",
        "2": "Asus - DRW-24D5MT OEM with BLURAY MDISC support"
    },
    "Deskripsi": {
        "0": "Blu-ray Writer, Internal, SATA, Box",
        "1": "Blu-ray Combo, Internal, SATA, Box",
        "2": "DVD\u00b1RW 24X, Internal, SATA, OEM"
    },
    "Harga": {
        "0": "Rp.1.365.000,-",
        "1": "Rp.1.015.000,-",
        "2": "Rp.195.000,-"
    },
    "Image Link": {
        "0": "http:\/\/www.nanokomputer.com\/images\/products\/Optical Drives\/Blu-Ray Burners\/Asus - BW-16D1HT.jpg?osCsid=9553cf7f8d84e274c002bfb81aac8bc3",
        "1": "http:\/\/www.nanokomputer.com\/images\/products\/Optical Drives\/Blu-Ray Drives\/Asus - BW-16D1HT.jpg?osCsid=90f47c46c9933ca8757d5523f1e70958",
        "2": "http:\/\/www.nanokomputer.com\/images\/products\/Optical Drives\/CD\/DVD Burners\/Asus_DRW-24D5MT.jpg?osCsid=bce61022878e1b47801089b3cdd06b5a"
    }
}
'''


##Screenshoot Program
###Source Code
![screenshot1](https://github.com/willysantoso05/Seleksi-2019-Tugas-1/blob/master/screenshots/Code1.png)
![screenshot2](https://github.com/willysantoso05/Seleksi-2019-Tugas-1/blob/master/screenshots/Code2.png)
![screenshot3](https://github.com/willysantoso05/Seleksi-2019-Tugas-1/blob/master/screenshots/Code3.png)

###Json Structure (with json formatter)
![screenshot4](https://github.com/willysantoso05/Seleksi-2019-Tugas-1/blob/master/screenshots/Json Structure.png)


##Reference
Library yang digunakan :
- __beautiful soup__  sebagai tools _data scraping_ untuk bahasa pemrograman python
- __requests__  untuk melakukan _request_ pada suatu web dan mengambil data informasinya  
- __pandas__  untuk mengelompokan data informasi menjadi suatu _dataframe_ dan diexport ke dalam file _json_
- __time__  untuk melakukan _delay_ pada setiap melakukan _request_

Website referensi :
- https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- https://medium.com/python-pandemonium/6-things-to-develop-an-efficient-web-scraper-in-python-1dffa688793c
- https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html
- https://www.youtube.com/channel/UCnVzApLJE2ljPZSeQylSEyg?pbjreload=10


<h2 align="center">
  <br>
  Willy Santoso - 13517066
  <br>
  <br>
</h2>