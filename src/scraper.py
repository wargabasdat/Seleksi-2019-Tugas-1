# File      : scraper.py
# NIM/Nama  : 13517141/Tasya Lailinissa Diandraputri

from requests import get
from bs4 import BeautifulSoup
import os
from json import dump

def scrapeChart(url, ua, f):
# Returns dictionary of songs chart scraping result from url with user-agent ua and from e

    # Request url resource
    r = get(url, headers = {'user-agent': ua, 'from': f})

    # Parse url resource
    soup = BeautifulSoup(r.text, 'html.parser')

    # Initialize dictionary
    data = {'songs': []}

    # Position
    position = soup.select('.number')
    for i in position:
        data['songs'].append({'position': int(i.text)})

    for i in range(len(data['songs'])):
        data['songs'][i].update({'songInfo': {}})
        data['songs'][i].update({'chartInfo': {}})
        
    # Song
    title = soup.select('.title-song')
    for i in range(len(title)):
        data['songs'][i]['songInfo'].update({'title': title[i].text.strip()})

    # Artist and label
    artist = soup.select('.title-artist')
    artistLabel = []
    for i in artist:
        artistLabel.append(i.text.strip().split(' | '))
    for i in range(len(artistLabel)):
        data['songs'][i]['songInfo'].update({'artist': artistLabel[i][0]})  # Artist
        data['songs'][i]['songInfo'].update({'label': artistLabel[i][1]})   # Label

    # Last week, time spent and highest position
    songStats = soup.select('.cell-value')
    for i in range(len(data['songs'])):
        for j in range(4):
            if j % 4 == 1:      # Last week's position
                data['songs'][i]['chartInfo'].update({'lastWeek': songStats[i * 4 + j].text})
            elif j % 4 == 2:    # Time spent on chart
                data['songs'][i]['chartInfo'].update({'timeSpent': int(songStats[i * 4 + j].text)})
            elif j % 4 == 3:    # Highest position on chart
                data['songs'][i]['chartInfo'].update({'highestPosition': int(songStats[i * 4 + j].text)})
    
    return data

def writeDict(file, data):
# Writes dictionary to file

    p = 'data/' # Path to data folder
    with open(os.path.join(p, file), 'w') as f:
        # Write to json format
        dump(data, f, indent = 4)
