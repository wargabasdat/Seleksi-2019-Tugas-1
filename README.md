<h1 align="center">
  <br>
  Data Scraping <i>jadwalnonton.com</i>
  <br>
  <br>
</h1>

## Description

jadwalnonton.com adalah situs yang menampilkan jadwal penayangan film untuk setiap teater di tiap kota yang tersedia pada data. Dalam web-scrapping ini, akan disimpan informasi teater di tiap kota serta jadwal beserta keterangan lainnya dari film yang ditayangkan pada tanggal hari ini.

## How to use

Berikut langkah-langkah untuk menjalankan program (Bagi pengguna windows) :
1. Buka cmd
2. Arahkan ke direktori yang dimaksud
3. Gunakan perintah make run atau make all

## Ideas and innovations in utilizing the data

Data yang diperoleh dari <i>jadwalnonton.com</i> dapat digunakan sebagai informasi bagi para penggemar film khususnya bioskop untuk menentukan jadwal yang tepat untuk menonton film tertentu di teater tertentu.

## JSON Structure

----Nama Kota
----Daftar Teater
--------Nama Teater
--------Alamat Teater
--------Telepon
--------Tanggal
----------Daftar Film
------------Judul
------------Tipe
------------Kategori
------------Durasi
------------Harga
------------Jadwal

## Screenshots

<strong>Source code</strong>
<img src="https://github.com/mahantiindah/Seleksi-2019-Tugas-1/blob/master/screenshots/src.png" title="source code">

<strong>Data JSON</strong>
<img src="https://github.com/mahantiindah/Seleksi-2019-Tugas-1/blob/master/screenshots/data.png" title="data json">

## Reference

Library yang digunakan dalam program adalah sebagai berikut.
- BeautifulSoup
- requests
- json
- re

<h4>
  <br>
  <i>Aisyah Nurul Izzah Adma - 13517046</i>
  <br>
</h4>
