#importing library
import json
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np


#requesting to scrape the web
def requesturl(url):
    header = {'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64); SamanthaOlivia/13517123@std.stei.itb.ac.id'}
    response = requests.get(url, headers = header).text
    soup = bs(response, 'html.parser')
    htmlcontent = soup.find('table', id="historicalRateTbl")
    return htmlcontent

#getting the data by parsing the html
def getDataMain(dataTable1, htmlcontent,x):
    try:
        for data in htmlcontent.find_all('tr'):
            dt = data.find_all('td')
            if len(dt) == 4 :
                date = x[-10:]
                dataTable1.append((date, dt[0].get_text(), dt[2].get_text(), dt[3].get_text()))
    except: pass

#getting data for the currency code
def getDataCode(dataTable2, htmlcontent):
    try:
        for data in htmlcontent.find_all('tr'):
            dt = data.find_all('td')
            if len(dt) == 4 :
                dataTable2.append((dt[0].get_text(), dt[1].get_text()))
    except: pass

#main program
print("WEB SCRAPING - from XE.COM ")
date1 = input("Enter the first date (format yyyy-mm-dd): ")
date2 = input("Enter the last date: ")

baselink = "https://www.xe.com/currencytables/?from=USD&date=" + date1[:-2]

print("--PRINTING THE DATA--")

dataTable1 = []
dataTable2 = []

for i in range(int(date1[-2:]),int(date2[-2:])+1):
    x = baselink + str(i)
    htmlcontent = requesturl(x)
    getDataMain(dataTable1, htmlcontent,x)
    
getDataCode(dataTable2, htmlcontent)

#making array of data
array1 = np.asarray(dataTable1)
array2 = np.asarray(dataTable2)

dataFrame1 = pd.DataFrame(array1)
dataFrame2 = pd.DataFrame(array2)
dataFrame1.columns = ['Date', 'Currency Code', 'Units per USD', 'USD per Unit']
dataFrame2.columns = ['Currency Code', 'Currency Name']

#printing the dataframe
print(dataFrame1)
print(dataFrame2)

#writing the data to json file
dataFrame1.to_json(r'data1.json',orient='records', lines=True)
dataFrame2.to_json(r'data2.json',orient='records', lines=True)