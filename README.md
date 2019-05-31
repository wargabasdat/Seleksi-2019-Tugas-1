<h1 align="center">
  <br>
    Seleksi 1 Basis Data
  <br>
  <br>
</h1>

<p align="left">
  <br>
    Website yang di-scrape: https://www.formula1.com
  <br>
  <br>
</p>


## Deskripsi
Program ini dibuat sebagai tugas seleksi Lab Basis Data, Institut Teknologi Bandung. Program yang dijalankan melakukan data scraping pada website  _https://www.formula1.com_. Website tersebut merupakan website official dari autosport Formula 1. Dalam website tersebut, semua hasil balapan Formula 1 disimpan dari tahun 1950 hingga sekarang. Namun, dengan alasan jumlah data yang banyak, maka data yang di-scrape melalui Program ini hanya merupakan data balapan Formula 1 dari tahun 2000 hingga 2019.

Program ini mengambil 3 data dari formula 1. Setelah itu ketiga jenis data tersebut disimpan dalam file JSON:
```
- Hasil balapan dalam Formula 1 (dalam bentuk urutan finish setiap balapan) -> RaceData.json
- Hasil poin yang dicapai setiap pembalap dalam Formula 1 (dalam bentuk poin yang dicapai setiap pembalap tiap tahun) -> ResultData.json
- Setiap balapan yang diselenggarakan oleh Formula 1 (dalam bentuk nama balapan tiap musimnya) -> SeasonData.json
```

Sebelum memasukkan data ke JSON tersebut, program melakukan HTTP request GET pada website _https://www.formula1.com_ Setelah mendapatkan data dari website tersebut, program memproses data-data yang didapat, membentuk data dalam bentuk tuple, lalu menghasilkan file JSON. Adapun data-data yang disimpan di dalam file JSON dapat dilihat di bawah pada bagian _Struktur JSON_.


## Spesifikasi
Program ini dibuat dengan menggunakan bahasa pemrograman _Python3_, versi 3.7.

Library python yang dibutuhkan untuk menjalankan program ini:
```
- Beautifulsoup
- Requests
- Json
- Copy
- Time
```

Program dapat dijalankan menggunakan:
- Makefile
- Command Line Interface (CLI)


## How to use
Program dapat dijalankan dengan CLI (Command Line Iterface) atau dengan memanfaatkan _Makefile_ yang terdapat dalam folder yang sama dengan _README_ ini. Makefile akan menghapus data yang terdapat dalam folder _data_ dan menjalankan program dalam folder _src_ untuk mendapatkan hasil scraping yang nanti disimpan dalam folder _data_.

__Windows__

Sebelum menjalankannya, dilakukan tahap ini untuk menginstalasi _python_ dan library-library yang dibutuhkan:
```
1. Download _python3_ dari _https://www.python.org/downloads/_
2. Masukkan path ke folder python ke environment (opsional)
3. Download _get-pip.py_ sript
4. Install _pip_ dengan menuliskan _python get-pip.py_ pada CLI
5. Install _beautifulsoup_ dengan menuliskan _pip install beautifulsoup4_ pada CLI
6. Install _requests_ dengan menuliskan _pip install requests_ pada CLI
```

Setelah instalasi, terdapat 2 cara u

## Ide dan inovasi dengan menggunakan data
- Data yang diperoleh mampu diguanakan untuk 

## Struktur JSON

## Referensi

### Author

12. Berikan `README` yang __WELL DOCUMENTED__ dengan cara __override__ _file_ `README.md` ini. `README` harus memuat minimal konten :
```
- Programion
- Specification
- How to use
- Ideas and innovations in utilizing the data
- JSON Structure
- Screenshot program (di-upload pada folder screenshots, di-upload file image nya, dan ditampilkan di dalam README)
- Reference (Library used, etc)
- Author
```

<p align="left">
  <br>
    Jan Meyer Saragih
  <br>
  <br>
</p>
