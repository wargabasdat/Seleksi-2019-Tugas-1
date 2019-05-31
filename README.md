<h1 align="center">
  <br>
  Seleksi 1 Warga Basdat 2019
  <br>
  <br>
</h1>

<h2 align="center">
  <br>
  Data Scraping from xe.com
  <br>
  <br>
</h2>

## Description
Program ini melakukan data scraping terhadap website xe.com. Website ini berisi data currency rate berbagai mata uang di dunia.
Data yang diperoleh dari scraping melalui program ini adalah currency rate berbagai mata uang terhadap mata uang USD (US Dollar) dari tanggal yang ditentukan hingga tanggal yang ditentukan melalui input ke program.


## Specifications
Runtime : python3
libraries : 
1. bs4
2. json
3. pandas
4. numpy
5. requests

## How To Use
1. Jalankan program dengan menggunakan
```
$ python3 src/main.py
'''
2. Masukan tanggal awal dan akhir data yang diinginkan
3. data akan diupdate ke dalam file json
```

### Ideas and inovation in utilizing the data
Dari data hasil scraping ini dapat digunakan untuk banyak hal.
1. Melakukan pengamatan terhadap ekonomi suatu negara yang dapat dikembangkan ke banyak hal.
  Memprediksi peluang impor dan ekspor yang tepat, investasi ke luar negeri
2. Mengetahui perbandingan kekuatan mata uang suatu negara terhadap USD.
  Melalui data ini juga dapat digunakan untuk melakukan investasi dengan menggunakan valuta asing
dan banyak lagi.


### JSON Structure
Example :
```
  {{"Date":"2019-05-27","Currency Code":"USD","Units per USD":"1.0000000000","USD per Unit":"1.0000000000"}}
```
```
  {{"Currency Code":"KYD","Currency Name":"Caymanian Dollar"}}
```


### Screenshot
![Screenshot](screenshots/screenshot_1.PNG)
![Screenshot](screenshots/screenshot_2.PNG)


### Reference

library used :
1. bs4
2. json
3. numpy
4. pandas
5. requests

<p align="center">
  <br>
  Samantha Olivia Tandri - 13517123
  <br>
  <br>
</p>
