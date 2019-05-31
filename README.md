<h1 align="center">
  <br>
  FIFA World Men's Ranking
  <br>
  <br>
</h1>

<h2 align="center">
  <br>
  Data Scraping
  <br>
  <br>
</h2>

## Description
The following is a program that is used to do scraping on FIFA websites to get country data along with points in the FIFA World Men's Ranking for the past 1 year. This program is created using Python programming language and is supported by several additional libraries such as BeautifulSoup, webdriver, time and json. Geckodriver is used as a webdriver on this program to run Mozilla Firefox.

## How to use
Before running this program, first download Geckodriver to run Mozilla Firefox on the page https://github.com/mozilla/geckodriver. After downloading, put the download results in the same directory as scraper.py. Run the program with this command

```
python scraper.py

```
The results of scraping will be in the form of json.

## Ideas and innovations in utilizing the data
Data can be used to see the development of the country's ranking based on the points it has gotten over the past year. Users can also compare any developments or points obtained by several countries in a given 

## JSON structure

```
{
  "data": [
    {
      "nation": "Belgium", 
      "point": "1737"
    }, 
    {
      "nation": "France", 
      "point": "1734"
    }, 
  ], 
  "date": "04 April 2019"
} 

```

## Screenshot program
![alt text](https://github.com/ramadhanriandi/web-scraper/blob/master/screenshots/1.png)
![alt text](https://github.com/ramadhanriandi/web-scraper/blob/master/screenshots/2.png)
![alt text](https://github.com/ramadhanriandi/web-scraper/blob/master/screenshots/3.png)

## Reference
[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
[Geckodriver](https://github.com/mozilla/geckodriver)
[Selenium](https://selenium-python.readthedocs.io/)

## Author
Mgs. Muhammad Riandi Ramadhan
