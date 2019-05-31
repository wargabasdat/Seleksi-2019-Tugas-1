from selenium import webdriver  # for web driver
from bs4 import BeautifulSoup # for scraping
import time # for delaying
import json # for converting to json

driver = webdriver.Firefox(executable_path='/home/riandi/Projects/py/web-scraper/src/geckodriver')  # using geckodriver as web driver
driver.get('https://www.fifa.com/fifa-world-ranking/ranking-table/men/') # web url to be scraped
data = [] # store scraping result

try:
  print ("-------------------------------------")
  print ("Starting to Scrape FIFA World Ranking")
  print ("-------------------------------------")
  print ""

  for i in range (10):
    # click dropdown button of dates
    targetUrl = "/html/body/div[3]/div/div[1]/div/div/div[2]/div/button"
    dateButton = driver.find_elements_by_xpath(targetUrl)[0]
    driver.execute_script("arguments[0].click();", dateButton)
    time.sleep(3)

    # choose the date
    dateUrl = "/html/body/div[3]/div/div[1]/div/div/div[2]/div/ul/li[{}]/a"
    dateUrl = dateUrl.format(i+1)
    dateButton = driver.find_elements_by_xpath(dateUrl)[0]
    driver.execute_script("arguments[0].click();", dateButton)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    print ("-------------------------------------")
    print ""
    print ("Scraping for " + str(soup.find("div", "fi-selected-item").text.encode('utf-8')))
    time.sleep(5)

    # scrape for every pagination
    temp = []
    for j in range (5):
      targetUrl = "/html/body/div[3]/div/section/div[2]/div/div[3]/div[3]/div[2]/div/ul/li[{}]"
      targetUrl = targetUrl.format(j+1)
      paginationButton = driver.find_elements_by_xpath(targetUrl)[0]
      driver.execute_script("arguments[0].click();", paginationButton)
      time.sleep(5)
      soup = BeautifulSoup(driver.page_source, 'html.parser')

      # get all nations and their points
      for nation in soup.find_all("tr", {"class":["odd", "even"]}):
        nationObject = {
          "nation" : nation.find("span", "fi-t__nText").text.encode('utf-8'),
          "point" : nation.find("td", "fi-table__points").text.encode('utf-8'),
        }
        temp.append(nationObject)

      print (str((j+1)*2*"#") + str((4-j)*2*"-") + " " + str((j+1)*20) + "%") 
    print ""

    # get the date
    dataObject = {
      "date" : soup.find("div", "fi-selected-item").text.encode('utf-8'),
      "data" : temp,
    }
    data.append(dataObject)
  
  # save to json file
  with open('data.json', 'w') as outfile:
    json.dump(data, outfile, sort_keys=True, indent=2)

# driver quit
finally:
  print ("-------------------------------------")
  print ("DONE, FIFA World Ranking has been scraped")
  driver.quit()