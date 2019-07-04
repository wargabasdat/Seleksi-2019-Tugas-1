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
3. Gunakan perintah make run atau make all
```cmd
   $ make run
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
                    "Ukuran": ,
                    "Refundable": 
                },
                "Harga": 
            }
        ]
    }
```
## Screenshots
> Source Code
![Source Code](/screenshots/dataScrapping.png)
> Json
![Json](/screenshots/data.png)

## Reference
Library yang digunakan antara lain.
    * requests
    * bs4
    * lxml
    * time
    * json
    * re

### Gama Pradipta Wirawan / 13517049