<h1 align="center">
  <br>
  Seleksi 1 Warga Basdat 2019
  <br>
  <br>
</h1>

<h2 align="center">
  <br>
  themusicnetwork Chart Scraping
  <br>
  <br>
</h2>

## Description

This program scrapes music chart data from https://themusicnetwork.com. A music chart, also known as a record chart, is a ranking of recorded music according to certain criteria during a given period of time, in this case, a week.

The data result includes:
- Position or ranking
- Song info:
	- Song title
	- Song artist
	- Song label
- Chart info:
	- Position or ranking last week
	- Time spent on the chart (week)
	- Highest position the song has reached


## Specifications

1. Lakukan _data scraping_ dari sebuah laman web untuk memperoleh data atau informasi tertentu __TANPA MENGGUNAKAN API__

2. Daftarkan judul topik yang akan dijadikan bahan _data scraping_ pada spreadsheet berikut: [Topik Data Scraping](https://docs.google.com/spreadsheets/d/1BokKV8Qky7Hmry0dSRsmlT3LKs6jFWEy-BPt32Oc9-o/edit?usp=sharing). Usahakan agar tidak ada peserta dengan topik yang sama. Akses edit ke spreadsheet akan ditutup tanggal __20 Mei 2019 pukul 20.00 WIB__

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
Preprocessing contohnya:
- Cleaning
- Parsing
- Transformation
- dan lainnya
```

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


## How to Use

1. Run this script from the root of this repository
```
$ python3 src/main.py
```

2. Input the music chart link you want to scrape

3. Input a file name where you want to save the data

4. Data can be found in data


## Ideas and Innovations in Utilizing the Data

Music chart data can be used to see the increase or decrease of a songs position. It can also be summarized by the end of the year making it a summary chart which is calculated from their component weekly charts. Component charts have become an increasingly important way to measure the commercial success of individual songs. Other than that, it can also measure the commercial success of an album or an artist.


## JSON Structure

The JSON Structure of the output file contains position, song info (title, artist and label) and chart info (position last week, time spent on the chart and highest position)
```
{
	"songs": [
		{
			"position": 1,
			"songInfo": {
				"title": "I Don't Care",
				"artist": "Ed Sheeran & Justin Bieber",
				"label": "WMA/UMA"
			},
			"chartInfo": {
				"lastWeek": "3",
				"timeSpent": 2,
				"highestPosition": 1
			}
		},
		...
	]
}
```


## Screenshot Program

![ScreenShot-issue1238-H100](https://raw.githubusercontent.com/tasyald/Seleksi-2019-Tugas-1/master/screenshots/ScreenShot-issue1238-H100.png)

![ScreenShot-issue1239-H100](https://raw.githubusercontent.com/tasyald/Seleksi-2019-Tugas-1/master/screenshots/ScreenShot-issue1239-H100.png)


## Reference

### Runtime
Python 3

### Library used
- requests
- bs4
- os
- json


<p align="center">
  <br>
  Tasya Lailinissa Diandraputri - 13517141
  <br>
  <br>
</p>
