import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

# Self-introduce
headers = requests.utils.default_headers()
headers.update({'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64); Hendry Prasetya/13517105@std.stei.itb.ac.id'})

# Scrape table content
def scrape_table(url):
    global headers

    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.content, 'lxml')
    type(soup)
    rows = soup.find_all('tr')
    list_rows = []
    for row in rows:
        cells = row.find_all('td')
        str_cells = str(cells)
        clean = re.compile('<.*?>')
        clean2 = (re.sub(clean, '',str_cells))
        list_rows.append(clean2)
    return list_rows

def obtain_dataframe(url1, url2):
    list = scrape_table(url1) # Scrape first page
    for i in range (2,16): # Scrape page 2 - 15
        list = list + (scrape_table(url2+str(i)))

    #Clean useless tuple
    list.remove('[]') 
    list.remove('[\xa0]')
        
    return pd.DataFrame(list)

def clean_dataframe(df):
    new_df = df[0].str.split(', ', expand = True)
    new_df[0] = new_df[0].str.strip('[')
    return new_df

def get_table_headers(url):
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.content, 'lxml')
    col_labels = soup.find_all('th')
    all_header = []
    col_str = str(col_labels)
    cleantext2 = BeautifulSoup(col_str, "lxml").get_text()
    all_header.append(cleantext2)
    df = pd.DataFrame(all_header)
    df = clean_dataframe(df)
    return df

url1 = "http://www.duniainvestasi.com/bei" # page one
url2 = "http://www.duniainvestasi.com/bei/prices/daily/20190529/page:" # page 2 or more
df = obtain_dataframe(url1, url2)

## CLEAN ##
df = clean_dataframe(df)

# Scrape table header
df2 = get_table_headers(url1)

# Change header of first dataframe
df = df.rename(columns=df2.iloc[0])

# Delete column that won't be used
df = df.drop(columns = "Chart")
df = df.drop(columns = "Detail]")

print(df)

# Export to JSON
with open('../data/out.json', 'w') as f:
    f.write(df.to_json(orient='records', lines=True))
