import time
import re
import requests
from bs4 import BeautifulSoup
import json

def ambil_data(url,header):
    response = requests.get(url, headers = header)
    soup = BeautifulSoup(response.text, "html.parser")
    data = {}
    nameTheater = soup.find("h1")
    data["Nama Theater"] = nameTheater.text.strip()
    
    detTheater = soup.find("p", {"style": "line-height: 18pt;"})
    data["Detail Theater"] = detTheater.text.strip()
    
    dateTheater = soup.find("span", {"class" : "right"})
    data["Tanggal"] = dateTheater.text.strip()
    
    movie = {}
    movieList = soup.find("div", {"class" : "mtom20"})
    nameList = movieList.find_all("div", {"class" : "rowl clearfix"})
    film = {}
    i = 1

    for name in nameList:
        movie = {}
        nameMovie = name.find("h2")
        genreMovie = name.find("p")
        priceMovie = name.findNext("p", {"class" : "htm"})
        movie["Judul Film"] = nameMovie.text.strip()
        movie["Genre Film"] = genreMovie.text.strip()[:-12]
        movie["Durasi"] = genreMovie.text.strip()[-9:]
        movie["Harga"] = priceMovie.text.strip()[18:]
        film["Film "+str(i)] = movie
        i = i+1
    data["Daftar Film"] = film


    """
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
    """
    return data

if __name__ == "__main__":
    header = {"user-agent" : "13517046@std.stei.itb.ac.id"}
    url = "https://jadwalnonton.com/bioskop/di-bandung/"
    response = requests.get(url, headers = header)
    soup = BeautifulSoup(response.text, "html.parser")

    hasil = []
    list = soup.find("div", {"class" : "row clearfix thlist"})
    thlist = list.find_all("a", {"class" : "mojadwal"}, href = True)
    for i in range (len(thlist)):
        print(thlist[i]["href"])
        hasil.append(ambil_data(thlist[i]["href"],header))
        #time.sleep(2)

    with open("data.json", "w") as outfile:
        json.dump(hasil, outfile, indent = 4)