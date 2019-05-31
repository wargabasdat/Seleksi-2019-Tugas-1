<h1 align="center">
  <br>
    Seleksi 1 Basis Data
  <br>
  <br>
</h1>

#### Website yang di-scrape: https://www.formula1.com


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
- Makefile: melakukan pembersihan folder data sebelum menjalankan program
- Command Line Interface (CLI): menjalankan program secara langsung


## How to use
Program dapat dijalankan langsung dengan CLI (Command Line Iterface) atau dengan memanfaatkan _Makefile_ yang terdapat dalam folder yang sama dengan _README_ ini. Makefile akan menghapus data yang terdapat dalam folder _data_ dan menjalankan program dalam folder _src_ untuk mendapatkan hasil scraping yang nanti disimpan dalam folder _data_.

__Perintah di bawah ini dijalankan pada OS Windows__

Sebelum menjalankannya, dilakukan tahap ini untuk menginstalasi _python_ dan library-library yang dibutuhkan:
```
1. Download _python3_ dari https://www.python.org/downloads/
2. Masukkan path ke folder python ke environment (opsional)
3. Download _get-pip.py_ sript
4. Install _pip_ dengan menuliskan _python get-pip.py_ pada CLI
5. Install _beautifulsoup_ dengan menuliskan _pip install beautifulsoup4_ pada CLI
6. Install _requests_ dengan menuliskan _pip install requests_ pada CLI
```

Setelah instalasi, terdapat 2 cara untuk menjalankan program ini, yaitu:
_Command Line Interface_
```
1. Membuka folder _Seleksi-2019-Tugas-1_ pada CLI
2. Memasukkan perintah python src/Script.py
```
_Makefile_
```
1. Membuka folder _Seleksi-2019-Tugas-1_ pada CLI
2. Memasukkan perintah 
```


## Ide dan inovasi dengan menggunakan data
Data yang diperoleh dari hasil scraping ini dapat digunakan dan dikembangkan untuk:
```
- Mencari hasil balapan dari setiap balapan Formula 1 dari tahun 2000 hingga 2019
- Mendapatkan hasil klasemen setiap musim balapan Formula 1 dari tahun 2000 hingga 2019
- Tracking perjalanan karir salah Formula 1 salah seorang driver yang tercatat pada data
- Mencari juara dunia, baik pembalap maupun konstruktor, dari tahun 2000 hingga 2019
- Membandingkan pentingnya meraih posisi 1 bagi pembalap untuk dapat mendapatkan gelar dunia sebelum aturan perubahan poin (tahun 2000 - 2009) dan setelah aturan perubahan poin (2010 - 2019)
```


## Struktur JSON

__RaceData.json__
```
[
    {
        "Year": <Tahun balapan>,
        "Race Nation": <Nama negara balapan>,
        "Driver Race Position": <Posisi pembalap>,
        "Driver Name": <Nama pembalap>,
        "Driver Finish Time": <Waktu yang dibutuhkan oleh pembalap tersebut untuk menyelesaikan balapan (relatif terhadap pemimpin)>
    }
]
```
Keterangan: _DNF_ pada <Driver Finish Time> berarti pembalap tersebut tidak menyelsaikan balapan

__ResultData.json__
```
[
    {
        "Year": <Tahun balapan>
        "Driver Classment Position": <Posisi pembalap pada klasemen>
        "Driver Name": <Nama pembalap>
        "Driver Nationality": <Asal negara pembalap>
        "Driver Team": <Tim pembalap (konstruktor)>
        "Driver Points": <Poin yang didapat pembalap>
    }
]
```

__SeasonData.json__
```
[
    {
        "Year": <Tahun balapan>
        "Race Nation": <Nama negara balapan>
        "Race Name": <Nama balapan tersebut>
        "Race Date": <Tanggal balapan>
    }
]
```


## Referensi
Library yang digunakan:
```
1. requests             -> Melakukan HTTP Request terhadap website
2. beautifulsoup (bs4)  -> Melakukan olah data pada hasil HTTP Request
3. json                 -> Menuliskan file ke format .json
4. copy                 -> Memastikan kekonsistenan data saat membuat file JSON
5. time                 -> Memberikan waktu sleep buat program sebagai interval waktu antar request
```


## Screenshot kode program
Screenshot kode
![Pencarian link](https://github.com/Meyjan/Seleksi-2019-Tugas-1/blob/master/screenshots/ss_script_1.png)
![Pembuat JSON](https://github.com/Meyjan/Seleksi-2019-Tugas-1/blob/master/screenshots/ss_script_2.png)
![Pemanggil request](https://github.com/Meyjan/Seleksi-2019-Tugas-1/blob/master/screenshots/ss_script_3.png)
![Kontrol hasil request](https://github.com/Meyjan/Seleksi-2019-Tugas-1/blob/master/screenshots/ss_script_4.png)
![Main](https://github.com/Meyjan/Seleksi-2019-Tugas-1/blob/master/screenshots/ss_script_5.png)

Screenshot json
![RaceData](https://github.com/Meyjan/Seleksi-2019-Tugas-1/blob/master/screenshots/ss_json_racedata.png)
![ResultData](https://github.com/Meyjan/Seleksi-2019-Tugas-1/blob/master/screenshots/ss_json_resultdata.png)
![SeasonData](https://github.com/Meyjan/Seleksi-2019-Tugas-1/blob/master/screenshots/ss_json_seasondata.png)

Screenshot program saat dieksekusi
![Run](https://github.com/Meyjan/Seleksi-2019-Tugas-1/blob/master/screenshots/ss_run.png)


##### Author: Jan Meyer Saragih / 13517131