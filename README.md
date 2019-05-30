<h1 align="center">
  <br>
  Seleksi 1 Warga Basdat 2019
  <br>
  <br>
</h1>

<h2 align="center">
  Data Scraping
</h2>


<h3 align="center">
  Peminat SBMPTN tahun 2018
  <br>
  <br>
  <br>
  oleh:
  <br>
  Fata Nugraha/13517109
  <br>
</h3>


## Description

Kode untuk mendapatkan data peminat SBMPTN tahun 2018 dari http://sbmptn.ltmpt.ac.id

## How to Use

Masuk ke folder src lalu jalankan perintah 'python data_scraping.py' di cmd (Windows) atau jalankan Makefile dengan perintah 'make' di terminal (Linux)

## Ideas and innovations in utilizing the data

1. Membandingkan daya tampung dan peminat antar program studi di berbagai universitas
2. Menentukan program studi yang paling diminati
3. Mengamati persebaran peminat berdasarkan wilayah dan program studi di berbagai program studi dan universitas
4. Membandingkan banyaknya peminat yang berasal dari satu provinsi dengan universitas tersebut dengan yang berasal dari luar provinsi

## JSON Structure

#### Contoh:
```
[
    ...
    {
        "Kode Universitas": "113",
        "Nama Universitas": "UNIVERSITAS TEUKU UMAR",
        "Daftar Prodi": [
            {
                "Kode Prodi": "1131011",
                "Nama Prodi": "TEKNIK SIPIL",
                "Kapasitas": "60",
                "Total Peminat": "262",
                "Rincian Peminat": [
                    {
                        "Asal Daerah": "Aceh",
                        "Peminat": "243"
                    },
                    {
                        "Asal Daerah": "Sumatera Utara",
                        "Peminat": "7"
                    },
                    {
                        "Asal Daerah": "Sumatera Barat",
                        "Peminat": "9"
                    },
                    {
                        "Asal Daerah": "Riau",
                        "Peminat": "1"
                    },
                    {
                        "Asal Daerah": "DKI Jakarta",
                        "Peminat": "1"
                    },
                    {
                        "Asal Daerah": "Kalimantan Timur",
                        "Peminat": "1"
                    }
                ]
            },
            ...
            ]
        },
    ...
]
```

Sebuah universitas terdiri dari:<br>
`Kode Universitas`: Kode dari universitas tersebut.<br>
`Nama Universitas`: Nama dari universitas tersebut.<br>
`Daftar Prodi`: List yang berisikan program studi yang dimiliki universitas tersebut.<br><br>
Sebuah program studi terdiri dari:<br>
`Kode Prodi`: Kode dari program studi tersebut.<br>
`Nama Prodi`: Nama dari program studi tersebut.<br>
`Daya Tampung`: Daya tampung program studi tersebut.<br>
`Total Peminat`: Total peminat program studi tersebut.<br>
`Rincian Peminat`: List yang berisikan banyaknya peminat untuk provinsi-provinsi tertentu.<br>

## Screenshot program

![SS_1](https://github.com/Ft-N/Seleksi-2019-Tugas-1/blob/master/screenshots/ss_1.png)
![SS_2](https://github.com/Ft-N/Seleksi-2019-Tugas-1/blob/master/screenshots/ss_2.png)
![SS_3](https://github.com/Ft-N/Seleksi-2019-Tugas-1/blob/master/screenshots/ss_3.png)

## Reference

1. bs4, BeautifulSoup: Library untuk melakukan data scraping
2. requests: Library untuk request ke suatu URL
3. re: Library regex, untuk string matching
4. json, copy, os: Library untuk formatting json (file keluaran)
