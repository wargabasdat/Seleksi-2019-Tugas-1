import time
import re
import requests
from bs4 import BeautifulSoup
import json

def ambil_data(url):
    global header
    response = requests.get(url, headers = header)
    soup = BeautifulSoup(response.text, "html.parser")
    data = {}
    nama = soup.find("h1", {"class" : "listingTitle"})
    data["Nama Kos"] = nama.text.strip()

    harga = nama.findNext("p", {"class" : "text-center"})
    data["Harga per Bulan"] = int(harga.text.strip("Rp. / bulan ").replace(',',''))
    
    lokasi_kos = {}
    lokasi = soup.find("table", {"class" : "table borderless listingDetailLokasinJenis"})
    provinsi = lokasi.find("td", {"class" : "col-md-7"})
    lokasi_kos["Provinsi"] = provinsi.text.strip()
    kota = provinsi.findNext("td", text = "Kota").findNextSibling().findNextSibling()
    lokasi_kos["Kota"] = kota.text.strip()
    kecamatan = kota.findNext("td", text = "Kecamatan").findNextSibling().findNextSibling()
    lokasi_kos["Kecamatan"] = kecamatan.text.strip()
    alamat = kecamatan.findNext("td", text = "Alamat").findNextSibling().findNextSibling()
    lokasi_kos["Alamat"] = alamat.text.strip()

    data["Lokasi Kos"] = lokasi_kos
    
    tipe_kos = {}
    tipe = lokasi.findNext("table", {"class" : "table borderless listingDetailLokasinJenis"})
    jenis = tipe.find("td", {"class" : "col-md-7"})
    tipe_kos["Jenis Kos"] = jenis.text.strip()
    umur = jenis.findNext("td", {"class" : "col-md-7"})
    if umur:
        tipe_kos["Umur Bangunan"] = umur.text.strip()
        jam = umur.findNext("td", text = "Jam Bertamu").findNextSibling().findNextSibling()
        tipe_kos["Jam Bertamu"] = jam.text.strip()
    else:
        tipe_kos["Umur Bangunan"] = "-"
        jam = jenis.findNext("td", text = "Jam Bertamu").findNextSibling().findNextSibling()
        tipe_kos["Jam Bertamu"] = jam.text.strip()
    pelihara = jam.findNext("td", text = "Pelihara Binatang").findNextSibling().findNextSibling()
    tipe_kos["Pelihara Binatang"] = pelihara.text.strip()

    data["Tipe Kos"] = tipe_kos

    jumlah = soup.find("div", {"class" : "dataListing dataRight"})
    data["Jumlah Kamar"] = int(re.findall("\d+", jumlah.text.strip())[0])
    ukuran = jumlah.findNext("div", {"class" : "dataListing dataRight"})
    data["Ukuran Kamar"] = ukuran.text.strip()
    luas = ukuran.findNext("div", {"class" : "dataListing dataRight"})
    data["Luas Kamar"] = int(re.findall("\d+", luas.text.strip())[0])
    
    fk = {}
    list_fk = ["AC", "Internet/ Wifi", "TV", "Lemari Pakaian", "Kamar Mandi Dalam", "Water Heater", "Kasur", "Meja Belajar", "Kursi Belajar", "Kulkas"]
    for fasilitas in list_fk:
        fk[fasilitas] = "tidak"
    fasilitas_kamar = soup.findAll("div", {"class" : "row text-left"})
    for fasilitas in fasilitas_kamar:
        if fasilitas.text.strip() in list_fk:
            fk[fasilitas.text.strip()] = "ya"
    data["Fasilitas Kamar"] = fk

    fb = {}
    list_fb = ["Ruang Tamu", "Ruang Makan", "Keamanan 24 Jam", "Parkir Mobil", "Parkir Motor", "Dapur", "Pembantu", "Mesin Cuci"]
    for fasilitas in list_fb:
        fb[fasilitas] = "tidak"
    fasilitas_bangunan = soup.find("h3", text = "Fasilitas Bangunan")
    fbs = fasilitas_bangunan.find_next_siblings("div", {"class" : "col-md-3 col-xs-6 fasilitas"})
    for fasilitas in fbs:
        if fasilitas.text.strip() in list_fb:
            fb[fasilitas.p.text.strip()] = "ya"
    data["Fasilitas Bangunan"] = fb
    
    fs = {}
    list_fs = ["ATM", "Mini Market", "Tempat Ibadah", "Warteg", "Restoran", "Laundry Shop", "Rumah Sakit", "GYM", "Mall"]
    for fasilitas in list_fs:
        fs[fasilitas] = "tidak"
    fasilitas_sekitar = soup.find("h3", text = "Fasilitas Sekitar")
    fss = fasilitas_sekitar.find_next_siblings("div", {"class" : "col-md-3 col-xs-6 fasilitas"})
    for fasilitas in fss:
        if fasilitas.text.strip() in list_fs:
            fs[fasilitas.p.text.strip()] = "ya"
    data["Fasilitas Sekitar"] = fs

    return data

if __name__ == "__main__":
    header = {"user-agent" : "mahantiindah@gmail.com"}
    url = "https://www.cari-kos.com/search/kos/dki-jakarta?price-from=0&price-to=10000000"
    response = requests.get(url, headers = header)
    soup = BeautifulSoup(response.text, "html.parser")

    hasil = []
    container = soup.find("div", {"id" : "listing-container"})
    details = container.find_all("a", href = True)
    for i in range (1):
        print(details[i]["href"])
        hasil.append(ambil_data(details[i]["href"]))
        time.sleep(2)

    with open("data/data.json", "w") as outfile:
        json.dump(hasil, outfile, indent = 4)