#Nama / NIM : Willy Santoso / 13517066
#Topik : Tugas Seleksi 1 Lab. Basis Data
#Sumber Data : www.nanokomputer.com

import requests
import bs4
import pandas
import time

#Fungsi yang mengembalikan sebuah soup hasil dari konfigurasi text dari request get
def requestAndGetSoup(link):
    try:
        time.sleep(5)
        res = requests.get(link, headers = header, timeout=10)
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
    except requests.exceptions.ConnectionError:
        print("Connection refused")
    except requests.exceptions.Timeout:
        print ("Timeout occurred")
    return soup

#Fungsi yang mengembalikan sebuah list yang berisi link yang ditunjuk pada laman yang dikonfigurasi menjadi parameter soup
def getLink(soup):
    listOfLink = []
    odd = soup.find_all('tr', attrs={'class' : 'productListing-odd'})
    even = soup.find_all('tr', attrs={'class' : 'productListing-even'})

    i=0
    while(i<len(even)):
        temp = odd[i].find('a', href=True)
        temp = str(temp['href'])
        listOfLink.append(temp)

        temp = even[i].find('a', href=True)
        temp = str(temp['href'])
        listOfLink.append(temp)

        i+=1

    if(len(odd)>len(even)):
        temp = odd[i].find('a', href=True)
        temp = str(temp['href'])
        listOfLink.append(temp)

    return listOfLink

#Fungsi yang mengembalikan info harga barang 
def getHarga(info):
    temp2 = info.find_all('span', attrs={'class' : 'productSpecialPrice'})

    if(len(temp2)!=0):
        harga = temp2[0].text
    else:
        harga = info.find('td', attrs = {'class' : 'pageHeadingP'}).get_text(strip=True)
        
    return harga

#Fungsi yang mengembalikan list data dari sebuah tuple yang berisi data informasi hasil scraping
def getData(data, soup):
    ID = soup.find('td', attrs = {'class' : 'smallText_SD'}).text
    nama = soup.find('td', attrs = {'class' : 'pageHeadingN'}).text
    deskripsi = soup.find('span', attrs={'class' : 'smallText_SD'}).get_text(strip=True)
    harga = getHarga(soup)
    imageLink = soup.find('a', attrs={'title' : nama}, href=True)
    imageLink = str(imageLink['href'])

    data.append((ID,nama,deskripsi,harga,imageLink))
    return data

#Fungsi yang mengembalikan data scraping dari part Processor yang dijual pada www.nanokomputer.com
def getProcessor():
    data = []
    links = []
    totalPages = 2

    for n in range (1,totalPages+1):
        url = "http://www.nanokomputer.com/index.php?cPath=26_528&sortcol=5&sortdir=a&page={}".format(n)
        soup = requestAndGetSoup(url)
        links += getLink(soup)

    for item in links:
        soup = requestAndGetSoup(item)
        data = getData(data,soup)
           
    return data

#Fungsi yang mengembalikan data scraping dari part Motherboard yang dijual pada www.nanokomputer.com
def getMotherboard():
    data = []
    links = []
    
    #Intel Motherboard
    totalPages = 5
    for n in range (1,totalPages+1):
        url = 'http://www.nanokomputer.com/index.php?cPath=27_41&sortcol=5&sortdir=a&page={}'.format(n)
        soup = requestAndGetSoup(url)
        links += getLink(soup)

    #AMD Motherboard
    totalPages = 3
    for n in range (1,totalPages+1):
        url = 'http://www.nanokomputer.com/index.php?cPath=27_40&sortcol=5&sortdir=a&page={}'.format(n)
        soup = requestAndGetSoup(url)
        links += getLink(soup)

    for item in links:
        soup = requestAndGetSoup(item)
        data = getData(data,soup)

    return data

#Fungsi yang mengembalikan data scraping dari part Memory yang dijual pada www.nanokomputer.com
def getMemory():
    data = []
    links = []
    totalPages = 6

    for n in range (1,totalPages+1):
        url = 'http://www.nanokomputer.com/index.php?cPath=28_562&sortcol=5&sortdir=a&page={}'.format(n)
        soup = requestAndGetSoup(url)
        links += getLink(soup)

    for item in links:
        soup = requestAndGetSoup(item)
        data = getData(data,soup)

    return data

#Fungsi yang mengembalikan data scraping dari part Graphic Cards yang dijual pada www.nanokomputer.com
def getGraphicCards():
    data = []
    links = []
    totalPages = 5

    for n in range (1,totalPages+1):
        url = 'http://www.nanokomputer.com/index.php?cPath=29_531&sortcol=5&sortdir=a&page={}'.format(n)
        soup = requestAndGetSoup(url)
        links += getLink(soup)

    for item in links:
        soup = requestAndGetSoup(item)
        data = getData(data,soup)

    return data

#Fungsi yang mengembalikan data scraping dari part Storage yang dijual pada www.nanokomputer.com
def getStorage():
    data = []
    links = []

    #Solid State Drive
    totalPages = 3
    for n in range (1,totalPages+1):
        url = 'http://www.nanokomputer.com/index.php?cPath=30_181&sortcol=5&sortdir=a&page={}'.format(n)
        soup = requestAndGetSoup(url)
        links += getLink(soup)

    #Hard Drive
    totalPages = 1
    for n in range (1,totalPages+1):
        url = 'http://www.nanokomputer.com/index.php?cPath=30_427&sortcol=5&sortdir=a&page={}'.format(n)
        soup = requestAndGetSoup(url)
        links += getLink(soup)

    for item in links:
        soup = requestAndGetSoup(item)
        data = getData(data,soup)

    return data

