from bs4 import BeautifulSoup
import requests
import json
import re

def getData(url,header):
    response = requests.get(url, headers = header)
    soup = BeautifulSoup(response.text, "html.parser")

    data = {}
    nameTheater = soup.find("h1")
    data["Nama Theater"] = nameTheater.text.strip()
    
    detTheater = soup.find("p", {"style": "line-height: 18pt;"})
    tempString = detTheater.text.strip()[:-9]
    x = re.search(r"Telp", tempString)
    if x != None:
        data["Alamat Theater"] = tempString[:x.start()]
        data["Telepon"] = tempString[x.start()+6:]

    else:
        data["Alamat Theater"] = tempString
        data["Telepon"] = ""

    dateTheater = soup.find("span", {"class" : "right"})
    data["Tanggal"] = dateTheater.text.strip()
    
    movie = {}
    movieList = soup.find("div", {"class" : "mtom20"})
    nameList = movieList.find_all("div", {"class" : "rowl clearfix"})
    data["Daftar Film"] = []
    i = 1

    for name in nameList:
        movie = {}

        nameMovie = name.find("h2")
        tempString = nameMovie.text.strip()
        x = re.search(r"\)", tempString)
        if x != None:
            movie["Judul Film"] = tempString[:x.start()+1]
            movie["Kategori"] = tempString[x.start()+1:]
        else:
            movie["Judul Film"] = tempString
            movie["Kategori"] = ""

        genreMovie = name.find("p")
        movie["Genre Film"] = genreMovie.text.strip()[:-12]
        movie["Durasi"] = genreMovie.text.strip()[-9:]
        
        priceMovie = name.findNext("p", {"class" : "htm"})
        movie["Harga"] = priceMovie.text.strip()[18:]
        data["Daftar Film"].append(movie)
        i = i+1

        movie["Jadwal"] = []
        temp = name.find("ul")
        scheduleList = temp.find_all("li")
        for schedule in scheduleList:
            movie["Jadwal"].append(schedule.text.strip())

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
        hasil.append(getData(thlist[i]["href"],header))

    with open("../data/data.json", "w") as outfile:
        json.dump(hasil, outfile, indent = 4)