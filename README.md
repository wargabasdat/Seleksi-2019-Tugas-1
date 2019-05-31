# Description
Untuk memenuhi ketentuan tugas seleksi pertama warga basdat 2019, saya membuat beberapa proyek yaitu:
1. GR_TopBooks_Spider (PROJECT UTAMA)
2. GR_Trivia_Spider (PROJECT SAMPINGAN untuk fun & exploration ^^ )

# 1 GR_TopBooks_Spider
Ini adalah program spider yang akan scraping data buku-buku secara lengkap dari www.goodreads.com. Andai kata anda masih belum familiar dengan nama tersebut, Goodreads adalah salah satu website terbesar dan paling digemari (termasuk saya) bagi para pembaca buku di seluruh dunia untuk eksplorasi buku baru, mencari data lengkap mengenai sebuah buku, melihat resensi buku dari reviewer yang professional tingkat dunia, platform untuk diskusi buku, penyedia komunitas untuk pembaca (dalam bentuk forum), quiz & trivia mengenai dunia literatur, dan lain-lain. Website goodreads adalah bagaikan pulau berharta karun bagi para data scraper dilihat dari data disana yang berlimpah-limpah.

Program ini dibuat dengan menggunakan framework scrapy yang menganut library Twisted yang bersifat asynchronous. Spider scrapy diimplementasikan bersamaan dengan library beautifulsoup. Sebenarnya scrapy saja sudah cukup, namun saya ingin eksplorasi kedua library tersebut. Alhasil, scrapy digunakan untuk mengirim request, baik GET(mengambil HTML data dari page) dan POST(untuk login), dan beautifulsoup digunakan untuk extract dan parse HTML content hasil dari request.

Hal yang akan dilakukan program adalah:
1. Melakukan sign-in ke Goodreads dengan credentials account yang diberikan (atau jika tidak, akan otomatis digunakan default dummy account). HAL INI PENTING, karena apparently, website Goodreads ada bug (intentional?) yang menyebabkan kita tidak bisa melihat top books dari genre apapun pada page selain page pertama. (Goodreads, I love you, but this kind of nonsense really makes me wanna pull my hair out...)

2. Program akan mengirim request ke "https://www.goodreads.com/shelf/show/<genre>" untuk mendapatkan html content dari top books dalam genre yang dispesifikasi user. Genre akan diberikan melalui command line arguments.

3. Dari page tersebut, program akan melacak hyperlink dari setiap judul buku di page tersebut dan akan mengirimkan request kesana secara iterative. Hal ini karena laman yang didedikasikan ke buku-buku secara individual memiliki informasi yang jauh lebih lengkap dari halaman top books listing.

4. Di page individual book details, program akan menggunakan beautifulsoup untuk meng-ekstrak setiap informasi dari laman tersebut. Juga digunakan Regex untuk parsing raw data sehingga data yang disimpan di .csv & .json adalah data yang atomik dan tidak perlu diformatting lagi. Data type juga sudah dikonversi secara sesuai dengan semantiknya.

5. Setelah seluruh data telah diekstraksi secara asynchronous, data ditulis ke suatu file .csv. Lalu program spider akan ditutup.

6. Setelah program spider ditutup, akan dijalankan data_organizer.py yang akan mengkonversi .csv menjadi .json, dan melakukan sort tabel hasil berdasarkan id.

# Specification
1. Disarankan untuk menggunakan UNIX environment seperti linux dalam menjalankan makefile.
2. Install scrapy dulu dengan pip: 
    pip install Scrapy
3. Install Beautifulsoup:
    pip install beautifulsoup4

# How to use
Disediakan makefile (MAKEFILE YANG DIBUAT DISESUAIKAN DENGAN ENVIRONMENT UNIX), hanya perlu menjalankan command:

    make genre=DESIRED_GENRE 

contoh: make genre=fantasy, make genre=thriller

Jika ingin menambahkan detil lanjut, disediakan beberapa parameter untuk dimodifikasi di command line:

    make username=YOUR_USERNAME password=YOUR_PASSWORD genre=DESIRED_GENRE init_pnum_=PAGE_MULAI last_pnum=PAGE_AKHIR

secara default, program menerima parameter: 
    
    make username=13517068@std.stei.itb.ac.id password=testgrspider genre=horror init_pnum=1 last_pnum=5

# Ideas and innovations in utilizing the data
Dengan data yang didapatkan, banyak hal yang dapat dilakukan, seperti:
1. Apakah popular books == quality books? (Analisis apakah buku-buku yang terpopuler di laman topbooks memiliki average ratings yang tinggi berdasarkan ratings count)
2. Apakah buku yang populer didominasi oleh buku-buku tua atau buku-buku baru? (Analisis banyaknya entry buku di top books list berdasarkan published date) Hal ini akan meng-ekspos jika adanya bias pembaca, reviewer, dan pengkritik pada buku-buku lama yang dianggap sebagai lebih menyerupai 'literatur' daripada buku zaman sekarang yang, menurut banyak opini, sebagai 'dumbed down literature'.
3. Genre buku manakah yang paling populer, paling tinggi average ratingsnya, dan paling banyak review_countnya.
4. Format buku manakah yang populer: Paperback(cover tipis), Hardcover(cover tebal), Audiobook, Kindle Edition & E-books, etc.?
5. Apakah banyaknya halaman pada suatu buku mempengaruhi average ratings dari buku tersebut? (Hal ini penting, karena bagi banyak penulis, ketebalan buku yang pas sangatlah sulit ditentukan dan tidak ada konvensi yang selalu benar. Ketebalan yang terlalu tebal berisiko membuat pembaca bosan dan move-on ke buku lain, dan terlalu tipis akan membuat kesan tulisan yang 'rushed' dan aspek-aspek yang underdeveloped)
6. Penulis manakah yang memiliki karya terbanyak pada halaman top books? Data ini dapat mengungkapkan kemampuan penulis yang sesungguhnya, terutama kecepatan menulis dari berbagai author dalam menghasilkan quality books(buku yang populer). (Yes, I am looking at you, Mr. Stephen King) 

dan masih banyak lagi. Saya harapkan dari data yang didapatkan bisa memberikan insight yang lebih dalam mengenai dunia literatur baik bagi penulis dan pembaca.

# JSON Structure
Berikut adalah headers yang tersedia:
'id',
'title', 
'author', 
'ISBN', 
'series', 
'avg_rating', 
'pages', 
'rating_count', 
'review_count', 
'book_format',
'published_date', 
'publisher'

contoh .json hasil:
    {
        "id": "241",
        "title": "The Phantom of the Opera",
        "author": "Gaston Leroux",
        "ISBN": "0060809248",
        "series": "NULL",
        "avg_rating": "3.97",
        "pages": "360",
        "rating_count": "181121",
        "review_count": "5613",
        "book_format": "Paperback",
        "published_date": "December 30th 1987",
        "publisher": "Harper Perennial"
    }

# Screenshots:
https://imgur.com/pnsDO2u

https://imgur.com/2By7yGU

https://imgur.com/PwZzEX6

# Reference:
  Python 3.7.
  Scrapy
  Beautifulsoup

  Selenium (Trivia project)
  Chromedriver (Trivia project)

# Author:
  Abel Stanley, NIM: 13517068
