# import library to parse html
from bs4 import BeautifulSoup
# import library to get HTML file from URLs
import requests
# import library to write json file
import json
# import library to add concruency while scraping
from concurrent.futures import ThreadPoolExecutor

# Get Product Name
def getName(product):
    return product.find('a', class_='product__name').string

# Get Product Price
def getPrice(product):
    return product.find('div', class_='product-price')['data-reduced-price']

# Get Product Production
def getCondition(product):
    return product.find('span', class_='product__condition').string

# Get Product Seller
def getSeller(product):
    return product.find('h5', class_='user__name').a.string

# Get Seller Location
def getLocation(product):
    return product.find('div', class_='user-city').span.string

# Get Product Brand
def getBrand(url):
    response = requests.get('https://www.bukalapak.com' + url, headers)
    product_brand = BeautifulSoup(response.content, 'lxml').find('div', class_='js-collapsible-product-detail').a
    if product_brand is not None:
        return product_brand.string.strip().split(' ')[0].lower().capitalize()
    else: 
        return 'NULL'

# Write data to the File
def writeData(data, file):
    print('Writing Data...')
    with open(file, 'w') as outfile:
        json.dump(data, outfile, indent=4)
    print('Finished Writing Data')

# Get data from the page
def getData(data, headers, page=1):
    url = f'https://www.bukalapak.com/c/handphone/hp-smartphone?page={page}'
    print(f'Loading Page {page}...')
    response = requests.get(url, headers)

    if response.ok:
        products = BeautifulSoup(response.content, 'lxml').find_all(lambda tag: tag.name == 'li' and tag.get('class') == ['col-12--2'])
        product_detail = {}
        for index, product in enumerate(products, start=1):
            print(f'Parsing page {page} product ({index}/{len(products)})')

            # Get the product name
            product_detail['name'] = getName(product)

            # Get the product price
            product_detail['price'] = getPrice(product)

            # Get the product condition
            product_detail['condition'] = getCondition(product)

            # Get the product seller
            product_detail['seller'] = getSeller(product)

            # Get the seller location
            product_detail['location'] = getLocation(product)

            # Get the product brand
            product_detail['brand'] = getBrand(product.find('a', class_='product-media__link').get('href'))

            data.append(product_detail)
            product_detail = {}
    else:
        print(f'Connection Issue in page {page}')

    return data

# Get data from all multiple page
def multiGetData(data, headers, start_page=1, end_page=5, workers=30):
    with ThreadPoolExecutor(max_workers=workers) as executor:
        [executor.submit(getData, data=data, headers=headers, page=i) for i in range(start_page, end_page+1)]

    print('Finished parsing data')
    return data

# GLOBAL VARIABLE
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0'}
data = []

# MAIN PROGRAM
if __name__ == '__main__':
    # Run the web scraping to get data
    multiGetData(data, headers)    

    # Write data to the json formatted file in the folder 'data'
    writeData(data, '../data/data.json')