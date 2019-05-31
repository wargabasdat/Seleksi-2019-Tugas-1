<h1>
  Daftar Pekerjaan
</h1>

<h4>
  Vincent Chuardi (13517103)
</h4>

## Deskripsi

Script ini melakukan <i>data scraping</i> pada laman [Jobs.id](https://www.jobs.id/lowongan-kerja)
<br>
Data yang didapatkan dan dipakai terdiri dari:
1. Nama Pekerjaan
2. Perusahaan Pekerjaan
3. Lokasi Pekerjaan
4. Rentang Gaji Pekerjaan
5. Tanggal Lowongan Pekerjaan di-<i>upload</i> di laman [Jobs.id](https://www.jobs.id)
6. Deskripsi Singkat Pekerjaan

## Spesifikasi

Runtime: Python 3
<p>
Library:
<br>
1. BeautifulSoup
  <br>
2. urllib
  <br>
3. json
</p>

## Cara Penggunaan

Jalankan script dengan memasukan perintah dibawah di Command Line:
1. cd src
1. python script.py

Hasil <i>data scraping</i> akan disimpan di direktori /data dengan nama result.json

## Ide Penggunaan Data

Data-data yang didapatkan digunakan untuk melihat kondisi lapangan-lapangan pekerjaan yang tersedia di Indonesia. Aspek yang diperhatikan bisa berupa penyebaran lokasi lapangan pekerjaan, pekerjaan jenis apa yang dibutuhkan, beserta gaji-gaji yang ditawarkan oleh perusahaan pemberi lowongan pekerjaan.

## Struktur JSON

JSON memiliki format sebuah key 'jobs' yang menyimpan data-data dari pekerjaan-pekerjaan yang didapatkan.

```
{
  "jobs": [
    {
      "job_title": title
      "company": company
      "location": location
      "salary": salary
      "upload_date": date
      "short_description": description
    },
    ...
  ]
}
```

## Screenshot

![screenshot](/screenshots/screenshot1.jpg)

## Reference

1. [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
2. [urllib](https://docs.python.org/3/library/urllib.html)
3. [json](https://docs.python.org/3/library/json.html?highlight=json#module-json)

## Author
Vincent Chuardi