#Fungsi yang mengembalikan data scraping dari part Power Supply yang dijual pada www.nanokomputer.com
def getPowerSupply():
    data = []
    links = []

    #Non Modular
    totalPages = 2
    for n in range (1,totalPages+1):
        url = 'http://www.nanokomputer.com/index.php?cPath=32_654&sortcol=5&sortdir=a&page={}'.format(n)
        soup = requestAndGetSoup(url)
        links += getLink(soup)

    #Modular
    totalPages = 3
    for n in range (1,totalPages+1):
        url = 'http://www.nanokomputer.com/index.php?cPath=32_655&sortcol=5&sortdir=a&page={}'.format(n)
        soup = requestAndGetSoup(url)
        links += getLink(soup)

    for item in links:
        soup = requestAndGetSoup(item)
        data = getData(data,soup)

    return data

#Fungsi yang mengembalikan data scraping dari part Optical Drive yang dijual pada www.nanokomputer.com
def getOpticalDrive():
    data = []
    links = []
    totalPages = 1

    for n in range (1,totalPages+1):
        url = 'http://www.nanokomputer.com/index.php?cPath=31&sortcol=5&sortdir=a&page={}'.format(n)
        soup = requestAndGetSoup(url)
        links += getLink(soup)

    for item in links:
        soup = requestAndGetSoup(item)
        data = getData(data,soup)

    return data

#Fungsi yang mengembalikan data scraping dari part Cooling yang dijual pada www.nanokomputer.com
def getCooling():
    data = []
    links = []

    #Air CPU Cooling
    totalPages = 4
    for n in range (1,totalPages+1):
        url = 'http://www.nanokomputer.com/index.php?cPath=431_492&sortcol=5&sortdir=a&page={}'.format(n)
        soup = requestAndGetSoup(url)
        links += getLink(soup)

    #Liquid CPU Cooling
    totalPages = 2
    for n in range (1,totalPages+1):
        url = 'http://www.nanokomputer.com/index.php?cPath=431_493&sortcol=5&sortdir=a&page={}'.format(n)
        soup = requestAndGetSoup(url)
        links += getLink(soup)

    for item in links:
        soup = requestAndGetSoup(item)
        data = getData(data,soup)

    return data

#Fungsi yang mengembalikan data scraping dari part Cases yang dijual pada www.nanokomputer.com
def getCases():
    data = []
    links = []
    totalPages = 7

    for n in range (1,totalPages+1):
        url = 'http://www.nanokomputer.com/index.php?cPath=33&sortcol=5&sortdir=a&page={}'.format(n)
        soup = requestAndGetSoup(url)
        links += getLink(soup)

    for item in links:
        soup = requestAndGetSoup(item)
        data = getData(data,soup)

    return data

#Main Program
if __name__ == "__main__":
    header = headers = {'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36', 'from' : '13517066@std.stei.itb.ac.id'}

    #Export file json database for processor 
    dataProcessor = getProcessor()
    export = pandas.DataFrame(dataProcessor, columns=['ID','Nama Processor', 'Deskripsi', 'Harga','Link Image'])
    export.to_json('../data/Processor.json')

    #Export file json database for motherboard
    dataMotherboard = getMotherboard()
    export = pandas.DataFrame(dataMotherboard, columns=['ID', 'Nama Motherboard', 'Deskripsi', 'Harga', 'Link Image'])
    export.to_json('../data/Motherboard.json')

    #Export file json database for Memory
    dataMemory = getMemory()
    export = pandas.DataFrame(dataMemory, columns=['ID','Nama Memory', 'Deskripsi', 'Harga', 'Image Link'])
    export.to_json('../data/Memory.json')

    #Export file json database for GraphicCards
    dataGraphicCards = getGraphicCards()
    export = pandas.DataFrame(dataGraphicCards, columns=['ID','Nama GraphicCards', 'Deskripsi', 'Harga', 'Image Link'])
    export.to_json('../data/GraphicCards.json')

    #Export file json database for Storage
    dataStorage = getStorage()
    export = pandas.DataFrame(dataStorage, columns=['ID','Nama Storage', 'Harga', 'Deskripsi', 'Link Image'])
    export = export.to_json('../data/Storage.json', orient='index')

    #Export file json database for PowerSupply
    dataPowerSupply = getPowerSupply()
    export = pandas.DataFrame(dataPowerSupply, columns=['ID','Nama PowerSupply', 'Deskripsi', 'Harga','Image Link'])
    export.to_json('../data/PowerSupply.json')

    #Export file json database for Cooling
    dataCooling = getCooling()
    export = pandas.DataFrame(dataCooling, columns=['ID','Nama Cooling', 'Deskripsi', 'Harga','Image Link'])
    export.to_json('../data/Cooling.json')

    #Export file json database for OpticalDrive
    dataOpticalDrive = getOpticalDrive()
    export = pandas.DataFrame(dataOpticalDrive, columns=['ID','Nama OpticalDrive', 'Deskripsi', 'Harga','Image Link'])
    export.to_json('../data/OpticalDrive.json')

    #Export file json database for Cases
    dataCases = getCases()
    export = pandas.DataFrame(dataCases, columns=['ID','Nama Cases', 'Deskripsi', 'Harga','Image Link'])
    export.to_json('../data/Cases.json')