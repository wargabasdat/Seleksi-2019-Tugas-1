<h1 align="center">
  <br>
    Seleksi 1 Warga Basdat 2019
  <br>
  <br>
</h1>

<h2 align="center">
  <br>
    Kulineran.com Data Scraping
  <br>
  <br>
</h2>

# Description
This is a program to get restaurants informations from https://kulineran.com.

# Specification
```
1. Lakukan _data scraping_ dari sebuah laman web untuk memperoleh data atau informasi tertentu __TANPA MENGGUNAKAN API__

2. Daftarkan judul topik yang akan dijadikan bahan _data scraping_ pada spreadsheet berikut: [Topik Data Scraping](https://docs.google.com/spreadsheets/d/1BokKV8Qky7Hmry0dSRsmlT3LKs6jFWEy-BPt32Oc9-o/edit?usp=sharing). Usahakan agar tidak ada peserta dengan topik yang sama. Akses edit ke spreadsheet akan ditutup tanggal __20 Mei 2019 pukul 20.00 WIB__

3. Dalam mengerjakan tugas, calon warga basdat terlebih dahulu melakukan _fork_ project github pada link berikut: https://github.com/wargabasdat/Seleksi-2019-Tugas-1. Sebelum batas waktu pengumpulan berakhir, calon warga basdat harus sudah melakukan _pull request_ dengan nama ```TUGAS_SELEKSI_1_[NIM]```

4. Pada _repository_ tugas 1, calon warga basdat harus mengumpulkan _file script_, json hasil _data scraping_. _repository_ terdiri dari _folder_ `src`, `data` dan `screenshots`. _Folder_ `src` berisi _file script_/kode yang __*WELL DOCUMENTED* dan *CLEAN CODE*__, _folder_ `data` berisi _file_ json hasil _scraper_ sedangkan  _folder_ `screenshot` berisi tangkapan layar program.

5. Peserta juga diminta untuk membuat `_Makefile` sesuai _template_ yang disediakan, sehingga _program_ dengan gampang di-_build_, di-_run_, dan di-_clean_
   Makefile
   all: clean build run
   clean: # remove data and binary folder
   build: # compile to binary (if you use interpreter, then do not implement it)
   run: # run your binary

6. Deadline pengumpulan tugas 1 adalah __31 Mei 2019 Pukul 23.59__

7. Hasil data scraping ini nantinya akan disimpan dalam DBMS  dan digunakan sebagai bahan tugas analisis dan visualisasi data

8. Sebagai referensi untuk mengenal _data scraping_, asisten menyediakan dokumen "_Short Guidance To Data Scraping_" yang dapat diakses pada link berikut: [Data Scraping Guidance](http://bit.ly/DataScrapingGuidance)

9. Tambahkan juga `.gitignore` pada _file_ atau _folder_ yang tidak perlu di-_upload_, __NB : BINARY TIDAK DIUPLOAD__

10. Mohon memperhatikan __etika__ dalam melakukan _scraping_

11. JSON harus dinormalisasi dan harus di-_preprocessing_
    Preprocessing contohnya :
    - Cleaning
    - Parsing
    - Transformation
    - dan lainnya

12. Berikan `README` yang __WELL DOCUMENTED__ dengan cara __override__ _file_ `README.md` ini. `README` harus memuat minimal konten :
    - Description
    - Specification
    - How to use
    - Ideas and innovations in utilizing the data
    - JSON Structure
    - Screenshot program (di-upload pada folder screenshots, di-upload file image nya, dan ditampilkan di dalam README)
    - Reference (Library used, etc)
    - Author
```

# How to Use
### Windows:
```
1. Open terminal
2. Move to the directory where you save the project (where there are data, screenshot, and src folder)
3. Enter this command -> python src\scrape.py
```
### Linux:
```
1. Open terminal
2. Move to the directory where you save the project (where there are data, screenshot, and src folder)
3. Enter this command -> make
```

# Ideas and innovations in utilizing the data
### The data can be utilized for:
```
1. To compare the price of a menu from one restaurant with another
2. To observe food trends
3. Where to eat references
```

# JSON Structure
### Each tuple of data contains:
```
1. A list of restaurant's category
2. The restaurant's name
3. The restaurant's address
4. A list of restaurant's phone number
5. The restaurant's likes number
6. The restaurant's dislikes number
7. The restaurant's logo link
8. A list of restaurant's menu where each tuple contains:
   a. Menu's id number
   b. Menu's name
   c. Menu's price
   d. Menu's description
9. A list of restaurant's food/drink photos
```

# Screenshot Program
### Source Code:
![screenshot1](https://github.com/vincentbudianto/Seleksi-2019-Tugas-1/blob/master/screenshots/4.png)
![screenshot2](https://github.com/vincentbudianto/Seleksi-2019-Tugas-1/blob/master/screenshots/5.png)
![screenshot3](https://github.com/vincentbudianto/Seleksi-2019-Tugas-1/blob/master/screenshots/6.png)
### JSON Data:
![screenshot4](https://github.com/vincentbudianto/Seleksi-2019-Tugas-1/blob/master/screenshots/9.png)
![screenshot5](https://github.com/vincentbudianto/Seleksi-2019-Tugas-1/blob/master/screenshots/10.png)

# Reference
### The program used the following library:
```
1. bs4             - for data scraping
2. json            - to convert the result into a .json file
3. copy            - to ensure the data doesn't change when converting into a .json file
4. os              - to change the directory from ../src to ../data
5. re              - to remove some unwanted character from the data
6. requests        - to open links from the internet
7. time            - to make delays between each request
```

<p align="center">
  <br>
    <b>
      Vincent Budianto - 13517137
    </b>
  <br>
  <br>
</p>
