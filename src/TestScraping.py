# Nama  : Jan Meyer Saragih
# NIM   : 13517131

# Web yang di-scrape : https://www.formula1.com

# Install
import json # Digunakan untuk membuat file JSON dari hasil scraping
import requests as req # Digunakan untuk mengambil request http dari sebuah website
from bs4 import BeautifulSoup as bs # Digunakan untuk memproses hasil HTTP request sebelum membuat file JSON
import time # Digunakan untuk mengimplementasikan sleep sebagai interval antar request HTTP
import copy # Digunakan untuk melakukan deepcopy dalam membuat file JSON

#---------------------------------------------------- METHOD PENCARI LINK --------------------------------------------------#

# Mendapatkan link yang berisi season-season (tahun) di mana F1 dijalankan
def getLinksOfSeason(year):
    strLink = "https://www.formula1.com/en/results.html/" + str(year) + "/races.html"
    return strLink

# Mendapatkan ranking yang berisi urutan hasil akhir posisi sebuah driver dalam satu tahun
def getLinksOfResults(year):
    strLink = "https://www.formula1.com/en/results.html/" + str(year) + "/drivers.html"
    return strLink

# Mendapatkan link-link tertentu yang berisi detail suatu balapan dalam sebuah season
def getLinksOfRaces(soup, year):
    listOfLinks = []
    checkLink = "/en/results.html/" + str(year) + "/races/"

    # Mendaftar link semua race dalam 1 season tersebut
    for link in soup.find_all("a", href=True):
        strLink = str(link['href'])
        if (strLink.startswith(checkLink) and strLink.endswith("race-result.html")):
            listOfLinks.append(strLink)
    
    # F1 menuliskan link untuk daftar racenya 2 kali. Yang pertama untuk rencana semua race dalam 1 season dan setelahnya daftar race yang sudah direalisasi
    # Maka dari itu, hapus semua race yang belum direalisasi dengan cara menghapus semua race yang direncanakan
    firstLink = listOfLinks[0]
    listOfLinks.pop(0)
    while listOfLinks[0] != firstLink:
        listOfLinks.pop(0)
    
    # Mengubah link tersebut sehingga dapat diakses pada berikutnya
    for i in range(len(listOfLinks)):
        link = listOfLinks[i]
        listOfLinks[i] = "https://www.formula1.com" + link

    return listOfLinks

#---------------------------------------------------- METHOD PEMBUAT JSON --------------------------------------------------#

# Membuat sebuah JSON File dari sebuah data
def createJSON(path, data):
    # Membuat JSON File dari data sebuah season
    seasonJSON = {}
    seasonData = []

    for season in data[0]:
        seasonJSON['Year'] = season[0]
        seasonJSON['Race Nation'] = season[1]
        seasonJSON['Race Name'] = season[2]
        seasonJSON['Race Date'] = season[3]
        seasonData.append(copy.deepcopy(seasonJSON))

    fullPath = path + 'SeasonData' + '.json'

    with open(fullPath, 'w', encoding = 'utf8') as fp:
        json.dump(seasonData, fp, indent = 4, ensure_ascii = False)
    
    # Membuat JSON File dari data detail balapan dalam season tersebut
    raceJSON = {}
    raceData = []

    for race in data[2]:
        raceJSON['Year'] = race[0]
        raceJSON['Race Nation'] = race[1]
        raceJSON['Driver Race Position'] = race[2]
        raceJSON['Driver Name'] = race[3]
        raceJSON['Driver Finish Time'] = race[4]
        raceData.append(copy.deepcopy(raceJSON))
    
    fullPath = path + 'RaceData' + '.json'

    with open(fullPath, 'w', encoding = 'utf8') as fp:
        json.dump(raceData, fp, indent = 4, ensure_ascii = False)
    
    # Membuat JSON File dari data detail balapan dalam season tersebut
    resultJSON = {}
    resultData = []

    for result in data[1]:
        resultJSON['Year'] = result[0]
        resultJSON['Driver Classment Position'] = result[1]
        resultJSON['Driver Name'] = result[2]
        resultJSON['Driver Nationality'] = result[3]
        resultJSON['Driver Team'] = result[4]
        resultJSON['Driver Points'] = result[5]

        resultData.append(copy.deepcopy(resultJSON))
    
    fullPath = path + 'ResultData' + '.json'

    with open(fullPath, 'w', encoding = 'utf8') as fp:
        json.dump(resultData, fp, indent = 4, ensure_ascii = False)

#---------------------------------------------------- METHOD PENGAMBIL REQUEST --------------------------------------------------#

# Melakukan HTTP Request GET kepada sebuah web server untuk data season
def takeRequestSeason(year):
    url = getLinksOfSeason(year)
    userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
    email = 'saragih.meyer0821@gmail.com'
    head = {'user-agent' : userAgent, 'from' : email}
    result = req.get(url, headers = head, timeout = 10)
    return result

# Melakukan HTTP Request GET kepada sebuah web server untuk data hasil season
def takeRequestResult(year):
    url = getLinksOfResults(year)
    userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
    email = 'saragih.meyer0821@gmail.com'
    head = {'user-agent' : userAgent, 'from' : email}
    result = req.get(url, headers = head, timeout = 10)
    return result

