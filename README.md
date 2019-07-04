<h1 align="center">
  <br>
  Scraping Data PegiPegi
  <br>
  <br>
</h1>

## Description
PegiPegi adalah perusahaan yang melayani pemesanan hotel, tiket pesawat dan tiket kereta api yang berbasis web. Pegi pegi secara fokus membantu kebutuhan liburan atau perjalanan bisnis masyakarat Indonesia.

## How to use
Langkah-Langkah untuk pengguna windows:
1. Buka cmd
2. Buka direktori yang dimaksud
3. Gunakan perintah make all
```cmd
   $ make all
```

## Ideas and Innovations in Utilizing the Data
Data yang diperoleh dari PegiPegi.com ini dapat digunakan untuk membandingkan harga sewa kamar dan fasilitas yang ditawarkan oleh masing-masing hotel.

## JSON Structure
```Json
{
        "Nama Hotel": ,
        "Bintang": ,
        "Alamat Hotel": ,
        "Fasilitas & Layanan Hotel": {
            "Spa": ,
            "Sauna": ,
            "Jacuzzi": ,
            "Fitness": ,
            "Gymnasium": ,
            "Field": ,
            "Tennis": ,
            "Indoor pool": ,
            "Outdoor pool": ,
            "Table tennis": ,
            "Kids club": ,
            "Billiard": ,
            "Game corner": ,
            "Karaoke": ,
            "Banquet hall": ,
            "BBQ": ,
            "Dry room": ,
            "Restaurant": ,
            "Coffee Shop": ,
            "Convenience store": ,
            "Bar": ,
            "Lounge": ,
            "Business center": ,
            "Conference room": ,
            "Non-smoking rooms": ,
            "Ice-making machine": ,
            "Morning Call": ,
            "Layanan Kamar": ,
            "Cleaning service": ,
            "Massage": ,
            "Rental cycle": ,
            "Voltage Converter": ,
            "Parking Area": 
        },
        "Aktivitas Olah Raga": {
            "Gymnasium": ,
            "Field": ,
            "Tennis": ,
            "Golf": ,
            "Putting golf": ,
            "Fishing": ,
            "Paraglider": ,
            "Horse riding": ,
            "Diving": ,
            "Rafting": ,
            "Canoe": 
        },
        "Internet & Wifi": {
            "Koneksi LAN (semua kamar)": ,
            "Bebas akses Wi-Fi di lobby": ,
            "Koneksi dial-up": ,
            "Kabel LAN": ,
            "Wireless LAN": ,
            "Tersedia rental PC": ,
            "Koneksi internet gratis": 
        },
        "Fasilitas Kamar": {
            "Bath and Toilet: All rooms": ,
            "Shower: All rooms": ,
            "Bathtub: All rooms": ,
            "Air conditioner: All rooms": ,
            "TV": ,
            "VCR atau DVD": ,
            "BS broadcast": ,
            "Refrigerator": ,
            "Mini Bar": ,
            "Kitchen: All rooms": ,
            "Trouser press (*including rental)": ,
            "Safety box": ,
            "Face towel, Hand towel": ,
            "Toothbrush and/or Toothpaste": ,
            "Bath towel": ,
            "Shampoo": ,
            "Hair Conditioner": ,
            "Body soap": ,
            "Soap": ,
            "Pajamas": ,
            "Bathrobe": ,
            "Sandal": ,
            "Hair Dryer": ,
            "Razor and/or Shaver": ,
            "Shower cap": ,
            "Cottonbud": ,
            "Shower Toilet": ,
            "Comb": 
        },
        "Pilihan Kamar": [
            {
                "Nama Kamar": ,
                "Info Kamar": {
                    "Maksimal Orang": ,
                    "Sarapan": ,
                    "Wifi Gratis": ,
                    "Ukuran": null,
                    "Refundable": 
                },
                "Harga": 
            }
        ]
    }
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
Preprocessing contohnya :
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

<h1 align="center">
  <br>
  Selamat Ber-Eksplorasi!
  <br>
  <br>
</h1>

<p align="center">
  <br>
  Basdat Industries - Lab Basdat 2019
  <br>
  <br>
</p>
