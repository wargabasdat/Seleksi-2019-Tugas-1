#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from pandas import *
import pandas
import json


# In[2]:


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"')


# In[16]:


path_to_chromedriver = '/usr/local/bin/chromedriver' # Path to access a chrome driver
browser = webdriver.Chrome(executable_path=path_to_chromedriver, options=chrome_options)


# In[17]:


url = 'https://stats.nba.com/team/1610612744/boxscores-traditional/'
browser.get(url)


# In[5]:


table = browser.find_element_by_class_name('nba-stat-table__overflow')


# In[6]:


team_date = []
team_win = []
team_stats = []
column_names = []

for line_id, lines in enumerate(table.text.split('\n')):
    if line_id == 0:
        column_names = lines.split(' ')[1:]
    else:
        temp = []
        parse = lines.split()
        team_date.append(parse[0] + " " + parse[1] + " " + parse[2] + " " + parse[3] + " " + parse[4] + " " + parse[5] + " " + parse[6])
        team_win.append(parse[7])
        for i in range(8,28):
            temp.append(float(parse[i]))
        team_stats.append(temp)


# In[7]:


# Next Page
browser.find_element_by_xpath('/html/body/main/div[2]/div/div/div[3]/div/div/div/nba-stat-table/div[3]/div/div/a[2]').click()


# In[8]:


table = browser.find_element_by_class_name('nba-stat-table__overflow')


# In[9]:


for line_id, lines in enumerate(table.text.split('\n')):
    if line_id == 0:
        column_names = lines.split(' ')[1:]
    else:
        temp = []
        parse = lines.split()
        team_date.append(parse[0] + " " + parse[1] + " " + parse[2] + " " + parse[3] + " " + parse[4] + " " + parse[5] + " " + parse[6])
        team_win.append(parse[7])
        for i in range(8,28):
            temp.append(float(parse[i]))
        team_stats.append(temp)


# In[10]:


db = pandas.DataFrame({'MATCH UP': team_date,
                       'W/L': team_win,
                       'MIN': [i[0] for i in team_stats],
                       'PTS': [i[1] for i in team_stats],
                       'FGM': [i[2] for i in team_stats], 
                       'FGA': [i[3] for i in team_stats],
                       'FG%': [i[4] for i in team_stats],
                       '3PM': [i[5] for i in team_stats],
                       '3PA': [i[6] for i in team_stats],
                       '3P%': [i[7] for i in team_stats],
                       'FTM': [i[8] for i in team_stats],
                       'FTA': [i[9] for i in team_stats],
                       'FT%': [i[10] for i in team_stats],
                       'OREB': [i[11] for i in team_stats],
                       'DREB': [i[12] for i in team_stats],
                       'REB': [i[13] for i in team_stats],
                       'AST': [i[14] for i in team_stats],
                       'TOV': [i[15] for i in team_stats],
                       'STL': [i[16] for i in team_stats],
                       'BLK': [i[17] for i in team_stats],
                       'PF': [i[18] for i in team_stats],
                       '+/-': [i[19] for i in team_stats],
                       }
                     )


# In[11]:


db


# In[12]:


# Set to Export Location
db.to_json(r'/Users/kevin/Documents/Sublime/SeleksiBasdat/data.json', orient='records', lines = True)


# In[13]:


browser.close()


# In[14]:


print('Export data to JSON file as "data.json" success')


# In[ ]:




