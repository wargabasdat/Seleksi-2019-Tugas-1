<h1 align="center">
  <br>
  Online Smartphone Sales in Indonesia
  <br>
  <br>
</h1>

## Description
This script is *web scraping* script to obtain smartphone sales data in Indonesia. Data was taken from one of the well-known e-commerce namely [Bukalapak](https://www.bukalapak.com/). It aims to get information about: 
- Name
- Price
- Condition
- Seller 
- Place
- Brand

## Specification
- Runtime : - Python
- Libraries : 
  - BeautifulSoup
  - lxml
  - requests

## How to Use
You can run this script using
```bash
$ cd src
$ python scrap.py
```
The results of scraping will be stored in the JSON file to the ```/data``` directory

## Ideas and Innovations in Utilizing the Data
For buyers, this data can be used to provide information about which smartphone is according to their wishes. Buyers can compare prices and location of sales because it can affect the cost of shipping later. 

For smartphone manufacturers, this data can be used to see the spread of smartphones that he sells in Indonesia both in terms of price and sales. This data can be used as a reference for marketing sales.

## JSON Structure
JSON is stored in the form of an array of smartphone data
```json
[
    {
      "name": "Realme 3 ram 3gb",
      "price": 1820000,
      "condition": "Baru",
      "seller": "CAHAYA PONSEL",
      "location": "Kab. Bekasi",
      "brand": "Realme"
    },
    {
        "name": "Vivo v 15 resmi",
        "price": 3619000,
        "condition": "Baru",
        "seller": "BinTanG cell",
        "location": "Jakarta Timur",
        "brand": "Vivo"
    },
    ...
]
```

## Screenshot

## Reference
[BeuatifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
[requests](https://realpython.com/python-requests/)
[concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html)

## Author
Muhammad Fikri Hizbullah
13517104
