<h1 align="center">
  <br>
  Data Scraping Part PC dari NanoKomputer
  <br>
  <br>
</h1>


## Description
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


## Specification
Program dibuat dalam bahasa pemograman python3, dan dapat dijalankan menggunakan sistem operasi linux. Untuk setiap kali melakukan _request_, program akan melakukan _sleep_ selama 5 detik agar tidak memberatkan server. Program akan mengambil data dari setiap laman part pc berupa id barang, nama barang, deskripsi barang, harga barang, dan link gambar barang yang dituju. Data yang diambil kemudian disimpan dalam suatu list dari _tuple_ data dan kemudian akan diexport ke dalam file dengan format _json_. Setiap komponen part PC akan diexport kedalam file _json_ masing-masing.


## How to Use
Penginstallan library yang diperlukan dengan perintah pada Command Line Interface (CLI) :
```
$ apt-get install python3-requests
$ apt-get install python3-bs4
```

Menjalankan program dengan perintah pada Command Line Interface (CLI) :
```
$ python3 src/Tugas1.py
```

File hasil _data scraping_ scraping akan disimpan dalam direktori ```/data``` dalam bentuk file _json_.


## Ideas and Innovations in Utilizing Data
- Data informasi part PC dari NanoKomputer dapat digunakan sebagai salah satu referensi daftar harga untuk perhitungan bagi orang-orang yang ingin merakit pc atau membeli komoonen untuk mengupgrade PC.
- Data informasi part PC dari NanoKomputer dapat digunakan sebagai salah satu referensi daftar barang komponen pc yang masuk dan dijual secara resmi di Indonesia


## Json Structure
Sampel struktur _json_ yang digunakan dengan orient column dan hasil penulisan file dengan _json_ formatter :
```
[
    {
        "ID": "[AD747KYBJCBOX]",
        "Nama Optical Drive": "AMD - A6-7470K",
        "Deskripsi": "Unlock Multiplier, GPU Type: Radeon R5 SeriesAMD A6-Series, Clock / Turbo: 3.7GHz / 4.0GHz, 1MB Total CacheDual Core, Godavari, 65W, FM2+",
        "Harga": "Rp.795.000,-",
        "Image Link": "http://www.nanokomputer.com/images/products/Processors/Desktop/AMD/Socket FM2+/AMD 1.jpg?osCsid=907bec22473d2d59b938f3a118f60a48"
    },
    {
        "ID": "[AD747KYBJCBOX]",
        "Nama Optical Drive": "AMD - A6-7470K",
        "Deskripsi": "Unlock Multiplier, GPU Type: Radeon R5 SeriesAMD A6-Series, Clock / Turbo: 3.7GHz / 4.0GHz, 1MB Total CacheDual Core, Godavari, 65W, FM2+",
        "Harga": "Rp.795.000,-",
        "Image Link": "http://www.nanokomputer.com/images/products/Processors/Desktop/AMD/Socket FM2+/AMD 1.jpg?osCsid=907bec22473d2d59b938f3a118f60a48"
    },
    {
        "ID": "[AD747KYBJCBOX]",
        "Nama Optical Drive": "AMD - A6-7470K",
        "Deskripsi": "Unlock Multiplier, GPU Type: Radeon R5 SeriesAMD A6-Series, Clock / Turbo: 3.7GHz / 4.0GHz, 1MB Total CacheDual Core, Godavari, 65W, FM2+",
        "Harga": "Rp.795.000,-",
        "Image Link": "http://www.nanokomputer.com/images/products/Processors/Desktop/AMD/Socket FM2+/AMD 1.jpg?osCsid=907bec22473d2d59b938f3a118f60a48"
    }
}
```


## Screenshoot Program
### Source Code
![screenshotCode1](https://github.com/willysantoso05/Seleksi-2019-Tugas-1/blob/master/screenshots/Code1.png)
![screenshotCode2](https://github.com/willysantoso05/Seleksi-2019-Tugas-1/blob/master/screenshots/Code2.png)
![screenshotCode3](https://github.com/willysantoso05/Seleksi-2019-Tugas-1/blob/master/screenshots/Code3.png)
![screenshotCode4](https://github.com/willysantoso05/Seleksi-2019-Tugas-1/blob/master/screenshots/Code3.png)
![screenshotCode5](https://github.com/willysantoso05/Seleksi-2019-Tugas-1/blob/master/screenshots/Code3.png)

### Json Structure (with json formatter)
![screenshotJsonStructure1](https://github.com/willysantoso05/Seleksi-2019-Tugas-1/blob/master/screenshots/Json_Structure.png)


## Reference
Library yang digunakan :
- __beautiful soup__  sebagai tools _data scraping_ untuk bahasa pemrograman python
- __requests__  untuk melakukan _request_ pada suatu web dan mengambil data informasinya  
- __json__  untuk mengelompokan data informasi dan diexport ke dalam file _json_
- __time__  untuk melakukan _delay_ pada setiap melakukan _request_

Website referensi :
- https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- https://medium.com/python-pandemonium/6-things-to-develop-an-efficient-web-scraper-in-python-1dffa688793c
- https://www.w3schools.com/python/python_json.asp
- https://www.youtube.com/channel/UCnVzApLJE2ljPZSeQylSEyg?pbjreload=10


<h2 align="center">
  <br>
  Willy Santoso - 13517066
  <br>
  <br>
</h2>