<h1 align="center">
  <br>
  Seleksi 1 Warga Basdat 2019
  <br>
  <br>
</h1>

<h2 align="center">
  <br>
  Scraping readmanhua.net
  <br>
  <br>
</h2>


## Description
In the midst of the hustle and bustle of assignments, entertaining ourself is a crucial task. For me, reading manga is an absolute necessity. Readmanhua is one of the best stalls that is worth a visit. In readmanhua, we can read manhua (Chinese manga) which is good, worth reading and rarely found.

## How to Use
 1. Open Command Prompt
 2. Go to `src` directory
 3. Use command `make run` or `make all` or `python readmanhua.py`

## Ideas and Innovations in Utilizing the Data
Data I get from readmanhua can help me decide which manga worth to read. I think this advantage can be felt by other Chinese manga lovers.

 
## JSON Structure
JSON Structure that I use is :

3. Dalam mengerjakan tugas, calon warga basdat terlebih dahulu melakukan _fork_ project github pada link berikut: https://github.com/wargabasdat/Seleksi-2019-Tugas-1. Sebelum batas waktu pengumpulan berakhir, calon warga basdat harus sudah melakukan _pull request_ dengan nama ```TUGAS_SELEKSI_1_[NIM]```

4. Pada _repository_ tugas 1, calon warga basdat harus mengumpulkan _file script_, json hasil _data scraping_. _repository_ terdiri dari _folder_ `src`, `data` dan `screenshots`. _Folder_ `src` berisi _file script_/kode yang __*WELL DOCUMENTED* dan *CLEAN CODE*__, _folder_ `data` berisi _file_ json hasil _scraper_ sedangkan  _folder_ `screenshot` berisi tangkapan layar program.

5. <span style="color:blue;">Peserta juga diminta untuk membuat _simple build tools_ semacam `Makefile`, `npm scripts`, `runjs` yang bertujuan untuk membuat _program_ dengan gampang di-_build_, di-_run_, dan di-_clean_.</span>

> Template `makefile`

```Makefile
all: clean build run

clean: # remove data and binary folder

build: # compile to binary (if you use interpreter, then do not implement it)

run: # run your binary

```

> Template `npm scripts`

```javascript
"scripts": {
  "build": // if any (optional)
  "clean": // delete node_modules
}
```

> Template `runjs`
```javascript
import { run } from 'runjs'

export function clean () {
}

export function start () {
}

export function build () {
  // if any (optional)
}
```

6. Deadline pengumpulan tugas 1 adalah __31 Mei 2019 Pukul 23.59__

7. Hasil data scraping ini nantinya akan disimpan dalam DBMS  dan digunakan sebagai bahan tugas analisis dan visualisasi data

