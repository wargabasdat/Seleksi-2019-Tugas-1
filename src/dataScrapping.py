#Name : Gama Pradipta Wirawan
#Email : gamapradipta88@gmail.com
#Data Source : PegiPegi

#import libraries
import requests
from bs4 import BeautifulSoup
from lxml import html
import time
import json
import re
def getFacility(facSoup):
    facList = {}
    for fac in facSoup.findAll('li'):
        if (fac.get("class")==['noactive']):
            facList[fac.find('span').text.strip()]=False
        else:
            facList[fac.find('span').text.strip()]=True
    return facList

def getRoomInfo(roomSoup):
    data = {}
    contentLeft = roomSoup.find('div',{'class':'contentLeft'})
    data['Nama Kamar'] = contentLeft.find('div',{'class':'title'}).text.strip()
    infoList = {}
    infoList['Maksimal Orang'] = None
    infoList['Sarapan'] = False
    infoList['Wifi Gratis'] = False
    infoList['Ukuran'] = None
    infoList['Refundable'] = True
    infoContainer = roomSoup.findAll('div',{'class':'info'})
    for info in infoContainer:
        infoText = info.find('span').text.strip()
        if 'orang' in infoText:
            infoList['Maksimal Orang'] = int(re.sub("\D","",infoText))
        elif 'sarapan' in infoText and (not('Tidak' in infoText)):
            infoList['Sarapan'] = True
        elif 'koneksi' in infoText and (not('Tidak' in infoText)):
            infoList['Wifi Gratis'] = True
        elif 'm²' in infoText:
            infoList['Ukuran'] = float(infoText.strip('m²').strip())
        elif 'Refundable' in infoText and ('Non' in infoText):
            infoList['Refundable'] = False
        else:
            pass
    data['Info Kamar'] = infoList
    data['Harga'] = int(re.sub("\D","",roomSoup.find('div',{'class':'normalPrice'}).text))
    return data


def getData(url):
    data = {}
    global header
    #query the website and return the html to the variable 'response'
    response = requests.get(url, headers = header)
    #parse the html using beautiful soup and store in variable 'soup'
    soup = BeautifulSoup(response.text,'html.parser')
    name = soup.find('h1', {'class':'title','itemprop':'name'})
    data['Nama Hotel'] = name.text.strip()
    data['Bintang'] = len(name.findAll('i',{'class':'fa fa-star'}))
    data['Alamat Hotel'] = soup.find('span',{'itemprop':'address'}).text.strip()
    data['Fasilitas & Layanan Hotel'] = None
    data['Aktivitas Olah Raga'] = None
    data['Internet & Wifi'] = None
    data['Fasilitas Kamar'] = None
    pilihanKamar = []
    kamarContainer = soup.findAll('div',{'class':'listContentRoom'})
    for kamar in kamarContainer:
        pilihanKamar.append(getRoomInfo(kamar))
    data['Pilihan Kamar'] = pilihanKamar
    regex = re.compile('.*boxFiturHotel.*')
    for facility in soup.findAll('div',{'class':regex}):
        data[facility.find('div',{'class':'contentLeft'}).text.strip()] = getFacility(facility)
    return data
    
def getPage(url,data):
    global header
    #query the website and return the html to the variable 'response'
    response = requests.get(url, headers = header)
    #parse the html using beautiful soup and store in variable 'soup'
    soup = BeautifulSoup(response.text,'html.parser')
    for link in soup.findAll('a',{'class':'overflowLink'}) :
        try:
            print(link['href'])
            data.append(getData(link['href']))
            print("success")
            time.sleep(1)
        except KeyError:
            print("error")
            pass
    searchNext = soup.findAll('a',class_="buttonNav", text=">")
    if len(searchNext) !=0:
        nextUrl = searchNext[0]['href']
        print(nextUrl)
    else:
        nextUrl = None
    return nextUrl, data

if __name__ == "__main__":
    header = {'user-agent' : 'gamapradipta88@gmail.com'}
    # specify the url
    url = 'https://www.pegipegi.com/hotel/malang/'
    #query the website and return the html to the variable 'response'
    response = requests.get(url, headers = header)
    #parse the html using beautiful soup and store in variable 'soup'
    data = []
    while url is not None:
        url,data = getPage(url,data)
    
    with open("data/data.json","w") as outfile:
        json.dump(data,outfile,indent = 4)