# Melakukan HTTP Request GET kepada sebuah web server untuk data setiap race dalam season
def takeRequestRace(url):
    userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
    email = 'saragih.meyer0821@gmail.com'
    head = {'user-agent' : userAgent, 'from' : email}
    result = req.get(url, headers = head, timeout = 10)
    return result

#---------------------------------------------------- METHOD PENGONTROL REQUEST --------------------------------------------------#

# Mengatur apa yang dilakukan terhadap response yang didapatkan dari HTTP GET sebuah server
def responseController(response, year):
    # List kosong
    seasonData = []
    resultData = []
    allRaceData = []

    # Mengubah response menjadi bentuk html dan mendaftarkan ke soup
    soup = bs(response[0].text, 'html.parser')

    # Mendapatkan semua data nama balapan
    racesData = soup.find_all('tr')

    # Mendaftarkan link semua balapan dalam season tersebut
    races = getLinksOfRaces(soup, year)

    # Sleep: Interval antar request
    time.sleep(3)
    
    for i in range(1, len(racesData)):
        # Mencari nama negara balapan
        raceNation = racesData[i].find('a').get_text(strip=True)
        # Mencari tanggal balapan
        raceDate = racesData[i].find('td', attrs = {'class' :'dark hide-for-mobile'}).text  

        # Melakukan pencarian ke link untuk balapan tersebut untuk mencari nama balapan tersebut dan urutan finishnya
        # Melakukan request ke link balapan tersebut
        raceResponse = takeRequestRace(races[i - 1])
        raceSoup = bs(raceResponse.text, 'html.parser')

        # Mencari nama balapan
        raceNameLong = raceSoup.find('h1', attrs = {'class' : 'ResultsArchiveTitle'}).get_text(strip=True)
        raceName = raceNameLong.split('\n')[0]

        # Mencari urutan finish dalam balapan
        # Urutan finish tersebut diurutkan berdasarkan urutan, nama pembalap, nama tim, dan waktu menyelesaikan balapan
        finishPositions = raceSoup.find_all('tr')


        # Iterasi untuk mendata setiap urutan finish dalam balapan tersebut
        for j in range(1, len(finishPositions)):
            # Posisip pembalap tersebut dalam balapan
            position = j
            
            # Mencari pemenang nama pembalap dan waktu menyelesaikan balapan
            darkBoldList = finishPositions[j].find_all('td', attrs = {'class' : 'dark bold'})
            driverName = darkBoldList[0].find('span', attrs = {'class' : 'hide-for-tablet'}).text + ' ' + darkBoldList[0].find('span', attrs = {'class' : 'hide-for-mobile'}).text
            raceFinishTime = darkBoldList[1].text

            # Memasukkan data pada list allRaceData
            allRaceData.append((year, raceNation, position, driverName, raceFinishTime))

        # Memasukkan data pada list seasonData
        seasonData.append((year, raceNation, raceName, raceDate))

        # Sleep: interval antar request
        time.sleep(3)
    
    # Mencari data poin yang didapatkan tiap pembalap dalam season tersebut
    resultSoup = bs(response[1].text, 'html.parser')

    # Mendapatkan data semua pembalap
    results = resultSoup.find('tbody').find_all('tr')

    for i in range(len(results)):
        res = results[i].find_all('td')
        # Mencari posisi pembalap tersebut dalam klasmen
        driverPosition = i + 1
        # Mendapatkan nama dari pembalap tersebut
        driverName = res[2].find('span', attrs = {'class' : 'hide-for-tablet'}).text + ' ' + res[2].find('span', attrs = {'class' : 'hide-for-mobile'}).text
        # Mendapatkan asal negara pembalap tersebut
        driverNationality = res[3].text
        # Mendapatkan tim dari pembalap tersebut
        driverTeam = res[4].find('a').text
        # Mendapatkan poin yang didapat dari pembalap tersebuts
        driverPoint = res[5].text
        # Memasukkannya ke resultData
        resultData.append((year, driverPosition, driverName, driverNationality, driverTeam, driverPoint))
    
    return (seasonData, resultData, allRaceData)

# ------------------------------------------------ MAIN METHOD ---------------------------------------------------- #

# MAIN
# Main program
def main():
    # List yang menyimpan keseluruhan data
    seasonData = []
    resultData = []
    raceData = []

    # Meminta request untuk daftar balapan F1 dari season 2000 hingga 2019
    for year in range (2019, 2020):
        # Mengambil response dari tahun tersebut
        response_first = takeRequestSeason(year)
        response_second = takeRequestResult(year)
        response = (response_first, response_second)
        data = responseController(response, year)

        # Melakukan extend terhadap file tersebut ke dalam  ke list ke
        seasonData.extend(data[0])
        resultData.extend(data[1])
        raceData.extend(data[2])
        
        # Memastikan response sudah diterima (200)
        print("Year = ", year, "; Status of season: ", response[0].status_code, "; Status of result: ", response[1].status_code)

        # Memberi istirahat 10 detik antar iterasi
        time.sleep(10)
    
    # Membuat file JSON dari data mengenai season dan balapan-balapan di dalamnya
    createJSON('../data/', (seasonData, resultData, raceData))

# Call main
main()