8. Sebagai referensi untuk mengenal _data scraping_, asisten menyediakan dokumen "_Short Guidance To Data Scraping_" yang dapat diakses pada link berikut: [Data Scraping Guidance](http://bit.ly/DataScrapingGuidance)

9. Tambahkan juga `.gitignore` pada _file_ atau _folder_ yang tidak perlu di-_upload_, __NB : BINARY TIDAK DIUPLOAD__

10. Mohon memperhatikan __etika__ dalam melakukan _scraping_

11. JSON harus dinormalisasi dan harus di-_preprocessing_

```
[
...
    {
        "Title": "Legend of Phoenix",
        "Url": "https://readmanhua.net/manga/legend-of-phoenix/",
        "Summary": "In an accident, an indifferent genius 10 year old boy falls along side a comet into a dreamland. There, he lives with the dwarves who inhabit the planet, using his talent and power to practice and grow his skills. Not only does he master the unparalleled smelting and forging techniques of the dwarves, but he develops a new form of martial arts as well. Just as he settles down and seems to be living a peaceful life, the cruel desires of others appear\u2026",
        "rateData": {
            "Rating": 4.6,
            "Vote": 20
        },
        "rankData": {
            "Ranking": 14,
            "Views": 1952
        },
        "Author": "Yun Tian Kong",
        "Artist": "Sen Memes",
        "Genres": [
            "Action",
            "Comedy",
            "Cultivation",
            "Fantasy",
            "Manhua"
        ],
        "Status": "OnGoing",
        "Release": [
            {
                "Chapter": "38",
                "Release Date": "",
                "Url Chapter": "https://readmanhua.net/manga/legend-of-phoenix/chapter-38?style=list"
            },
            {
                "Chapter": "37",
                "Release Date": "07 Jul 19",
                "Url Chapter": "https://readmanhua.net/manga/legend-of-phoenix/chapter-37?style=list"
            },
            {
                "Chapter": "36",
                "Release Date": "26 Jun 19",
                "Url Chapter": "https://readmanhua.net/manga/legend-of-phoenix/chapter-36?style=list"
            },
            {
                "Chapter": "35",
                "Release Date": "17 Jun 19",
                "Url Chapter": "https://readmanhua.net/manga/legend-of-phoenix/chapter-35?style=list"
            },
            {
                "Chapter": "34",
                "Release Date": "06 Jun 19",
                "Url Chapter": "https://readmanhua.net/manga/legend-of-phoenix/chapter-34?style=list"
            },
            {
                "Chapter": "33",
                "Release Date": "27 May 19",
                "Url Chapter": "https://readmanhua.net/manga/legend-of-phoenix/chapter-33?style=list"
            },
            {
                "Chapter": "32",
                "Release Date": "21 May 19",
                "Url Chapter": "https://readmanhua.net/manga/legend-of-phoenix/chapter-32?style=list"
            },
            {
                "Chapter": "31",
                "Release Date": "21 May 19",
                "Url Chapter": "https://readmanhua.net/manga/legend-of-phoenix/chapter-31?style=list"
            },
            {
                "Chapter": "30",
                "Release Date": "12 May 19",
                "Url Chapter": "https://readmanhua.net/manga/legend-of-phoenix/chapter-30?style=list"
            },
            {
                "Chapter": "29",
                "Release Date": "11 May 19",
                "Url Chapter": "https://readmanhua.net/manga/legend-of-phoenix/chapter-29?style=list"
            },
            {
                "Chapter": "28",
                "Release Date": "11 May 19",
                "Url Chapter": "https://readmanhua.net/manga/legend-of-phoenix/chapter-28?style=list"
            },
            {
                "Chapter": "27",
                "Release Date": "05 May 19",
                "Url Chapter": "https://readmanhua.net/manga/legend-of-phoenix/chapter-27?style=list"
            },
            {
                "Chapter": "26",
                "Release Date": "23 Apr 19",
                "Url Chapter": "https://readmanhua.net/manga/legend-of-phoenix/chapter-26?style=list"
            },
            {
                "Chapter": "25",
                "Release Date": "14 Apr 19",
                "Url Chapter": "https://readmanhua.net/manga/legend-of-phoenix/chapter-25?style=list"
            },
            {
                "Chapter": "24",
                "Release Date": "31 Mar 19",
                "Url Chapter": "https://readmanhua.net/manga/legend-of-phoenix/chapter-24?style=list"
            },
            {
                "Chapter": "23",
                "Release Date": "24 Mar 19",
                "Url Chapter": "https://readmanhua.net/manga/legend-of-phoenix/chapter-23?style=list"
            },
            {
                "Chapter": "22",
                "Release Date": "02 Mar 19",
                "Url Chapter": "https://readmanhua.net/manga/legend-of-phoenix/chapter-22?style=list"
            },
            {
                "Chapter": "21",
                "Release Date": "02 Mar 19",
                "Url Chapter": "https://readmanhua.net/manga/legend-of-phoenix/chapter-21?style=list"
            },
            {
                "Chapter": "20",
                "Release Date": "02 Mar 19",
                "Url Chapter": "https://readmanhua.net/manga/legend-of-phoenix/chapter-20?style=list"
            },
            {
                "Chapter": "19",
                "Release Date": "02 Mar 19",
                "Url Chapter": "https://readmanhua.net/manga/legend-of-phoenix/chapter-19?style=list"
            },
            {
                "Chapter": "18",
                "Release Date": "02 Mar 19",
                "Url Chapter": "https://readmanhua.net/manga/legend-of-phoenix/chapter-18?style=list"
            },
            {
                "Chapter": "17",
                "Release Date": "02 Mar 19",
                "Url Chapter": "https://readmanhua.net/manga/legend-of-phoenix/chapter-17?style=list"
            },
            {
                "Chapter": "16",
                "Release Date": "02 Mar 19",
                "Url Chapter": "https://readmanhua.net/manga/legend-of-phoenix/chapter-16?style=list"
            },
            {
                "Chapter": "15",
                "Release Date": "02 Mar 19",
                "Url Chapter": "https://readmanhua.net/manga/legend-of-phoenix/chapter-15?style=list"
            },
            {
                "Chapter": "14",
                "Release Date": "02 Mar 19",
                "Url Chapter": "https://readmanhua.net/manga/legend-of-phoenix/chapter-14?style=list"
            },
            {
                "Chapter": "13",
                "Release Date": "02 Mar 19",
                "Url Chapter": "https://readmanhua.net/manga/legend-of-phoenix/chapter-13?style=list"
            },
            {
                "Chapter": "12",
                "Release Date": "02 Mar 19",
                "Url Chapter": "https://readmanhua.net/manga/legend-of-phoenix/chapter-12?style=list"
            },
            {
                "Chapter": "11",
                "Release Date": "02 Mar 19",
                "Url Chapter": "https://readmanhua.net/manga/legend-of-phoenix/chapter-11?style=list"
            },
            {
                "Chapter": "10",
                "Release Date": "02 Mar 19",
                "Url Chapter": "https://readmanhua.net/manga/legend-of-phoenix/chapter-10?style=list"
            },
            {
                "Chapter": "9",
                "Release Date": "02 Mar 19",
                "Url Chapter": "https://readmanhua.net/manga/legend-of-phoenix/chapter-9?style=list"
            },
            {
                "Chapter": "8",
                "Release Date": "02 Mar 19",
                "Url Chapter": "https://readmanhua.net/manga/legend-of-phoenix/chapter-8?style=list"
            },
            {
                "Chapter": "7",
                "Release Date": "02 Mar 19",
                "Url Chapter": "https://readmanhua.net/manga/legend-of-phoenix/chapter-7?style=list"
            },
            {
                "Chapter": "6",
                "Release Date": "02 Mar 19",
                "Url Chapter": "https://readmanhua.net/manga/legend-of-phoenix/chapter-6?style=list"
            },
            {
                "Chapter": "5",
                "Release Date": "02 Mar 19",
                "Url Chapter": "https://readmanhua.net/manga/legend-of-phoenix/chapter-5?style=list"
            },
            {
                "Chapter": "4",
                "Release Date": "02 Mar 19",
                "Url Chapter": "https://readmanhua.net/manga/legend-of-phoenix/chapter-4?style=list"
            },
            {
                "Chapter": "3",
                "Release Date": "02 Mar 19",
                "Url Chapter": "https://readmanhua.net/manga/legend-of-phoenix/chapter-3?style=list"
            },
            {
                "Chapter": "2",
                "Release Date": "02 Mar 19",
                "Url Chapter": "https://readmanhua.net/manga/legend-of-phoenix/chapter-2?style=list"
            },
            {
                "Chapter": "1",
                "Release Date": "02 Mar 19",
                "Url Chapter": "https://readmanhua.net/manga/legend-of-phoenix/chapter-1?style=list"
            },
            {
                "Chapter": "0",
                "Release Date": "02 Mar 19",
                "Url Chapter": "https://readmanhua.net/manga/legend-of-phoenix/chapter-0?style=list"
            }
        ]
    },
    ...
]
```
## Screenshoot
![ss json](https://github.com/bluejaden99/TUGAS_SELEKSI_1_13517037/blob/master/screenshots/json.png)
![ss src](https://github.com/bluejaden99/TUGAS_SELEKSI_1_13517037/blob/master/screenshots/source.png)
## References


 - Libraries used are json, time, requests, re, and BeautifulSoup.
 - [https://www.youtube.com/watch?v=XQgXKtPSzUI&t=124s](https://www.youtube.com/watch?v=XQgXKtPSzUI&t=124s)

12. <span style="color:blue">Berikan `README` yang __WELL DOCUMENTED__ dengan cara __override__ _file_ `README.md` ini. `README` harus memuat minimal konten :</span>
```
- Description
- Specification (optional)
- How to use
- Ideas and innovations in utilizing the data
- JSON Structure
- Screenshot program (di-upload pada folder screenshots, di-upload file image nya, dan ditampilkan di dalam README)
- Reference (Library used, etc)
- Author
```



>**DESYA ANUGRAH S.P - 13517037**
