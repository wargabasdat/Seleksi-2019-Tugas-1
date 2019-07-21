from bs4 import BeautifulSoup
import requests
import json
import re

def getData(url,header):
    response = requests.get(url, headers = header)
    soup = BeautifulSoup(response.text, "html.parser")

    data = {}
    nameTheater = soup.find("h1")
    data["Nama Teater"] = nameTheater.text.strip()

    detTheater = soup.find("p", {"style": "line-height: 18pt;"})
    tempString = detTheater.text.strip()[:-9]
    x = re.search(r"Telp", tempString)
    if x != None:
        data["Alamat Teater"] = tempString[:x.start()]
        data["Telepon"] = tempString[x.start()+6:]

    else:
        data["Alamat Teater"] = tempString
        data["Telepon"] = "-"

    dateTheater = soup.find("span", {"class" : "right"})
    if (dateTheater != None):
        data["Tanggal"] = dateTheater.text.strip()
        
        movie = {}
        movieList = soup.find("div", {"class" : "mtom20"})
        nameList = movieList.find_all("div", {"class" : "rowl clearfix"})
        data["Daftar Film"] = []
        
        for name in nameList:
            movie = {}
            nameMovie = name.find("h2")
            tempString = nameMovie.text.strip()
            x = re.search(r"\)", tempString)
            y = re.search(r"\(", tempString)
            if x != None:
                movie["Judul"] = tempString[:y.start()]
                movie["Tipe"] = tempString[y.start()+1:x.start()]
                movie["Kategori"] = tempString[x.start()+1:]
            else:
                movie["Judul"] = tempString
                movie["Tipe"] = "-"
                movie["Kategori"] = "-"

            durationMovie = name.find("p")
            tempString = durationMovie.text.strip()
            x = re.search(r"-", tempString)
            if x != None:
                movie["Durasi"] = tempString[x.start()+2:]
            else:
                movie["Durasi"] = "-"
            
            priceMovie = name.findNext("p", {"class" : "htm"})
            if priceMovie != None :
                movie["Harga"] = priceMovie.text.strip()[18:]
            else :
                movie["Harga"] = "-"

            data["Daftar Film"].append(movie)

            movie["Jadwal"] = []
            temp = name.find("ul")
            scheduleList = temp.find_all("li")
            for schedule in scheduleList:
                movie["Jadwal"].append(schedule.text.strip())

    return data

if __name__ == "__main__":
    header = {"user-agent" : "13517046@std.stei.itb.ac.id"}
    url = "https://jadwalnonton.com/bioskop/"
    response = requests.get(url, headers = header)
    soup = BeautifulSoup(response.text, "html.parser")
  
    result = []
    city = soup.find("ul", {"class" : "ctlist"})
    cityList = city.find_all("a", href = True)
    for i in range (len(cityList)):
        city = {}
        city["Nama Kota"] = cityList[i].text
        url = cityList[i]["href"]
        response = requests.get(url, headers = header)
        soup = BeautifulSoup(response.text, "html.parser")
        theater = soup.find("div", {"class" : "row clearfix thlist"})
        if (theater != None) :
            city["Daftar Teater"] = []
            theaterList = theater.find_all("a", {"class" : "mojadwal"}, href = True)
            for i in range (len(theaterList)):
                city["Daftar Teater"].append(getData(theaterList[i]["href"],header))
        result.append(city)

    with open("../data/data.json", "w") as outfile:
        json.dump(result, outfile, indent = 4)