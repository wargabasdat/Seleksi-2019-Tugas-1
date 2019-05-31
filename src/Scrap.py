import requests
import sys
from bs4 import BeautifulSoup
import pandas as pd

def getFilmList(genre):
        url = "https://www.imdb.com/search/title?genres="+ str(genre) +"&start={}&view=advanced"
        data = []
        for i in range(1, 1001, 50):
                soup = BeautifulSoup(requests.get(url.format(i)).content, 'html5lib')
                table = soup.find('div', {'class':'lister-list'})
                for row2 in table.findAll('div', attrs = {'class':'lister-item mode-advanced'}):
                        judul = row2.find('h3', attrs = {'class':'lister-item-header'}).a.text
                        genres = row2.find('span', {'class':'genre'})
                        if(genres!=None):
                                genres = str(genres.next_element)[1:]
                        runtime = row2.find('span', {'class':'runtime'})
                        if(runtime!=None):
                                runtime = runtime.next_element
                        rate = row2.find('span', {'class':'value'})
                        if(rate!=None):
                                rate = rate.next_element
                        data.append({'Title' : judul,'Genre' : genres, 'Rating':rate, 'Runtime':runtime})
        return data

#main
Data = {'1000 Top '+ str(sys.argv[1]) +' Film List(Based on Popularity)' : getFilmList(sys.argv[1])}
df = pd.DataFrame(Data)
Export = df.to_json(r'..\data\Film.json')