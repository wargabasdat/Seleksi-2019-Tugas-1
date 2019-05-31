<h1 align="center">
  <br>
  Seleksi 1 Warga Basdat 2019
  <br>
  <br>
</h1>

<h2 align="center">
  <br>
  Data Scraping
  <br>
  Muhammad Hendry Prasetya
  <br>
  13517105
  <br>
  <br>
</h2>

## Description

Berikut adalah data scraping pada website http://www.duniainvestasi.com yang memiliki daftar saham perusahaan-perusahaan. Data scraping dilakukan dengan me-request data tabel daftar saham pada laman web. Setelah data di-scrape, data di-clean dari data yang tidak diinginkan. Kemudian, data diformat ke dalam file JSON. Tools yang digunakan dalam data scraping kali ini adalah python.

## Requirement

- Python 3.x
- Node.js version >= 8.2

## How to use

- How to use makefile:
```
1. Open Command Prompt
2. Move to master/root folder
3. Type "make"
```

- How to use npm scripts:
```
1. Open Command Prompt
2. Move to master/root folder
3. Type "npm run scripts"
```

- How to use runjs:
```
1. Open Command Prompt
2. Move to master/root folder
3. Type "npx run runfile.js"
```

## Ideas and Innovations

- Data dibersihkan dari kolom kosong
- Baris yang mengandung None/Null dihapus

## JSON Structure

Struktur JSON berdasarkan record file
```
  {"Kolom1":content1, Kolom2:content1, Kolom3:content1, Kolom4:content1}
  {"Kolom1":content2, Kolom2:content2, Kolom3:content2, Kolom4:content2}
```

## Screenshot Program

![Screenshot1](screenshots/1.jpg?raw=true "Title")
![Screenshot2](screenshots/2.jpg?raw=true "Title")
![Screenshot3](screenshots/3.jpg?raw=true "Title")

## Reference

Library used:
```
Pandas
Requests
BeautifulSoup
Regular Expression
```

Referensi bacaan
```
https://hackernoon.com/simple-build-tools-npm-scripts-vs-makefile-vs-runjs-31e578278162
https://stackoverflow.com/
https://www.datacamp.com/community/tutorials/web-scraping-using-python
https://nodejs.org/
```

Sumber data
```
http://www.duniainvestasi.com
```

## Author
Muhammad Hendry Prasetya - 13517105
